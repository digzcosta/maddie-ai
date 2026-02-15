def format_context(context: dict) -> str:
    return f"""
You are {context['name']}.
{context['description']}

Objective:
{context['objective']}

Tone:
{context['tone']}

Behavior:
- {"\n- ".join(context['behavior'])}

Limits:
- {"\n- ".join(context['limits'])}
""".strip()


def format_user_profile(user_profile: dict) -> str:
    """Format user profile in minimal, reference-only style"""
    return f"""
--- USER REFERENCE DATA (use sparingly) ---
Name: {user_profile['user_info']['name']}
Technical background: {', '.join(user_profile['professional_context']['skills'])}
Current focus: {user_profile['professional_context']['goal']}
Learning style: {user_profile['learning_preferences']['approach']}
--- END REFERENCE ---
""".strip()


def build_system_prompt(context: str, user_profile: str) -> str:
    """
    Builds the system prompt by combining Maddie's context with user profile.
    User profile is marked as reference-only to prevent forced connections.
    """
    
    prompt = f"""{context}

{user_profile}

CRITICAL: The user reference data above is for context ONLY. 
- Do NOT mention it unless the user's question directly relates to it
- Do NOT make small talk about their projects or background
- Do NOT ask follow-up questions about their work unless they bring it up first
- When in doubt, ignore the reference data and answer the question directly"""
    
    return prompt.strip()