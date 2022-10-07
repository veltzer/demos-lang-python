import time
from mingus.midi import fluidsynth
from mingus.containers import NoteContainer

# mingus documentation:
# http://bspaans.github.io/python-mingus/
# This DOESNT turn off fluidsynth logging...
# import logging
# logger = logging.getLogger("fluidsynth")
# logger.setLevel(logging.ERROR)

# fluidsynth.init('/usr/share/sounds/sf2/FluidR3_GM.sf2', "pulseaudio")
fluidsynth.init(sf2="/usr/share/sounds/sf2/TimGM6mb.sf2", driver="pulseaudio")
fluidsynth.play_NoteContainer(NoteContainer(["C", "Eb", "G"]))
time.sleep(1)
fluidsynth.stop_NoteContainer(NoteContainer(["C", "Eb", "G"]))
fluidsynth.play_NoteContainer(NoteContainer(["C", "E", "G"]))
time.sleep(1)
fluidsynth.stop_NoteContainer(NoteContainer(["C", "E", "G"]))
# You don't have to call the next method
# fluidsynth.stop_everything()
