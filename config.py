# ==========================================================
# CONFIGURAZIONE CRM "A CASA DI AMICI"
# ==========================================================

# Repository GitHub

GITHUB_OWNER = "depietromarco65"
GITHUB_REPOSITORY = "nuovaAI"
GITHUB_BRANCH = "main"

# Database

DATABASE_FILE = "database_ospiti.csv"

# URL RAW del database

RAW_DATABASE_URL = (
    f"https://raw.githubusercontent.com/"
    f"{GITHUB_OWNER}/"
    f"{GITHUB_REPOSITORY}/"
    f"{GITHUB_BRANCH}/"
    f"{DATABASE_FILE}"
)

# API GitHub

API_CONTENT_URL = (
    f"https://api.github.com/repos/"
    f"{GITHUB_OWNER}/"
    f"{GITHUB_REPOSITORY}/contents/"
    f"{DATABASE_FILE}"
)

# Titolo applicazione

APP_TITLE = "🏡 CRM - A Casa di Amici"

# Versione

VERSIONE = "1.0"

DATABASE_XLSX = "database_ospiti.xlsx"

BACKUP_FOLDER = "data/backup"

IMPORT_FOLDER = "data/import"

AUTO_BACKUP = True

CHECK_DUPLICATES = True

EMAIL_CORRECTION = True

EMPTY_VALUE = "nd"
