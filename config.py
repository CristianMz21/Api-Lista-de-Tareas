from pydantic_settings import BaseSettings
from datetime import timedelta
import os
from typing import Optional

class Settings(BaseSettings):
    # Configuración de seguridad
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Configuración de base de datos
    DATABASE_URL: Optional[str] = "sqlite:///./sql_app.db"

    class Config:
        env_file = ".env"

settings = Settings()