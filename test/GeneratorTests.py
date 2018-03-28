import unittest
from main.Generator import *

class TestInitialization(unittest.TestCase):
    def test_empty(self):
        generator = Generator()
    def test_negative(self):
        generator = Generator(-5)
    def test_large(self):
        generator = Generator(5)
    def test_ok(self):
        generator = Generator(50)


if __name__ == '__main__':
    unittest.main()
