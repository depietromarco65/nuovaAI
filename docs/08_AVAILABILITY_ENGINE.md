# Documento

08_AVAILABILITY_ENGINE.md

Versione: 1.0
Stato: APPROVATO

---

# Availability Engine

## Introduzione

L'Availability Engine è il componente responsabile della gestione della disponibilità delle unità commerciali.

Nessun altro modulo della piattaforma può determinare autonomamente la disponibilità.

Ogni verifica passa esclusivamente attraverso questo motore.

---

# Obiettivi

L'Availability Engine deve:

- determinare se una configurazione commerciale è prenotabile;
- bloccare automaticamente le unità fisiche coinvolte;
- evitare overbooking;
- gestire soggiorni minimi e massimi;
- applicare le regole di disponibilità;
- sincronizzare i calendari con i Channel Manager.

---

# Principio fondamentale

La disponibilità NON è un campo della tabella PRENOTAZIONI.

È un dato calcolato.

---

# Fonti dei dati

Il motore utilizza:

- Unità fisiche
- Configurazioni commerciali
- Prenotazioni confermate
- Prenotazioni opzionali
- Blocchi manutenzione
- Chiusure stagionali
- Regole commerciali
- Vincoli OTA
- Regole Revenue

---

# Stati di una configurazione

DISPONIBILE

↓

OPZIONATA

↓

PRENOTATA

↓

CHECK-IN

↓

CHECK-OUT

↓

LIBERA

---

# Tipologie di blocco

## Prenotazione

Blocca le unità fisiche.

---

## Manutenzione

Blocco tecnico.

---

## Pulizie

Intervallo non prenotabile.

---

## Chiusura stagionale

Periodo escluso dalla vendita.

---

## Uso personale

La struttura è riservata dal proprietario.

---

# Regole

## Nessun overbooking

Per impostazione predefinita il sistema impedisce prenotazioni sovrapposte.

L'overbooking potrà essere abilitato solo per specifiche configurazioni commerciali.

---

## Soggiorno minimo

Ogni configurazione commerciale può avere:

- soggiorno minimo globale;
- soggiorno minimo stagionale;
- soggiorno minimo per canale di vendita.

---

## Gap tra soggiorni

È possibile configurare un intervallo minimo tra due prenotazioni consecutive.

---

## Chiusure all'arrivo

È possibile impedire il check-in in determinati giorni della settimana.

---

## Chiusure alla partenza

È possibile impedire il check-out in determinati giorni della settimana.

---

## Occupazione

Ogni configurazione commerciale definisce:

- occupazione minima;
- occupazione standard;
- occupazione massima.

---

# Calendario

Il motore genera un calendario giornaliero.

Ogni giorno può assumere uno stato:

LIBERO

OCCUPATO

CHIUSO

MANUTENZIONE

PULIZIA

USO PROPRIETARIO

---

# Sincronizzazione

Il motore esporta e importa disponibilità tramite:

- iCal
- API OTA
- Channel Manager

---

# Audit

Ogni modifica allo stato di disponibilità viene registrata.

Sono memorizzati:

- utente;
- data e ora;
- motivo della modifica;
- origine (manuale, OTA, AI, sincronizzazione).

---

# Prestazioni

L'Availability Engine deve essere ottimizzato per rispondere in tempo reale anche con migliaia di prenotazioni e unità ricettive.

---

# Obiettivo finale

La disponibilità deve essere sempre il risultato di un calcolo, mai di un'informazione inserita manualmente.
