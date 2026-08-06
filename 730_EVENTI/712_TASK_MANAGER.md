# 712_TASK_MANAGER.md

# TASK MANAGER

> *"Una richiesta rappresenta un'esigenza. Un Task rappresenta un'azione concreta. Il Task Manager trasforma le decisioni in attività organizzate, monitorate e completabili."*

---

# Scopo

Il Task Manager costituisce il motore operativo dell'ecosistema **Vacanze Sicure**.

Ha il compito di pianificare, assegnare, monitorare e verificare tutte le attività operative generate dall'ecosistema.

Non gestisce solamente le attività manuali.

Gestisce qualsiasi azione che debba essere svolta da:

- persone;
- Intelligenza Artificiale;
- sistemi automatici;
- servizi esterni.

---

# Visione

Ogni evento dell'ecosistema può generare uno o più Task.

Una prenotazione.

↓

Un check-in.

↓

Una richiesta.

↓

Una manutenzione.

↓

Una pulizia.

↓

Un evento.

↓

Un pagamento.

↓

Una recensione.

Tutto può produrre attività.

---

# Obiettivi

Il modulo deve consentire di:

- organizzare il lavoro;
- evitare dimenticanze;
- distribuire i carichi;
- monitorare lo stato operativo;
- automatizzare le attività ripetitive;
- supportare gli operatori;
- alimentare la Timeline.

---

# Attori

## Operatore

Può:

- creare;
- modificare;
- assegnare;
- completare;
- sospendere;
- chiudere.

---

## Assistente AI

Può:

- generare Task;
- modificare priorità;
- suggerire assegnazioni;
- creare checklist;
- verificare scadenze;
- chiudere Task automatici.

---

## Sistema

Può creare Task automaticamente.

---

# Modello Dati

Ogni Task possiede un Fascicolo.

Campi minimi.

---

## Identificativo

ID univoco.

---

## Titolo

Descrizione sintetica.

---

## Descrizione

Dettaglio completo.

---

## Data Creazione

Timestamp.

---

## Scadenza

Data e ora.

---

## Priorità

Livello operativo.

---

## Stato

Workflow.

---

## Responsabile

Operatore assegnato.

---

## Richiesta collegata

Collegamento al modulo Gestione Richieste.

---

## Prenotazione

Eventuale prenotazione collegata.

---

## Ospite

Eventuale Fascicolo Ospite.

---

## Struttura

Struttura interessata.

---

## Documenti

Allegati.

---

## Timeline

Eventi generati.

---

# Origine dei Task

Un Task può nascere da:

- richiesta;
- prenotazione;
- check-in;
- check-out;
- pagamento;
- documento;
- evento;
- manutenzione;
- AI;
- operatore;
- sistema.

---

# Categorie

## Ospitalità

- check-in
- check-out
- accoglienza
- informazioni

---

## Manutenzione

- guasti
- verifiche
- controlli

---

## Pulizie

- pulizia camere
- cambio biancheria
- sanificazione

---

## Amministrazione

- fatture
- ricevute
- pagamenti

---

## Marketing

- newsletter
- social
- campagne
- recensioni

---

## Territorio

- eventi
- itinerari
- esperienze

---

## Documentazione

- contratti
- privacy
- documenti ospite

---

# Workflow

Nuovo

↓

Assegnato

↓

Accettato

↓

In lavorazione

↓

In attesa

↓

Completato

↓

Verificato

↓

Chiuso

↓

Archiviato

---

# Stati

## Nuovo

Appena creato.

---

## Assegnato

In attesa di presa in carico.

---

## Accettato

L'operatore conferma.

---

## In lavorazione

Attività in corso.

---

## In attesa

Dipende da eventi esterni.

---

## Completato

Attività conclusa.

---

## Verificato

Controllo positivo.

---

## Chiuso

Workflow terminato.

---

# Priorità

## 🔴 Critica

Intervento immediato.

---

## 🟠 Alta

Entro poche ore.

---

## 🟡 Media

Entro la giornata.

---

## 🔵 Bassa

Programmabile.

---

# Priorità Dinamica

La priorità non è fissa.

Può cambiare automaticamente in funzione di:

- arrivo dell'ospite;
- alta stagione;
- eventi territoriali;
- meteo;
- guasti;
- SLA;
- ritardi;
- carico degli operatori.

L'AI ricalcola continuamente la priorità.

---

# Task Automatici

Il sistema genera automaticamente attività.

Esempi.

Prenotazione confermata

↓

