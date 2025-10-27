"""
Issue one prompt to anthropic
"""

import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

models = client.models.list()
response = client.messages.create(
    model=models.first_id,
    max_tokens=1000,
    messages=[{"role": "user", "content": "Who was George Washington?"}]
)

print(response.content[0].text)
