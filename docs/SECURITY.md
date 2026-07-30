# SECURITY.md

# Vacanze Sicure nel Salento
## Security Policy
Versione: 1.0.0

---

# Premessa

La sicurezza costituisce uno dei pilastri fondamentali dell'intera piattaforma.

Ogni componente del sistema dovrà essere progettato secondo il principio **Security by Design**, evitando che vulnerabilità applicative possano consentire l'accesso a dati appartenenti ad altri utenti o ad altre strutture ricettive.

Ogni nuova funzionalità dovrà rispettare integralmente le regole contenute in questo documento.

---

# Principi fondamentali

La piattaforma adotta i seguenti principi:

- Security by Design
- Privacy by Design
- Least Privilege
- Zero Trust
- Defense in Depth
- Multi-Tenant Isolation
- Secure Default Configuration
- Auditability

---

# Multi Tenant

L'intera piattaforma è multi-struttura.

Ogni record del database appartiene obbligatoriamente ad una struttura ricettiva.

Nessun record può essere condiviso automaticamente tra strutture differenti.

Ogni query dovrà sempre verificare l'appartenenza della risorsa alla struttura autenticata.

---

# Controllo di autorizzazione

Ogni richiesta API dovrà verificare almeno:

- utente autenticato
- ruolo
- struttura
- permessi
- stato dell'account

Il semplice possesso di un identificativo di una risorsa non autorizza il suo utilizzo.

---

# UUID

Gli identificativi numerici del database non devono mai essere esposti all'esterno.

Tutte le API utilizzeranno esclusivamente UUID.

Esempio corretto

```
/api/bookings/61d98c8e-50d4-4d90-a4f2-3d45f4d9ab32
```

Esempio non consentito

```
/api/bookings/152
```

---

# Query sicure

Ogni interrogazione al database dovrà sempre filtrare la struttura proprietaria.

Esempio corretto

```
SELECT *
FROM booking
WHERE uuid = :booking_uuid
AND structure_uuid = :structure_uuid;
```

Qualunque query che non filtri la struttura è considerata non conforme.

---

# JWT

Ogni token dovrà contenere almeno:

- user_uuid
- structure_uuid
- role
- expiration

Il backend non dovrà mai fidarsi esclusivamente del token senza effettuare ulteriori verifiche sul database.

---

# Password

Le password non devono mai essere salvate in chiaro.

È obbligatorio utilizzare hashing sicuro.

Sono vietati:

- MD5
- SHA1
- password reversible

---

# API

Tutte le API devono essere protette.

Ogni endpoint deve verificare:

- autenticazione
- autorizzazione
- validazione input
- struttura proprietaria

---

# Rate Limiting

Le API pubbliche dovranno prevedere limitazioni di frequenza.

In particolare:

- Login
- Password Recovery
- Customer Care
- Chat AI
- WhatsApp
- Booking Engine

---

# Validazione Input

Ogni dato ricevuto deve essere validato.

Sono vietati:

- SQL Injection
- Command Injection
- HTML Injection
- Script Injection

Ogni input dovrà essere trattato come potenzialmente malevolo.

---

# File Upload

Ogni file caricato dovrà essere verificato.

Controlli obbligatori:

- estensione
- MIME Type
- dimensione
- scansione antivirus (quando disponibile)

---

# Log

Ogni operazione sensibile dovrà essere registrata.

Almeno:

- data
- ora
- utente
- struttura
- indirizzo IP
- browser
- operazione
- esito

---

# Audit Log

Le seguenti operazioni dovranno produrre audit obbligatorio:

- login
- logout
- modifica dati cliente
- cancellazione dati
- accesso prenotazioni
- accesso pagamenti
- esportazioni
- download documenti
- modifica permessi

---

# Customer Care

Le conversazioni sono isolate.

Una struttura non può visualizzare conversazioni appartenenti ad un'altra struttura.

Ogni messaggio dovrà verificare:

- conversation_uuid
- structure_uuid
- permessi utente

---

# AI

L'Intelligenza Artificiale non dovrà mai poter recuperare dati appartenenti ad altre strutture.

Ogni richiesta AI dovrà essere filtrata utilizzando il contesto dell'utente autenticato.

---

# Backup

I backup dovranno essere:

- cifrati
- verificati
- versionati

---

# GDPR

Il sistema dovrà rispettare il Regolamento UE 2016/679.

Dovranno essere implementate funzionalità per:

- esportazione dati
- diritto all'oblio
- anonimizzazione
- gestione del consenso
- registro dei trattamenti

---

# Incident Response

Ogni incidente di sicurezza dovrà prevedere:

- identificazione
- contenimento
- analisi
- ripristino
- report finale

---

# Vulnerabilità note

La piattaforma dovrà impedire in particolare:

- Broken Object Level Authorization (BOLA)
- Broken Authentication
- Broken Access Control
- SQL Injection
- Cross Site Scripting (XSS)
- Cross Site Request Forgery (CSRF)
- Remote Code Execution
- Path Traversal
- Session Hijacking
- Token Theft
- Privilege Escalation

---

# Principio finale

La sicurezza prevale sempre sulla funzionalità.

Una funzionalità non sicura non deve essere pubblicata.

Ogni nuovo modulo sviluppato dovrà essere conforme a questo documento.
