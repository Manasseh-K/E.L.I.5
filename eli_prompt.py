def build_eli5_prompt(topic, level="5"):
    return f"""
Explain the following topic as if the listener is {level} years old.

Rules:
- Use very simple words
- Short sentences
- No technical jargon
- Use everyday examples
- If it sounds like a textbook, rewrite it

Topic:
{topic}
"""