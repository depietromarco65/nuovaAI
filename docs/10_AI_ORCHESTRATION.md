# Documento

10_AI_ORCHESTRATION.md

Versione: 1.0
Stato: APPROVATO

---

# AI Orchestration Layer

## Introduzione

L'AI Orchestration Layer è il componente che coordina l'interazione tra l'utente, l'intelligenza artificiale e i moduli della piattaforma.

L'AI non accede direttamente al database.

Ogni richiesta viene interpretata, validata e trasformata in operazioni autorizzate.

---

# Obiettivi

L'AI deve:

- comprendere il linguaggio naturale;
- identificare l'intento dell'utente;
- recuperare i dati necessari;
- richiamare i servizi della piattaforma;
- verificare le regole di business;
- generare una risposta comprensibile.

---

# Principi

L'AI non modifica mai direttamente il database.

Ogni modifica passa attraverso le API ufficiali.

---

# Flusso

Utente

↓

AI Orchestrator

↓

Intent Recognition

↓

Decision Engine

↓

Business Services

↓

Database

↓

Risposta

---

# Tipologie di richieste

## Informative

Esempi

"Quante prenotazioni ho ad agosto?"

"Qual è il fatturato di luglio?"

---

## Operative

Esempi

"Crea una prenotazione."

"Annulla il preventivo."

---

## Analitiche

Esempi

"Quali appartamenti hanno il miglior tasso di occupazione?"

---

## Predittive

Esempi

"Quale sarà il periodo più richiesto il prossimo anno?"

---

## Consulenziali

Esempi

"Quale promozione conviene attivare?"

---

# Sicurezza

L'AI opera con gli stessi permessi dell'utente autenticato.

Non può accedere a dati non autorizzati.

---

# Log

Ogni conversazione viene registrata.

Sono memorizzati:

- utente;
- data e ora;
- intento;
- moduli coinvolti;
- esito.

---

# Estensioni

L'AI potrà utilizzare più modelli linguistici.

Ogni modello sarà intercambiabile senza modificare il software.
