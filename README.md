# 📊 Progetti Data Science (2026)

Questo repository raccoglie l'insieme dei progetti realizzati nell'ambito del percorso di **Data Science**, coprendo diverse aree tematiche dell'Intelligenza Artificiale: dalla **Conversational AI** con Rasa e Telegram, al **Deep Learning** per la Sentiment Analysis con BERT, all'**Analisi delle Reti** (SNA), al **Natural Language Processing avanzato** su articoli di giornale, e alle **Serie Temporali** meteorologiche con modelli SARIMAX.

---

## 📚 Indice dei Progetti

1. [⚽ Milan Store Chatbot (Conversational AI)](#1--milan-store-chatbot-conversational-ai)
2. [🎬 Sentiment Analysis su Recensioni Cinematografiche con BERT](#2--sentiment-analysis-su-recensioni-cinematografiche-con-bert)
3. [🕸️ Social Network Analysis (SNA) su TV Show](#3️-social-network-analysis-sna-su-grafo-tv-show)
4. [📰 NLP & Text Mining su BBC News Archive](#4--nlp--text-mining-su-bbc-news-archive)
5. [📈 Analisi delle Serie Temporali](#5--analisi-delle-serie-temporali-precipitazioni-di-londra)

---

## 1. ⚽ Milan Store Chatbot (Conversational AI)

### 📌 Descrizione
Sviluppo di un assistente virtuale intelligente in grado di interagire con gli utenti per fornire informazioni sul catalogo prodotti dello store ufficiale dell'**AC Milan** (maglie, abbigliamento da allenamento, kit da gara, accessori, prezzi, disponibilità e taglie).

### 🛠️ Tecnologie e Framework Usati
- **Rasa Framework (v3.x)**: NLU (Natural Language Understanding) e Gestione delle Politiche di Dialogo (DIETClassifier, TEDPolicy, RulePolicy).
- **Python 3.x & Pandas**: Caricamento, pulizia e interrozione dinamica del dataset prodotti (`AC_Milan_Store_Products.csv`).
- **TheFuzz (Fuzzy String Matching)**: Riconoscimento tollerante agli errori di battitura dei nomi dei prodotti.
- **Flask**: Webhook server per l'integrazione con Telegram.
- **Telegram Bot API & Ngrok**: Esposizione dell'endpoint e interfaccia utente di messaggistica reale.

### 💡 Funzionalità Principali
- Risposta a domande su **disponibilità**, **prezzo**, **taglie** e **colori** dei prodotti.
- Filtraggio dinamico per categoria (*Kit Da Gara*, *Allenamento*) e per target (*Uomo*, *Donna*, *Bambino*).
- Gestione delle varianti e dei suggerimenti contestuali post-risposta.

---

## 2. 🎬 Sentiment Analysis su Recensioni Cinematografiche con BERT

### 📌 Descrizione
Implementazione e fine-tuning di un modello di **Deep Learning** basato su architettura Transformer per la classificazione binaria del sentiment (Recensione Positiva / Negativa) a partire dal dataset `movie_cleaned.csv` (oltre 39.000 recensioni).

### 🛠️ Tecnologie e Framework Usati
- **PyTorch & Hugging Face Transformers**: Utilizzo dell'architettura pre-addestrata `bert-base-uncased`.
- **BertTokenizer**: Tokenizzazione nativa WordPiece con gestione del troncamento e del padding a lunghezza fissa.
- **AdamW Optimizer & Linear Warmup Scheduler**: Ottimizzazione del rate di apprendimento con regolarizzazione del dropout ($p=0.3$).
- **Scikit-Learn & Seaborn/Matplotlib**: Calcolo delle metriche (Accuracy, F1-Score, Precision, Recall) e visualizzazione della Matrice di Confusione e dei grafici di Loss/Accuracy.

### 💡 Risultati e Metodologia
- Divisione del dataset in 80% Training e 20% Test set stratificato.
- Implementazione dell'**Early Stopping** con salvataggio automatico dei pesi del modello migliore (*best model checkpoint*).
- Ottenimento di elevate prestazioni nella distinzione del tono emotivo e delle opinioni nelle recensioni.

---

## 3. 🕸️ Social Network Analysis (SNA) su Grafo TV Show

### 📌 Descrizione
Studio delle proprietà topologiche e strutturali di una rete complessa di relazioni (*TV Show Edges dataset*), applicando le principali metriche della **Network Science** per identificare nodi centrali, comunità e sottostrutture rilevanti.

### 🛠️ Tecnologie e Framework Usati
- **NetworkX**: Costruzione ed elaborazione del grafo non orientato.
- **Matplotlib & Seaborn**: Layouting avanzato dei grafi (Spring Layout, Kamada-Kawai) e rendering delle mappe di calore/istogrammi.
- **NumPy & Pandas**: Elaborazione matriciale delle metriche di centralità.

### 💡 Metriche e Strutture Analizzate
- **Metriche Globali**: Raggio, diametro, densità del grafo, grado di connessione e coefficiente di clustering medio.
- **Centralità dei Nodi**:
  - *Degree Centrality* (connessioni dirette).
  - *Closeness Centrality* (prossimità media a tutti gli altri nodi).
  - *Betweenness Centrality* (ruolo di ponte nei cammini minimi).
  - *Eigenvector Centrality* (influenza basata sull'importanza dei vicini).
- **Sub-strutture**: Individuazione delle *Cliques massimali* (e clique massima), estrazione del *K-Core* del grafo ed analisi delle *Ego Networks* per nodi chiave.

---

## 4. 📰 NLP & Text Mining su BBC News Archive

### 📌 Descrizione
Progetto completo di **Natural Language Processing** e **Text Mining** eseguito sul dataset *BBC News Archive* (2.225 articoli giornalistici divisi in 5 categorie: *Business*, *Entertainment*, *Politics*, *Sport*, *Tech*).

### 🛠️ Tecnologie e Framework Usati
- **TextBlob**: Sentiment Analysis (Polarità e Soggettività degli articoli).
- **FastText**: Classificazione automatica del testo veloce e robusta.
- **spaCy (`en_core_web_sm`)**: Named Entity Recognition (NER) per l'estrazione di Persone, Organizzazioni e Luoghi.
- **WordCloud & NLTK**: Visualizzazione nuvole di parole e pre-processing del testo (lowercasing, rimozione stop-words ed espressioni regolari).
- **LaTeX**: Redazione della documentazione accademica completa.

### 💡 Risultati e Pipeline
- **Pre-processing**: Riduzione del rumore e analisi comparativa delle statistiche del vocabolario.
- **Sentiment Analysis**: Rilevazione del tono prevalente per ciascuna categoria (es. tono più entusiastico in *Entertainment* e *Sport*, più neutro/distaccato in *Business*).
- **Classificazione FastText**: Raggiungimento di un'**Accuracy globale del 99%** sul Test set (445 articoli).
- **NER con spaCy**: Estrazione dei protagonisti principali per categoria (es. Tony Blair in Politics, aziende tech in Tech, atleti ed eventi in Sport).

---

## 5. 📈 Analisi delle Serie Temporali (Precipitazioni di Londra)

### 📌 Descrizione
Modellazione statistica e predittiva delle serie storiche meteorologiche della città di Londra dal 1979 al 2020 a partire dal dataset `london_weather.csv`.

### 🛠️ Tecnologie e Framework Usati
- **Statsmodels**: Test di Stazionarietà Augmented Dickey-Fuller (ADF), funzioni ACF/PACF, modelli **ARIMA** e **SARIMAX**.
- **Pandas & NumPy**: Resampling mensile con somme/medie e interpolazione lineare delle variabili continue.
- **Scikit-Learn**: Metriche di valutazione ed errore (RMSE, MAE, MAPE, ME, R).

### 💡 Architettura del Flusso di Lavoro
1. **Resampling Mensile**: Aggregazione dei dati giornalieri a livello mensile per stabilizzare la varianza ed eliminare il rumore ad alta frequenza.
2. **Test ADF & Autocorrelazioni**: Verifica della stazionarietà della serie e analisi dei grafici ACF/PACF per determinare i parametri $(p, d, q)$.
3. **Modello Baseline ARIMA(1,0,2)**: Prima stima lineare non stagionale.
4. **Modello Avanzato SARIMAX(1,0,1)x(0,1,1)₁₂ con Esogene**: Integrazione della componente stagionale annuale e delle variabili meteo esogene (*cloud cover*, *global radiation*, *mean temperature*).
5. **Consistenza Fisica**: Applicazione del clipping inferiore a 0 per garantire la correttezza fisica delle stime di precipitazione.
6. **Analisi dei Residui**: Verifica della distribuzione dei residui (KDE) e assenza di autocorrelazione rimanente.

---

## 📂 Struttura del Repository

```
.
├── milan_bot_fresh/      # Codice, configurazioni Rasa, NLU, custom actions e Telegram webhook
├── bert26/               # Notebooks Colab/locali, script di creazione e dataset recensioni film
├── sna/                  # Script Python, notebook ed esecuzione analisi del grafo TV Show
├── NLP/                  # Notebooks, immagini, script di analisi e sorgenti LaTeX della tesina NLP
├── serieTemporali/       # Notebook di time series analysis, dataset London Weather e relazioni tecniche
├── Python26.pdf          # Documentazione e materiale didattico/progetto Python
└── README.md             # Documento di sintesi del repository
```

---

## ✒️ Erxhes Dedja
