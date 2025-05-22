from typing import Dict, Any
from google.adk.tools import ToolContext

def example_tool(parametro: str, tool_context: ToolContext) -> Dict[str, Any]:
    """
    Exemplo de ferramenta que pode ser utilizada pelos agentes.
    
    Args:
        parametro: Descrição do parâmetro
        tool_context: Contexto da ferramenta para acesso ao estado da sessão
        
    Returns:
        Dict[str, Any]: Resultado da execução da ferramenta
    """
    try:
        # Lógica da ferramenta aqui
        resultado = {"status": "sucesso", "mensagem": f"Processado: {parametro}"}
        
        # Exemplo de uso do tool_context
        tool_context.state["ultimo_resultado"] = resultado
        
        return resultado
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)} 