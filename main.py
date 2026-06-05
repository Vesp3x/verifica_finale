import streamlit as st
import pandas as pd
import joblib
import json
from urllib.request import urlopen


# ==============================
# CARICAMENTO MODELLO ED ENCODER
# ==============================

model = joblib.load("lightgbm_best_model.pkl")
encoder = joblib.load("ordinal_encoder.pkl")


# ==============================
# COLONNE DEL MODELLO
# ==============================

FEATURE_COLUMNS = [
    "year",
    "manufacturer",
    "model",
    "condition",
    "cylinders",
    "fuel",
    "odometer",
    "title_status",
    "transmission",
    "drive",
    "size",
    "type",
    "paint_color",
    "state"
]

CATEGORICAL_COLUMNS = [
    "manufacturer",
    "model",
    "condition",
    "cylinders",
    "fuel",
    "title_status",
    "transmission",
    "drive",
    "size",
    "type",
    "paint_color",
    "state"
]


# ==============================
# LISTA MARCHE PRESENTI NEL DATASET
# ==============================

MARCHE_AUTO = [
    "ford",
    "ram",
    "kia",
    "toyota",
    "chevrolet",
    "volkswagen",
    "lincoln",
    "volvo",
    "bmw",
    "acura",
    "chrysler",
    "buick",
    "nissan",
    "dodge",
    "jeep",
    "hyundai",
    "jaguar",
    "gmc",
    "honda",
    "cadillac",
    "mazda",
    "audi",
    "mercedes-benz",
    "lexus",
    "mitsubishi",
    "infiniti",
    "fiat",
    "mini",
    "porsche",
    "datsun",
    "subaru",
    "tesla",
    "harley-davidson",
    "alfa-romeo",
    "rover"
]


# ==============================
# DIZIONARI ITALIANO -> MODELLO
# ==============================

CONDIZIONI_MAP = {
    "Sconosciute": "Unknown",
    "Nuova": "new",
    "Come nuova": "like new",
    "Eccellenti": "excellent",
    "Buone": "good",
    "Discrete": "fair",
    "Da recupero / molto danneggiata": "salvage"
}

CILINDRI_MAP = {
    "Sconosciuto": "Unknown",
    "3 cilindri": "3 cylinders",
    "4 cilindri": "4 cylinders",
    "5 cilindri": "5 cylinders",
    "6 cilindri": "6 cylinders",
    "8 cilindri": "8 cylinders",
    "10 cilindri": "10 cylinders",
    "12 cilindri": "12 cylinders",
    "Altro": "other"
}

CARBURANTE_MAP = {
    "Benzina": "gas",
    "Diesel": "diesel",
    "Ibrida": "hybrid",
    "Elettrica": "electric",
    "Altro": "other"
}

STATO_LEGALE_MAP = {
    "Regolare": "clean",
    "Ricostruita": "rebuilt",
    "Da recupero": "salvage",
    "Con vincolo / pegno": "lien",
    "Documenti mancanti": "missing",
    "Solo per pezzi di ricambio": "parts only"
}

CAMBIO_MAP = {
    "Automatico": "automatic",
    "Manuale": "manual",
    "Altro": "other"
}

TRAZIONE_MAP = {
    "Sconosciuta": "Unknown",
    "Trazione anteriore": "fwd",
    "Trazione posteriore": "rwd",
    "Trazione integrale / 4x4": "4wd"
}

DIMENSIONE_MAP = {
    "Sconosciuta": "Unknown",
    "Molto piccola": "sub-compact",
    "Compatta": "compact",
    "Media": "mid-size",
    "Grande": "full-size"
}

TIPO_VEICOLO_MAP = {
    "Sconosciuto": "Unknown",
    "Berlina": "sedan",
    "SUV": "SUV",
    "Camion / truck": "truck",
    "Pick-up": "pickup",
    "Coupé": "coupe",
    "Hatchback": "hatchback",
    "Station wagon": "wagon",
    "Cabriolet": "convertible",
    "Monovolume piccola": "mini-van",
    "Van / furgone": "van",
    "Bus": "bus",
    "Fuoristrada": "offroad",
    "Altro": "other"
}

COLORE_MAP = {
    "Sconosciuto": "Unknown",
    "Nero": "black",
    "Bianco": "white",
    "Argento": "silver",
    "Grigio": "grey",
    "Rosso": "red",
    "Blu": "blue",
    "Verde": "green",
    "Marrone": "brown",
    "Giallo": "yellow",
    "Arancione": "orange",
    "Viola": "purple",
    "Personalizzato": "custom"
}


