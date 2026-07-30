# Documento

09_BUSINESS_RULES_ENGINE.md

Versione: 1.0
Stato: APPROVATO

---

# Business Rules Engine

## Introduzione

Il Business Rules Engine (BRE) è il componente incaricato di applicare tutte le regole di business della piattaforma.

Le regole non devono essere distribuite nel codice dell'applicazione, ma centralizzate in un unico motore.

---

# Obiettivi

Il Business Rules Engine deve:

- validare ogni operazione;
- applicare le regole commerciali;
- applicare le regole fiscali;
- applicare le regole territoriali;
- applicare le regole operative;
- fornire motivazioni in caso di rifiuto.

---

# Principio fondamentale

Il codice dell'applicazione non deve contenere regole di business.

Ogni decisione deve essere presa dal Business Rules Engine.

---

# Ambiti di applicazione

## Prenotazioni

- soggiorno minimo;
- soggiorno massimo;
- giorni di check-in;
- giorni di check-out;
- capienza minima;
- capienza massima.

---

## Clienti

- blacklist;
- storico no-show;
- limitazioni operative;
- documentazione obbligatoria.

---

## Pagamenti

- saldo richiesto;
- pagamento in struttura;
- Formula Fiduciaria;
- eventuali cauzioni.

---

## Territorio

Il sistema accetta esclusivamente strutture situate nel Salento geografico.

La validazione avviene tramite il database territoriale ufficiale.

---

## Revenue

- Rack Rate;
- sconti;
- promozioni;
- offerte;
- regole di priorità.

---

## Servizi

Verifica della disponibilità di:

- animali;
- parcheggio;
- Wi-Fi;
- accessibilità;
- servizi aggiuntivi.

---

# Tipologie di regole

## Regole obbligatorie

Devono sempre essere rispettate.

Esempio:

Il CIN è obbligatorio.

---

## Regole configurabili

Possono essere modificate dall'amministratore.

Esempio:

Soggiorno minimo.

---

## Regole temporanee

Valide solo in un determinato periodo.

Esempio:

Promozione estiva.

---

## Regole dinamiche

Calcolate in tempo reale.

Esempio:

Occupazione residua.

---

# Priorità

Le regole vengono valutate nel seguente ordine:

1. Sicurezza
2. Normativa
3. Disponibilità
4. Regole commerciali
5. Promozioni
6. Preferenze cliente

---

# Output

Ogni controllo produce:

- ESITO
- MOTIVAZIONE
- REGOLA APPLICATA

---

# Esempio

Richiesta:

Check-in il sabato.

Soggiorno di 2 notti.

Configurazione con soggiorno minimo di 7 notti.

Output:

Esito:
NON CONSENTITO

Motivazione:

Violazione della regola "Soggiorno minimo".

---

# Audit

Ogni decisione viene registrata.

Sono memorizzati:

- data e ora;
- utente;
- regola applicata;
- esito.

---

# Estensioni future

Il Business Rules Engine potrà essere esteso senza modificare il codice applicativo, aggiungendo nuove regole configurabili.
