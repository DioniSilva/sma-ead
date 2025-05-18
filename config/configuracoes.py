from dataclasses import dataclass
from typing import Dict

@dataclass
class Config:
    """
    Configurações globais do projeto.
    """
    # Configurações do modelo
    MODEL_NAME: str = "gemini-1.5-pro-001"
    
    # Configurações de ambiente
    env_vars: Dict[str, str] = {
        "PROJECT_ID": "seu-projeto-id",
        "LOCATION": "us-central1",
        "API_VERSION": "v1"
    }
    
    # Outras configurações
    MAX_RETRIES: int = 3
    TIMEOUT: int = 30

# Instância global de configuração
CONFIG = Config() 