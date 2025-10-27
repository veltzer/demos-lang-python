"""
Submit a simple query to openai
"""

import passpy
import openai

store = passpy.Store()
api_key = store.get_key("keys/openai").rstrip()
# print(f"api_key is [{api_key}]")

client = openai.OpenAI(api_key=api_key)
models = client.models.list()
response = client.chat.completions.create(
    # model="gpt-5",
    model="gpt-4.1",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
print(response.choices[0].message.content)
