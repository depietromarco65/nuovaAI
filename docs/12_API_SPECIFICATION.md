# API SPECIFICATION

Versione: 1.0

Stato: APPROVATO

---

# Introduzione

Tutte le funzionalità della piattaforma sono accessibili esclusivamente tramite API.

Nessun client può accedere direttamente al database.

I client supportati sono:

- Frontend Web
- App Mobile
- AI Assistant
- Portale Proprietario
- Portale Cliente
- OTA Connector
- Channel Manager
- Servizi esterni

---

# Architettura

Client

↓

API Gateway

↓

Authentication

↓

Authorization

↓

Business Service

↓

Repository

↓

Database

---

# Versionamento

Tutte le API saranno versionate.

Esempio

/api/v1/

/api/v2/

---

# Formato dati

JSON UTF-8

---

# Autenticazione

OAuth2

JWT

Refresh Token

---

# Risposta standard

{
    "success": true,
    "data": {},
    "errors": [],
    "warnings": [],
    "execution_time": 15
}

---

# Errori

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

409 Conflict

422 Validation Error

500 Internal Error

---

# Naming

GET

POST

PUT

PATCH

DELETE

---

# Convenzione URL

/api/v1/{dominio}/{servizio}

Esempio

/api/v1/booking/checkAvailability

/api/v1/crm/searchCustomer

/api/v1/revenue/calculatePrice

---

# Logging

Ogni chiamata API registra:

utente

timestamp

indirizzo IP

endpoint

tempo risposta

esito

---

# Rate Limiting

Configurabile.

---

# OpenAPI

Ogni endpoint sarà documentato mediante OpenAPI 3.1.
