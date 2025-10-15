import re
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class ActionCheckProductAvailability(Action):
    def name(self) -> Text:
        return "action_check_product_availability"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product_name = tracker.get_slot("product_name")
        print(f"Slot 'product_name': {product_name}")  # Log per il debug

        if not product_name:
            dispatcher.utter_message(text="Non hai specificato un prodotto per verificare la disponibilità.")
            print("Nessun prodotto specificato.")  # Log per il debug
            return []

        file_path = "C:/Users/MrWhi/OneDrive/Desktop/univpm/DataScience/Progetto_Datascience/chatbotGEGE/AC_Milan_Store_Products.csv"
        
        try:
            print(f"Sto cercando di leggere il file: {file_path}")  # Log per il debug
            df = pd.read_csv(file_path, sep=";", encoding="latin1")
            print(f"File caricato con successo. Colonne disponibili: {df.columns}")  # Log per il debug

            required_columns = ["Nome", "Disponibilità", "Prezzo"]
            if not all(col in df.columns for col in required_columns):
                dispatcher.utter_message(text=f"Il file CSV non contiene le colonne richieste: {', '.join(required_columns)}.")
                print(f"Colonne mancanti: {', '.join(required_columns)}")  # Log per il debug
                return []

            df["Nome"] = df["Nome"].fillna("").str.strip().astype(str)
            df["Disponibilità"] = df["Disponibilità"].fillna("").str.strip().astype(str)

            # Ricerca del prodotto
            product_info = df[df["Nome"].str.contains(rf'\b{product_name}\b', case=False, na=False)]

            if not product_info.empty:
                availability = product_info.iloc[0]["Disponibilità"]
                if availability.lower() == "si":
                    dispatcher.utter_message(text=f"Il prodotto '{product_info.iloc[0]['Nome']}' è disponibile.")
                else:
                    dispatcher.utter_message(text=f"Purtroppo, il prodotto '{product_info.iloc[0]['Nome']}' non è disponibile al momento.")
            else:
                dispatcher.utter_message(text=f"Non ho trovato informazioni sul prodotto '{product_name}'.")
                print(f"Prodotto '{product_name}' non trovato.")  # Log per il debug

        except FileNotFoundError:
            dispatcher.utter_message(text="Il file dei prodotti non è stato trovato.")
            print("File non trovato.")  # Log per il debug
        except UnicodeDecodeError as e:
            dispatcher.utter_message(text=f"Errore di decodifica nel file CSV: {str(e)}. Assicurati che il file abbia la codifica corretta.")
            print(f"Errore di decodifica: {str(e)}")  # Log per il debug
        except Exception as e:
            dispatcher.utter_message(text=f"Si è verificato un errore nel verificare la disponibilità dei prodotti: {str(e)}")
            print(f"Errore generico: {str(e)}")  # Log per il debug

        return []


