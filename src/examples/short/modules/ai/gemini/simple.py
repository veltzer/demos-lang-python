"""
A simple example of asking gemini a question

To make this example work you need to install the `google-generativeai` module
"""

import passpy
import google.generativeai as genai

store = passpy.Store()
api_key = store.get_key("keys/ai.google.dev")
assert api_key is not None
api_key = api_key.rstrip()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")
question = "What are the benefits of renewable energy?"
response = model.generate_content(question)
print(f"Question: {question}")
print(f"Answer: {response.text}")
