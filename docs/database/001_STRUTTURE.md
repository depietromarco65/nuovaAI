# TABELLA 001

# STRUTTURE

Versione: 1.0

Stato: APPROVATO

---

# Scopo

La tabella STRUTTURE rappresenta il livello più alto del PMS.

Ogni struttura ricettiva registrata nel sistema possiede un proprio record.

Una struttura può contenere una o più Unità Ricettive.

Esempi:

- A Casa di Amici
- Residence XYZ
- Villaggio ABC

---

# Relazioni

Una STRUTTURA può avere:

∞ Unità Ricettive

∞ Prenotazioni

∞ Listini

∞ Fotografie

∞ Servizi

∞ Documenti

∞ Utenti autorizzati

---

# Campi

| Campo | Tipo | Obbl. | Descrizione |
|---------|---------|---------|----------------|
| id | INTEGER | SI | Chiave primaria |
| nome | TEXT | SI | Nome commerciale |
| ragione_sociale | TEXT | NO | Ragione sociale |
| partita_iva | TEXT | NO | Partita IVA |
| codice_fiscale | TEXT | NO | Codice fiscale |
| cin | TEXT | SI | Codice Identificativo Nazionale |
| cir | TEXT | NO | Codice Regionale |
| tipologia | TEXT | SI | Casa Vacanze, B&B, Hotel... |
| descrizione | TEXT | NO | Descrizione |
| email | TEXT | NO | Email |
| pec | TEXT | NO | PEC |
| telefono | TEXT | NO | Telefono |
| whatsapp | TEXT | NO | WhatsApp |
| sito_web | TEXT | NO | URL sito |
| indirizzo | TEXT | SI | Via |
| civico | TEXT | NO | Numero |
| cap | TEXT | SI | CAP |
| comune_id | INTEGER | SI | FK COMUNI |
| provincia_id | INTEGER | SI | FK PROVINCE |
| latitudine | REAL | NO | Coordinate |
| longitudine | REAL | NO | Coordinate |
| checkin_dalle | TIME | NO | Ora Check-in |
| checkin_alle | TIME | NO | Ora Check-in |
| checkout_entro | TIME | NO | Ora Checkout |
| animali_ammessi | BOOLEAN | SI | Animali |
| fumatori | BOOLEAN | SI | Consentito |
| wifi | BOOLEAN | SI | WiFi |
| parcheggio | BOOLEAN | SI | Parcheggio |
| aria_condizionata | BOOLEAN | SI | Climatizzazione |
| videosorveglianza | BOOLEAN | SI | Videosorveglianza |
| stato | TEXT | SI | Attiva, Sospesa |
| created_at | DATETIME | SI | Creazione |
| updated_at | DATETIME | SI | Ultima modifica |

---

# Chiave primaria

id

---

# Chiavi esterne

comune_id → COMUNI

provincia_id → PROVINCE

---

# Indici

nome

cin

comune_id

provincia_id

stato

---

# Record di esempio

Nome

A Casa di Amici

Comune

Salve

Provincia

Lecce

CIN

IT075066C200054604

---

# Regole

Il CIN deve essere univoco.

Una struttura non può essere eliminata se possiede prenotazioni.

Una struttura può essere disattivata.

La cancellazione sarà logica.

---

# Tabelle collegate

UNITA_RICETTIVE

PRENOTAZIONI

LISTINI

CLIENTI

UTENTI

FOTO

DOCUMENTI

CONFIGURAZIONI
