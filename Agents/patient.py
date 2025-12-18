from autogen import AssistantAgent
from config.llm_config import llm_config

patient_agent = AssistantAgent(
    name="Patient_A2",
    system_message="""
You are a patient.
You describe symptoms realistically.
You ask follow-up questions like a real human.
Do not give medical advice.
""",
    llm_config=llm_config,
)
