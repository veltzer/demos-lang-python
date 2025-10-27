"""
List all anthropic model names
"""

import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

models = client.models.list()
for model in models:
    print(model.id)
