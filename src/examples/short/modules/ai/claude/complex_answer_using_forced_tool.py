"""
Issue one prompt to anthropic and force the answer through a strict tool call

The modules you need to install to make this work are `passpy` and `anthropic`
"""

import passpy
import anthropic
from anthropic.types import ToolParam, ToolChoiceToolParam

QUERY = """
What is the capitol of France and how many residents are there?
"""

TOOL: ToolParam = {
    "name": "record_answer",
    "description": "Record the capitol city of a country and its population",
    "strict": True,
    "input_schema": {
        "type": "object",
        "properties": {
            "city": {"type": "string"},
            "country": {"type": "string"},
            "residents": {"type": "integer"},
        },
        "required": ["city", "country", "residents"],
        "additionalProperties": False,
    },
}
TOOL_CHOICE: ToolChoiceToolParam = {"type": "tool", "name": "record_answer"}

store = passpy.Store()
api_key = store.get_key("keys/claude.ai")
assert api_key is not None
api_key = api_key.rstrip()
client = anthropic.Anthropic(api_key=api_key)
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1000,
    messages=[{"role": "user", "content": QUERY}],
    tools=[TOOL],
    tool_choice=TOOL_CHOICE,
)

# `strict` guarantees the input validates against the schema, already parsed
data = next(b.input for b in response.content if b.type == "tool_use")  # type: ignore[union-attr]
print(data)
print(f"{data['city']}, {data['country']}: {data['residents']} residents")
