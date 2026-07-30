"""
Costanti globali dell'applicazione.

Questo modulo contiene esclusivamente costanti che non cambiano
durante l'esecuzione del programma.
"""

# ==========================================================
# APPLICAZIONE
# ==========================================================

APP_NAME = "Vacanze Sicure nel Salento"
APP_VERSION = "0.1.0"

# ==========================================================
# AMBIENTI
# ==========================================================

ENV_DEVELOPMENT = "development"
ENV_TEST = "test"
ENV_PRODUCTION = "production"

# ==========================================================
# LINGUE
# ==========================================================

LANG_IT = "it"
LANG_EN = "en"
LANG_DE = "de"
LANG_FR = "fr"

DEFAULT_LANGUAGE = LANG_IT

# ==========================================================
# VALUTA
# ==========================================================

DEFAULT_CURRENCY = "EUR"

# ==========================================================
# NAZIONE
# ==========================================================

DEFAULT_COUNTRY = "IT"

# ==========================================================
# TIMEZONE
# ==========================================================

DEFAULT_TIMEZONE = "Europe/Rome"

# ==========================================================
# DATABASE
# ==========================================================

SQLITE = "sqlite"
POSTGRESQL = "postgresql"

# ==========================================================
# STATO RECORD
# ==========================================================

STATUS_ACTIVE = "ACTIVE"
STATUS_INACTIVE = "INACTIVE"

# ==========================================================
# CUSTOMER CARE
# ==========================================================

CHANNEL_EMAIL = "EMAIL"
CHANNEL_PHONE = "PHONE"
CHANNEL_WHATSAPP = "WHATSAPP"
CHANNEL_CHAT = "CHAT"
CHANNEL_AI = "AI"

# ==========================================================
# PRENOTAZIONI
# ==========================================================

BOOKING_PENDING = "PENDING"
BOOKING_CONFIRMED = "CONFIRMED"
BOOKING_CANCELLED = "CANCELLED"
BOOKING_COMPLETED = "COMPLETED"

# ==========================================================
# PAGAMENTI
# ==========================================================

PAYMENT_PENDING = "PENDING"
PAYMENT_PAID = "PAID"
PAYMENT_REFUNDED = "REFUNDED"

# ==========================================================
# LOG
# ==========================================================

LOG_INFO = "INFO"
LOG_WARNING = "WARNING"
LOG_ERROR = "ERROR"
LOG_DEBUG = "DEBUG"
LOG_CRITICAL = "CRITICAL"
