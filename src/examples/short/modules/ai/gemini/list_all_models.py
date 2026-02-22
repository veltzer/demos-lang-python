"""
List all models behind gemini

The `google-generativeai` module is deprecated.
Install `google-genai` so that this example runs.
"""

import passpy
from google import genai

store = passpy.Store()
api_key = store.get_key("keys/ai.google.dev")
assert api_key is not None
api_key = api_key.rstrip()

client = genai.Client(api_key=api_key)
print("Available models:")
for model in client.models.list():
    print(f"Model Name: {model.name}")
    print(f"Supported Actions: {model.supported_actions}")
