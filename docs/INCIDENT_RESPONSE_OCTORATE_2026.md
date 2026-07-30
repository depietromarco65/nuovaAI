# INCIDENT_RESPONSE_OCTORATE_2026.md

# Gestione Evento di Sicurezza Octorate
## Adempimenti GDPR artt. 33 e 34

Versione: 1.0

---

# Evento

## Data notifica

29 luglio 2026

## Fornitore coinvolto

Octorate S.r.l.
Roma (Italia)

Contatti:

- tech@octorate.com
- dpo@octorate.com

---

# Descrizione dell'incidente

Secondo la comunicazione ricevuta da Octorate S.r.l., nel periodo compreso tra il **23 luglio 2026** ed il **25 luglio 2026** è stata sfruttata una vulnerabilità presente in un endpoint della chat.

L'incidente ha consentito, mediante l'utilizzo improprio di un token di accesso sottratto ad un account cliente, la lettura non autorizzata di un numero limitato di conversazioni appartenenti ad altre strutture ricettive.

I dati potenzialmente coinvolti comprendono:

- nominativo dell'ospite;
- numero di telefono;
- dettagli della prenotazione.

Successivamente sono stati segnalati tentativi di phishing e smishing tramite WhatsApp ai danni degli ospiti.

---

# Azioni di contenimento adottate dal CRM

Il CRM "Vacanze Sicure nel Salento" registra l'evento ed applica automaticamente le seguenti misure cautelative.

## 1. Comunicazione Anti-Phishing

L'Assistente AI supporta il Titolare del trattamento nella predisposizione e nell'invio della comunicazione prevista dall'art. 34 del GDPR verso tutti gli ospiti potenzialmente interessati.

Per il presente evento i destinatari sono:

- Lead del Blocco A
- Prenotazioni attive con arrivo nel mese di Agosto 2026

La comunicazione dovrà ricordare che:

- A Casa di Amici non richiede mai password o codici OTP;
- non richiede dati della carta di credito tramite WhatsApp, SMS o e-mail;
- non richiede pagamenti improvvisi;
- tutte le comunicazioni economiche devono essere verificate utilizzando esclusivamente i recapiti ufficiali.

Dovrà inoltre essere evidenziato il principio della **Formula Fiduciaria**, che prevede l'assenza di acconti anticipati per le prenotazioni aderenti.

---

## 2. Blocco cautelativo integrazioni

Fino alla completa chiusura dell'incidente vengono sospese, ove tecnicamente possibile, le integrazioni che utilizzano webhook provenienti da Octorate.

La riattivazione dovrà essere autorizzata esclusivamente dal Titolare del trattamento dopo la verifica della cessazione del rischio.

---

# Regola CRM

In presenza di un data breach confermato da un fornitore esterno (Channel Manager, PMS o software collegati), il CRM attiva automaticamente la modalità:

**"Notifica GDPR Art. 34"**

all'interno del sistema di comunicazione omnicanale.

L'operatore potrà esclusivamente:

- verificare il testo;
- personalizzarlo se necessario;
- autorizzarne l'invio.

---

# Template obbligatorio

Ogni comunicazione dovrà rassicurare l'ospite specificando chiaramente che:

- A Casa di Amici non conserva i dati delle carte di credito dei propri ospiti;
- eventuali dati di pagamento non sono presenti nel database del CRM;
- le prenotazioni effettuate con la Formula Fiduciaria prevedono il pagamento direttamente presso la struttura, senza acconti anticipati;
- qualsiasi richiesta di pagamento ricevuta tramite WhatsApp, SMS o e-mail deve essere considerata sospetta fino a verifica diretta con la struttura.

---

# Registrazione Audit

Ogni invio della comunicazione dovrà essere registrato nell'Audit Log indicando almeno:

- data e ora;
- operatore o AI che ha predisposto il messaggio;
- destinatario;
- canale utilizzato;
- esito dell'invio;
- riferimento all'incidente di sicurezza.

---

# Principio di sicurezza

Ogni incidente di sicurezza comunicato da un fornitore esterno dovrà essere registrato nel CRM come evento permanente, al fine di garantire la tracciabilità delle decisioni adottate e delle misure di mitigazione implementate.
