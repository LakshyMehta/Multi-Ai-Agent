from autogen import GroupChat, GroupChatManager
from agents.doctor import doctor_agent
from agents.patient import patient_agent
from agents.judge import judge_agent

group_chat = GroupChat(
    agents=[patient_agent, doctor_agent, judge_agent],
    messages=[],
    max_round=3
)

manager = GroupChatManager(groupchat=group_chat)

# Start conversation
patient_agent.initiate_chat(
    manager,
    message="""
I have fever, sore throat, and body pain for 2 days.
What should I do?
"""
)
