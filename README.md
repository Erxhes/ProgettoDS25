# 📊 Progetti di Data Science, Natural Language Processing, Machine Learning e Network Analysis (2026)

Questo repository raccoglie l'insieme completo dei progetti realizzati nell'ambito del percorso di **Data Science**, coprendo a 360 gradi le principali metodologie dell'Intelligenza Artificiale e dell'Analisi dei Dati: dalla **Conversational AI** con Rasa e Telegram, al **Deep Learning** con BERT, alla **Network Science** (SNA), al **Natural Language Processing avanzato**, fino all'intero ciclo di analisi del dataset meteorologico (*Analisi Descrittiva*, *Classificazione Binaria*, *Clustering/Segmentazione* e *Serie Temporali SARIMAX*).

---

## 📚 Indice dei Progetti

1. [⚽ Milan Store Chatbot (Conversational AI)](#1--milan-store-chatbot-conversational-ai)
2. [🎬 Sentiment Analysis su Recensioni Cinematografiche con BERT](#2--sentiment-analysis-su-recensioni-cinematografiche-con-bert)
3. [🕸️ Social Network Analysis (SNA) su TV Show](#3️-social-network-analysis-sna-su-grafo-tv-show)
4. [📰 NLP & Text Mining su BBC News Archive](#4--nlp--text-mining-su-bbc-news-archive)
5. [📊 Analisi Descrittiva e Climatologica di Londra (AD26)](#5--analisi-descrittiva-e-climatologica-di-londra-ad26)
6. [🎯 Classificazione Binaria delle Precipitazioni (Classificazione26)](#6--classificazione-binaria-delle-precipitazioni-classificazione26)
7. [🧩 Clustering e Profilazione dei Regimi Meteorologici (Clustering26)](#7--clustering-e-profilazione-dei-regimi-meteorologici-clustering26)
8. [📈 Analisi delle Serie Temporali delle Precipitazioni (SerieTemporali)](#8--analisi-delle-serie-temporali-delle-precipitazioni-serietemporali)

---

## 1. ⚽ Milan Store Chatbot (Conversational AI)

### 📌 Descrizione
Sviluppo di un assistente virtuale intelligente in grado di interagire con gli utenti per fornire informazioni sul catalogo prodotti dello store ufficiale dell'**AC Milan** (maglie, abbigliamento da allenamento, kit da gara, accessori, prezzi, disponibilità e taglie).

### 🛠️ Tecnologie e Framework Usati
- **Rasa Framework (v3.x)**: NLU (Natural Language Understanding) e Gestione delle Politiche di Dialogo (DIETClassifier, TEDPolicy, RulePolicy).
- **Python 3.x & Pandas**: Caricamento, pulizia e interrogazione dinamica del dataset prodotti (`AC_Milan_Store_Products.csv`).
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

## 3. 🕸️ Social Network Analysis (SNA) su TV Show

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

## 5. 📊 Analisi Descrittiva e Climatologica di Londra (AD26)

### 📌 Descrizione
Studio esplorativo, statistico e climatologico approfondito dei dati meteorologici della città di Londra dal 1979 al 2020 a partire dal dataset `london_weather.csv`.

### 🛠️ Tecnologie e Framework Usati
- **Pandas & NumPy**: Manipolazione dati ed imputazione differenziata.
- **Matplotlib & Seaborn**: Istogrammi con stima KDE, boxplot temporali/stagionali e visualizzazioni pluviometriche.
- **Plotly Express**: Line-chart e Scatterplot 3D interattivi (Temperatura vs Precipitazioni vs Radiazione Solare).
- **SciPy (`scipy.stats.linregress`)**: Calcolo delle regressioni lineari e verifica della significatività statistica ($p$-value).

### 💡 Metodologia e Risultati Scientifici
- **Imputazione Differenziata**: Interpolazione lineare per le variabili continue; riempimento con 0 (*zero-filling*) per le precipitazioni e la neve per evitare l'introduzione artificiale di "piogge fantasma".
- **Analisi delle Anomalie (Standard WMO 1981-2010)**: Calcolo delle anomalie termiche annuali rispetto al trentennio di riferimento climatologico World Meteorological Organization (WMO).
- **Trend di Riscaldamento Globale**: Individuazione di un trend di riscaldamento statisticamente significativo ($p < 0.001$) con un tasso di crescita di $+0.038\ ^\circ\text{C/anno}$ a Londra, confermato anche dalle medie mobili a 5 anni.
- **Classificazione Pluviometrica**: Categorizzazione dell'intensità di pioggia in 4 classi (*Asciutto*, *Pioggia Leggera*, *Moderata*, *Forte*).

---

## 6. 🎯 Classificazione Binaria delle Precipitazioni (Classificazione26)

### 📌 Descrizione
Sviluppo di modelli di Machine Learning per la predizione binaria del verificarsi di eventi piovosi (*Pioggia / No Pioggia*) a Londra, integrando strategie rigorose contro il *Data Leakage*.

### 🛠️ Tecnologie e Framework Usati
- **Scikit-Learn**: Scaler, Pipeline, TimeSeriesSplit, Voting Classifier e metriche di valutazione.
- **XGBoost & Random Forest**: Modelli ad albero e gradient boosting ad alte prestazioni.
- **Yellowbrick**: Diagnostic tools (ROC Curve, Precision-Recall Curve, Learning Curves).

### 💡 Architettura Anti-Leakage e Workflow
1. **Feature Engineering**: Creazione di *Lag Features* al giorno precedente (`precip_lag1`, `sunshine_lag1`, `cloud_lag1`), media mobile a 3 giorni (`precip_ma3`) e One-Hot Encoding per i 12 mesi.
2. **Target Binario Rigoroso**: La soglia di precipitazione ($60^\circ$ percentile) viene determinata **esclusivamente sul Training Set ($< 2019$)** per prevenire contaminazioni informative sul Test set.
3. **Selezione Anti-Multicollinearità**: Eliminazione delle variabili termiche fortemente correlate per garantire la stabilità matematica dei modelli.
4. **Split Temporale & Cross-Validation**: Divisione rigida in Train ($1979-2018$) e Test ($2019-2020$) con `TimeSeriesSplit` a 5 fold applicato all'interno delle `Pipeline`.
5. **Voting Classifier & Threshold Tuning**: Soft Voting Ensemble tra Random Forest e XGBoost con ottimizzazione della soglia di decisione lungo la curva Precision-Recall per la massimizzazione dell'F1-Score.

---

## 7. 🧩 Clustering e Profilazione dei Regimi Meteorologici (Clustering26)

### 📌 Descrizione
Segmentazione non supervisionata e profilazione dei pattern climatici di Londra, confrontando algoritmi di partizionamento, gerarchici e basati sulla densità.

### 🛠️ Tecnologie e Framework Usati
- **Scikit-Learn**: `KMeans`, `AgglomerativeClustering`, `DBSCAN`, `StandardScaler`, `PCA`.
- **Yellowbrick**: `KElbowVisualizer` e `SilhouetteVisualizer`.

### 💡 Metodologia e Risultati di Clustering
- **Scelta del $K$ Ottimale**: Metodo Elbow (WCSS) e Silhouette Score ($K=4$).
- **Regimi Termici Identificati**: *Molto Freddo*, *Freddo Transizione*, *Fresco/Mite*, *Caldo*.
- **Regimi Pluviometrico-Solari**: *Secco/Soleggiato*, *Asciutto/Nuvoloso*, *Piovoso/Nuvoloso*, *Molto Piovoso*.
- **Riduzione Dimensionale PCA**: Proiezione dello spazio multidimensionale in 2 componenti principali ($PCA1$, $PCA2$) per la visualizzazione dei cluster.
- **DBSCAN & Curva $K$-distance**: Scelta oggettiva del parametro $\epsilon=0.5$ (tramite il "ginocchio" del $5^\circ$ vicino) ed analisi di sensibilità su 6 valori di $\epsilon$ per la rilevazione di outliers e giornate anomale.

---

## 8. 📈 Analisi delle Serie Temporali delle Precipitazioni (SerieTemporali)

### 📌 Descrizione
Modellazione statistica e predittiva delle serie storiche meteorologiche della città di Londra dal 1979 al 2020 basata su modelli autoregressivi e stagionali.

### 🛠️ Tecnologie e Framework Usati
- **Statsmodels**: Test ADF (Augmented Dickey-Fuller), autocorrelazioni ACF/PACF, modelli **ARIMA** e **SARIMAX**.
- **Pandas & NumPy**: Resampling mensile temporale e vincolo di consistenza fisica (`clip(lower=0)`).
- **Scikit-Learn**: Metriche di errore (RMSE, MAE, MAPE, ME, R).

### 💡 Pipeline di Modellazione
1. **Resampling Mensile**: Aggregazione dei dati giornalieri a livello mensile per stabilizzare la varianza ed eliminare il rumore ad alta frequenza.
2. **Stazionarietà e ACF/PACF**: Rifiuto dell'ipotesi nulla di non-stazionarietà (Test ADF) e analisi dei ritardi stagionali a 12 mesi.
3. **Baseline ARIMA(1,0,2)**: Primo modello lineare non stagionale.
4. **SARIMAX(1,0,1)x(0,1,1)₁₂ Avanzato con Esogene**: Modello completo con stagionalità annuale ed esogene meteorologiche (*cloud cover*, *global radiation*, *mean temperature*).
5. **Analisi dei Residui**: Verifica della distribuzione gaussiana e casuale del rumore residuo (KDE).

---

## 📂 Struttura del Repository

```
.
├── milan_bot_fresh/      # Codice Rasa, NLU, custom actions, Telegram webhook e dataset prodotti
├── bert26/               # Notebook Colab/locali BERT, script di creazione e dataset recensioni
├── sna/                  # Script Python, notebook ed esecuzione analisi del grafo TV Show
├── NLP/                  # Notebooks, immagini, script di analisi e sorgenti LaTeX della tesina NLP
├── AD26/                 # Notebook di Analisi Descrittiva, grafici climatologici e relazione descrittiva
├── classificazione26/    # Notebook di Classificazione Binaria, pipeline anti-leakage, immagini e relazioni
├── clustering26/         # Notebook di Clustering (K-Means, Hierarchical, DBSCAN), PCA e relazioni
├── serieTemporali/       # Notebook di Time Series Analysis (SARIMAX), dataset ed esecuzione
├── Python26.pdf          # Documentazione e materiale didattico/progetto Python
└── README.md             # Documento di sintesi generale del repository
```

---

## ✒️Erxhes Dedja