# ==============================
# DIZIONARI MODELLO -> ITALIANO
# ==============================

CONDIZIONI_INV = {v: k for k, v in CONDIZIONI_MAP.items()}
CILINDRI_INV = {v: k for k, v in CILINDRI_MAP.items()}
CARBURANTE_INV = {v: k for k, v in CARBURANTE_MAP.items()}
STATO_LEGALE_INV = {v: k for k, v in STATO_LEGALE_MAP.items()}
CAMBIO_INV = {v: k for k, v in CAMBIO_MAP.items()}
TRAZIONE_INV = {v: k for k, v in TRAZIONE_MAP.items()}
DIMENSIONE_INV = {v: k for k, v in DIMENSIONE_MAP.items()}
TIPO_VEICOLO_INV = {v: k for k, v in TIPO_VEICOLO_MAP.items()}
COLORE_INV = {v: k for k, v in COLORE_MAP.items()}


# ==============================
# FUNZIONI UTILI
# ==============================

def normalizza_testo(valore):
    if valore is None or valore == "":
        return "Unknown"
    return str(valore).strip().lower()


def gestisci_categorie_sconosciute(df):
    """
    Evita errori se l'utente inserisce una categoria mai vista durante il training.
    Se possibile sostituisce con 'Unknown'.
    """

    if not hasattr(encoder, "categories_"):
        return df

    df = df.copy()

    for colonna, categorie in zip(CATEGORICAL_COLUMNS, encoder.categories_):
        categorie_set = set(categorie)
        valore = df.loc[0, colonna]

        if valore not in categorie_set:
            if "Unknown" in categorie_set:
                df.loc[0, colonna] = "Unknown"
            elif "unknown" in categorie_set:
                df.loc[0, colonna] = "unknown"
            else:
                df.loc[0, colonna] = categorie[0]

    return df


def predici_prezzo(df):
    df_model = df.copy()

    df_model = gestisci_categorie_sconosciute(df_model)

    df_model[CATEGORICAL_COLUMNS] = encoder.transform(
        df_model[CATEGORICAL_COLUMNS]
    )

    df_model = df_model[FEATURE_COLUMNS]

    predizione = model.predict(df_model)

    return predizione[0]


@st.cache_data(ttl=60 * 60 * 6)
def ottieni_tasso_cambio_usd_eur():
    """
    Recupera il cambio USD -> EUR aggiornato usando Frankfurter.
    Frankfurter non richiede API key e usa tassi di riferimento aggiornati giornalmente.

    Se la connessione non funziona, usa un tasso di fallback così l'app resta utilizzabile.
    """

    tasso_fallback = 0.92

    try:
        url = "https://api.frankfurter.dev/v1/latest?base=USD&symbols=EUR"

        with urlopen(url, timeout=5) as risposta:
            dati = json.loads(risposta.read().decode("utf-8"))

        tasso = float(dati["rates"]["EUR"])
        data_cambio = dati.get("date", "data non disponibile")

        return tasso, data_cambio, False

    except Exception:
        return tasso_fallback, "fallback", True


def converti_dollari_in_euro(importo_dollari, tasso_usd_eur):
    return float(importo_dollari) * float(tasso_usd_eur)


def formatta_euro(importo):
    # Formato italiano: €12.345 invece di €12,345
    return f"€{importo:,.0f}".replace(",", ".")


def crea_riepilogo_italiano(df):
    """
    Crea una tabella leggibile per l'utente finale.
    Qui mostriamo le etichette in italiano.
    """

    riga = df.iloc[0]

    riepilogo = {
        "Anno": int(riga["year"]),
        "Marca": riga["manufacturer"],
        "Modello": riga["model"],
        "Condizioni": CONDIZIONI_INV.get(riga["condition"], riga["condition"]),
        "Cilindri": CILINDRI_INV.get(riga["cylinders"], riga["cylinders"]),
        "Carburante": CARBURANTE_INV.get(riga["fuel"], riga["fuel"]),
        "Chilometri percorsi": int(riga["odometer"]),
        "Stato legale": STATO_LEGALE_INV.get(riga["title_status"], riga["title_status"]),
        "Cambio": CAMBIO_INV.get(riga["transmission"], riga["transmission"]),
        "Trazione": TRAZIONE_INV.get(riga["drive"], riga["drive"]),
        "Dimensione": DIMENSIONE_INV.get(riga["size"], riga["size"]),
        "Tipo veicolo": TIPO_VEICOLO_INV.get(riga["type"], riga["type"]),
        "Colore": COLORE_INV.get(riga["paint_color"], riga["paint_color"]),
        "Stato USA": riga["state"]
    }

    return pd.DataFrame(
        list(riepilogo.items()),
        columns=["Campo", "Valore inserito"]
    )

