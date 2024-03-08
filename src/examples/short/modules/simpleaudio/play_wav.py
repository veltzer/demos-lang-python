"""
Example of how to play a .wav file using simpleaudio

References:
- https://simpleaudio.readthedocs.io/en/latest/simpleaudio.html
"""

import simpleaudio

wave_obj = simpleaudio.WaveObject.from_wave_file("data_samples/wav/sample.wav")
play_obj = wave_obj.play()
play_obj.wait_done()
