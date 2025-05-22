"""personalized_learning: ."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

personalized_learning_coordinator = LlmAgent(
    name="personalized_learning_coordinator",
    model=MODEL,
    description=(
        "analyzing seminal papers provided by the users, "
        "providing research advice, locating current papers "
        "relevant to the seminal paper, generating suggestions "
        "for new research directions, and accessing web resources "
        "to acquire knowledge"
    ),
    instruction=prompt.PERSONALIZED_LEARNING_COORDINATOR_PROMPT,
    # output_key=" ",
    tools=[
        # AgentTool(agent=academic_websearch_agent),
    ],
)

root_agent = personalized_learning_coordinator