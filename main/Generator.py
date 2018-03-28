import pygame.midi

class Generator():
    """
        Generates chords and melodies
    """
    def __init__(self, instrument=None):
        if instrument is None or not 0 <= instrument <= 127:
            raise NotImplementedError
        self.intervals = {
            'C': 0,
            'C#': 1,
            'C##': 2,
            'D': 2,
            'Db': 1,
            'Dbb': 0,
            'D#': 3,
            'D##': 4,
            'E': 4,
            'Eb': 3,
            'Ebb': 2,
            'E#': 5,
            'E##': 6,
            'F': 5,
            'Fb': 4,
            'Fbb': 5,
            'F#': 6,
            'F##': 7,
            'G': 7,
            'Gb': 6,
            'Gbb': 5,
            'G#': 8,
            'G##': 9,
            'A': 9,
            'Ab': 8,
            'Abb': 7,
            'A#': 10,
            'A##': 11,
            'B': 11,
            'Bb': 10,
            'Bbb': 9,
            'B#': 12,
            'B##': 13
        }
        self.notes = {
            0: 'C',
            1: 'C#',
            2: 'D',
            3: 'D#',
            4: 'E',
            5: 'F',
            6: 'F#',
            7: 'G',
            8: 'G#',
            9: 'A',
            10: 'A#',
            11: 'B',
        }
        pygame.midi.init()
        player = pygame.midi.Output(0, 0)
        player.set_instrument(instrument)
        del player
        pygame.midi.quit()

    def get_chord(self, root='C', type='major'):
        """
            Generate a chord

            Keyword arguments:
                root -- capital letter from A to G, (default 'C')
                type -- string representing the type of chord:
                    major, minor, diminished or augmented (default 'major')
            Return:
                tuple of three notes the chord consists of, e.g. ('C', 'E', 'G')
        """
        if root not in self.intervals.keys():
            raise ValueError
        if type == 'major':
            third = self.intervals[root] + 4
            if third >= 12:
                third -= 12
            third = self.notes[third]
            fifth = self.intervals[root] + 7
            if fifth >= 12:
                fifth -= 12
            fifth = self.notes[fifth]
            return (root, third, fifth)
        elif type == 'minor':
            third = self.intervals[root] + 3
            if third >= 12:
                third -= 12
            third = self.notes[third]
            fifth = self.intervals[root] + 7
            if fifth >= 12:
                fifth -= 12
            fifth = self.notes[fifth]
            return (root, third, fifth)
        else:
            raise NotImplementedError

def main():
    generator = Generator(0)
    print(generator.get_chord('D', 'major'))

if __name__ == '__main__':
    main()