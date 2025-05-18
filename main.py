from google.adk import AdkApp
from agents.workflow_agents.orquestrador import OrquestradorWorkflow
from config.configuracoes import CONFIG

def main():
    """
    Função principal que inicializa e configura o sistema multi-agente.
    """
    # Configuração do agente principal
    orquestrador = OrquestradorWorkflow(
        name="orquestrador_principal_v1.0",
        model="gemini-1.5-pro-001",
        description="Orquestrador principal do sistema multi-agente",
        instruction="Instruções detalhadas para o orquestrador"
    )
    
    # Configuração da aplicação ADK
    app = AdkApp(
        agent=orquestrador,
        requirements="requirements.txt",
        env_vars=CONFIG.env_vars
    )
    
    return app

if __name__ == "__main__":
    app = main() 