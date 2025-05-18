from google.adk import SequentialAgent, LlmAgent

class OrquestradorWorkflow(SequentialAgent):
    """
    Orquestrador principal do sistema multi-agente.
    Responsável por coordenar a execução dos diferentes agentes especializados.
    """
    
    def __init__(self, name: str, model: str, description: str, instruction: str):
        super().__init__(
            name=name,
            model=model,
            description=description,
            instruction=instruction,
            sub_agents=[
                LlmAgent(
                    name="agente_especifico",
                    model=model,
                    description="Descrição do agente específico",
                    instruction="Instruções específicas"
                )
            ]
        ) 