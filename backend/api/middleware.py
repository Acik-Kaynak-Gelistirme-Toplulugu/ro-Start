import functools
import time
import logging
from typing import Callable, Any
from backend.core.exceptions import ValidationError
from pydantic import ValidationError as PydanticValidationError

# Memory cache for simple caching strategy
_cache: dict[str, tuple[float, Any]] = {}

def async_cache(ttl_seconds: int = 300):
    """
    Asenkron sonuçlar için TTL tabanlı minimalist önbellekleme decoratörü.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            
            # Cache hit check
            if cache_key in _cache:
                timestamp, result = _cache[cache_key]
                if time.time() - timestamp < ttl_seconds:
                    return result
            
            # Execute and store
            result = await func(*args, **kwargs)
            _cache[cache_key] = (time.time(), result)
            return result
        return wrapper
    return decorator

def validate_input(schema: Any):
    """
    Pydantic kullanarak girdi doğrulaması yapan decorator.
    Zero Trust prensibini uygular.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        async def wrapper(data: Any, *args, **kwargs):
            try:
                validated_data = schema(**data) if isinstance(data, dict) else schema(data)
                return await func(validated_data, *args, **kwargs)
            except PydanticValidationError as e:
                logging.error(f"Input validation failed: {e.json()}")
                raise ValidationError(message="Geçersiz veri girdisi", details=e.errors())
        return wrapper
    return decorator

def performance_logger(func: Callable):
    """
    Fonksiyon çalışma süresini loglayan performans izleyici.
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()
        logging.info(f"Performance: {func.__name__} executed in {end_time - start_time:.4f}s")
        return result
    return wrapper
