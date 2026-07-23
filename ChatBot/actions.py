import os
import re
from thefuzz import process, fuzz
import pandas as pd
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# ──────────────────────────────────────────────
# Caricamento e pulizia del dataset
# ──────────────────────────────────────────────
CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "AC_Milan_Store_Products.csv")

def load_data() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH, encoding="utf-8-sig", sep=";")
    df["Nome"]          = (df["Nome"]
                          .str.strip()
                          .str.replace(r"  +", " ", regex=True)   # doppi spazi → singolo
                          .str.replace("\\\\", "/", regex=False))  # backslash → slash
    df["Disponibilità"] = df["Disponibilità"].str.strip().str.upper().fillna("NO")
    df["Sesso"]         = df["Sesso"].str.strip().fillna("Unisex")
    df["Taglie"]      = (df["Taglie"]
                          .str.strip()
                          .str.replace(r"\s*cm\s*", "cm", regex=True)  # normalizza "68-70 cm" → "68-70cm"
                          .fillna(""))
    df["Colore"]        = df["Colore"].str.strip().fillna("")
    df["Categoria"]     = df["Categoria"].str.strip().fillna("")
    df["Tipologia"]     = df["Tipologia"].str.strip().fillna("")
    return df

DF = load_data()
PRODUCT_NAMES = DF["Nome"].dropna().unique().tolist()


def find_product(query: str) -> str | None:
    if not query:
        return None
    query_lower = query.strip().lower()
    # 1) Match esatto
    for name in PRODUCT_NAMES:
        if name.lower() == query_lower:
            return name
    # 2) Match parziale (query contenuta nel nome o viceversa)
    for name in PRODUCT_NAMES:
        if query_lower in name.lower() or name.lower() in query_lower:
            return name
    # 3) Fuzzy matching con thefuzz (coerente con il PDF)
    best_match, score = process.extractOne(
        query_lower,
        [n.lower() for n in PRODUCT_NAMES],
        scorer=fuzz.WRatio
    )
    if score >= 85:
        idx = [n.lower() for n in PRODUCT_NAMES].index(best_match)
        return PRODUCT_NAMES[idx]
    return None


def get_product_row(name: str) -> pd.DataFrame:
    return DF[DF["Nome"].str.lower() == name.lower()]


def _suggest_after(action_name: str) -> str:
    """Restituisce un messaggio di suggerimento in base all'azione appena eseguita."""
    if action_name == "availability":
        return "Ti dico anche il prezzo o le taglie? Scrivi 'prezzo' o 'taglie'."
    elif action_name == "price":
        return "Vuoi conoscere le taglie? Scrivi 'taglie'."
    elif action_name == "sizes":
        return "Posso dirti anche il prezzo. Scrivi 'prezzo'."
    elif action_name == "color":
        return "Posso aiutarti con disponibilità, prezzo o taglie."
    return None  # P9: nessun messaggio se non c'è suggerimento


def _dispatch_suggestion(dispatcher: CollectingDispatcher, action_name: str) -> None:
    """Invia il suggerimento solo se non vuoto (P9)."""
    suggestion = _suggest_after(action_name)
    if suggestion:
        dispatcher.utter_message(text=suggestion)


# ──────────────────────────────────────────────
# ACTION: Informazioni sullo store
# ──────────────────────────────────────────────
class ActionStoreInfo(Action):
    def name(self) -> Text:
        return "action_store_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict) -> List:
        msg = (
            "🏬 *Milan Store Ufficiale* — ecco cosa puoi trovare:\n\n"
            "• *Kit Da Gara* — maglie, pantaloncini e calzettoni ufficiali\n"
            "• *Allenamento* — maglie, pantaloni, giacche e palloni\n\n"
            "Puoi chiedermi disponibilità, prezzi e taglie di qualsiasi prodotto!"
        )
        dispatcher.utter_message(text=msg)
        return []


