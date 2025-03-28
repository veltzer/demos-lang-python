""" scale.py """

import time
from mingus.midi import fluidsynth
from mingus.containers import Note


# the soundfont arugment is required and does not have a default
# the second argument "driver" is the driver and could be "pulseaudio" but is autodetected properly.
fluidsynth.init(sf2="/usr/share/sounds/sf2/FluidR3_GM.sf2")
# C is actually C-4
scale = ["C", "D", "E", "F", "G", "A", "B", "C-5"]
for note in scale:
    n = Note(note, 4)
    fluidsynth.play_Note(n)
    time.sleep(1)
    # you have to stop the note otherwise it will stay sustained
    fluidsynth.stop_Note(n)
