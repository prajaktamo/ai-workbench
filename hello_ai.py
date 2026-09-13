import os
import sys
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIConnectionError

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")
if not(api_key):
    print("=" * 50)
    print("ERROR: OPENAI_API_KEY not found!")
    print()
    print("Setup steps:")
    print("  1. Copy .env.example to .env")
    print("  2. Replace 'sk-your-key-here' with your real API key")
    print("  3. Get a key at: https://platform.openai.com/api-keys")
    print("=" * 50)
    sys.exit(1)

client=OpenAI(api_key=api_key)
MODEL=os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


print("=" * 50)
print("Lab 1A: Your First LLM API Call")
print("=" * 50)
print(f"Model: {MODEL}")
print(f"API Key: {api_key[:8]}...{api_key[-4:]}")
print()
# ------------the call -----------


print("Sending Prompt: 'What is generative AI in one sentence?'")

try:
    response=client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role":"system", "content":"You are helpful assistance. Be concise."},
            {"role":"user", "content": "What is generative AI in one sentence"},
        ],
        temperature=0.7,
        max_tokens=100,
    )

    # response + errors
    print()
    print("Response:")
    print(f"Response : {response.choices[0].message.content}")
    print()
    print("-" * 50)
    print("Response metadata:")
    print(f"  Model used:        {response.model}")
    print(f"  Prompt tokens:     {response.usage.prompt_tokens}")
    print(f"  Completion tokens: {response.usage.completion_tokens}")
    print(f"  Total Token used : {response.usage.total_tokens}")
    print()
    print("✓ Success! You just talked to an AI from Python.")
    print("=" * 50)

except AuthenticationError:
    print("Error: Invalid API key. Check your .env file.")
except APIConnectionError:
    print("Error: Cannot connect. Check your internet")
except Exception as e:
    print(f"Unexpected error: {e}")