900_ARCHITECTURE_EVOLUTION.md

Decisione:

La versione 1.0 utilizzerà:

css/
    main.css

js/
    main.js

per semplificare lo sviluppo.

Prima della versione Beta il codice verrà rifattorizzato in moduli ES6:

css/
    reset.css
    variables.css
    typography.css
    navbar.css
    hero.css
    sections.css
    footer.css
    responsive.css
    animations.css

js/
    main.js
    navbar.js
    scroll.js
    hero.js
    gallery.js
    season.js
    trust.js
    notifications.js
    ai.js
    utils.js

Motivazione:

- maggiore manutenibilità
- caricamento modulare
- debugging più semplice
- predisposizione alla piattaforma completa
