"""
Issue one prompt to anthropic and force the answer into a JSON schema

The modules you need to install to make this work are `passpy` and `anthropic`
"""

import json

import anthropic
import passpy

QUERY = """
What is the capitol of France and how many residents are there?
"""

SCHEMA = {
    "type": "object",
    "properties": {
        "city": {"type": "string"},
        "country": {"type": "string"},
        "residents": {"type": "integer"},
    },
    "required": ["city", "country", "residents"],
    "additionalProperties": False,
}

store = passpy.Store()
api_key = store.get_key("keys/claude.ai")
assert api_key is not None
api_key = api_key.rstrip()
client = anthropic.Anthropic(api_key=api_key)
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1000,
    messages=[{"role": "user", "content": QUERY}],
    output_config={"format": {"type": "json_schema", "schema": SCHEMA}},
)

text = next(b.text for b in response.content if b.type == "text")  # type: ignore[union-attr]
data = json.loads(text)
print(data)
print(f"{data['city']}, {data['country']}: {data['residents']} residents")
