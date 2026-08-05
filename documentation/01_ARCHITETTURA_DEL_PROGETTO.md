# Documento

001_ARCHITETTURA_DEL_PROGETTO.md

## Scopo

...

## Stato

🟡 In evoluzione

## Versione

0.1

## Dipende da

000_MASTER_PLAN.md

## Alimenta

200_GOVERNANCE

400_CENTRO_STUDI

500_AI

...

## Documenti correlati

...

## Ultimo aggiornamento

05/08/2026

## Responsabile

Centro Studi Vacanze Sicure

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

---

# Esperienze Digitali

## Principio

Vacanze Sicure è un'unica piattaforma composta da servizi condivisi e da differenti esperienze digitali.

Non esistono applicazioni separate per ciascuna categoria di utenti.

Esiste un unico ecosistema che adatta automaticamente interfaccia, funzionalità e contenuti in funzione dell'identità digitale e dei permessi dell'utente.

---

# Esperienze previste

La piattaforma può presentarsi in modo differente, ad esempio, per:

- Visitatore pubblico;
- Ospite;
- Proprietario;
- Property Manager;
- Collaboratore;
- Manutentore;
- Fornitore di servizi;
- Ente pubblico;
- Amministratore Vacanze Sicure.

Ogni esperienza utilizza gli stessi dati e gli stessi servizi applicativi, mostrando esclusivamente le informazioni e gli strumenti necessari allo svolgimento delle attività consentite.

---

# Vantaggi

Questo modello consente di:

- utilizzare un'unica base dati;
- evitare duplicazioni di funzionalità;
- mantenere un'unica autenticazione;
- garantire coerenza tra tutti i servizi;
- semplificare manutenzione ed evoluzione della piattaforma;
- personalizzare l'esperienza utente senza frammentare il sistema.

---

# Adattamento Dinamico

L'interfaccia della piattaforma viene costruita dinamicamente in funzione di:

- ruolo dell'utente;
- permessi assegnati;
- dispositivo utilizzato;
- contesto operativo;
- preferenze personali;
- lingua.

Lo stesso utente può accedere a esperienze differenti qualora ricopra più ruoli.

---

# Principio Vacanze Sicure

Vacanze Sicure non sviluppa piattaforme differenti.

Sviluppa un unico ecosistema capace di offrire esperienze digitali differenti, mantenendo un'infrastruttura comune, coerente e integrata.

001_ARCHITETTURA_DELL_ECOSISTEMA.md

---

# Obbligo di Riservatezza

L'intero patrimonio documentale, progettuale, organizzativo e tecnologico di Vacanze Sicure costituisce un bene strategico dell'ecosistema.

Tutti i soggetti che partecipano allo sviluppo del progetto, a qualsiasi titolo, sono tenuti al massimo riserbo sulle informazioni alle quali hanno accesso durante lo svolgimento delle proprie attività.

L'obbligo di riservatezza riguarda, a titolo esemplificativo:

- documentazione progettuale;
- codice sorgente;
- architetture software;
- workflow;
- algoritmi;
- modelli di Intelligenza Artificiale;
- studi e analisi del Centro Studi;
- informazioni raccolte dall'Osservatorio Permanente;
- strategie commerciali;
- dati statistici;
- banche dati;
- informazioni sui partner;
- informazioni sugli utenti;
- procedure interne;
- qualsiasi informazione non destinata alla diffusione pubblica.

Ogni collaboratore, sviluppatore, consulente, partner o fornitore dovrà sottoscrivere specifici accordi di riservatezza (NDA) e utilizzare le informazioni esclusivamente per le finalità autorizzate.

La violazione dell'obbligo di riservatezza costituisce grave inadempimento contrattuale e potrà comportare la risoluzione del rapporto, il risarcimento degli eventuali danni e ogni altra tutela prevista dalla normativa vigente.

---

# Principio Vacanze Sicure

La fiducia rappresenta uno dei pilastri dell'ecosistema.

Proteggere il patrimonio di conoscenza significa tutelare il lavoro, le idee, l'innovazione e il valore creato da tutte le persone che contribuiscono alla crescita di Vacanze Sicure.

La riservatezza non ha lo scopo di limitare la collaborazione, ma di garantire che il patrimonio comune venga condiviso esclusivamente nell'interesse del progetto e nel rispetto dei diritti di tutti i soggetti coinvolti.
