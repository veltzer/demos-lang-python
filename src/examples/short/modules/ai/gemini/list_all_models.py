"""
List all models behind gemini

To make this example work you need to install the `google-generativeai` module
"""

import passpy
import google.generativeai as genai

store = passpy.Store()
api_key = store.get_key("keys/ai.google.dev")
assert api_key is not None
api_key = api_key.rstrip()

genai.configure(api_key=api_key)
print("Available models:")
for model in genai.list_models():
    print(f"  {model.name}")
