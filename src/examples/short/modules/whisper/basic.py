"""
Simple example of whisper

The module you need to install to make this work is `openai-whisper`
"""

import whisper
model=whisper.load_model("medium")
# model=whisper.load_model("small")
result=model.transcribe("out.wav", language="he")
print(result["text"])
