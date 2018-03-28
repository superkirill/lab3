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

if __name__ == '__main__':
    unittest.main()
