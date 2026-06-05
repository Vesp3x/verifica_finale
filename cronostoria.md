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

#### 💾 Addestramento dei modelli
* **Assegnazione:** *Diego*
* **Descrizione:** Modello CatBoost

  In una prima fase ho eseguito una serie di test con una configurazione di iperparametri leggera, con l’obiettivo di ottenere rapidamente una valutazione preliminare delle prestazioni del modello, pur consapevole che il    risultato sarebbe stato meno accurato. Dopo aver osservato un miglioramento significativo rispetto al modello precedente, in particolare grazie alla rimozione degli outlier, che ha stabilizzato la distribuzione dei        prezzi sono passato all'ottimizzazione.

  In questa seconda fase ho utilizzato Optuna per effettuare una ricerca più ampia e sistematica degli iperparametri ottimali. L’obiettivo era ridurre ulteriormente l’errore del modello, esplorando uno spazio di ricerca     più esteso, così da ottenere una configurazione più performante e robusta.

* **Assegnazione:** *Roberto*
* **Descrizione:** Modello LightGBM

  Ho inizialmente addestrato il modello utilizzando una configurazione di iperparametri volutamente semplice, con l’obiettivo di ottenere una valutazione preliminare delle prestazioni in tempi rapidi. In una fase            successiva ho progressivamente incrementato la complessità degli iperparametri, osservando una riduzione significativa dell’errore man mano che il modello veniva reso più espressivo.   

  Per migliorare ulteriormente il processo di ottimizzazione, ho introdotto Optuna, che mi ha permesso di esplorare in modo sistematico e automatizzato uno spazio di ricerca più ampio. Grazie a questa procedura, è stato     possibile individuare una combinazione di iperparametri più efficace, con un impatto positivo sulle metriche di valutazione e sulla capacità predittiva complessiva del modello LightGBM.
  
* **Assegnazione:** *Luigi*
* **Descrizione:** Modello XGBoost
  Inizialmente sono stati gestiti i valori categorici in particolare attraverso due tecniche: Il one hot encoding per le feature che presentavano una bassa cardinalità, mentre nel caso di model e manufacturer presentando    una elevata quantità di valori unici si è preferito fare un encoding in cui i valori di model e manufacturer sono stati sostituiti con il prezzo medio per modello e per marca. Dopo aver valutato attraverso le metriche     adatte alla regressione si è pensato di fare un tuning dei parametri attraverso Optuna

* **Assegnazione:** *Antonio*
* **Descrizione:** Modello RandomForest

  Ho generato diversi grafici per individuare i veicoli che presentavano le maggiori discrepanze tra il prezzo reale e quello predetto. Dall’osservazione di tali visualizzazioni è emerso che gli errori più elevati erano     associati a marche con una presenza molto limitata nel dataset. La scarsità di dati relativi a questi brand impediva al modello di apprendere in modo adeguato le loro caratteristiche, generando così previsioni poco        accurate.

  Per approfondire il comportamento del modello, ho stato effettuato un ulteriore test aumentando il numero di alberi, con l’obiettivo di migliorare la stabilità delle predizioni. L’incremento del numero di estimatori ha    effettivamente contribuito a rendere il modello più robusto, anche se il problema legato alla scarsità di dati per alcune marche è rimasto un limite strutturale.

  * **Confronto dei modelli:**
  Dal confronto tra i modelli è emerso che il modello LightGBM ha ottenuto le prestazioni migliori, registrando l’errore più basso tra tutti i modelli testati. La sua struttura basata su gradient boosting e la capacità      di gestire in modo efficiente dataset di grandi dimensioni hanno contribuito a renderlo il modello più accurato e stabile per il nostro problema di previsione del prezzo dei veicoli usati.
 
    
  #### 📊 Visualizzazione
  * **Visualizzazione grafica:**
  Per la fase di visualizzazione dei risultati è stato scelto il modello LightGBM, in quanto, tra tutti i modelli testati, è quello che ha ottenuto l’errore più basso.

  Per la realizzazione dell’interfaccia di visualizzazione è stata utilizzata la libreria streamlit che offre widget come slider, selectbox, input numerici e testuali. Un altra caratteristica è l'aggiornamento in tempo      reale, l’interfaccia si aggiorna automaticamente a ogni modifica dei parametri. Tramite questa libreria siamo riusciti a sviluppare un’applicazione interattiva, in grado di offrire un’esperienza dinamica all’utente.

  L’interfaccia consente all’utente di inserire le caratteristiche principali del proprio veicolo come: marca, modello, anno, chilometraggio e altre specifiche e di ottenere in tempo reale una stima del prezzo generata      dal modello LightGBM ottimizzato.


  #### 📄 Presentazione del progetto
  * **power point**
Abbiamo realizzato una presentazione in PowerPoint con l’obiettivo di illustrare in modo chiaro e strutturato tutte le fasi dello sviluppo del nostro modello. La presentazione ripercorre l’intero percorso svolto: dalla selezione e pulizia del dataset, all’addestramento dei modelli, fino alla scelta finale di LightGBM e alla realizzazione dell’interfaccia interattiva. Questo supporto visivo ci permette di comunicare in modo efficace i risultati ottenuti e le motivazioni delle scelte tecniche effettuate.

  

  ## GRUPPO 2 | Giorno 3 (05/06/2026)

#### 📊 Ottimizzazione della visualizzazione degli errori

* **Assegnazione:** *Valutazione di gruppo*
* **Descrizione:** Ogni membro del team ha contribuito all’ottimizzazione della visualizzazione degli errori relativi al proprio modello. Sono stati migliorati i grafici e le analisi comparative per rendere più chiara l’interpretazione delle prestazioni dei diversi algoritmi, evidenziando le differenze tra valori reali e valori predetti.

#### 🔧 Ottimizzazione e riaddestramento del modello migliore

* **Assegnazione:** *Antonio e Roberto*
* **Descrizione:** Sono state apportate le ultime modifiche al modello risultato più performante, ovvero **LightGBM**. Dopo aver perfezionato alcuni aspetti della configurazione e della gestione dei dati, il modello è stato riaddestrato per ottenere una versione finale più stabile e accurata, pronta per essere utilizzata nell’applicazione di previsione.

#### 🖥️ Miglioramento dell’interfaccia di previsione

* **Assegnazione:** *Antonio e Roberto*
* **Descrizione:** È stata prodotta e migliorata la visualizzazione del programma dedicato alla previsione del prezzo dell’auto. L’interfaccia consente all’utente di inserire le caratteristiche principali del veicolo e ottenere una stima del costo in modo semplice, chiaro e interattivo.

#### 📄 Aggiornamento della presentazione del progetto

* **Assegnazione:** *Luigi e Diego*
* **Descrizione:** È stata migliorata e portata avanti la presentazione PowerPoint del progetto. Sono state integrate le ultime modifiche relative ai modelli, alle metriche di valutazione, alla scelta finale di LightGBM e alla visualizzazione dell’interfaccia utente, così da rendere la presentazione più completa e coerente con lo stato finale del lavoro.

      
    

  
