from fastapi import HTTPException, status


class ApplicationException(Exception):
    """
    Eccezione base dell'applicazione.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ValidationException(ApplicationException):
    """
    Errore di validazione.
    """
    pass


class NotFoundException(ApplicationException):
    """
    Risorsa non trovata.
    """
    pass


class AuthenticationException(ApplicationException):
    """
    Errore di autenticazione.
    """
    pass


class AuthorizationException(ApplicationException):
    """
    Errore di autorizzazione.
    """
    pass


def bad_request(message: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=message,
    )


def unauthorized(message: str = "Autenticazione richiesta") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=message,
    )


def forbidden(message: str = "Accesso negato") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=message,
    )


def not_found(message: str = "Risorsa non trovata") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=message,
    )


def conflict(message: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=message,
    )


def internal_error(message: str = "Errore interno del server") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=message,
    )
