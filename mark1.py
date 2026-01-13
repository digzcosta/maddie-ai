from ollama import chat
from ollama import ChatResponse
import json
from database import save_message, load_history

with open("maddie_context.json", "r", encoding="utf-8") as f:
    context = json.load(f)

system_prompt = f"""
You are {context['name']}.
{context['description']}

Objective:
{context['objective']}

Tone:
{context['tone']}

Limits:
- {"\n- ".join(context['limits'])}
"""

exit_message = ["exit", "quit"]

message_history = load_history()
print(message_history)

while True:

    user_input = str(input("Digite sua mensagem: ")).lower()

    if user_input in exit_message:
        break
    

    else:

        response: ChatResponse = chat(model='phi3:mini', messages= [
            { # Maddie's config (Context)
            "role": "system",
            "content": system_prompt
        },
        { # User's message
            "role": "user",
            "content": user_input
        }
        ])
        save_message("user", user_input)
        print(f"MADDIE: {response.message.content}")    
        save_message("maddie", response.message.content)
    
    
    