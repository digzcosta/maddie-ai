def build_system_prompt(context: dict) -> str:
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