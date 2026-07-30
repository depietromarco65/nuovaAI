# Documento

05_DATA_DICTIONARY.md

Versione: 1.0
Stato: APPROVATO
Ultimo aggiornamento: 30/07/2026

Autore:
Marco Antonio De Pietro

Progetto:
Vacanze Sicure nel Salento

---

# Data Dictionary

## Introduzione

Il Data Dictionary rappresenta il catalogo ufficiale del database.

Ogni tabella presente nella piattaforma deve essere documentata in questo file prima della sua realizzazione.

Lo scopo del documento è garantire uniformità, coerenza e facilità di manutenzione.

---

# Standard di progettazione

Per ogni tabella saranno definiti:

- Nome
- Descrizione
- Chiave primaria
- Campi
- Tipo dati
- Lunghezza
- Obbligatorietà
- Valore predefinito
- Chiavi esterne
- Indici
- Vincoli
- Note

---

# Convenzioni

## Chiave primaria

Tutte le tabelle utilizzano:

id

INTEGER AUTOINCREMENT

---

## Date

Formato ISO

YYYY-MM-DD

---

## Data e ora

YYYY-MM-DD HH:MM:SS

---

## Boolean

0 = False

1 = True

---

## Testo

UTF-8

---

# Elenco Tabelle

## AREA SISTEMA

CONFIGURAZIONI

RUOLI

PERMESSI

UTENTI

LOG

AUDIT

BACKUP

---

## AREA STRUTTURE

STRUTTURE

UNITA_RICETTIVE

TIPOLOGIE_UNITA

SERVIZI

DOTAZIONI

FOTO

PREZZI

STAGIONI

LISTINI

---

## AREA PRENOTAZIONI

PRENOTAZIONI

PREVENTIVI

DISPONIBILITA

CALENDARIO

CHECKIN

CHECKOUT

OSPITI

DOCUMENTI

---

## AREA CLIENTI

CLIENTI

CONTATTI

COMUNICAZIONI

NEWSLETTER

BLACKLIST

---

## AREA PAGAMENTI

PAGAMENTI

FATTURE

SCADENZE

RIMBORSI

---

## AREA AI

PROMPT

REGOLE_AI

LOG_AI

RISPOSTE_AI

---

## AREA TERRITORIO

PROVINCE

COMUNI

FRAZIONI

MARINE

SPIAGGE

PORTI

TORRI_COSTIERE

PUNTI_INTERESSE

EVENTI

---

# Regole

Nessuna tabella potrà essere implementata senza essere prima documentata nel presente Data Dictionary.

Ogni modifica dovrà essere registrata nel CHANGELOG.
