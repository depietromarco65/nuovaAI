# docs/SECURITY_INCIDENT_PROCEDURE.md

# Procedura Gestione Incidenti di Sicurezza

Versione 1.0

---

# Obiettivo

Garantire una gestione uniforme, documentata e tracciabile di qualsiasi incidente di sicurezza che possa coinvolgere:

- dati personali;
- sistemi informatici;
- infrastrutture;
- fornitori esterni;
- ospiti;
- dipendenti;
- collaboratori.

---

# Ambito

La procedura si applica a:

- CRM Vacanze Sicure nel Salento
- Sito Web
- Booking Engine
- API
- Database
- Email
- WhatsApp Business
- Gateway di pagamento
- PMS
- Channel Manager
- Cloud Provider
- Sistemi AI

---

# Fase 1 - Individuazione

L'incidente può essere rilevato da:

- operatore;
- AI Assistant;
- sistema di monitoraggio;
- fornitore;
- ospite;
- autorità;
- software antivirus.

Ogni evento genera automaticamente un codice incidente.

Esempio:

INC-2026-0001

---

# Fase 2 - Classificazione

Il sistema richiede di classificare:

□ Data Breach

□ Tentativo di Phishing

□ Malware

□ Furto credenziali

□ API compromessa

□ Token compromesso

□ Vulnerabilità Software

□ Errore umano

□ Altro

---

# Fase 3 - Priorità

P1 Critico

Sistema inutilizzabile.

P2 Alto

Possibile violazione dati.

P3 Medio

Impatto limitato.

P4 Basso

Nessun rischio immediato.

---

# Fase 4 - Contenimento

Il CRM propone automaticamente le azioni.

Ad esempio:

□ blocco API

□ disattivazione webhook

□ reset password

□ revoca token

□ isolamento account

□ sospensione integrazione

□ backup immediato

□ blocco comunicazioni automatiche

---

# Fase 5 - Valutazione GDPR

Il sistema guida il Titolare nella valutazione.

Domande:

Sono coinvolti dati personali?

SI / NO

Sono coinvolti dati particolari?

SI / NO

Il rischio per gli interessati è elevato?

SI / NO

Serve notifica al Garante?

SI / NO

Serve comunicazione agli interessati?

SI / NO

---

# Fase 6 - Comunicazione

Se necessario vengono predisposti:

- Email
- SMS
- WhatsApp

nelle lingue:

- Italiano
- Inglese
- Tedesco
- Francese

utilizzando i template ufficiali.

---

# Fase 7 - Registrazione

Ogni attività viene registrata.

Per ogni operazione:

- utente
- AI
- data
- ora
- indirizzo IP
- operazione
- esito

---

# Fase 8 - Chiusura

L'incidente può essere chiuso solo quando:

✓ vulnerabilità eliminata

✓ sistemi verificati

✓ comunicazioni inviate

✓ audit completato

✓ documentazione archiviata

---

# Lesson Learned

Ogni incidente genera automaticamente un report finale.

Il report contiene:

- cause

- impatti

- tempi di risposta

- misure adottate

- miglioramenti proposti

Il report rimane archiviato permanentemente.

---

# Incidenti storici

Il CRM conserva uno storico completo.

Per ogni incidente:

- numero
- data
- categoria
- fornitore
- gravità
- durata
- azioni adottate
- esito

---

# Caso Studio

INC-2026-0001

Fornitore:

Octorate S.r.l.

Categoria:

Data Breach

Periodo:

23-25 luglio 2026

Data notifica:

29 luglio 2026

Azioni:

✓ Comunicazione multilingua agli ospiti

✓ Blocco cautelativo webhook

✓ Monitoraggio phishing

✓ Registrazione Audit

✓ Attivazione workflow GDPR

Stato:

CHIUSO
