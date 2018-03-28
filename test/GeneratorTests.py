import unittest
from main.Generator import *

class TestInitialization(unittest.TestCase):
    def test_empty(self):
        self.failUnlessRaises(NotImplementedError, Generator, )
    def test_negative(self):
        self.failUnlessRaises(NotImplementedError, Generator, -5)
    def test_large(self):
        self.failUnlessRaises(NotImplementedError, Generator, 999)


if __name__ == '__main__':
    unittest.main()
