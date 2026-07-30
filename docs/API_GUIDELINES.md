# API_GUIDELINES.md

# Vacanze Sicure nel Salento
## Linee guida per lo sviluppo delle API REST

Versione: 1.0.0

---

# Obiettivo

Questo documento definisce le regole obbligatorie per la realizzazione delle API REST della piattaforma.

Ogni endpoint dovrà rispettare queste regole.

---

# Filosofia

Le API devono essere:

- semplici
- sicure
- prevedibili
- documentate
- versionabili
- coerenti

---

# Versionamento

Tutte le API saranno versionate.

Esempio

/api/v1/

In futuro

/api/v2/

---

# Formato

Le API utilizzano esclusivamente JSON.

Request

application/json

Response

application/json

---

# HTTPS

È obbligatorio utilizzare HTTPS.

HTTP non è consentito in produzione.

---

# Autenticazione

Autenticazione tramite JWT.

Ogni richiesta autenticata dovrà contenere

Authorization

Bearer <token>

---

# Autorizzazione

L'autenticazione non implica l'autorizzazione.

Ogni endpoint deve verificare:

- utente
- ruolo
- struttura
- permessi

---

# Multi Tenant

Ogni endpoint deve verificare che il record richiesto appartenga alla struttura autenticata.

Mai fidarsi dell'UUID ricevuto dal client.

---

# UUID

Le API espongono esclusivamente UUID.

Mai utilizzare ID numerici.

---

# Verbi HTTP

GET

lettura

POST

creazione

PUT

aggiornamento completo

PATCH

aggiornamento parziale

DELETE

eliminazione logica

---

# Codici HTTP

200

Operazione eseguita

201

Risorsa creata

204

Nessun contenuto

400

Richiesta errata

401

Non autenticato

403

Accesso negato

404

Risorsa inesistente

409

Conflitto

422

Errore di validazione

500

Errore interno

---

# Naming

Utilizzare nomi plurali.

Corretto

/api/v1/bookings

/api/v1/guests

/api/v1/payments

Errato

/api/v1/getBooking

---

# Paginazione

Le liste devono essere paginabili.

Parametri standard

page

page_size

---

# Ordinamento

Supportare

sort

order

Esempio

sort=arrival_date

order=asc

---

# Filtri

Le ricerche devono essere effettuate tramite query string.

Esempio

/api/v1/bookings?status=confirmed

---

# Errori

Le risposte di errore devono essere coerenti.

Formato

{
    "detail": "Messaggio di errore"
}

---

# Validazione

Ogni input deve essere validato.

Non fidarsi mai dei dati ricevuti.

---

# Logging

Le operazioni importanti devono essere registrate.

---

# Audit

Le operazioni sensibili devono produrre Audit Log.

---

# Performance

Le API devono evitare:

- query duplicate
- N+1 query
- caricamenti inutili

---

# Idempotenza

PUT

PATCH

DELETE

devono essere idempotenti.

---

# Upload

I file devono essere caricati mediante endpoint dedicati.

---

# Download

I documenti devono essere autorizzati prima del download.

---

# Rate Limiting

Applicare limiti alle API pubbliche.

---

# Documentazione

Ogni endpoint dovrà avere:

- descrizione
- parametri
- risposta
- codici errore

---

# Compatibilità

Le nuove versioni delle API non devono rompere la retrocompatibilità quando possibile.

---

# Regola finale

Le API rappresentano il contratto tra frontend e backend.

Una modifica incompatibile richiede una nuova versione delle API.
