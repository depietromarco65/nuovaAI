# docs/SECURITY_CENTER.md

# Security Center
## Centro di Gestione della Sicurezza

Versione 1.0

---

# Obiettivo

Il modulo **Security Center** costituisce il centro di controllo della sicurezza del CRM "Vacanze Sicure nel Salento".

Ha lo scopo di:

- registrare ogni incidente di sicurezza;
- assistere il Titolare del trattamento negli adempimenti previsti dal GDPR;
- proteggere gli ospiti da tentativi di phishing;
- mantenere uno storico completo degli eventi;
- coordinare le comunicazioni di emergenza.

---

# Principi

Il modulo segue i principi di:

- Security by Design
- Privacy by Design
- GDPR Accountability
- Data Minimization
- Zero Trust
- Audit completo
- Massima trasparenza verso gli ospiti

---

# Tipologie di incidente

Il sistema deve poter registrare almeno le seguenti categorie.

## Data Breach

Violazione dei dati personali.

## Phishing

Tentativi di truffa verso gli ospiti.

## Smishing

SMS fraudolenti.

## Vishing

Telefonate fraudolente.

## Malware

Incidenti causati da software malevolo.

## Ransomware

Attacco ransomware.

## Vulnerabilità Software

Bug critici comunicati dai fornitori.

## Accesso non autorizzato

Account compromessi.

## Problemi infrastrutturali

Disservizi Cloud.

---

# Informazioni registrate

Ogni incidente deve contenere:

- UUID
- Data apertura
- Data chiusura
- Livello di gravità
- Fornitore coinvolto
- Sistema coinvolto
- Descrizione
- Categoria
- Stato
- Responsabile
- Azioni adottate
- Documentazione allegata

---

# Livelli di gravità

## Informativo

Nessun impatto.

## Basso

Rischio limitato.

## Medio

Possibile impatto sugli ospiti.

## Alto

Data breach confermato.

## Critico

Violazione estesa.

---

# Workflow

## 1. Registrazione

L'operatore registra l'incidente.

---

## 2. Valutazione

Il Titolare valuta:

- natura dei dati;
- numero di interessati;
- rischio per gli ospiti.

---

## 3. Contenimento

Il CRM propone automaticamente le misure previste.

Ad esempio:

- sospensione webhook;
- revoca API Key;
- cambio password;
- disabilitazione integrazione.

---

## 4. Comunicazione

Se necessario il CRM abilita automaticamente il workflow:

**Notifica GDPR Art.34**

I destinatari possono essere selezionati mediante:

- periodo prenotazione;
- struttura;
- gruppo clienti;
- nazionalità;
- lingua;
- singolo ospite.

---

## 5. Audit

Ogni operazione viene registrata.

---

# Comunicazioni automatiche

Il sistema deve poter inviare:

- Email
- WhatsApp
- SMS

utilizzando modelli predefiniti.

---

# Template disponibili

- Anti Phishing
- Data Breach
- Aggiornamento sicurezza
- Chiusura incidente
- Richiesta verifica contatti

---

# Caso reale registrato

## Incidente

Octorate S.r.l.

Data notifica:

29 luglio 2026

Periodo incidente:

23-25 luglio 2026

Descrizione:

Sottrazione di token di accesso ed exploit dell'endpoint della chat.

Possibile esposizione di:

- nome;
- cognome;
- telefono;
- dettagli della prenotazione.

Segnalati tentativi di phishing tramite WhatsApp.

Azioni adottate:

- invio comunicazione multilingua agli ospiti;
- blocco cautelativo delle integrazioni Octorate;
- monitoraggio continuo;
- registrazione audit.

---

# Formula Fiduciaria

Durante ogni incidente il CRM deve ricordare agli ospiti che:

- A Casa di Amici non richiede acconti anticipati per le prenotazioni aderenti alla Formula Fiduciaria;
- non vengono richiesti dati della carta di credito tramite WhatsApp, SMS o e-mail;
- qualsiasi richiesta di pagamento ricevuta attraverso canali non ufficiali deve essere verificata direttamente con la struttura.

---

# Integrazione con il CRM

Il modulo Security Center dialoga con:

- Ospiti
- Prenotazioni
- Comunicazioni
- Audit
- AI Assistant
- Gestione Documentale

---

# Dashboard

La dashboard mostrerà:

- Incidenti aperti
- Incidenti chiusi
- Comunicazioni inviate
- Ospiti coinvolti
- Stato degli adempimenti GDPR
- Fornitori coinvolti
- Livello di rischio attuale

---

# Obiettivo finale

Ogni evento di sicurezza deve essere gestito con procedure standardizzate, documentate e completamente tracciabili, garantendo la tutela degli ospiti, la conformità al GDPR e la continuità operativa della struttura.
