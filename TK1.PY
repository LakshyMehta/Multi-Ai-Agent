import os
from google.genai import Client

# Set your Gemini API key
os.environ["GEMINI_API_KEY"] = "AIzaSyACBmkGu5m0XX3BhKe7p0KVNCB_bnptXBU"

# Initialize client
client = Client(api_key=os.environ["GEMINI_API_KEY"])

# Create a chat session with a supported model
chat = client.chats.create(model="gemini-2.5-flash")  # or another supported model

# Send a message through the chat
response = chat.send_message("Hello! Are you working?")

# Print the model’s reply
print(response.text)