# ==============================
# INTERFACCIA STREAMLIT
# ==============================

st.set_page_config(
    page_title="Valutatore Auto Usate",
    page_icon="🚗",
    layout="wide"
)

# ==============================
# STILE CSS
# ==============================

st.markdown(
    """
    <style>
div.stButton > button:first-child {
        width: 100%;
        height: 140px;      
        font-size: 60px !important;    
        font-weight: 900;
        border-radius: 25px;
        background-color: #16a34a;
        color: white;
        border: 3px solid #15803d;
        box-shadow: 0px 8px 18px rgba(22, 163, 74, 0.35);
        transition: all 0.2s ease-in-out;
    }

    div.stButton > button:first-child p {
        font-size: 60px !important;
    }

    div.stButton > button:first-child:hover {
        background-color: #15803d;
        color: white;
        border: 3px solid #166534;
        transform: scale(1.01);
    }

    div.stButton > button:first-child:active {
        background-color: #166534;
        color: white;
        border: 3px solid #14532d;
    }

    .range-box {
        padding: 35px;
        border-radius: 22px;
        background: linear-gradient(135deg, #064e3b, #16a34a);
        text-align: center;
        margin-top: 25px;
        margin-bottom: 25px;
        border: 4px solid #bbf7d0;
        box-shadow: 0px 10px 24px rgba(0, 0, 0, 0.22);
    }

    .range-title {
        color: #ffffff;
        font-size: 72px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .range-value {
        color: #fef08a;
        font-size: 52px;
        font-weight: 950;
        margin-bottom: 10px;
    }

    .range-subtitle {
        color: #dcfce7;
        font-size: 20px;
        font-weight: 500;
    }

    .info-box {
        padding: 22px;
        border-radius: 18px;
        background-color: #eff6ff;
        border: 2px solid #bfdbfe;
        color: #1e3a8a;
        margin-bottom: 25px;
    }

    .info-box h4 {
        color: #1e40af;
        margin-bottom: 8px;
    }

    .info-box p {
        color: #1e3a8a;
        font-size: 17px;
        margin-bottom: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ==============================
# TITOLO
# ==============================

st.title("Valutatore di Auto 🚗 Usate di Avocado 🥑 TEAM")

st.markdown(
    """
    <div class="info-box">
        <h4>Inserisci i dati dell'auto dalla barra laterale</h4>
        <p>
            Il programma restituirà un range stimato del valore dell'auto.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ==============================
# SIDEBAR INPUT IN ITALIANO
# ==============================

st.sidebar.header("Inserisci i dati della tua auto!")

manufacturer = st.sidebar.selectbox(
    "Marca",
    MARCHE_AUTO
)

car_model = st.sidebar.text_input(
    "Modello",
    placeholder="Esempio: civic, accord, mazda3 i"
)

year = st.sidebar.number_input(
    "Anno di produzione",
    min_value=1900,
    max_value=2026,
    value=2015,
    step=1
)

odometer = st.sidebar.number_input(
    "Chilometri percorsi",
    min_value=0,
    max_value=1000000,
    value=100000,
    step=1000
)

condition_it = st.sidebar.selectbox(
    "Condizioni dell'auto",
    list(CONDIZIONI_MAP.keys())
)

cylinders_it = st.sidebar.selectbox(
    "Numero di cilindri",
    list(CILINDRI_MAP.keys())
)

fuel_it = st.sidebar.selectbox(
    "Tipo di alimentazione",
    list(CARBURANTE_MAP.keys())
)

title_status_it = st.sidebar.selectbox(
    "Stato legale del veicolo",
    list(STATO_LEGALE_MAP.keys())
)

transmission_it = st.sidebar.selectbox(
    "Tipo di cambio",
    list(CAMBIO_MAP.keys())
)

drive_it = st.sidebar.selectbox(
    "Tipo di trazione",
    list(TRAZIONE_MAP.keys())
)

size_it = st.sidebar.selectbox(
    "Dimensione del veicolo",
    list(DIMENSIONE_MAP.keys())
)

vehicle_type_it = st.sidebar.selectbox(
    "Tipo di veicolo",
    list(TIPO_VEICOLO_MAP.keys())
)

paint_color_it = st.sidebar.selectbox(
    "Colore dell'auto",
    list(COLORE_MAP.keys())
)

state = st.sidebar.text_input(
    "Stato USA",
    placeholder="Esempio: ca, ny, fl, oh"
)


# ==============================
# CONVERSIONE ITALIANO -> MODELLO
# ==============================

dati_auto = {
    "year": float(year),
    "manufacturer": manufacturer,
    "model": normalizza_testo(car_model),
    "condition": CONDIZIONI_MAP[condition_it],
    "cylinders": CILINDRI_MAP[cylinders_it],
    "fuel": CARBURANTE_MAP[fuel_it],
    "odometer": float(odometer),
    "title_status": STATO_LEGALE_MAP[title_status_it],
    "transmission": CAMBIO_MAP[transmission_it],
    "drive": TRAZIONE_MAP[drive_it],
    "size": DIMENSIONE_MAP[size_it],
    "type": TIPO_VEICOLO_MAP[vehicle_type_it],
    "paint_color": COLORE_MAP[paint_color_it],
    "state": normalizza_testo(state)
}

df_input = pd.DataFrame([dati_auto], columns=FEATURE_COLUMNS)

# ==============================
# PULSANTE PREDIZIONE IN ALTO
# ==============================

col1, col2, col3 = st.columns([1, 2.5, 1])

# 2. Utilizziamo il blocco 'with' per dire a Streamlit di scrivere nella colonna 2
with col2:
    # Inseriamo il pulsante interattivo
    bottone_calcola = st.button("Calcola Valore Stimato", use_container_width=True)

# 3. Gestione del click sul pulsante
if bottone_calcola:
    try:
        # Il modello restituisce una stima in dollari, quindi convertiamo l'output in euro.
        valore_stimato_usd = predici_prezzo(df_input)

        valore_minimo_usd = max(0, valore_stimato_usd - 1500)
        valore_massimo_usd = valore_stimato_usd + 1500

        tasso_usd_eur, data_cambio, usa_fallback = ottieni_tasso_cambio_usd_eur()

        valore_stimato_eur = converti_dollari_in_euro(valore_stimato_usd, tasso_usd_eur)
        valore_minimo_eur = converti_dollari_in_euro(valore_minimo_usd, tasso_usd_eur)
        valore_massimo_eur = converti_dollari_in_euro(valore_massimo_usd, tasso_usd_eur)

        st.success("Predizione completata con successo!")

        st.markdown(
            f"""
            <div class="range-box">
                <div class="range-title">
                    Valore stimato dell'auto usata
                </div>
                <div class="range-value">
                    {formatta_euro(valore_minimo_eur)} - {formatta_euro(valore_massimo_eur)}
                </div>
                <div class="range-subtitle">
                    Range stimato sulla base dei dati inseriti.<br>
                    Ma Yuri ti consiglia {formatta_euro(valore_stimato_eur)}.<br>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as errore:
        st.error("Si è verificato un errore durante la predizione.")
        st.exception(errore)


st.divider()


# ==============================
# RIEPILOGO RAPIDO
# ==============================

st.subheader("📌 Riepilogo rapido")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Marca", manufacturer)

with col2:
    st.metric("Anno", int(year))

with col3:
    st.metric("Chilometri", f"{int(odometer):,}".replace(",", "."))

with col4:
    st.metric("Alimentazione", fuel_it)


st.divider()


# ==============================
# RIEPILOGO DATI INSERITI IN BASSO
# ==============================

st.subheader("📋 Riepilogo dati inseriti")

riepilogo_italiano = crea_riepilogo_italiano(df_input)

st.dataframe(
    riepilogo_italiano,
    use_container_width=True,
    hide_index=True
)


# ==============================
# DATI TECNICI PER IL MODELLO
# ==============================

with st.expander("🔧 Visualizza dati tecnici inviati al modello"):
    st.write(
        "Questa tabella mostra i dati nel formato originale richiesto dal modello, "
        "quindi con valori in inglese."
    )

    st.dataframe(
        df_input,
        use_container_width=True
    )