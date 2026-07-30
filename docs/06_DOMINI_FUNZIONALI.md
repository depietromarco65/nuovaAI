# Documento

06_DOMINI_FUNZIONALI.md

Versione: 1.0
Stato: APPROVATO
Ultimo aggiornamento: 30/07/2026

Autore:
Marco Antonio De Pietro

Progetto:
Vacanze Sicure nel Salento

---

# Domini Funzionali

## Introduzione

La piattaforma è suddivisa in domini funzionali indipendenti.

Ogni dominio rappresenta un insieme di funzionalità omogenee che condividono dati, logiche di business e processi operativi.

Questo approccio permette di sviluppare, testare ed estendere il software senza compromettere gli altri moduli.

---

# Dominio 01 - Sistema

Gestisce il funzionamento dell'intera piattaforma.

## Comprende

- Utenti
- Ruoli
- Permessi
- Configurazioni
- Audit
- Log
- Backup
- API
- Notifiche

---

# Dominio 02 - Strutture

Gestisce le strutture ricettive.

## Comprende

- Anagrafica strutture
- Contatti
- Configurazioni
- Servizi
- Media
- Documenti
- Utenti associati
- Social
- Coordinate

---

# Dominio 03 - Unità Ricettive

Gestisce ogni unità prenotabile.

## Comprende

- Appartamenti
- Ville
- Monolocali
- Camere
- Suite
- Pajare
- Casali

Ogni unità dispone di:

- caratteristiche
- fotografie
- disponibilità
- listini
- servizi
- dotazioni

---

# Dominio 04 - Prenotazioni

Gestisce il ciclo completo della prenotazione.

## Comprende

- Preventivi
- Prenotazioni
- Calendari
- Disponibilità
- Check-in
- Check-out
- Ospiti
- Documenti
- Contratti

---

# Dominio 05 - CRM

Gestione del cliente.

Comprende

- Anagrafiche
- Comunicazioni
- WhatsApp
- Email
- Telefonate
- Preventivi
- Storico
- Fidelizzazione

---

# Dominio 06 - Revenue Management

Comprende

- Rack Rate
- Listini
- Stagionalità
- Sconti
- Promozioni
- Offerte
- Analisi occupazione
- KPI

---

# Dominio 07 - Pagamenti

Comprende

- Pagamenti
- Acconti
- Saldi
- Rimborsi
- Fatture
- Ricevute

---

# Dominio 08 - Territorio

Comprende

- Province
- Comuni
- Marine
- Frazioni
- Spiagge
- Porti
- Torri Costiere
- Attrazioni
- Eventi

---

# Dominio 09 - AI

Comprende

- Prompt
- Regole
- Log
- Cronologia
- Classificazioni
- Automazioni

---

# Dominio 10 - Portale Pubblico

Comprende

- Ricerca strutture
- Schede strutture
- Schede unità
- Prenotazione online
- Blog
- Eventi
- Guide del territorio

---

# Dominio 11 - Owner Area

Comprende

- Dashboard
- Occupazione
- Statistiche
- Calendari
- Ricavi
- Documentazione

---

# Dominio 12 - Client Area

Comprende

- Prenotazioni
- Pagamenti
- Documenti
- Check-in online
- Assistenza
- Chat AI

---

# Regola progettuale

Ogni dominio sarà progettato in modo indipendente.

Per ciascun dominio saranno definiti:

- obiettivi;
- processi;
- modello dati;
- tabelle;
- relazioni;
- API;
- interfacce utente;
- regole di business.

Solo dopo l'approvazione del dominio si procederà alla scrittura dello schema SQL.
