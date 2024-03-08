import os
import pygame


def play_note(samples, note_name):
    """ play a note """
    if note_name in samples:
        samples[note_name].play()


def main():
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load rendered piano samples
    sample_dir = "rendered_samples"
    samples = {}
    for filename in os.listdir(sample_dir):
        if filename.endswith(".wav"):
            note_name = filename.split(".")[0]
            samples[note_name] = pygame.mixer.Sound(os.path.join(sample_dir, filename))
    # Example usage
    play_note(samples, "C4")
    pygame.time.delay(2000)

    # Clean up
    pygame.mixer.quit()


if __name__ == "__main__":
    main()
