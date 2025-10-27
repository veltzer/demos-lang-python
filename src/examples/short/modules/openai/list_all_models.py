"""
List all openai models
"""


import passpy
import openai

store = passpy.Store()
api_key = store.get_key("keys/openai").rstrip()
client = openai.OpenAI(api_key=api_key)
models = client.models.list()
for model in models.data:
    print(model.id)
