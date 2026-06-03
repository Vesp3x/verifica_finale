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
  * *La Marca dell'Auto:* Se in un annuncio manca il nome del produttore (ad esempio se non sappiamo se l'auto sia una Ford o una Fiat), quella riga viene completamente eliminata. L'operazione si compone di due passaggi logici concatenati: la rimozione del record incompleto dalle caratteristiche del veicolo e il successivo riallineamento con la tabella dei prezzi.
  * *Lo Stato dell'Auto:* Formazioni come lo stato di usura dell'auto (eccellente, buono, carrozzeria da rivedere) presentano molti valori mancanti. In questo caso si è preferito invece sostituire i *NaN* con la stringa `'Unknown'`; questo perché se cancellassimo tutte le righe perderemmo gran parte del dataset, privando il modello di altre informazioni utili (come l'anno o i chilometri).

* **Visualizzazione grafica:** È stata realizzata una semplice visualizzazione tramite grafici a barre (*bar plot*) per analizzare i brand presenti nel dataset. Nello specifico, sono stati messi a confronto il numero di modelli unici per ciascuna marca e il numero complessivo di modelli (compresi i duplicati) registrati per ciascun brand.
