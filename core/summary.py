# Function to summarize messages when the /save command is called.
from ollama import chat

def generate_summary(user_message, assistant_message):
    prompt = f"""Summarize this interaction in 2-3 clear and objective sentences, focusing on the main topic and what was discussed:

    User: {user_message.content}
    Assistant: {assistant_message.content}

    Summary:"""

    messages = [
        {"role": "system", "content": "You are an assistant specialized in creating concise and informative conversation summaries."},
        {"role": "user", "content": prompt}
    ]
    
    try:
        response = chat(
            model="phi3:mini",
            messages=messages
        )
        return response.message.content.strip()
    
    except Exception as e:
        print(f"[ERROR] Failed to generate summary: {e}")
        return None