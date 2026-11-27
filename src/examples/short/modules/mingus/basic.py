""" basic.py """

import time

from mingus.containers import NoteContainer
from mingus.midi import fluidsynth

# mingus documentation:
# http://bspaans.github.io/python-mingus/
# This DOESNT turn off fluidsynth logging...
# import logging  # noqa: ERA001  teaching: kept in the comment for the reader
# logger = logging.getLogger("fluidsynth")  # noqa: ERA001  teaching: kept in the comment for the reader
# logger.setLevel(logging.ERROR)  # noqa: ERA001  teaching: kept in the comment for the reader

# fluidsynth.init("/usr/share/sounds/sf2/FluidR3_GM.sf2", "pulseaudio")  # noqa: ERA001  teaching: kept in the comment for the reader
fluidsynth.init(sf2="/usr/share/sounds/sf2/TimGM6mb.sf2", driver="pulseaudio")
fluidsynth.play_NoteContainer(NoteContainer(["C", "Eb", "G"]))
time.sleep(1)
fluidsynth.stop_NoteContainer(NoteContainer(["C", "Eb", "G"]))
fluidsynth.play_NoteContainer(NoteContainer(["C", "E", "G"]))
time.sleep(1)
fluidsynth.stop_NoteContainer(NoteContainer(["C", "E", "G"]))
# You dont have to call the next method
# fluidsynth.stop_everything()  # noqa: ERA001  teaching: kept in the comment for the reader