class ActionCheckPrice(Action):
    def name(self) -> Text:
        return "action_check_price"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product_name = tracker.get_slot("product_name")
        print(f"Slot 'product_name': {product_name}")  # Log per il debug

        if not product_name:
            dispatcher.utter_message(text="Non hai specificato un prodotto per verificare il prezzo.")
            print("Nessun prodotto specificato.")  # Log per il debug
            return []

        file_path = "C:/Users/MrWhi/OneDrive/Desktop/univpm/DataScience/Progetto_Datascience/chatbotGEGE/AC_Milan_Store_Products.csv"
        
        try:
            print(f"Sto cercando di leggere il file: {file_path}")  # Log per il debug
            df = pd.read_csv(file_path, sep=";", encoding="latin1")
            print(f"File caricato con successo. Colonne disponibili: {df.columns}")  # Log per il debug

            required_columns = ["Nome", "Disponibilità", "Prezzo"]
            if not all(col in df.columns for col in required_columns):
                dispatcher.utter_message(text=f"Il file CSV non contiene le colonne richieste: {', '.join(required_columns)}.")
                print(f"Colonne mancanti: {', '.join(required_columns)}")  # Log per il debug
                return []

            df["Nome"] = df["Nome"].fillna("").str.strip().astype(str)
            df["Prezzo"] = pd.to_numeric(df["Prezzo"], errors='coerce')

            # Ricerca del prodotto
            product_info = df[df["Nome"].str.contains(rf'\b{product_name}\b', case=False, na=False)]

            if not product_info.empty:
                price = product_info.iloc[0]["Prezzo"]
                if pd.notna(price):  # Verifica se il prezzo è valido
                    dispatcher.utter_message(text=f"Il prezzo del prodotto '{product_info.iloc[0]['Nome']}' è {price:.2f}€.")  # Formatta con due decimali
                else:
                    dispatcher.utter_message(text=f"Il prezzo del prodotto '{product_info.iloc[0]['Nome']}' non è valido o mancante.")
            else:
                dispatcher.utter_message(text=f"Non ho trovato informazioni sul prodotto '{product_name}'.")
                print(f"Prodotto '{product_name}' non trovato.")  # Log per il debug

        except FileNotFoundError:
            dispatcher.utter_message(text="Il file dei prodotti non è stato trovato.")
            print("File non trovato.")  # Log per il debug
        except UnicodeDecodeError as e:
            dispatcher.utter_message(text=f"Errore di decodifica nel file CSV: {str(e)}. Assicurati che il file abbia la codifica corretta.")
            print(f"Errore di decodifica: {str(e)}")  # Log per il debug
        except Exception as e:
            dispatcher.utter_message(text=f"Si è verificato un errore nel verificare il prezzo del prodotto: {str(e)}")
            print(f"Errore generico: {str(e)}")  # Log per il debug

        return []


class ActionCheckSizeAvailability(Action):
    def name(self) -> Text:
        return "action_check_size_availability"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product_name = tracker.get_slot("product_name")
        size = tracker.get_slot("size")  # Slot opzionale

        if not product_name:
            dispatcher.utter_message(text="Per favore, specifica un prodotto per verificare la disponibilità delle taglie.")
            return []

        file_path = "C:/Users/MrWhi/OneDrive/Desktop/univpm/DataScience/Progetto_Datascience/chatbotGEGE/AC_Milan_Store_Products.csv"

        try:
            # Caricamento del file CSV
            df = pd.read_csv(file_path, sep=";", encoding="latin1")
            df["Nome"] = df["Nome"].fillna("").str.strip().str.lower()
            df["Taglie"] = df["Taglie"].fillna("").str.strip()
            df["Taglie"] = df["Taglie"].apply(lambda x: [s.strip().upper() for s in x.split(",") if s.strip()])

            # Validazione delle taglie
            all_sizes = set(tag for tags in df["Taglie"] for tag in tags)
            if size and size not in all_sizes:
                dispatcher.utter_message(text=f"La taglia {size} non esiste per nessun prodotto nel nostro catalogo.")
                return []

            # Raggruppamento per prodotto
            df = df.groupby("Nome", as_index=False).agg({
                "Taglie": lambda x: sorted(set(tag for sublist in x for tag in sublist))
            })

            # Normalizzazione dell'input
            product_name = product_name.lower().strip()
            size = size.strip().upper() if size else None

            # Filtraggio del prodotto specifico
            product_info = df[df["Nome"].str.contains(rf'\b{re.escape(product_name)}\b', case=False, na=False)]

            if product_info.empty:
                dispatcher.utter_message(text=f"Non ho trovato informazioni sul prodotto '{product_name}'.")
                return []

            available_sizes = product_info.iloc[0]["Taglie"]

            if size:  # Se l'utente richiede una taglia specifica
                if size in available_sizes:
                    dispatcher.utter_message(text=f"La taglia {size} per il prodotto '{product_name}' è disponibile.")
                else:
                    dispatcher.utter_message(text=f"Purtroppo, la taglia {size} per il prodotto '{product_name}' non è disponibile.")
            else:  # Se l'utente richiede tutte le taglie disponibili
                dispatcher.utter_message(text=f"Le taglie disponibili per '{product_name}' sono: {', '.join(available_sizes)}.")

        except FileNotFoundError:
            dispatcher.utter_message(text="Il file dei prodotti non è stato trovato.")
        except Exception as e:
            dispatcher.utter_message(text=f"Si è verificato un errore nel verificare le taglie: {str(e)}")

        return []