Inviare istruzioni check-in

↓

Preparare struttura

↓

Verifica pulizia

↓

Aggiornare disponibilità

---

# Task Generati dagli Eventi

Un evento può produrre:

- comunicazione ospiti;
- aggiornamento sito;
- newsletter;
- promozione social;
- preparazione materiale;
- suggerimenti AI.

---

# Task Ricorrenti

Supportati:

- giornalieri;
- settimanali;
- mensili;
- stagionali;
- annuali.

---

# Alta Stagione

Durante Ferragosto, Natale, Pasqua e ponti.

Il sistema:

- aumenta priorità;
- anticipa promemoria;
- evidenzia ritardi;
- riduce attività secondarie;
- concentra il lavoro sull'ospitalità.

---

# Checklist

Ogni Task può contenere checklist.

Esempio.

Pulizia appartamento.

□ Pavimenti

□ Bagno

□ Cucina

□ Lenzuola

□ Asciugamani

□ Climatizzatore

□ Wi-Fi

□ Fotografie finali

---

# Dipendenze

Un Task può dipendere da altri.

Pulizia

↓

Controllo qualità

↓

Check-in

---

# SLA

Ogni Task possiede:

- tempo di assegnazione;
- tempo massimo;
- ritardo;
- storico.

---

# Dashboard

Visualizzare.

- Task aperti;
- Task oggi;
- Task in ritardo;
- Task critici;
- Task completati;
- carico operatori.

---

# Ricerca

Ricerca per:

- struttura;
- ospite;
- prenotazione;
- categoria;
- responsabile;
- data;
- stato;
- priorità.

---

# KPI

Monitorare.

- Task creati;
- completati;
- ritardi;
- tempo medio;
- produttività;
- Task AI;
- Task automatici;
- Task ricorrenti.

---

# AI

L'Assistente può:

- creare Task;
- assegnarli;
- modificarli;
- suggerire priorità;
- individuare colli di bottiglia;
- prevedere ritardi;
- proporre redistribuzione del lavoro.

---

# Integrazione

Dialoga con:

- 101_FASCICOLO_OSPITE.md
- 102_FASCICOLO_PRENOTAZIONE.md
- 610_MOTORE_DOCUMENTALE.md
- 611_COMMUNICATION_ENGINE.md
- 620_MOTORE_DI_INTEGRAZIONE_DATI.md
- 621_MOTORE_WORKFLOW.md
- 622_MOTORE_NOTIFICHE.md
- 623_MOTORE_AUTOMAZIONI.md
- 624_MOTORE_REGOLE.md
- 625_MOTORE_ANALISI.md
- 626_MOTORE_CONVERSAZIONALE.md
- 715_GESTIONE_RICHIESTE.md
- 717_TIMELINE_DEGLI_EVENTI.md
- 719_GESTIONE_OPPORTUNITA.md
- 730_EVENTI_E_TERRITORIO.md
- 731_CALENDARIO_EVENTI.md
- 736_ESPERIENZE.md

---

# Sicurezza

Registrare:

- autore;
- modifiche;
- data;
- ora;
- stato precedente;
- stato successivo.

Audit completo.

---

# Privacy

Applicare GDPR.

Ogni Task eredita le autorizzazioni del Fascicolo collegato.

---

# Best Practice

- un Task deve avere un solo responsabile;
- ogni Task deve avere una scadenza;
- evitare Task duplicati;
- utilizzare checklist;
- automatizzare le attività ripetitive;
- mantenere aggiornato lo stato.

---

# Evoluzione

Il Task Manager evolverà verso un motore decisionale capace di:

- prevedere il carico di lavoro;
- suggerire l'assegnazione ottimale;
- anticipare criticità;
- distribuire automaticamente le attività;
- coordinare operatori umani e Assistente AI.

---

# Principio Vacanze Sicure

Il Task Manager non rappresenta una semplice lista di cose da fare.

È il motore operativo dell'ecosistema.

Ogni Task collega persone, strutture, ospiti, documenti, eventi e processi in un'unica rete organizzativa.

L'obiettivo non è controllare il lavoro degli operatori.

L'obiettivo è fare in modo che nessuna attività importante venga dimenticata, che ogni operatore sappia sempre cosa fare e che l'ecosistema continui a funzionare anche nei periodi di massimo carico operativo.

Ogni Task completato contribuisce ad aumentare l'efficienza dell'organizzazione, la qualità dell'accoglienza e la conoscenza condivisa dell'intero sistema.
