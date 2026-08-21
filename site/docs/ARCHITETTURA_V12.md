# Vacanze Sicure V12

## Separazione
- Aruba: distribuzione del sito statico/PHP.
- GitHub: sorgente, versionamento e file di deploy.
- Supabase: Data Core, FAQ pubbliche, traduzioni, eventi di sicurezza.
- Backend VìSì: unico punto autorizzato per AI, lettura dati e handoff.

## Regola
Il browser non deve conoscere service_role, password, prompt interni, security patterns riservati o endpoint amministrativi.
