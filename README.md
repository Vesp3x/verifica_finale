# 🚗 Predizione del Prezzo delle Auto Usate tramite Machine Learning

I Creatori:

Venturini Antonio https://www.linkedin.com/in/antonio-venturini-a34912138/ 

Vespa Diego https://www.linkedin.com/in/diego-vespa-55b970335/

Compagnone Roberto Karol https://www.linkedin.com/in/roberto-karol-compagnone-a05312414/

Scalisi Luigi https://www.linkedin.com/in/luigi-scalisi-8495ba286/

## 🎯 Sunto del Progetto
Questo progetto ha l'obiettivo di sviluppare un sistema predittivo in grado di stimare il corretto valore di mercato di un'auto usata. A partire dall'inserimento di caratteristiche specifiche del veicolo (come marca, anno di immatricolazione, chilometraggio, tipo di carburante e tipologia di cambio), il sistema utilizza un algoritmo di Machine Learning per restituire una stima del prezzo affidabile e in tempo reale.

## 📊 Origine dei Dati
I dati utilizzati per l'addestramento del modello provengono da Kaggle e consistono in un ampio archivio di annunci reali estratti da Craigslist riguardanti il mercato automobilistico statunitense.
* **Link al Dataset:** [Craigslist Cars & Trucks Data](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data/data)

## 🛠️ Fasi del Progetto
L'intero ciclo di sviluppo è stato suddiviso in tre macro-fasi:

1. **Pulizia del Dataset (Data Cleaning)**
   * Rimozione delle colonne superflue non necessarie per l'analisi (es. id, URL, descrizioni testuali, coordinate GPS).
   * Gestione dei valori nulli e degli outlier (es. rimozione di inserzioni con prezzi fasulli o chilometraggi irrealistici).
   * Preparazione delle feature (es. conversione delle miglia in chilometri).

2. **Addestramento del Modello (Machine Learning)**
   * Ingegneria delle feature e codifica dei dati categorici (marca, alimentazione, trasmissione).
   * Divisione del dataset in set di training e testing.
   * Addestramento e ottimizzazione di un modello di regressione capace di prevedere la variabile target (prezzo).

3. **Creazione dell'Interfaccia di Valutazione**
   * Sviluppo di un'interfaccia utente semplice e intuitiva.
   * Tramite la dashboard, l'utente può inserire le caratteristiche della propria auto in appositi form e interrogare direttamente il modello addestrato, ottenendo immediatamente il prezzo di vendita stimato.

## 📖 Dizionario dei Dati (Data Dictionary)

Il dataset finale utilizzato per l'addestramento è composto dalle seguenti feature (variabili):

* **`manufacturer`**: La marca costruttrice del veicolo (es. *Ford, Acura, Buick*).
* **`model`**: Il modello specifico dell'auto (es. *F-150, MDX, F-250 Super Duty*).
* **`year`**: L'anno di produzione o di prima immatricolazione del veicolo.
* **`condition`**: Lo stato di usura generale del veicolo (es. *excellent, good*). I valori non dichiarati negli annunci sono stati raggruppati sotto la categoria *Unknown*.
* **`cylinders`**: La configurazione del motore espressa in numero di cilindri (es. *8 cylinders, 6 cylinders*).
* **`fuel`**: Il tipo di alimentazione o carburante (es. *gas* per benzina, *diesel*, *electric*).
* **`odometer`**: La distanza totale percorsa dal veicolo. 
* **`title_status`**: Lo stato legale e burocratico del certificato di proprietà (es. un titolo *clean* indica un'auto in regola, senza incidenti distruttivi pregressi o problemi legali).
* **`transmission`**: La tipologia di cambio o trasmissione (es. *automatic, manual, other*).
* **`drive`**: Il tipo di trazione del veicolo (*fwd* = trazione anteriore, *rwd* = trazione posteriore, *4wd* = trazione integrale).
* **`size`**: La classe dimensionale del veicolo (es. *full-size, mid-size, compact*).
* **`type`**: La categoria di carrozzeria o segmento di mercato (es. *SUV, truck, pickup, sedan*).
* **`paint_color`**: Il colore esterno della carrozzeria.


## 💻 Manuale d'Uso dell'Applicazione

Il file `app.py` contiene il programma principale e l'architettura logica per l'esecuzione del modello predittivo. L'interfaccia grafica è stata sviluppata sfruttando il framework **Streamlit**.

### 1. Prerequisiti e Avvio
Per avviare l'applicazione in locale, assicurarsi di aver installato le dipendenze necessarie e lanciare il seguente comando all'interno del terminale, posizionandosi nella cartella del progetto:

```bash
streamlit run app.py