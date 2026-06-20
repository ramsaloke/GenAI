from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def cot_prompt(question):

    prompt = f"""
    Act as a senior software engineer.

    Question:
    {question}

    Think step by step:

    1. Understand the problem
    2. Explain core concepts
    3. Give example
    4. Mention advantages
    5. Mention disadvantages
    6. Final summary give one answer only with word this if final
    """

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content

print(cot_prompt("expresjs or nestjs which is best ?"))