from typing import Any, Optional
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    """Standart hata çıktı formatı."""
    success: bool = False
    error_code: str
    message: str
    details: Optional[Any] = None

class BaseAppException(Exception):
    """Uygulama genelinde temel hata sınıfı."""
    def __init__(self, message: str, error_code: str = "INTERNAL_ERROR", details: Any = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.details = details

class ValidationError(BaseAppException):
    """Girdi doğrulama hataları için."""
    def __init__(self, message: str, details: Any = None):
        super().__init__(message, error_code="VALIDATION_FAILED", details=details)

class UnauthorizedError(BaseAppException):
    """Yetkilendirme hataları için."""
    def __init__(self, message: str = "Yetkisiz erişim"):
        super().__init__(message, error_code="UNAUTHORIZED")

def global_exception_handler(error: Exception) -> ErrorResponse:
    """
    Tüm istisnaları yakalayıp standart formata dönüştüren merkezi handler.
    """
    if isinstance(error, BaseAppException):
        return ErrorResponse(
            error_code=error.error_code,
            message=error.message,
            details=error.details
        )
    
    # Beklenmeyen hatalar için
    return ErrorResponse(
        error_code="UNEXPECTED_ERROR",
        message="Beklenmeyen bir hata oluştu.",
        details=str(error) if True else None # Production'da str(error) gizlenmeli
    )
