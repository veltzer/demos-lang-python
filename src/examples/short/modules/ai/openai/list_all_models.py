"""
List all openai models

The modules you need to install to make this work are `passpy` and `openai`
"""


import passpy
import openai

store = passpy.Store()
api_key = store.get_key("keys/openai")
assert api_key is not None
api_key = api_key.rstrip()
client = openai.OpenAI(api_key=api_key)
models = client.models.list()
for model in models.data:
    print(model.id)
