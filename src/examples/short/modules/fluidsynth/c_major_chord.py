import time
import fluidsynth

# Initialize FluidSynth
fs = fluidsynth.Synth()

# Load a SoundFont (you may need to adjust the path)
# fs.start(driver="alsa")  # or "pulseaudio" depending on your system
fs.start(driver="pulseaudio")  # or "pulseaudio" depending on your system
sfid = fs.sfload("/usr/share/sounds/sf2/FluidR3_GM.sf2")

# Select an instrument (0 is usually a piano)
fs.program_select(0, sfid, 0, 0)

# Define the notes for a C major chord (C4, E4, G4)
# MIDI note numbers: C4 = 60, E4 = 64, G4 = 67
c_major_chord = [60, 64, 67]

# Play the chord
for note in c_major_chord:
    fs.noteon(0, note, 100)  # channel 0, note, velocity

# Hold the chord for 2 seconds
time.sleep(2)

# Release the notes
for note in c_major_chord:
    fs.noteoff(0, note)

# Clean up
fs.delete()
