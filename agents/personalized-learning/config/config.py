from dataclasses import dataclass
from typing import Dict

@dataclass
class Config:
    """
    Configurações globais do agente.
    """
    # Configurações do modelo
    MODELS: Dict[str, str] = {
        "GEMINI_2_0_FLASH": "gemini-2.0-flash",
        "GPT4O": "openai/gpt-4o",
        "CLAUDE_SONNET": "anthropic/claude-3-sonnet-20240229"
    }
    
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