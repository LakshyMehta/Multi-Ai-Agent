from autogen import AssistantAgent
from config.llm_config import llm_config

doctor_agent = AssistantAgent(
    name="Doctor_A1",
    system_message="""
You are a licensed medical expert.
You have to suggest appropriate medicine and treatment based on patient symptoms.
You give accurate, safe, and evidence-based medical advice.
If unsure, you say you are unsure.
Never hallucinate.
""",
    llm_config=llm_config,
)
