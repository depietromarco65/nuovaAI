# CODING_STANDARDS.md

# Vacanze Sicure nel Salento
## Standard di sviluppo

Versione: 1.0.0

---

# Obiettivo

Questo documento definisce le regole obbligatorie di sviluppo dell'intero progetto.

Ogni sorgente dovrà rispettare questi standard.

---

# Principi

Il codice deve essere:

- leggibile
- semplice
- documentato
- riutilizzabile
- testabile
- sicuro
- facilmente manutenibile

---

# Lingua

Il codice sorgente sarà scritto in inglese.

Le descrizioni funzionali potranno essere in italiano.

Esempio

Classe

Booking

Metodo

create_booking()

Variabile

arrival_date

Non utilizzare nomi misti.

---

# Naming

Classi

PascalCase

```
Booking
Guest
Invoice
Conversation
```

Funzioni

snake_case

```
create_booking()
calculate_price()
send_email()
```

Variabili

snake_case

```
arrival_date
total_price
guest_count
```

Costanti

UPPER_CASE

```
DEFAULT_LANGUAGE
MAX_UPLOAD_SIZE
```

---

# File

Un file deve contenere una sola responsabilità.

Esempio

```
booking.py
```

non dovrà contenere codice relativo ai pagamenti.

---

# Classi

Ogni classe deve avere una sola responsabilità.

---

# Funzioni

Una funzione dovrebbe essere breve.

Preferibilmente inferiore a 50 righe.

---

# Commenti

Commentare il motivo.

Non descrivere ciò che è evidente.

---

# Import

Ordine

1 Librerie standard

2 Librerie esterne

3 Moduli interni

---

# Database

Mai utilizzare SQL nel codice applicativo se non strettamente necessario.

Utilizzare SQLAlchemy.

---

# UUID

Tutte le entità esposte pubblicamente utilizzano UUID.

Mai utilizzare gli ID numerici nelle API.

---

# Errori

Ogni errore deve essere gestito.

Mai utilizzare

```
except:
```

Utilizzare sempre eccezioni specifiche.

---

# Logging

Mai utilizzare

```
print()
```

nel codice di business.

Utilizzare il sistema di logging.

Eccezione:

fase iniziale di bootstrap.

---

# API

Ogni endpoint deve:

- validare gli input
- autenticare
- autorizzare
- restituire errori coerenti

---

# Modelli

Ogni modello dovrà:

ereditare

```
Base
```

e

```
BaseMixin
```

---

# Schemas

Ogni modello avrà il proprio schema Pydantic.

---

# Repository

L'accesso al database avviene esclusivamente tramite Repository.

---

# Services

La logica di business non deve essere presente negli endpoint.

---

# Endpoint

Gli endpoint devono essere molto piccoli.

Devono limitarsi a:

- ricevere richiesta
- chiamare il service
- restituire risposta

---

# Sicurezza

Ogni nuova funzionalità deve rispettare SECURITY.md.

---

# Commit Git

Ogni commit deve rappresentare una modifica logica completa.

Esempi

```
Aggiunto modello Guest

Aggiunto sistema JWT

Implementato Customer Care
```

---

# Refactoring

Non modificare la struttura del progetto senza una decisione condivisa.

Prima si completa una funzionalità.

Successivamente si valuta il refactoring.

---

# Regola principale

Mai rompere il codice già funzionante.

La retrocompatibilità è una priorità del progetto.
