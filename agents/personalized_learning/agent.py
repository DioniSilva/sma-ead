"""personalized_learning: ."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from .tools import vark_questionnaire_tool
from opik.integrations.adk import OpikTracer

from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

opik_tracer = OpikTracer()

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
    before_agent_callback=opik_tracer.before_agent_callback,
    after_agent_callback=opik_tracer.after_agent_callback,
    before_model_callback=opik_tracer.before_model_callback,
    after_model_callback=opik_tracer.after_model_callback,
    before_tool_callback=opik_tracer.before_tool_callback,
    after_tool_callback=opik_tracer.after_tool_callback,
)

root_agent = personalized_learning_coordinator