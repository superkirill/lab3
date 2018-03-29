import unittest
from main.Generator import *

class TestInitialization(unittest.TestCase):
    def test_empty(self):
        self.failUnlessRaises(NotImplementedError, Generator, )
    def test_negative(self):
        self.failUnlessRaises(NotImplementedError, Generator, -5)
    def test_large(self):
        self.failUnlessRaises(NotImplementedError, Generator, 999)

class TestChords(unittest.TestCase):
    def test_chord_A(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('A'), ('A', 'C#', 'E'))
    def test_chord_A_sharp(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('A#'), ('A#', 'D', 'F'))
    def test_chord_B(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('B'), ('B', 'D#', 'F#'))
    def test_chord_C(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('C'), ('C', 'E', 'G'))
    def test_chord_C_sharp(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('C#'), ('C#', 'F', 'G#'))
    def test_chord_D(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('D'), ('D', 'F#', 'A'))
    def test_chord_D_sharp(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('D#'), ('D#', 'G', 'A#'))
    def test_chord_E(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('E'), ('E', 'G#', 'B'))
    def test_chord_F(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('F'), ('F', 'A', 'C'))
    def test_chord_F_sharp(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('F#'), ('F#', 'A#', 'C#'))
    def test_chord_G(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('G'), ('G', 'B', 'D'))
    def test_chord_G_sharp(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('G#'), ('G#', 'C', 'D#'))

    def test_chord_A_minor(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('A', 'minor'), ('A', 'C', 'E'))
    def test_chord_A_sharp_minor(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('A#', 'minor'), ('A#', 'C#', 'F'))
    def test_chord_B_minor(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('B', 'minor'), ('B', 'D', 'F#'))
    def test_chord_C_minor(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('C', 'minor'), ('C', 'D#', 'G'))
    def test_chord_C_sharp_minor(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('C#', 'minor'), ('C#', 'E', 'G#'))
    def test_chord_D_minor(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('D', 'minor'), ('D', 'F', 'A'))
    def test_chord_D_sharp_minor(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('D#', 'minor'), ('D#', 'F#', 'A#'))
    def test_chord_E_minor(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('E', 'minor'), ('E', 'G', 'B'))
    def test_chord_F_minor(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('F', 'minor'), ('F', 'G#', 'C'))
    def test_chord_F_sharp_minor(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('F#', 'minor'), ('F#', 'A', 'C#'))
    def test_chord_G_minor(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('G', 'minor'), ('G', 'A#', 'D'))
    def test_chord_G_sharp_minor(self):
        generator = Generator(0)
        self.assertEqual(generator.get_chord('G#', 'minor'), ('G#', 'B', 'D#'))

    def test_non_existent_type_of_chord(self):
        generator = Generator(0)
        self.failUnlessRaises(NotImplementedError, generator.get_chord, 'G#', 'superchord')
    def test_non_existent_chord_root(self):
        generator = Generator(0)
        self.failUnlessRaises(ValueError, generator.get_chord, 'X#', 'major')

class TestPlay(unittest.TestCase):
    def test_play_note(self):
        generator = Generator(0)
        generator.play(note='C')
    def test_play_chord(self):
        generator = Generator(0)
        generator.play(chord=('C', 'E', 'G'))
    def test_play_chord_instead_of_note(self):
        generator = Generator(0)
        self.failUnlessRaises(ValueError, generator.play, note=('C', 'E', 'G'))
    def test_play_note_instead_of_chord(self):
        generator = Generator(0)
        self.failUnlessRaises(ValueError, generator.play, chord='C')
    def test_play_incorrect_note(self):
        generator = Generator(0)
        self.failUnlessRaises(ValueError, generator.play, note='losi1')
    def test_play_incorrect_chord(self):
        generator = Generator(0)
        self.failUnlessRaises(ValueError, generator.play, chord='losi2')
    def test_play_in_negative_octave(self):
        generator = Generator(0)
        self.failUnlessRaises(ValueError, generator.play, note='C', octave=-5)
    def test_play_in_large_octave(self):
        generator = Generator(0)
        self.failUnlessRaises(ValueError, generator.play, note='C', octave=500)
    def test_play_in_incorrect_octave(self):
        generator = Generator(0)
        self.failUnlessRaises(ValueError, generator.play, note='C', octave='losi3')
    def test_play_with_negative_duration(self):
        generator = Generator(0)
        self.failUnlessRaises(ValueError, generator.play, note='C', duration=-5)
    def test_play_with_incorrect_duration(self):
        generator = Generator(0)
        self.failUnlessRaises(ValueError, generator.play, note='C', octave='losilosilosi')

class TestMelody(unittest.TestCase):
    def test_get_melody(self):
        generator = Generator(0)
        chord_dur = [1, 0.2]
        pause = [0.15, 1]
        progression = [(generator.get_chord('E', 'minor'), chord_dur[0]),
                       pause[0],
                       (generator.get_chord('E', 'minor'), chord_dur[1]),
                       pause[1],
                       (generator.get_chord('E', 'minor'), chord_dur[0]),
                       pause[0],
                       (generator.get_chord('E', 'minor'), chord_dur[1]),
                       pause[1],
                       (generator.get_chord('D', 'major'), chord_dur[0]),
                       pause[0],
                       (generator.get_chord('D', 'major'), chord_dur[1]),
                       pause[1],
                       (generator.get_chord('G', 'major'), chord_dur[0]),
                       pause[0],
                       (generator.get_chord('G', 'major'), chord_dur[1]),
                       pause[1],
                       (generator.get_chord('C', 'major'), chord_dur[0]),
                       pause[0],
                       (generator.get_chord('C', 'major'), chord_dur[1]),
                       pause[1],
                       (generator.get_chord('E', 'minor'), chord_dur[0]),
                       pause[0],
                       (generator.get_chord('E', 'minor'), chord_dur[1]),
                       pause[1],
                       (generator.get_chord('E', 'minor'), chord_dur[0]),
                       pause[0],
                       (generator.get_chord('E', 'minor'), chord_dur[1]),
                       pause[1],
                       ]
        generator.get_melody(progression)

    def test_get_melody_wrong_progression(self):
        generator = Generator(0)
        self.failUnlessRaises(ValueError, generator.get_melody, 'E')

    def test_get_melody_without_progression(self):
        generator = Generator(0)
        self.failUnlessRaises(ValueError, generator.get_melody)

    def test_get_melody_with_wrong_max_notes(self):
        generator = Generator(0)
        self.failUnlessRaises(ValueError, generator.get_melody, (('E','G#','B'),1), -1000)

    def test_get_melody_without_progression_and_with_wrong_max_notes(self):
        generator = Generator(0)
        self.failUnlessRaises(ValueError, max_notes=-1000)


if __name__ == '__main__':
    unittest.main()
