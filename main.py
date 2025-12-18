from autogen import GroupChat, GroupChatManager
from Agents.doctor import doctor_agent
from Agents.patient import patient_agent
from Agents.judge import judge_agent

group_chat = GroupChat(
    agents=[patient_agent, doctor_agent, judge_agent],
    messages=[],
    max_round=3
)

manager = GroupChatManager(groupchat=group_chat)

patient_agent.initiate_chat(
    manager,
    message="""
I have fever, sore throat, and body pain for 2 days.
What should I do?
"""
)
