from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# -------------------------
# CoT Templates
# -------------------------

def concept_cot(question):
    return f"""
You are a Senior Software Engineer.

Question:
{question}

Think step by step:

1. Define the concept.
2. Explain why it was created.
3. Explain the problem it solves.
4. Explain how it works.
5. Explain important components.
6. Give a real-world example.
7. Advantages.
8. Disadvantages.
9. Final summary.
"""


def comparison_cot(question):
    return f"""
You are a Senior Software Engineer.

Question:
{question}

Think step by step:

1. Explain both options.
2. Compare architecture.
3. Compare performance.
4. Compare scalability.
5. Compare learning curve.
6. Compare job market.
7. Compare real-world usage.
8. Recommend one option.
9. Explain why.
"""


def debugging_cot(question):
    return f"""
You are a Senior Software Engineer.

Problem:
{question}

Think step by step:

1. Understand the issue.
2. Identify possible causes.
3. Investigate each cause.
4. Find root cause.
5. Suggest fixes.
6. Explain why the fix works.
"""


# -------------------------
# Router
# -------------------------

def classify_question(question):

    q = question.lower()

    if q.startswith("what is"):
        return "concept"

    if " vs " in q or " or " in q:
        return "comparison"

    if any(word in q for word in [
        "error",
        "bug",
        "issue",
        "not working",
        "failed",
        "exception"
    ]):
        return "debugging"

    return "concept"


def build_prompt(question):

    category = classify_question(question)

    if category == "concept":
        return concept_cot(question)

    elif category == "comparison":
        return comparison_cot(question)

    elif category == "debugging":
        return debugging_cot(question)

    return concept_cot(question)


# -------------------------
# Main Function
# -------------------------

def ask_llm(question):

    prompt = build_prompt(question)

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# -------------------------
# Teacher's Questions
# -------------------------

questions = [
    "What is JWT?",
    "What is Redis?",
    "What is Docker?",
    "What is PostgreSQL?",
    "What is FastAPI?"
]

for q in questions:
    print("\n" + "=" * 60)
    print(q)
    print("=" * 60)

    answer = ask_llm(q)
    print(answer)