import pygame.midi

class Generator():
    """
        Generates chords and melodies
    """
    def __init__(self, instrument=None):
            pygame.midi.init()
            player = pygame.midi.Output(0, 0)
            player.set_instrument(instrument)
            del player
            pygame.midi.quit()
