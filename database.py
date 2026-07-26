# ==========================================================
# DATABASE.PY
# Gestione lettura database da GitHub
# ==========================================================

import pandas as pd

from io import StringIO

import requests

from config import RAW_DATABASE_URL


def carica_database():

    """
    Legge il database CSV direttamente dal repository GitHub.
    """

    try:

        risposta = requests.get(
            RAW_DATABASE_URL,
            timeout=20
        )

        risposta.raise_for_status()

        df = pd.read_csv(

            StringIO(risposta.text),

            dtype=str,

            keep_default_na=False,

            encoding="utf-8-sig",

            engine="python",

            on_bad_lines="skip"

        )

        df.columns = [c.strip() for c in df.columns]

        return df

    except Exception as errore:

        raise Exception(
            f"Errore caricamento database:\n{errore}"
        )
