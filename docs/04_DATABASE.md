# Documento

04_DATABASE.md

Versione: 1.0
Stato: APPROVATO
Ultimo aggiornamento: 30/07/2026

Autore:
Marco Antonio De Pietro

Progetto:
Vacanze Sicure nel Salento

---

# Database della piattaforma

## Introduzione

Il database rappresenta il cuore dell'intera piattaforma "Vacanze Sicure nel Salento".

Ogni informazione viene memorizzata, gestita e recuperata esclusivamente tramite il database.

Il software non deve contenere dati hardcoded, ad eccezione delle costanti strettamente necessarie al funzionamento del linguaggio.

---

# Filosofia

La piattaforma adotta il principio:

## Database First

Il database è l'unica fonte ufficiale dei dati.

Ogni modulo della piattaforma utilizza lo stesso database.

---

# Obiettivi

Il database deve garantire:

- integrità dei dati
- sicurezza
- elevate prestazioni
- semplicità di manutenzione
- scalabilità
- tracciabilità delle modifiche

---

# Motore Database

Versione iniziale

SQLite

Versione futura

PostgreSQL

L'intera progettazione dovrà essere compatibile con entrambi.

---

# Convenzioni

## Nomi delle tabelle

Sempre MAIUSCOLI.

Esempio:

```
CLIENTI
PRENOTAZIONI
UNITA_RICETTIVE
STRUTTURE
```

---

## Chiave primaria

Ogni tabella possiede una chiave primaria denominata:

```
id
```

---

## Chiavi esterne

Le chiavi esterne utilizzano sempre il prefisso

```
id_
```

Esempi

```
id_cliente

id_prenotazione

id_struttura

id_unita_ricettiva
```

---

## Date

Le date iniziano sempre con

```
data_
```

Esempio

```
data_checkin

data_checkout

data_creazione
```

---

## Timestamp

I timestamp utilizzano la convenzione

```
created_at

updated_at

deleted_at
```

---

## Boolean

I campi booleani iniziano sempre con

```
is_
```

Esempio

```
is_attiva

is_disponibile

is_online

is_cancellata
```

---

# Integrità Referenziale

Ogni relazione dovrà utilizzare chiavi esterne.

Non saranno ammessi riferimenti testuali tra tabelle.

---

# Normalizzazione

Il database dovrà rispettare almeno la Terza Forma Normale (3NF).

Duplicazioni dei dati dovranno essere evitate.

---

# Indici

Saranno creati indici sulle colonne maggiormente utilizzate.

Ad esempio

- cognome
- email
- telefono
- data_checkin
- data_checkout
- stato_prenotazione

---

# Trigger

I trigger saranno utilizzati esclusivamente per:

- controllo integrità
- aggiornamenti automatici
- audit
- log

Non dovranno contenere logiche applicative complesse.

---

# View

Le viste saranno utilizzate per:

- dashboard
- report
- statistiche
- esportazioni

---

# Backup

Il database dovrà prevedere backup automatici.

Ogni backup dovrà essere versionato.

---

# Audit

Ogni modifica importante dovrà essere registrata.

Saranno memorizzati:

- utente
- data
- ora
- operazione
- tabella
- record modificato

---

# Sicurezza

Le autorizzazioni saranno gestite dall'applicazione.

Il database dovrà impedire la perdita accidentale dei dati.

---

# Struttura logica

Il database sarà suddiviso in macro aree.

## Anagrafiche

- STRUTTURE
- UNITA_RICETTIVE
- CLIENTI
- OSPITI
- UTENTI

---

## Operatività

- PRENOTAZIONI
- PREVENTIVI
- PAGAMENTI
- FATTURE
- CONTRATTI

---

## CRM

- CONTATTI
- COMUNICAZIONI
- CAMPAGNE
- NOTE

---

## Territorio

- PROVINCE
- COMUNI
- FRAZIONI
- MARINE
- SPIAGGE
- PORTI
- TORRI
- PUNTI_INTERESSE

---

## Sistema

- CONFIGURAZIONI
- LOG
- AUDIT
- PERMESSI
- RUOLI

---

# Versionamento

Ogni modifica allo schema del database dovrà essere registrata.

Le migrazioni saranno numerate progressivamente.

---

# Obiettivo finale

Il database dovrà essere sufficientemente flessibile da gestire:

- una singola struttura
- più strutture
- migliaia di prenotazioni
- migliaia di clienti
- future integrazioni con API esterne

senza modificare l'architettura generale.

---

# Regola fondamentale

Ogni nuova tabella dovrà rispettare integralmente le convenzioni definite nel presente documento.

Nessuna eccezione è ammessa senza aggiornamento ufficiale della documentazione.
