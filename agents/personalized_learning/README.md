# Sistema Multi-Agente com Google ADK

Este projeto implementa um sistema multi-agente utilizando o Google Agent Development Kit (ADK) e Google Genai, permitindo a criação de agentes inteligentes que podem trabalhar em conjunto para resolver tarefas complexas.

## 🚀 Tecnologias Utilizadas

- Python 3.9+
- Google ADK
- Google Genai
- Pydantic
- Python-dotenv

## 📋 Pré-requisitos

- Python 3.9 ou superior
- Conta Google Cloud Platform (GCP)
- API Key do Google Genai
- Git

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
```

2. Crie e ative um ambiente virtual:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
# Copie o arquivo de exemplo
cp .env-example .env

# Edite o arquivo .env com suas configurações
# - GOOGLE_API_KEY: Sua chave de API do Google Genai
# - PROJECT_ID: ID do seu projeto GCP
# - Outras configurações conforme necessário
```

## 🏃‍♂️ Como Executar

1. Certifique-se de que todas as dependências estão instaladas e o ambiente virtual está ativo

2. Execute o projeto:
```bash
python main.py
```

## 📁 Estrutura do Projeto

```
projeto/
├── agents/                    # Agentes do sistema
│   ├── workflow_agents/       # Agentes de orquestração
│   ├── llm_agents/           # Agentes baseados em LLM
│   └── custom_agents/        # Agentes customizados
├── tools/                    # Ferramentas disponíveis
├── schemas/                  # Schemas de dados
├── config/                   # Configurações
├── utils/                    # Utilitários
└── main.py                   # Ponto de entrada
```

## 🔑 Configuração do Ambiente

1. Obtenha uma API Key do Google Genai:
   - Acesse o [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Crie uma nova API Key
   - Copie a chave para o arquivo `.env`

2. Configure o arquivo `.env`:
```env
GOOGLE_API_KEY=sua-api-key-aqui
PROJECT_ID=seu-projeto-id
MODEL_NAME=gemini-1.5-pro-001
```

## 🛠️ Desenvolvimento

### Adicionando Novos Agentes

1. Crie um novo arquivo em `agents/llm_agents/` ou `agents/custom_agents/`
2. Implemente a classe do agente herdando de `LlmAgent` ou `CustomAgent`
3. Registre o agente no orquestrador em `agents/workflow_agents/orquestrador.py`

Exemplo:
```python
from google.adk import LlmAgent

class MeuNovoAgente(LlmAgent):
    def __init__(self, name: str, model: str, description: str, instruction: str):
        super().__init__(
            name=name,
            model=model,
            description=description,
            instruction=instruction
        )
```

### Adicionando Novas Ferramentas

1. Adicione a função da ferramenta em `tools/ferramentas.py`
2. Documente a ferramenta com docstrings detalhadas
3. Registre a ferramenta no agente que irá utilizá-la

Exemplo:
```python
from google.adk import ToolContext

def minha_ferramenta(parametro: str, tool_context: ToolContext):
    """
    Descrição da ferramenta.
    
    Args:
        parametro: Descrição do parâmetro
        tool_context: Contexto da ferramenta
        
    Returns:
        Dict com o resultado
    """
    return {"status": "sucesso", "resultado": parametro}
```

## 📝 Logs

Os logs são configurados para exibir informações detalhadas sobre a execução do sistema. Você pode ajustar o nível de log no arquivo `.env`:

```env
LOG_LEVEL=INFO  # Opções: DEBUG, INFO, WARNING, ERROR, CRITICAL
```

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ⚠️ Troubleshooting

### Problemas Comuns

1. **Erro de API Key não encontrada**
   - Verifique se o arquivo `.env` existe e contém a chave correta
   - Confirme se a API Key é válida no Google AI Studio

2. **Erro de dependências**
   - Certifique-se de que o ambiente virtual está ativo
   - Execute `pip install -r requirements.txt` novamente

3. **Erro de importação**
   - Verifique se todas as dependências estão instaladas
   - Confirme se está usando a versão correta do Python

## 📞 Suporte

Para suporte, abra uma issue no repositório ou entre em contato através de [seu-email@exemplo.com]. 