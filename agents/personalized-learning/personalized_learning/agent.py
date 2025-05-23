"""personalized_learning: ."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from .tools import vark_questionnaire_tool

from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

personalized_learning_coordinator = LlmAgent(
    name="personalized_learning_coordinator",
    model=MODEL,
    description="""
        Responsible for providing adaptive support by acting as a virtual tutor.
        A key functionality of this agent is the ability to deliver explanatory feedback,
        justifying its suggestions and interventions to enhance transparency and student metacognition.
    """,
    instruction=prompt.PERSONALIZED_LEARNING_COORDINATOR_PROMPT,
    tools=[
        vark_questionnaire_tool,
        # AgentTool(agent=academic_websearch_agent),
    ],
)

root_agent = personalized_learning_coordinator