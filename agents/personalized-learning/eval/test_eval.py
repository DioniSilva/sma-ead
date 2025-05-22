"""Basic evalualtion for Personalized Learning"""

import pathlib

import dotenv
import pytest
from google.adk.evaluation.agent_evaluator import AgentEvaluator


@pytest.fixture(scope="session", autouse=True)
def load_env():
    dotenv.load_dotenv()


def test_all():
    """Test the agent's basic ability on a few examples."""
    AgentEvaluator.evaluate(
        "personalized_learning",
        str(pathlib.Path(__file__).parent / "data"),
        num_runs=1,
    )
