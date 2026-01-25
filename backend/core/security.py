import re
import logging
from typing import Any

class SensitiveDataFilter(logging.Filter):
    """
    Logan sisteminde PII (Hassas Veri) maskeleme için kullanılan filtre.
    Email, IP adresi ve özel şifre alanlarını maskeler.
    """
    
    # Basit regex örnekleri (Geliştirilebilir)
    EMAIL_PATTERN = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    IP_PATTERN = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    
    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        
        # Maskeleme işlemleri
        message = re.sub(self.EMAIL_PATTERN, "[MASKED_EMAIL]", message)
        message = re.sub(self.IP_PATTERN, "[MASKED_IP]", message)
        
        # Orijinal mesajı güncelle (Basitleştirilmiş yaklaşım)
        record.msg = message
        record.args = ()
        return True

def mask_sensitive_payload(data: dict[str, Any]) -> dict[str, Any]:
    """
    API verilerinde hassas alanları maskelemek için yardımcı fonksiyon.
    """
    mask_keys = ["password", "secret", "token", "apiKey"]
    masked_data = data.copy()
    
    for key in masked_data:
        if any(mk in key.lower() for mk in mask_keys):
            masked_data[key] = "********"
        elif isinstance(masked_data[key], dict):
            masked_data[key] = mask_sensitive_payload(masked_data[key])
            
    return masked_data