# ──────────────────────────────────────────────
# ACTION: Lista prodotti (tutti o per tipologia)
# ──────────────────────────────────────────────
class ActionListProducts(Action):
    def name(self) -> Text:
        return "action_list_products"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict) -> List:
        tipologia = tracker.get_slot("tipologia")
        sesso = tracker.get_slot("sesso")
        df = DF.copy()

        if tipologia:
            df = df[df["Tipologia"].str.lower() == tipologia.lower()]
        if sesso:
            df = df[df["Sesso"].str.lower() == sesso.lower()]

        if df.empty:
            msg = "Non ho trovato prodotti"
            if tipologia:
                msg += f" di tipo '{tipologia}'"
            if sesso:
                msg += f" per '{sesso}'"
            msg += "."
            dispatcher.utter_message(text=msg)
            return [SlotSet("tipologia", None), SlotSet("sesso", None)]

        nomi = sorted(df["Nome"].dropna().unique().tolist())
        intestazione = "Ecco i prodotti"
        if tipologia:
            intestazione += f" di tipo *{tipologia}*"
        if sesso:
            intestazione += f" per *{sesso}*"
        intestazione += ":"
        lista = "\n".join(f"• {n}" for n in nomi)
        dispatcher.utter_message(text=f"{intestazione}\n\n{lista}")
        return [SlotSet("tipologia", None), SlotSet("sesso", None)]


# ──────────────────────────────────────────────
# ACTION: Disponibilità
# ──────────────────────────────────────────────
class ActionCheckAvailability(Action):
    def name(self) -> Text:
        return "action_check_availability"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict) -> List:
        raw = tracker.get_slot("product_name") or tracker.latest_message.get("text", "")
        found = find_product(raw)
        if not found:
            dispatcher.utter_message(
                text=f"Non ho trovato nessun prodotto chiamato '{raw}'. "
                     f"Prova a scrivere il nome più precisamente."
            )
            return [SlotSet("product_name", None)]

        rows = get_product_row(found)
        sesso = tracker.get_slot("sesso")
        if sesso:
            rows = rows[rows["Sesso"].str.lower() == sesso.lower()]
            if rows.empty:
                dispatcher.utter_message(
                    text=f"Non ho trovato '{found}' per '{sesso}'."
                )
                return [SlotSet("product_name", found), SlotSet("sesso", None)]

        # P3: gestione disponibilità mista (alcune taglie/colori SI, altre NO)
        valori_disp = rows["Disponibilità"].unique().tolist()
        if "SI" in valori_disp and "NO" in valori_disp:
            msg = f"⚠️ Il prodotto *'{found}'* è parzialmente disponibile (alcune varianti esaurite)."
        elif "SI" in valori_disp:
            msg = f"✅ Il prodotto *'{found}'* è disponibile!"
        else:
            msg = f"❌ Il prodotto *'{found}'* non è disponibile al momento."
        if sesso:
            msg += f" (per {sesso})"

        dispatcher.utter_message(text=msg)
        _dispatch_suggestion(dispatcher, "availability")
        return [SlotSet("product_name", found), SlotSet("sesso", None)]


# ──────────────────────────────────────────────
# ACTION: Prezzo
# ──────────────────────────────────────────────
class ActionCheckPrice(Action):
    def name(self) -> Text:
        return "action_check_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict) -> List:
        raw = tracker.get_slot("product_name") or tracker.latest_message.get("text", "")
        found = find_product(raw)
        if not found:
            dispatcher.utter_message(
                text=f"Non ho trovato nessun prodotto chiamato '{raw}'."
            )
            return [SlotSet("product_name", None)]

        rows = get_product_row(found)
        sesso = tracker.get_slot("sesso")
        if sesso:
            rows = rows[rows["Sesso"].str.lower() == sesso.lower()]
            if rows.empty:
                dispatcher.utter_message(
                    text=f"Non ho informazioni sul prezzo di '{found}' per '{sesso}'."
                )
                return [SlotSet("product_name", found), SlotSet("sesso", None)]

        # P4: prezzi multipli → mostra range invece di solo il primo
        prezzi = rows["Prezzo"].dropna().unique().tolist()
        if not prezzi:
            msg = f"Il prezzo di *'{found}'* non è al momento disponibile."
        elif len(prezzi) == 1:
            msg = f"💰 Il prezzo di *'{found}'* è **{prezzi[0]:.2f}€**."
        else:
            p_min, p_max = min(prezzi), max(prezzi)
            msg = f"💰 Il prezzo di *'{found}'* va da **{p_min:.2f}€** a **{p_max:.2f}€** (a seconda della variante)."
        if sesso:
            msg += f" (per {sesso})"

        dispatcher.utter_message(text=msg)
        _dispatch_suggestion(dispatcher, "price")
        return [SlotSet("product_name", found), SlotSet("sesso", None)]


