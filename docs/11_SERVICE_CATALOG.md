# Documento

11_SERVICE_CATALOG.md

Versione: 1.0
Stato: APPROVATO

---

# Service Catalog

## Introduzione

Il Service Catalog rappresenta il catalogo ufficiale di tutti i servizi esposti dalla piattaforma.

Ogni funzionalità del sistema dovrà essere implementata come un servizio indipendente.

Nessun modulo accederà direttamente al database.

L'accesso ai dati avverrà esclusivamente attraverso i servizi ufficiali.

---

# Architettura

```

Utente

↓

Frontend

↓

API Gateway

↓

Service Catalog

↓

Database

```

---

# Standard

Ogni servizio possiede:

- identificativo
- dominio
- nome
- descrizione
- input
- output
- permessi richiesti
- log
- audit

---

# Convenzione di naming

I servizi utilizzano il formato:

```

dominio.azione()

```

Esempio

```

booking.verificaDisponibilita()

crm.cercaCliente()

pms.creaStruttura()

```

---

# Domini

## PMS

Gestione strutture

---

## CRM

Gestione clienti

---

## Booking

Prenotazioni

---

## Revenue

Prezzi

---

## Payments

Pagamenti

---

## AI

Servizi AI

---

## Territory

Territorio

---

## Notifications

Notifiche

---

# Regole

Ogni servizio deve essere:

Idempotente quando possibile.

Documentato.

Versionato.

Testabile.

Tracciabile.
