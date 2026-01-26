from ollama import chat
from ollama import ChatResponse
from core.repository import save_message
from core.config import CONTEXT
from core.prompt import build_system_prompt
from core.database import engine, Base
import core.models

Base.metadata.create_all(engine)

system_prompt = build_system_prompt(CONTEXT)
exit_message = ["exit", "quit"]


while True:

    user_input = str(input("Digite sua mensagem: "))

    if user_input.lower() in exit_message:
        break

    try:
        response: ChatResponse = chat(
            model="phi3:mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input},
            ],
        )

        save_message("user", user_input)
        print(f"MADDIE: {response.message.content}")
        save_message("maddie", response.message.content)

    except Exception as e:
        print(f"[ERROR] {e}")