# ──────────────────────────────────────────────
# ACTION: Taglie
# ──────────────────────────────────────────────
class ActionCheckSizes(Action):
    def name(self) -> Text:
        return "action_check_sizes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict) -> List:
        raw = tracker.get_slot("product_name") or tracker.latest_message.get("text", "")
        found = find_product(raw)
        if not found:
            dispatcher.utter_message(
                text=f"Non ho trovato nessun prodotto chiamato '{raw}'."
            )
            return [SlotSet("product_name", None)]

        rows = get_product_row(found)
        sesso = tracker.get_slot("sesso")
        if sesso:
            rows = rows[rows["Sesso"].str.lower() == sesso.lower()]
            if rows.empty:
                dispatcher.utter_message(
                    text=f"Non ho taglie per '{found}' per '{sesso}'."
                )
                return [SlotSet("product_name", found), SlotSet("sesso", None)]

        taglie = sorted(rows["Taglie"].dropna().unique().tolist())
        taglie = [t for t in taglie if t]
        if taglie:
            lista = ", ".join(taglie)
            msg = f"📏 Le taglie di *'{found}'* sono: **{lista}**."
            if sesso:
                msg += f" (per {sesso})"
        else:
            msg = f"Non ho informazioni sulle taglie di *'{found}'*."

        dispatcher.utter_message(text=msg)
        _dispatch_suggestion(dispatcher, "sizes")
        return [SlotSet("product_name", found), SlotSet("sesso", None)]


# ──────────────────────────────────────────────
# ACTION: Colore
# ──────────────────────────────────────────────
class ActionCheckColor(Action):
    def name(self) -> Text:
        return "action_check_color"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict) -> List:
        raw = tracker.get_slot("product_name") or tracker.latest_message.get("text", "")
        found = find_product(raw)
        if not found:
            dispatcher.utter_message(
                text=f"Non ho trovato nessun prodotto chiamato '{raw}'."
            )
            return [SlotSet("product_name", None)]

        rows = get_product_row(found)
        # P8: filtra per sesso se disponibile
        sesso = tracker.get_slot("sesso")
        if sesso:
            filtered = rows[rows["Sesso"].str.lower() == sesso.lower()]
            if not filtered.empty:
                rows = filtered

        colori = rows["Colore"].dropna().unique().tolist()
        colori = [c for c in colori if c and c != "-"]
        if colori:
            if len(colori) == 1:
                msg = f"🎨 Il colore di *'{found}'* è: **{colori[0]}**."
            else:
                msg = f"🎨 I colori di *'{found}'* sono: **{', '.join(sorted(colori))}**."
        else:
            msg = f"Non ho informazioni sul colore di *'{found}'*."
        if sesso:
            msg += f" (per {sesso})"

        dispatcher.utter_message(text=msg)
        _dispatch_suggestion(dispatcher, "color")
        return [SlotSet("product_name", found), SlotSet("sesso", None)]


# ──────────────────────────────────────────────
# ACTION: Prodotti per categoria o sesso
# ──────────────────────────────────────────────
class ActionFilterProducts(Action):
    def name(self) -> Text:
        return "action_filter_products"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict) -> List:
        sesso     = tracker.get_slot("sesso")
        categoria = tracker.get_slot("categoria")
        df = DF.copy()

        if sesso:
            df = df[df["Sesso"].str.lower() == sesso.lower()]
        if categoria:
            df = df[df["Categoria"].str.lower() == categoria.lower()]

        if df.empty:
            msg = "Non ho trovato prodotti con i filtri selezionati."
        else:
            nomi = sorted(df["Nome"].dropna().unique().tolist())
            filtro = ""
            if sesso:
                filtro += f" per *{sesso}*"
            if categoria:
                filtro += f" categoria *{categoria}*"
            lista = "\n".join(f"• {n}" for n in nomi)
            msg = f"Prodotti{filtro}:\n\n{lista}"

        dispatcher.utter_message(text=msg)
        return [SlotSet("sesso", None), SlotSet("categoria", None)]