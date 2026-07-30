# Dominio 02

# STRUTTURE

Versione: 1.0

Stato: APPROVATO

---

# Scopo

Il dominio STRUTTURE gestisce l'anagrafica completa delle strutture ricettive registrate nella piattaforma.

Rappresenta il punto di partenza dell'intero sistema PMS.

Tutti gli altri domini fanno riferimento ad almeno una struttura.

---

# Obiettivi

Il dominio deve consentire di:

- registrare una nuova struttura;
- modificarne i dati;
- sospenderla;
- riattivarla;
- configurarne il funzionamento;
- gestirne documenti e media;
- associarvi utenti autorizzati.

---

# Attori

## Super Amministratore

Può creare qualsiasi struttura.

Può modificarla.

Può eliminarla logicamente.

Può trasferirne la proprietà.

---

## Proprietario

Può gestire esclusivamente le proprie strutture.

---

## Operatore

Può operare soltanto sulle strutture autorizzate.

---

## AI Assistant

Può consultare i dati.

Può proporre modifiche.

Non modifica mai direttamente il database.

---

# Casi d'uso

## UC-01

Creazione struttura

---

## UC-02

Modifica dati anagrafici

---

## UC-03

Configurazione operativa

---

## UC-04

Gestione servizi

---

## UC-05

Caricamento fotografie

---

## UC-06

Gestione documenti

---

## UC-07

Attivazione

---

## UC-08

Disattivazione

---

## UC-09

Archiviazione

---

# Flusso operativo

1. Creazione della struttura.
2. Assegnazione del proprietario.
3. Configurazione iniziale.
4. Inserimento delle unità ricettive.
5. Pubblicazione.
6. Apertura alle prenotazioni.

---

# Regole di business

## RB-01

Ogni struttura appartiene a un solo proprietario.

---

## RB-02

Ogni struttura deve appartenere a un comune del Salento.

---

## RB-03

Il CIN deve essere univoco.

---

## RB-04

Una struttura senza unità ricettive non può essere pubblicata.

---

## RB-05

Una struttura con prenotazioni future non può essere eliminata.

---

## RB-06

L'archiviazione è sempre logica.

I dati non vengono eliminati fisicamente.

---

## RB-07

Ogni modifica deve essere registrata nell'audit.

---

# Stati della struttura

BOZZA

↓

IN_CONFIGURAZIONE

↓

ATTIVA

↓

SOSPESA

↓

ARCHIVIATA

---

# Workflow

BOZZA

↓

Configurazione

↓

Inserimento unità

↓

Pubblicazione

↓

Prenotabile

↓

Sospensione

↓

Riattivazione

↓

Archiviazione

---

# Modello dati

Il dominio sarà composto dalle seguenti tabelle:

STRUTTURE

STRUTTURE_CONTATTI

STRUTTURE_CONFIGURAZIONE

STRUTTURE_SERVIZI

STRUTTURE_MEDIA

STRUTTURE_DOCUMENTI

STRUTTURE_SOCIAL

STRUTTURE_MAPPE

STRUTTURE_NOTE

STRUTTURE_UTENTI

---

# API

Il dominio esporrà API REST dedicate.

GET

POST

PUT

DELETE

SEARCH

---

# Sicurezza

Ogni operazione sarà soggetta ai permessi RBAC.

---

# Audit

Ogni modifica sarà tracciata.

---

# Estensioni future

Catene alberghiere.

Franchising.

Multi proprietà.

Gestioni esterne.

Integrazione con OTA.
