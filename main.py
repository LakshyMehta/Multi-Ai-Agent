import json
from autogen import GroupChat, GroupChatManager
from Agents.doctor import doctor_agent
from Agents.patient import patient_agent
from Agents.judge import judge_agent
from config.llm_config import llm_config

# Initialize group chat
group_chat = GroupChat(
    agents=[patient_agent, doctor_agent, judge_agent],
    messages=[],
    max_round=10
)

manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config   
)

# Start chat with patient question
patient_agent.initiate_chat(
    manager,
    message="""
I have fever, sore throat, and body pain for 2 days.
What should I do?
"""
)

# Wait until all agents have replied (assuming synchronous for simplicity)
# Capture the latest reply from each agent
answers = {
    "P": patient_agent.chat_messages[patient_agent][-1]['content'] if patient_agent.chat_messages.get(patient_agent) else "",
    "D": doctor_agent.chat_messages[doctor_agent][-1]['content'] if doctor_agent.chat_messages.get(doctor_agent) else "",
    "J": judge_agent.chat_messages[judge_agent][-1]['content'] if judge_agent.chat_messages.get(judge_agent) else ""
}

# Save to JSON file
with open("agent_answers.json", "w") as f:
    json.dump(answers, f, indent=4)

print("Answers saved to agent_answers.json")
