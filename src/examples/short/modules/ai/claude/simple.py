"""
Issue one prompt to anthropic

The modules you need to install to make this work are `passpy` and `anthropic`
"""

import anthropic
import passpy

QUERY="""
What is the capitol of France and how many residents are there?
Make your answer just a string and number with a comma in the middle
"""

store = passpy.Store()
api_key = store.get_key("keys/claude.ai")
assert api_key is not None
api_key = api_key.rstrip()
client = anthropic.Anthropic(api_key=api_key)
# models = client.models.list()
response = client.messages.create(
    # model=str(models.first_id),
    model="claude-opus-4-8",
    max_tokens=1000,
    messages=[{"role": "user", "content": QUERY }],
    # messages=[{"role": "user", "content": "Who was George Washington?"}]
)

print(response.content[0].text)  # type: ignore[union-attr]
