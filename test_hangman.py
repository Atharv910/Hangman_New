"""
Atharv Gupta
Test Hangman
"""
import unittest
from hangman_selector import HangmanSelector


class TestPasswordManager(unittest.TestCase):

    def test_get_categories(self):
        """Test Hangman Selector get_categories"""

        hs = HangmanSelector("Atharv")
        categories = hs.get_categories()

        self.assertListEqual(categories,
                             ['movie', 'actor', 'country', 'sport'])

    def test_fetch_random_word(self):
        """Test Hangman Selector fetch_random_word for movie category"""

        hs = HangmanSelector("Atharv")
        random_word = hs.fetch_random_word('movie')

        self.assertIn(random_word,
                      ['inception', 'titanic', 'jurassicpark', 'starwars',
                       'gladiator'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
