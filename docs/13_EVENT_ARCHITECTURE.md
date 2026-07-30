# EVENT ARCHITECTURE

Versione 1.0

---

# Filosofia

La piattaforma utilizza una architettura Event Driven.

Ogni evento importante genera una notifica interna.

I moduli non comunicano direttamente.

Comunicano attraverso eventi.

---

# Evento

Un evento rappresenta qualcosa che è accaduto.

Esempio

Prenotazione creata.

Pagamento ricevuto.

Cliente registrato.

---

# Schema

Producer

↓

Event Bus

↓

Consumer

---

# Eventi Booking

BookingCreated

BookingUpdated

BookingCancelled

BookingConfirmed

BookingCheckedIn

BookingCheckedOut

---

# Eventi CRM

CustomerCreated

CustomerUpdated

CustomerBlacklisted

CustomerDeleted

---

# Eventi Revenue

PriceChanged

DiscountCreated

PromotionActivated

PromotionExpired

---

# Eventi AI

PromptExecuted

ResponseGenerated

SuggestionAccepted

SuggestionRejected

---

# Eventi Sistema

UserCreated

UserDisabled

RoleAssigned

BackupCompleted

AuditGenerated

---

# Eventi Pagamenti

PaymentReceived

RefundCompleted

InvoiceIssued

---

# Eventi Territorio

MunicipalityUpdated

BeachUpdated

EventPublished

---

# Regole

Gli eventi sono immutabili.

Ogni evento possiede:

UUID

Timestamp

Producer

Payload

Versione
