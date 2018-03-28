import pygame.midi

class Generator():
    """
        Generates chords and melodies
    """
    def __init__(self, instrument=None):
        if instrument is None or not 0 <= instrument <= 127:
            raise NotImplementedError
        pygame.midi.init()
        player = pygame.midi.Output(0, 0)
        player.set_instrument(instrument)
        del player
        pygame.midi.quit()
