"""
Issue one prompt to anthropic
"""

import passpy
import anthropic

store = passpy.Store()
api_key = store.get_key("keys/claude.ai")
assert api_key is not None
api_key = api_key.rstrip()
client = anthropic.Anthropic(api_key=api_key)
models = client.models.list()
response = client.messages.create(
    model=str(models.first_id),
    max_tokens=1000,
    messages=[{"role": "user", "content": "Who was George Washington?"}]
)

print(response.content[0].text)  # type: ignore[union-attr]
