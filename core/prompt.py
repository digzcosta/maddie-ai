def format_context(context: dict) -> str:
    return f"""
You are {context['name']}.
{context['description']}

Objective:
{context['objective']}

Tone:
{context['tone']}

Limits:
- {"\n- ".join(context['limits'])}
""".strip()


def format_user_profile(user_profile: dict) -> str:
    return f"""
USER PROFILE:
Name: {user_profile['user_info']['name']}
Language: {user_profile['user_info']['language']}

Professional Context:
- Status: {user_profile['professional_context']['status']}
- Skills: {', '.join(user_profile['professional_context']['skills'])}
- Goal: {user_profile['professional_context']['goal']}

Active Projects:
- {chr(10).join(f"  • {project}" for project in user_profile['projects']['active'])}

Learning Preferences:
- Style: {user_profile['learning_preferences']['style']}
- Approach: {user_profile['learning_preferences']['approach']}
""".strip()


def build_system_prompt(context: str, user_profile: str) -> str:
    # Combining Maddie's context with User information
    return f"{context}\n\n{user_profile}".strip()