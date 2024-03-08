import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Load rendered piano samples
sample_dir = "rendered_samples"
samples = {}
for filename in os.listdir(sample_dir):
    if filename.endswith(".wav"):
        note_name = filename.split(".")[0]
        samples[note_name] = pygame.mixer.Sound(os.path.join(sample_dir, filename))

# Play a note
def play_note(note_name):
    if note_name in samples:
        samples[note_name].play()

# Example usage
play_note("C4")
pygame.time.delay(2000)

# Clean up
pygame.mixer.quit()
