from typing import Dict, Any, List
from google.adk.tools import ToolContext, FunctionTool

VARK_QUESTIONNAIRE = [
    {
        "question": "Quando você está aprendendo algo novo, o que você prefere fazer?",
        "options": {
            "A": "Ver diagramas, gráficos ou imagens explicativas.",
            "B": "Ouvir explicações ou discussões sobre o assunto.",
            "C": "Ler textos ou escrever resumos sobre o tema.",
            "D": "Fazer atividades práticas ou experimentos."
        }
    },
    {
        "question": "Como você prefere receber instruções para realizar uma tarefa?",
        "options": {
            "A": "Com ilustrações ou diagramas que mostrem o processo.",
            "B": "Com explicações verbais detalhadas.",
            "C": "Com manuais ou listas de instruções escritas.",
            "D": "Com demonstrações práticas ou tentando fazer diretamente."
        }
    },
    {
        "question": "Quando você está estudando, o que mais te ajuda a entender o conteúdo?",
        "options": {
            "A": "Usar mapas mentais, gráficos ou tabelas.",
            "B": "Participar de discussões ou ouvir podcasts.",
            "C": "Ler livros ou anotar informações importantes.",
            "D": "Fazer exercícios ou simulações práticas."
        }
    },
    {
        "question": "Qual das seguintes atividades você prefere em um ambiente de aprendizado?",
        "options": {
            "A": "Observar apresentações visuais ou vídeos.",
            "B": "Ouvir palestras ou explicações.",
            "C": "Ler materiais de estudo ou escrever resumos.",
            "D": "Participar de atividades práticas ou workshops."
        }
    },
    {
        "question": "Como você prefere revisar o conteúdo aprendido?",
        "options": {
            "A": "Revisar gráficos, diagramas ou mapas conceituais.",
            "B": "Ouvir gravações ou discutir com colegas.",
            "C": "Reler anotações ou criar resumos escritos.",
            "D": "Refazer exercícios ou realizar experimentos."
        }
    },
    {
        "question": "Quando você está resolvendo um problema, como você prefere abordá-lo?",
        "options": {
            "A": "Desenhando ou visualizando o problema.",
            "B": "Conversando sobre o problema com alguém.",
            "C": "Escrevendo os passos ou analisando informações escritas.",
            "D": "Testando soluções práticas ou experimentando."
        }
    },
    {
        "question": "Qual formato de material de estudo você acha mais útil?",
        "options": {
            "A": "Slides com imagens e diagramas.",
            "B": "Áudios ou vídeos explicativos.",
            "C": "Textos detalhados ou apostilas.",
            "D": "Kits de experimentação ou ferramentas práticas."
        }
    },
    {
        "question": "Como você prefere aprender um novo software ou ferramenta?",
        "options": {
            "A": "Assistindo a tutoriais visuais ou diagramas.",
            "B": "Ouvindo explicações ou instruções.",
            "C": "Lendo manuais ou guias escritos.",
            "D": "Explorando a ferramenta e aprendendo na prática."
        }
    }
]

def generate_vark_questionnaire(tool_context: ToolContext) -> Dict[str, Any]:
    """
    Generates and stores a VARK questionnaire in the tool context.

    The purpose of this function is to create a questionnaire based on the VARK model (Visual, Auditory, Reading/Writing, Kinesthetic),
    which helps identify the user's learning style. The questionnaire is saved in the context state for later use.

    Args:
        tool_context: The tool context to access and modify the session state.

    Returns:
        Dict[str, Any]: Dictionary containing the operation status and the generated questionnaire.
    """
    try:
        # Example of VARK questions
        questionnaire = VARK_QUESTIONNAIRE
        
        # Store the questionnaire in the context state
        tool_context.state["vark_questionnaire"] = questionnaire
        
        return {"status": "success", "questionnaire": questionnaire}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
vark_questionnaire_tool = FunctionTool(func=generate_vark_questionnaire)