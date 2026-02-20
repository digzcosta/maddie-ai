from ollama import chat
from ollama import ChatResponse
from core.repository import save_message, get_cache_messages, clear_cache
from core.config import CONTEXT, USER_PROFILE
from core.prompt import format_context, format_user_profile, build_system_prompt
from core.database import engine, Base
import core.models
import uuid

Base.metadata.create_all(engine)

user_profile = format_user_profile(USER_PROFILE)
context = format_context(CONTEXT)

system_prompt = build_system_prompt(context, user_profile)

exit_message = ["/exit", "/quit"]

session_id = str(uuid.uuid4())
clear_cache()


while True:

    user_input = str(input("Digite sua mensagem: "))

    if user_input.lower() in exit_message:
        break
    
    try:

        cache_history = get_cache_messages(limit=10)

        messages = [
            {"role": "system", "content": system_prompt}
        ] + cache_history + [
            {"role": "user", "content": user_input}
        ]

        response: ChatResponse = chat(
            model="phi3:mini",
            messages=messages,
        )

        save_message(role="user", content=user_input, is_cache=True, session_id=session_id)
        print(f"MADDIE: {response.message.content}")
        save_message(role="assistant", content=response.message.content, is_cache=True, session_id=session_id)

    except Exception as e:
        print(f"[ERROR] {e}")

clear_cache()