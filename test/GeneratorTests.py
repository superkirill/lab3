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
        generator.get_chord('A')

    def test_chord_B(self):
        generator = Generator(0)
        generator.get_chord('B')

    def test_chord_C(self):
        generator = Generator(0)
        generator.get_chord('C')

    def test_chord_D(self):
        generator = Generator(0)
        generator.get_chord('D')

    def test_chord_E(self):
        generator = Generator(0)
        generator.get_chord('E')

    def test_chord_F(self):
        generator = Generator(0)
        generator.get_chord('F')

    def test_chord_G(self):
        generator = Generator(0)
        generator.get_chord('G')

if __name__ == '__main__':
    unittest.main()
