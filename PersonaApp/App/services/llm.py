import os
import importlib

from openai import OpenAI
from dotenv import load_dotenv
from fastapi import HTTPException

# Load environment variables
load_dotenv()

# Gemini Client
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def load_persona(persona: str):
    """
    Dynamically loads a persona's system prompt and examples.
    """

    # Make persona name case-insensitive
    persona = persona.strip().lower()

    try:

        system_prompt_module = importlib.import_module(
            f"App.personas.{persona}.system_prompt"
        )

        examples_module = importlib.import_module(
            f"App.personas.{persona}.examples"
        )

        return (
            system_prompt_module.SYSTEM_PROMPT,
            examples_module.EXAMPLES,
        )

    except ModuleNotFoundError:

        raise HTTPException(
            status_code=404,
            detail=f"Persona '{persona}' not found."
        )


def get_chat_response(persona: str, message: str) -> str:
    """
    Generates an AI response for the selected persona.
    """

    system_prompt, examples = load_persona(persona)

    messages = []

    # System Prompt
    messages.append(
        {
            "role": "system",
            "content": system_prompt
        }
    )

    # Few-shot Examples
    for example in examples:

        messages.append(
            {
                "role": "user",
                "content": example["user"]
            }
        )

        messages.append(
            {
                "role": "assistant",
                "content": example["assistant"]
            }
        )

    # Actual User Question
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    try:

        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=messages
        )

        return response.choices[0].message.content

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Gemini API Error: {str(e)}"
        )