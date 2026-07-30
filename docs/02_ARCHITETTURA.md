# Documento

02_ARCHITETTURA.md

Versione: 1.0  
Stato: APPROVATO  
Ultimo aggiornamento: 30/07/2026

Autore: Marco Antonio De Pietro

Progetto: Vacanze Sicure nel Salento

---

# Architettura della Piattaforma

## Introduzione

La piattaforma "Vacanze Sicure nel Salento" è progettata secondo un'architettura modulare, scalabile e database-first.

Ogni componente opera in maniera indipendente ma comunica attraverso servizi condivisi e un database centralizzato.

---

# Principi Architetturali

L'architettura è basata sui seguenti principi:

- Database First
- Modularità
- Scalabilità
- Multi Struttura
- Multi Utente
- AI Native
- API First
- Sicurezza
- Configurazione centralizzata

---

# Struttura generale

La piattaforma è composta dai seguenti moduli.

```
                    VACANZE SICURE NEL SALENTO
──────────────────────────────────────────────────────────

                Portale Pubblico
                       │
                       ▼
                Booking Engine
                       │
                       ▼
                     CRM
                       │
                       ▼
                      PMS
                       │
      ┌────────────────┼─────────────────┐
      ▼                ▼                 ▼

 Revenue       Channel Manager      AI Assistant

      ▼                ▼                 ▼

          API REST / Database
```

---

# Core della piattaforma

Il cuore del sistema è costituito dal PMS.

Tutti gli altri moduli comunicano con esso.

---

# Moduli

## PMS

Gestisce:

- strutture
- unità ricettive
- disponibilità
- prenotazioni
- ospiti
- check-in
- check-out

---

## CRM

Gestisce:

- clienti
- preventivi
- offerte
- storico contatti
- marketing

---

## Booking Engine

Gestisce:

- prenotazioni dirette
- disponibilità
- pagamenti
- conferme

---

## AI Assistant

L'AI rappresenta un componente nativo della piattaforma.

Supporta:

- preventivi
- email
- WhatsApp
- analisi dati
- suggerimenti
- revenue management
- assistenza operativa

---

## Revenue Management

Gestisce:

- Rack Rate
- sconti
- offerte
- prezzi dinamici
- statistiche

---

## Channel Manager

Sincronizza:

- Booking.com
- Airbnb
- Holidu
- Vrbo
- altri OTA

---

## Portale Turistico

Permette:

- ricerca strutture
- informazioni sul territorio
- eventi
- itinerari
- esperienze

---

# Database

La piattaforma utilizza un database relazionale.

Il database rappresenta l'unica fonte ufficiale dei dati.

Tutte le configurazioni vengono lette dal database.

---

# API

Ogni modulo comunica tramite API interne.

Le API permettono future integrazioni con software esterni.

---

# Sicurezza

Sono previsti:

- autenticazione
- autorizzazioni
- ruoli
- log operazioni
- backup
- audit

---

# Struttura delle cartelle

```
src/

    core/

    database/

    crm/

    pms/

    booking/

    ai/

    revenue/

    reports/

    api/

    portal/

    utilities/
```

---

# Workflow generale

```
Richiesta Cliente

↓

CRM

↓

Preventivo AI

↓

Prenotazione

↓

PMS

↓

Check-in

↓

Soggiorno

↓

Check-out

↓

CRM

↓

Marketing
```

---

# Evoluzioni future

La piattaforma è progettata per supportare:

- App Android
- App iOS
- API Pubbliche
- Intelligenza Artificiale avanzata
- Dashboard Business Intelligence
- Gestione multi-azienda

---

# Conclusioni

L'architettura è progettata per garantire:

- semplicità
- modularità
- espandibilità
- elevate prestazioni
- sicurezza
- manutenzione facilitata

Ogni nuovo modulo dovrà rispettare integralmente questa architettura.
