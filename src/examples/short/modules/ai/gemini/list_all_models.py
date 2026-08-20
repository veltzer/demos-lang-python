"""
List all models behind gemini

The modules you need to install to make this work are `passpy` and `google-genai`.
Note that the `google-generativeai` module is deprecated, so install `google-genai`.
"""

import google.genai
import passpy

store = passpy.Store()
api_key = store.get_key("keys/ai.google.dev")
assert api_key is not None
api_key = api_key.rstrip()

client = google.genai.Client(api_key=api_key)
print("Available models:")
for model in client.models.list():
    print(f"Model Name: {model.name}")
    print(f"Supported Actions: {model.supported_actions}")
