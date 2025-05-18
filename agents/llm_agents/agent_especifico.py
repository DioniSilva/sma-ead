from google.adk import LlmAgent
from tools.ferramentas import ferramenta_exemplo

class AgenteEspecifico(LlmAgent):
    """
    Agente especializado para uma tarefa específica.
    """
    
    def __init__(self, name: str, model: str, description: str, instruction: str):
        super().__init__(
            name=name,
            model=model,
            description=description,
            instruction=instruction,
            tools=[ferramenta_exemplo]
        ) 