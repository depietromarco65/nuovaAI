# 327_CANALI_DI_MESSAGGISTICA.md

# CANALI DI MESSAGGISTICA

> *"La messaggistica rappresenta il principale punto di contatto tra l'ecosistema Vacanze Sicure e le persone. Il sistema deve essere indipendente dal canale utilizzato, garantendo continuità della conversazione, tracciabilità e integrazione con tutti i processi operativi."*

---

# Scopo

Questo documento definisce l'architettura dei canali di messaggistica utilizzabili all'interno dell'ecosistema Vacanze Sicure.

L'obiettivo non è supportare una singola piattaforma.

L'obiettivo è costruire un sistema capace di utilizzare qualsiasi canale presente oggi o disponibile in futuro.

---

# Visione

L'utente sceglie il canale.

L'ecosistema mantiene la conversazione.

Ogni messaggio viene:

- acquisito;
- classificato;
- archiviato;
- collegato al Fascicolo corretto;
- inserito nella Timeline;
- reso disponibile all'Assistente AI.

---

# Obiettivi

Il sistema deve consentire di:

- centralizzare tutte le conversazioni;
- evitare la dispersione delle informazioni;
- automatizzare le comunicazioni ripetitive;
- mantenere lo storico completo;
- permettere il lavoro multioperatore;
- garantire la continuità della relazione.

---

# Principi

Ogni conversazione deve essere:

- unica;
- contestualizzata;
- indipendente dal canale;
- archiviata;
- ricercabile;
- collegata ai Fascicoli.

---

# Architettura

L'ecosistema distingue tra:

## Canale

Il mezzo utilizzato.

Esempio:

- WhatsApp
- Telegram
- Messenger

---

## Conversazione

L'insieme dei messaggi relativi ad uno stesso contesto.

---

## Messaggio

Ogni singolo elemento della conversazione.

Può contenere:

- testo;
- immagini;
- documenti;
- posizione;
- audio;
- video;
- contatti.

---

# Canali Supportati

## WhatsApp

Utilizzo:

- richieste informazioni;
- preventivi;
- prenotazioni;
- assistenza;
- follow-up.

Funzioni:

- Business
- API
- Template
- QR Code
- Catalogo
- Risposte rapide
- Messaggi automatici

---

## Telegram

Telegram rappresenta uno dei canali più flessibili.

Può essere utilizzato per:

- chatbot;
- notifiche;
- gruppi di lavoro;
- canali informativi;
- invio documenti;
- automazioni.

### Bot

Possibili utilizzi:

- richiesta disponibilità;
- invio preventivi;
- check-in;
- invio PIN;
- documenti;
- pagamenti.

### Gruppi

Per:

- housekeeping;
- manutenzione;
- amministrazione;
- reception.

### Canali

Per:

- proprietari;
- partner;
- comunicazioni interne;
- formazione.

---

## Facebook Messenger

Utilizzo:

- richieste provenienti da Facebook;
- campagne pubblicitarie;
- assistenza.

---

## Instagram Direct

Gestione delle richieste provenienti da Instagram.

---

## Signal

Per comunicazioni ad elevata riservatezza.

---

## Google Messages (RCS)

Canale emergente destinato a sostituire progressivamente gli SMS.

---

## SMS

Per:

- codici;
- OTP;
- emergenze;
- notifiche.

---

## Apple Messages

Supporto per utenti Apple.

---

## Email

Pur non essendo messaggistica istantanea, rappresenta un canale integrato.

---

# Comunicazioni Automatiche

Il sistema può inviare automaticamente:

- conferme;
- reminder;
- documentazione;
- check-in;
- check-out;
- richieste recensione;
- follow-up;
- recupero prenotazioni.

---

# Multioperatore

Ogni conversazione può essere:

- assegnata;
- trasferita;
- condivisa;
- supervisionata.

---

# Fascicolo Ospite

Ogni conversazione viene collegata automaticamente al Fascicolo Ospite.

---

# Fascicolo Prenotazione

Le comunicazioni operative vengono associate alla prenotazione.

---

# Customer Journey

La messaggistica accompagna tutte le fasi:

Richiesta

↓

Preventivo

↓

Prenotazione

↓

Preparazione soggiorno

↓

Check-in

↓

