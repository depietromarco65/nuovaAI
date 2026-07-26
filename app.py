# ==========================================================
# CRM A CASA DI AMICI
# APP PRINCIPALE
# ==========================================================

import streamlit as st

from config import APP_TITLE, VERSIONE
from database import carica_database

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🏡",
    layout="wide"
)

st.title(APP_TITLE)
st.caption(f"Versione {VERSIONE}")

try:

    df = carica_database()

    st.success(f"Database caricato correttamente.")

    st.info(f"Record presenti: {len(df)}")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

except Exception as e:

    st.error(str(e))
