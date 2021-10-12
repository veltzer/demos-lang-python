from mingus.midi import fluidsynth
from mingus.containers import Note
import time


fluidsynth.init('/usr/share/sounds/sf2/FluidR3_GM.sf2', "pulseaudio")
scale = ["C", "D", "E", "F", "G", "A", "B", "C"]
for note in scale:
    n = Note(note, 4)
    fluidsynth.play_Note(n)
    time.sleep(1)
    fluidsynth.stop_Note(n)
