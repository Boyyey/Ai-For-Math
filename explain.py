import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_solution(equation_str):
    prompt = f"Explain how to solve this equation step-by-step:\n{equation_str}"
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
