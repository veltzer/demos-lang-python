"""
List all anthropic model names
"""

import passpy
import anthropic

store = passpy.Store()
api_key = store.get_key("keys/claude.ai")
assert api_key is not None
api_key = api_key.rstrip()
client = anthropic.Anthropic(api_key=api_key)
models = client.models.list()
for model in models:
    print(model.id)
