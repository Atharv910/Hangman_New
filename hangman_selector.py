"""
Atharv Gupta
Hangman Selector
"""
import random


class HangmanSelector:
    NEW_LINE = "\n"
    __CATEGORIES = ['movie', 'actor', 'country', 'sport']

    def __init__(self, user_name, delimiter=":", file="words.txt"):
        """ Constructor of HangmanSelector with user name and default value
        of key-value delimiter and file name containing words """

        self.__user_name = user_name
        self.delimiter = delimiter
        self.file = file

    def __str__(self):
        """ Returns class description with user name """
        return "Hangman game selector for {}".format(self.__user_name)

    def get_categories(self):
        """ Returns available game categories """
        return self.__CATEGORIES

    def fetch_random_word(self, category):
        """ Fetch random word from file for given category """
        words_to_guess = self.__fetch_all_words_to_guess(category)
        random_word = random.choice(words_to_guess.split(','))
        return random_word

    def __fetch_all_words_to_guess(self, category):
        """ Fetch all available words from file for given category """
        word_file = None
        words_to_guess = None
        try:
            word_file = open(self.file, 'r')

            for line in word_file:
                category_words = line.strip(HangmanSelector.NEW_LINE).split(
                    self.delimiter)
                if category_words[0] == category:
                    words_to_guess = category_words[1]
            return words_to_guess
        except FileNotFoundError as error:
            print("Input file is not found", error)
        finally:
            word_file.close()
