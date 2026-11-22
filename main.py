import os
from dotenv import load_dotenv
import argparse

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("No API detected")

from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)



parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
#verbose
args = parser.parse_args()
#to access 'args.user_prompt'

messages=[
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ]

response = client.chat.completions.create(
    model="openrouter/free",
    messages = messages,
)


if response.usage is None:
    raise RuntimeError("usage does not exist")


if args.verbose is True:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")

print(f"Response: {response.choices[0].message.content}")
