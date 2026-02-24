import ollama


def generate_explanation(entities, eligible_schemes):

    prompt = f"""
You are an assistant helping citizens understand government scheme eligibility.

User details:
{entities}

Eligible schemes:
{eligible_schemes}

Explain in simple clear English WHY the user is eligible.
Keep explanation short and helpful.
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]