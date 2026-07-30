#!/usr/bin/env python

"""
Simple example of whisper

The module you need to install to make this work is `openai-whisper`
"""

import torch
import whisper
# model=whisper.load_model("medium")
model=whisper.load_model("small")
result=model.transcribe("data_samples/wav/speaking_en.wav", language="en", fp16=torch.cuda.is_available())
print(result["text"])
