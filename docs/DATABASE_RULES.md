# DATABASE_RULES.md

# Vacanze Sicure nel Salento
## Regole di progettazione del Database

Versione: 1.0.0

---

# Obiettivo

Questo documento definisce le regole obbligatorie per la progettazione del database.

Ogni nuova tabella dovrà rispettare queste regole.

---

# Filosofia

Il database rappresenta il cuore dell'applicazione.

La qualità del software dipende principalmente dalla qualità della progettazione del database.

Ogni modifica dovrà privilegiare:

- semplicità
- normalizzazione
- estendibilità
- sicurezza
- prestazioni

---

# Chiavi Primarie

Ogni tabella utilizza:

id

intero autoincrementale.

L'id non dovrà mai essere esposto tramite API.

---

# UUID

Ogni tabella deve contenere anche:

uuid

UUID versione 4.

L'UUID rappresenta l'identificativo pubblico.

---

# Timestamp

Ogni tabella deve contenere almeno:

created_at

updated_at

---

# Stato

Ogni tabella deve contenere:

enabled

boolean

per consentire la disattivazione logica dei record.

---

# Soft Delete

I record non devono essere cancellati fisicamente.

Quando necessario utilizzare:

deleted_at

oppure

enabled = False

La cancellazione fisica sarà riservata ai processi amministrativi.

---

# Multi Tenant

Ogni dato appartenente ad una struttura dovrà contenere:

structure_uuid

Non sono ammessi record condivisi tra strutture salvo esplicita progettazione.

---

# Relazioni

Utilizzare sempre Foreign Key.

Non utilizzare campi testuali per rappresentare relazioni.

Corretto

booking.guest_id

Errato

booking.guest_name

---

# Denormalizzazione

La denormalizzazione è ammessa solo dopo aver dimostrato un reale vantaggio prestazionale.

---

# Indici

Creare indici su:

- uuid
- foreign key
- campi utilizzati frequentemente nelle ricerche
- date
- email
- telefono

Evitare indici inutili.

---

# Campi testuali

Utilizzare:

VARCHAR

quando la lunghezza è nota.

TEXT

solo quando realmente necessario.

---

# Date

Utilizzare sempre timezone.

---

# Valori monetari

Non utilizzare FLOAT.

Utilizzare:

NUMERIC

oppure

DECIMAL.

---

# Boolean

Utilizzare BOOLEAN.

Evitare:

Y/N

S/N

0/1

---

# Enum

Quando i valori sono stabili utilizzare ENUM applicativo.

Quando i valori possono cambiare utilizzare tabelle dedicate.

---

# Audit

I dati critici dovranno poter essere tracciati.

Le modifiche importanti dovranno essere registrate.

---

# Nomenclatura

Nomi tabelle

snake_case

Singolare.

Esempio

guest

booking

invoice

payment

conversation

---

# Colonne

snake_case

Esempio

arrival_date

departure_date

created_at

---

# Foreign Key

Formato

guest_id

booking_id

payment_id

Mai

guest

booking

payment

---

# File

I documenti non saranno salvati nel database.

Nel database verranno memorizzati solamente:

- percorso
- nome
- hash
- dimensione
- MIME Type

---

# Coordinate

Utilizzare:

latitude

longitude

---

# Email

Sempre:

VARCHAR(255)

indicizzata.

---

# Telefono

Conservare il numero in formato internazionale.

Esempio

+393481234567

---

# Password

Mai salvare password in chiaro.

---

# Token

Mai salvare token senza una reale necessità.

Quando possibile memorizzarne esclusivamente l'hash.

---

# GDPR

Le informazioni personali dovranno poter essere:

- esportate
- anonimizzate
- cancellate

secondo quanto previsto dal Regolamento UE 2016/679.

---

# Backup

Il database dovrà poter essere ripristinato integralmente.

---

# Migrazioni

Ogni modifica dello schema dovrà essere gestita tramite Alembic.

È vietata la modifica manuale delle tabelle in produzione.

---

# Regola finale

Prima di creare una nuova tabella chiedersi sempre:

Questa informazione esiste già?

Se la risposta è sì, evitare duplicazioni.

La qualità del database è la qualità dell'intero progetto.