Soggiorno

↓

Check-out

↓

Recensione

↓

Fidelizzazione

---

# Timeline

Ogni messaggio genera un evento nella Timeline.

---

# Documenti

I canali possono trasmettere:

- preventivi;
- contratti;
- ricevute;
- regolamenti;
- mappe;
- fotografie;
- brochure;
- voucher.

---

# Assistente AI

L'Assistente AI può:

- rispondere automaticamente;
- suggerire risposte;
- tradurre;
- riassumere conversazioni;
- classificare richieste;
- individuare urgenze;
- estrarre Task.

---

# Workflow

Una conversazione può generare:

- Task;
- Documenti;
- Fascicoli;
- Pratiche;
- Reminder;
- Notifiche.

---

# Sicurezza

Garantire:

- autenticazione;
- cifratura;
- backup;
- gestione permessi;
- conservazione.

---

# Privacy

Il sistema deve rispettare:

- GDPR;
- consenso;
- diritto alla cancellazione;
- conservazione dei dati;
- gestione allegati.

---

# KPI

Monitorare:

- conversazioni;
- tempo di risposta;
- tempo di presa in carico;
- conversione in prenotazioni;
- soddisfazione utenti;
- canale più utilizzato;
- numero messaggi automatici;
- interventi AI.

---

# Best Practice

- Un solo numero ufficiale per ogni struttura.
- Utilizzare template approvati.
- Personalizzare sempre le risposte.
- Automatizzare solo le attività ripetitive.
- Archiviare tutte le conversazioni.
- Evitare l'utilizzo di numeri personali.

---

# Errori da Evitare

- utilizzare canali non gestiti;
- perdere la cronologia;
- duplicare le conversazioni;
- rispondere da account personali;
- non collegare le conversazioni ai Fascicoli.

---

# Checklist

## Configurazione

☐ Canali configurati

☐ Profili completi

☐ Logo

☐ Descrizione

☐ Orari

☐ Link sito

---

## Automazioni

☐ Benvenuto

☐ Assenza

☐ Reminder

☐ Check-in

☐ Check-out

☐ Follow-up

☐ Recensioni

---

## Integrazione

☐ Communication Engine

☐ Fascicolo Ospite

☐ Fascicolo Prenotazione

☐ Customer Journey

☐ Motore Documentale

☐ Assistente AI

☐ Task Manager

---

# Evoluzioni Future

Il sistema dovrà poter integrare facilmente nuovi canali senza modificare l'architettura.

Ogni nuovo servizio di messaggistica dovrà essere implementato come un semplice connettore.

---

# Collegamenti

- 310_STRATEGIA_DI_COMUNICAZIONE.md
- 313_MESSAGGI_PER_TARGET.md
- 325_PIANO_EDITORIALE.md
- 326_NEWSLETTER.md
- 611_COMMUNICATION_ENGINE.md
- 620_MOTORE_DI_INTEGRAZIONE_DATI.md
- 100.20_CUSTOMER_JOURNEY.md
- 101_FASCICOLO_OSPITE.md
- 102_FASCICOLO_PRENOTAZIONE.md
- 715_GESTIONE_RICHIESTE.md

---

# Principio Vacanze Sicure

L'ecosistema non comunica attraverso WhatsApp, Telegram o altri strumenti.

L'ecosistema comunica con le persone.

I canali di messaggistica rappresentano semplicemente i mezzi attraverso cui avviene la relazione.

L'architettura deve quindi essere indipendente dal fornitore tecnologico, consentendo di aggiungere, sostituire o integrare nuovi canali senza modificare i processi operativi.

L'obiettivo non è gestire applicazioni di messaggistica.

L'obiettivo è costruire un sistema di comunicazione unificato, continuo, intelligente e perfettamente integrato con tutti i moduli dell'ecosistema Vacanze Sicure.
## Continuità della conversazione

L'utente può iniziare una conversazione su un canale (es. WhatsApp) e proseguirla sul sito web senza perdere il contesto.

L'Assistente AI deve recuperare automaticamente:

- dati del contatto;
- richiesta iniziale;
- documenti inviati;
- preventivi;
- Fascicolo Ospite;
- Customer Journey.

La conversazione deve apparire continua indipendentemente dal canale utilizzato.
