"""
Simple example of whisper
"""

import whisper
model=whisper.load_model("medium")
result=model.transcribe("out.wav", language="he")
print(result["text"])
