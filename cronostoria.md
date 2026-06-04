# Progetto Machine Learning
## GRUPPO 2 | Giorno 1 (03/06/2026)

### 📌 Informazioni Generali
* **Progetto:** Predizione del prezzo di auto usate
* **Data:** 03 Giugno 2026
* **Team di Sviluppo:** Gruppo 2

---

### 📝 Attività Svolte e Assegnazioni

#### 👥 Selezione della traccia e reperimento dei dati
* **Assegnazione:** *Valutazione di gruppo*
* **Descrizione:** Scelta iniziale del tema progettuale tra quelli proposti, seguita da una ricerca sul web per individuare il dataset più idoneo. È stata verificata la struttura e la qualità delle caratteristiche (*features*) dei diversi dataset disponibili su Kaggle e altre piattaforme. In questa fase iniziale, ogni membro del team ha proposto almeno un dataset, contribuendo attivamente alla scelta finale del file.

#### 🔧 Configurazione dell'ambiente di lavoro
* **Assegnazione:** *Diego*
* **Descrizione:** Creazione del repository remoto (GitHub) e successivo invito ai vari membri del team per abilitare la collaborazione e il controllo di versione del codice.

#### 📄 Redazione del file README
* **Assegnazione:** *Antonio*
* **Descrizione:** Scrittura del documento introduttivo contenente una breve descrizione dello scopo del progetto, il link alla fonte dei dati di addestramento e la roadmap strutturata in 3 macro-fasi:
  1. Pulizia e pre-elaborazione del dataset.
  2. Addestramento e valutazione di uno o più modelli di Machine Learning.
  3. Sviluppo di un'interfaccia utente finale che permetta di predire il prezzo di un'auto sulla base delle caratteristiche inserite.

#### 📊 Analisi esplorativa e Data Cleaning
* **Assegnazione:** *Roberto*
* **Descrizione:** Analisi approfondita dei dati tramite la libreria `Pandas` ed identificazione delle colonne poco informative o ridondanti, che sono state successivamente rimosse per ottimizzare le prestazioni complessive dei modelli.

#### 💾 Esportazione del dataset ottimizzato
* **Assegnazione:** *Luigi*
* **Descrizione:** Creazione, formattazione e salvataggio del file CSV finale ridotto e standardizzato, denominato `vehicles_dataset.csv`, pronto per le successive fasi di training.

* **Eliminazione dei valori nulli:** Per la gestione dei dati mancanti si è deciso di procedere con due approcci differenti in base all'importanza della caratteristica:
  * *La Marca dell'Auto:* Se in un annuncio manca il nome del produttore (ad esempio se non sappiamo se l'auto sia una Ford o una Fiat), quella riga viene completamente eliminata.
  * *Lo Stato dell'Auto:* Formazioni come lo stato di usura dell'auto (eccellente, buono, carrozzeria da rivedere) presentano molti valori mancanti. In questo caso si è preferito invece sostituire i *NaN* con la stringa `'Unknown'`; questo perché se cancellassimo tutte le righe perderemmo gran parte del dataset, privando il modello di altre informazioni utili (come l'anno o i chilometri).

* **Visualizzazione grafica:** È stata realizzata una semplice visualizzazione tramite grafici a barre (*bar plot*) per analizzare i brand presenti nel dataset. Nello specifico, sono stati messi a confronto il numero di modelli unici per ciascuna marca e il numero complessivo di modelli (compresi i duplicati) registrati per ciascun brand.

* **Addestramento dei modelli:** Sono stati scelti 4 modelli da addestrare in modo tale da valutare per ciascuno di essi le performance in termini di **MSE**, **RMSE** e **$R^2$**. In particolare, sono stati impiegati:
  * **XGBoost**
  * **LightGBM**
  * **CatBoost**
  * **Random Forest**
* **Addestramento dei modelli:** In particolare è necessario gestire le colonne categoriche Stringhe attraverso tecniche quali il one hot encoding, label encoding o altri metodi che permettano di gestire valori non numerici.

## GRUPPO 2 | Giorno 2 (04/06/2026)

  *  **Rimozione degli outlier:** Attraverso la visualizzazione con dei boxplot viene visualizzata la distribuzione dei valori di prezzo, e successivamente si è     scelto di mantenere solo le auto i cui prezzi rientrano nel range 500-100000 $.
  *  **Bar plot dei prezzi :** In questi grafici si può apprezzare il prezzo medio per ciascun brand produttore

  *  Dopo la rimozione degli outlier, completata la pulizia dei valori nulli e la trasformazione dei dati stringa, siamo passati all'addestramento dei modelli

#### 📊 Addestramento dei modelli
* **Assegnazione:** *Diego*
* **Descrizione:** Modello CatBoost, un modello progettato per gestire in modo nativo le variabili categoriali, evitando la necessità di una pre‑elaborazione pesante come il one‑hot encoding.

* In una prima fase ho eseguito una serie di test con una configurazione di iperparametri leggera, con l’obiettivo di ottenere rapidamente una valutazione preliminare delle prestazioni del modello, pur consapevole che il    risultato sarebbe stato meno accurato. Dopo aver osservato un miglioramento significativo rispetto al modello precedente, in particolare grazie alla rimozione degli outlier, che ha stabilizzato la distribuzione dei        prezzi sono passato all'ottimizzazione.

* In questa seconda fase ho utilizzato Optuna per effettuare una ricerca più ampia e sistematica degli iperparametri ottimali. L’obiettivo era ridurre ulteriormente l’errore del modello, esplorando uno spazio di ricerca     più esteso, così da ottenere una configurazione più performante e robusta.
     
