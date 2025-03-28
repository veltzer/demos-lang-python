""" play_notes.py """

import simpleaudio
import numpy as np

# Define the note frequency
note_freq = 440.0  # A4 note

# Define the sample rate
sample_rate = 44100

duration = 2  # in seconds

# Generate a sine wave for the note
t = np.linspace(0, duration, int(sample_rate * duration), False)
note = np.sin(2.0 * np.pi * note_freq * t)
audio_data = note.astype(np.int16)

for x in note:
    print(x)
print(note)

# Create an audio object from the sine wave
audio = simpleaudio.play_buffer(audio_data=audio_data, num_channels=1, bytes_per_sample=2, sample_rate=sample_rate)

# Wait for the note to finish
audio.wait_done()
