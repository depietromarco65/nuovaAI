from pathlib import Path
import zipfile
import pypandoc

base = Path("/mnt/data/nuovaAI-main")
if not base.exists():
    # try alternate extracted folder name
    candidates = [p for p in Path("/mnt/data").iterdir() if p.is_dir() and "nuovaAI" in p.name]
    if candidates:
        base = candidates[0]
docs = base / "documentation"
docs.mkdir(parents=True, exist_ok=True)

text = """# DATABASE_MASTER.md

# nuovaAI - Database Master

Versione: 1.0

## Scopo

Questo documento definisce l'architettura ufficiale del database del progetto nuovaAI.

## Principi

- PostgreSQL
- SQLAlchemy
- Alembic
- UUID come chiavi primarie
- Architettura multi-tenant
- Soft delete
- Audit log
- Integrità referenziale

## Macro-aree

1. Core
2. Strutture
3. Alloggi
4. CRM
5. Prenotazioni
6. Disponibilità
7. Prezzi
8. Pagamenti
9. Servizi
10. Housekeeping
11. Comunicazioni
12. Channel Manager
13. AI
14. Business Intelligence

## Convenzione

Ogni tabella dovrà documentare:
- Scopo
- Colonne
- Tipi dati
- PK
- FK
- Indici
- Vincoli
- Regole di business

## Workflow importazione

CSV / OTA / Booking Engine
↓
Validator
↓
Normalizer
↓
PostgreSQL

Questo documento sarà progressivamente esteso fino a descrivere tutte le tabelle del sistema.
"""

outfile = docs/"DATABASE_MASTER.md"
pypandoc.convert_text(text,"md",format="md",outputfile=str(outfile),extra_args=["--standalone"])

zip_path="/mnt/data/nuovaAI-main_con_DATABASE_MASTER.zip"
with zipfile.ZipFile(zip_path,"w",zipfile.ZIP_DEFLATED) as z:
    if base.exists():
        for f in base.rglob("*"):
            z.write(f,f.relative_to(base.parent))
    else:
        z.write(outfile, Path("nuovaAI-main")/"documentation"/"DATABASE_MASTER.md")

print(outfile, zip_path)
