"""
A simple example of asking gemini a question

The modules you need to install to make this work are `passpy` and `google-genai`.
Note that the `google-generativeai` module is deprecated, so install `google-genai`.
"""

import passpy
from google import genai

store = passpy.Store()
api_key = store.get_key("keys/ai.google.dev")
assert api_key is not None
api_key = api_key.rstrip()

client = genai.Client(api_key=api_key)
question = "What are the benefits of renewable energy?"
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=question,
)
print(f"Question: {question}")
print(f"Answer: {response.text}")
