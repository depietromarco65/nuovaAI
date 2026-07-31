"""
Servizi per la generazione dei messaggi destinati agli ospiti.

Le funzioni presenti in questo modulo devono rispettare il
PROMEMORIA DI CONFIGURAZIONE AI e gli Standard Operativi
di nuovaAI.
"""


def genera_messaggio_due_checkin(
    nome_ospite: str,
    alloggio: str,
    data_arrivo: str,
    info_extra: str = "",
    avviso_security: dict | None = None,
) -> str:
    """
    Genera il Messaggio 2 (Imminente Check-in).

    Sequenza obbligatoria:

    1. Saluto personalizzato
    2. Conferma check-in
    3. Protocollo Water Welcome Refrigerato
    4. Informazioni di viaggio
    5. Informazioni personalizzate
    6. Avvisi di sicurezza (se necessari)
    7. Chiusura calorosa
    """

    msg = ""

    # ------------------------------------------------------------------
    # 1. Saluto personalizzato
    # ------------------------------------------------------------------
    msg += (
        f"Buongiorno {nome_ospite}! Che bello leggerti, siamo felici che sia "
        "finalmente arrivato il momento delle vostre vacanze. "
        "Vi auguriamo un ottimo e sereno viaggio! 💪\n\n"
    )

    # ------------------------------------------------------------------
    # 2. Conferma del check-in
    # ------------------------------------------------------------------
    msg += (
        f"Ti confermiamo al 100% l'orario del check-in per domani, {data_arrivo}, "
        "a partire dalle ore 17:00 "
        "(la fascia ideale d'arrivo per l'accoglienza al bancone è tra le "
        "17:00 e le 18:00). "
        f"L'alloggio {alloggio} vi aspetta pronto e climatizzato.\n\n"
    )

    # ------------------------------------------------------------------
    # 3. Protocollo Water Welcome Refrigerato (OBBLIGATORIO)
    # ------------------------------------------------------------------
    msg += "🍼 UN PICCOLO GESTO DI BENVENUTO:\n"

    msg += (
        "Dopo un viaggio così lungo, ci farà piacere accogliervi con alcune "
        "bottiglie di acqua minerale già refrigerate nel frigorifero del vostro "
        "alloggio.\n"
        "Preferite acqua naturale oppure frizzante? "
        "Così prepareremo tutto prima del vostro arrivo.\n\n"
    )

    # ------------------------------------------------------------------
    # 4. Informazioni di viaggio
    # ------------------------------------------------------------------
    msg += "🚗 INFORMAZIONI DI VIAGGIO:\n"

    msg += (
        "Vi auguriamo un viaggio sereno. Durante il percorso verso il Capo di "
        "Leuca vi consigliamo di rispettare sempre i limiti di velocità e la "
        "segnaletica stradale. Nel periodo estivo sono presenti numerosi "
        "controlli della velocità sulle principali arterie (SS16, SS101 e "
        "SS274). Qualche minuto in più di viaggio vale sempre la tranquillità "
        "e la sicurezza.\n\n"
    )

    # ------------------------------------------------------------------
    # 5. Informazioni personalizzate
    # ------------------------------------------------------------------
    if info_extra:

        msg += "ℹ️ INFORMAZIONI PERSONALIZZATE:\n"
        msg += f"{info_extra}\n\n"

    # ------------------------------------------------------------------
    # 6. Avvisi di sicurezza
    # ------------------------------------------------------------------
    if avviso_security:

        msg += "🚨 AVVISO DI SICUREZZA:\n"

        msg += (
            f"• L'incidente informatico:\n"
            f"{avviso_security['incidente']}\n\n"
        )

        msg += (
            f"• Cosa deve fare l'ospite:\n"
            f"{avviso_security['comportamento']}\n\n"
        )

    # ------------------------------------------------------------------
    # 7. Chiusura calorosa
    # ------------------------------------------------------------------
    msg += (
        "Buon viaggio di cuore a tutti voi, "
        "vi aspettiamo domani a Torre Pali! 🚗☀️"
    )

    return msg
