from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
import os

class Settings(BaseSettings):
    """
    Project Configuration using Pydantic Settings.
    Secret management via .env file or environment variables.
    """
    # App Info
    APP_NAME: str = "Ro-Start"
    APP_VERSION: str = "1.2.0"
    DEBUG: bool = False
    
    # Security
    API_SECRET_KEY: str = "change-me-in-production" # Default for safety, override in Vault/.env
    ALLOWED_CORS_ORIGINS: list[str] = ["app://ro-start", "http://localhost:5173"]
    
    # Caching
    CACHE_TTL: int = 3600  # 1 hour
    
    # Storage Paths
    LOG_LEVEL: str = "INFO"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

# Singleton instance
settings = Settings()
