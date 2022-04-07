import unittest
from fzzbuzz import *

class TestFizz(unittest.TestCase):
    def test_returns_fizz(self):
        self.assertEqual("fizz", fizz_buzz(3))

    def test_returns_buzz(self):
        self.assertEqual("buzz", fizz_buzz(5))

    def test_returns_fizz_buss(self):
        self.assertEqual("fizzbuzz", fizz_buzz(15))    

    def test_returns_number_is_string(self):
        self.assertEqual("7", fizz_buzz(7))