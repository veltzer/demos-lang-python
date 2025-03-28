""" play_better.py """

import numpy as np
import simpleaudio as sa

# calculate note frequencies
A_freq = 440
Csh_freq = A_freq * 2 ** (4 / 12)
E_freq = A_freq * 2 ** (7 / 12)

# get timesteps for each sample, T is note duration in seconds
sample_rate = 44100
T = 0.5
t = np.linspace(0, T, int(T * sample_rate), False)

# generate sine wave tone
tone = np.sin(440 * t * 2 * np.pi)

# normalize to 24-bit range
tone *= 8388607 / np.max(np.abs(tone))

# convert to 32-bit data
tone = tone.astype(np.int32)

# convert from 32-bit to 24-bit by building a new byte buffer, skipping every fourth bit
# note: this also works for 2-channel audio
i = 0
byte_array = []
for b in tone.tobytes():
    if i % 4 != 3:
        byte_array.append(b)
    i += 1
audio = bytearray(byte_array)

# start playback
play_obj = sa.play_buffer(audio, 1, 3, sample_rate)

# wait for playback to finish before exiting
play_obj.wait_done()
