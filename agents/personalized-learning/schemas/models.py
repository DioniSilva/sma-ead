from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class EntradaAgente(BaseModel):
    """
    Schema para entrada de dados do agente.
    """
    texto: str
    parametros: Optional[Dict[str, Any]] = None

class SaidaAgente(BaseModel):
    """
    Schema para saída de dados do agente.
    """
    resultado: str
    metadados: Optional[Dict[str, Any]] = None
    status: str = "sucesso" 