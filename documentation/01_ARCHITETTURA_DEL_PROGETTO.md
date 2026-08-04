# 01_ARCHITETTURA_DEL_PROGETTO.md

# ARCHITETTURA DEL PROGETTO

## Premessa

Vacanze Sicure non è un semplice portale turistico.

È una piattaforma digitale progettata per gestire l'intero ecosistema dell'ospitalità, mettendo in relazione ospiti, operatori, enti, istituzioni e servizi attraverso un insieme coordinato di processi, conoscenze e strumenti intelligenti.

L'architettura del progetto definisce l'organizzazione logica dell'intero sistema.

Non descrive il software.

Descrive come il sistema è stato pensato.

---

# Filosofia

L'architettura segue alcuni principi fondamentali.

- Centralità della persona.
- Centralità della conoscenza.
- Separazione tra dati e processi.
- Trasparenza.
- Modularità.
- Evoluzione continua.
- Tracciabilità.
- Interoperabilità.

Ogni componente deve poter evolvere senza compromettere l'intero sistema.

---

# I Pilastri

L'intero ecosistema si fonda su dieci pilastri.

## 1. Filosofia

Definisce i valori del progetto.

Documenti principali:

- 00_FILOSOFIA_DEL_PROGETTO.md
- 99_MANIFESTO.md

---

## 2. Governance

Definisce ruoli, responsabilità e modalità di gestione.

Documenti principali:

- 02_GOVERNANCE_DEL_PROGETTO.md
- Area Istituzionale

---

## 3. Conoscenza

Gestisce tutte le informazioni ufficiali.

Comprende:

- Knowledge Engine
- Knowledge Base
- FAQ
- Documentazione

---

## 4. Processi

Descrive il funzionamento operativo della piattaforma.

Comprende:

- candidature;
- validazione;
- certificazione;
- prenotazioni;
- ricollocazioni;
- notifiche;
- workflow.

---

## 5. Certificazione

Garantisce qualità e affidabilità.

Comprende:

- validazione;
- certificazione;
- monitoraggio;
- controlli.

---

## 6. Esperienza Utente

Supporta ospiti e operatori.

Comprende:

- Search Engine;
- Recommendation Engine;
- Assistente AI;
- Content Engine.

---

## 7. Gestione Operativa

Comprende:

- Fascicoli;
- prenotazioni;
- preventivi;
- Formula Fiduciaria;
- documentazione.

---

## 8. Tutela

Comprende:

- tutela dell'ospite;
- tutela dell'operatore;
- ricollocazione;
- gestione delle criticità.

---

## 9. Analisi

Comprende:

- benchmark;
- statistiche;
- miglioramento continuo;
- Registro Idee.

---

## 10. Evoluzione

Ogni componente della piattaforma deve poter evolvere senza alterare i principi fondamentali.

---

# Il Core di Vacanze Sicure

L'intera piattaforma ruota attorno ad un unico nucleo centrale.

## Vacanze Sicure Core

Il Core coordina:

- Knowledge;
- Decision;
- Workflow;
- Notification;
- Search;
- Recommendation;
- Assistente AI.

Questi non rappresentano software distinti ma servizi integrati che collaborano tra loro.

---

# Separazione delle responsabilità

Ogni componente ha un ruolo preciso.

## Il Knowledge Engine

Conosce.

---

## Il Content Engine

Comunica.

---

## Il Search Engine

Comprende i bisogni.

---

## Il Recommendation Engine

Suggerisce.

---

## Il Decision Engine

Applica le regole.

---

## Il Workflow Engine

Esegue i processi.

---

## L'Assistente AI

Dialoga con le persone.

---

# Fascicoli Digitali

Ogni informazione significativa viene conservata in un Fascicolo Digitale.

Ad esempio:

- Fascicolo della Struttura;
- Fascicolo dell'Operatore;
- Fascicolo della Prenotazione;
- Fascicolo delle Segnalazioni;
- Fascicolo della Certificazione.

I Fascicoli costituiscono la memoria storica della piattaforma.

---

# Architettura aperta

Vacanze Sicure nasce per dialogare con:

- enti pubblici;
- software gestionali;
- channel manager;
- sistemi di pagamento;
- sistemi di autenticazione;
- servizi esterni.

L'interoperabilità rappresenta uno dei principi fondamentali del progetto.

---

# Principio Architetturale

Ogni nuovo componente deve rispondere a tre domande.

1. Quale problema risolve?

2. In quale pilastro si colloca?

3. Con quali altri componenti interagisce?

Se non è possibile rispondere chiaramente a queste domande, il componente deve essere riprogettato.

---

# Filosofia Finale

L'architettura non nasce per gestire software.

Nasce per gestire fiducia.

Ogni componente della piattaforma esiste esclusivamente per migliorare l'esperienza degli ospiti, supportare gli operatori e rendere il turismo più trasparente, sicuro e collaborativo.
