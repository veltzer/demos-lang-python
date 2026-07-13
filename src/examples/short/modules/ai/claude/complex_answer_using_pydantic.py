"""
Issue one prompt to anthropic and get back a validated pydantic object

The modules you need to install to make this work are `passpy`, `anthropic` and `pydantic`
"""

import passpy
import anthropic
from pydantic import BaseModel

QUERY = """
What is the capitol of France and how many residents are there?
"""


class Capitol(BaseModel):
    city: str
    country: str
    residents: int


store = passpy.Store()
api_key = store.get_key("keys/claude.ai")
assert api_key is not None
api_key = api_key.rstrip()
client = anthropic.Anthropic(api_key=api_key)
response = client.messages.parse(
    model="claude-opus-4-8",
    max_tokens=1000,
    messages=[{"role": "user", "content": QUERY}],
    output_format=Capitol,
)

# already validated against the model
data = response.parsed_output
assert data is not None
print(data)
print(f"{data.city}, {data.country}: {data.residents} residents")
