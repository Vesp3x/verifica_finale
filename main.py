import joblib
import pandas as pd
import numpy as np

# Caricamento modello ed encoder
model = joblib.load("lightgbm_best_model.pkl")
encoder = joblib.load("ordinal_encoder.pkl")

# Colonne esatte usate nel CSV di training
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

# Colonne numeriche
NUMERIC_COLUMNS = ["year", "odometer"]

# Colonne categoriche da passare all'encoder
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


def chiedi_input(testo, default="Unknown"):
    valore = input(testo).strip()

    if valore == "":
        return default

    return valore.lower()


def chiedi_float(testo):
    while True:
        valore = input(testo).strip().replace(",", ".")

        try:
            return float(valore)
        except ValueError:
            print("Valore non valido. Inserisci un numero.")


def prepara_input_auto():
    print("\nBenvenuto nel programma per stimare il valore della tua auto usata!\n")

    dati = {}

    dati["manufacturer"] = chiedi_input(
        "Inserisci la marca della tua auto, ad esempio: mazda, honda, ford, bmw\n> "
    )

    dati["model"] = chiedi_input(
        "Inserisci il modello della tua auto, ad esempio: civic, accord, mazda3 i\n> "
    )

    dati["year"] = chiedi_float(
        "Inserisci l'anno di produzione della tua auto, ad esempio: 2016\n> "
    )

    dati["odometer"] = chiedi_float(
        "Quanti km/miglia ha percorso la tua auto?\n> "
    )

    dati["condition"] = chiedi_input(
        "Inserisci le condizioni dell'auto.\n"
        "Esempi: new, like new, excellent, good, fair, salvage, Unknown\n> "
    )

    dati["cylinders"] = chiedi_input(
        "Inserisci il numero di cilindri.\n"
        "Esempi: 4 cylinders, 6 cylinders, 8 cylinders, Unknown\n> "
    )

    dati["fuel"] = chiedi_input(
        "Inserisci il tipo di carburante.\n"
        "Esempi: gas, diesel, electric, hybrid, other\n> "
    )

    dati["title_status"] = chiedi_input(
        "Inserisci lo stato legale del veicolo.\n"
        "Esempi: clean, rebuilt, salvage, lien, missing, parts only\n> "
    )

    dati["transmission"] = chiedi_input(
        "Inserisci il cambio.\n"
        "Esempi: automatic, manual, other\n> "
    )

    dati["drive"] = chiedi_input(
        "Inserisci il tipo di trazione.\n"
        "Esempi: fwd, rwd, 4wd, Unknown\n> "
    )

    dati["size"] = chiedi_input(
        "Inserisci la dimensione dell'auto.\n"
        "Esempi: compact, mid-size, full-size, sub-compact, Unknown\n> "
    )

    dati["type"] = chiedi_input(
        "Inserisci il tipo di veicolo.\n"
        "Esempi: sedan, SUV, truck, wagon, coupe, hatchback, mini-van, convertible, other\n> "
    )

    dati["paint_color"] = chiedi_input(
        "Inserisci il colore.\n"
        "Esempi: black, white, silver, blue, red, grey, brown, custom, Unknown\n> "
    )

    dati["state"] = chiedi_input(
        "Inserisci lo stato, come nel dataset.\n"
        "Esempi: ca, ny, fl, oh, tn, ar\n> "
    )

    # Creo DataFrame con lo stesso ordine delle colonne di training
    df = pd.DataFrame([dati], columns=FEATURE_COLUMNS)

    return df


def gestisci_categorie_sconosciute(df):
    """
    Se l'OrdinalEncoder non è stato allenato con handle_unknown,
    una categoria mai vista nel training potrebbe causare errore.

    Questa funzione sostituisce i valori non conosciuti con 'Unknown',
    se 'Unknown' era presente tra le categorie viste dall'encoder.
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
                # Se non esiste Unknown, uso la prima categoria conosciuta
                df.loc[0, colonna] = categorie[0]

    return df


def predici_prezzo(df):
    # Copia del dataframe originale
    df_model = df.copy()

    # Gestione categorie mai viste
    df_model = gestisci_categorie_sconosciute(df_model)

    # Encoding delle colonne categoriche
    df_model[CATEGORICAL_COLUMNS] = encoder.transform(df_model[CATEGORICAL_COLUMNS])

    # Riordino finale delle colonne
    df_model = df_model[FEATURE_COLUMNS]

    # Predizione
    predizione = model.predict(df_model)

    return predizione[0]


while True:
    auto_df = prepara_input_auto()

    print("\nDati inseriti:")
    print(auto_df)

    valore_stimato = predici_prezzo(auto_df)

    print("\n---------------------------------------")
    print(f"Valore stimato dell'auto usata: {valore_stimato:,.2f}")
    print("---------------------------------------\n")

    continua = input("Vuoi stimare un'altra auto? sì/no\n> ").strip().lower()

    if continua not in ["sì", "si", "yes", "y"]:
        print("Programma terminato.")
        break