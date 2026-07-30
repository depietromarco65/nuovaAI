# MODELLO DATI DEL PMS

Versione: 1.0

Stato: APPROVATO

---

# Filosofia

Ogni entità deve rappresentare un solo concetto.

Non sono ammesse tabelle "contenitore".

---

# Livello 1

La struttura ricettiva.

```
STRUTTURE
```

Contiene solo:

- identificativi
- dati fiscali
- localizzazione

---

# Livello 2

Configurazione della struttura

```
STRUTTURE_CONFIGURAZIONE
```

Contiene:

- check-in
- check-out
- soggiorno minimo
- soggiorno massimo
- politica animali
- politica bambini
- tassa soggiorno
- cauzione
- ecc.

---

# Livello 3

Contatti

```
STRUTTURE_CONTATTI
```

Contiene:

- telefono

- cellulare

- whatsapp

- email

- PEC

- sito web

---

# Livello 4

Social Network

```
STRUTTURE_SOCIAL
```

Facebook

Instagram

TikTok

YouTube

LinkedIn

Pinterest

Telegram

---

# Livello 5

Coordinate

```
STRUTTURE_MAPPE
```

latitudine

longitudine

Google Maps

What3Words

---

# Livello 6

Servizi

```
STRUTTURE_SERVIZI
```

WiFi

Piscina

Parcheggio

Ascensore

Colazione

Navetta

Animali

ecc.

---

# Livello 7

Documentazione

```
STRUTTURE_DOCUMENTI
```

SCIA

CIN

CIR

Assicurazioni

Contratti

Licenze

---

# Livello 8

Fotografie

```
STRUTTURE_MEDIA
```

Foto

Video

Virtual Tour

Brochure

PDF

---

# Livello 9

Utenti autorizzati

```
STRUTTURE_UTENTI
```

Amministratore

Reception

Collaboratore

Pulizie

Manutenzione

---

# Vantaggi

Database molto più pulito.

Più semplice da estendere.

Maggiore velocità.

Minor duplicazione dati.

Manutenzione facilitata.
