"""
Atharv Gupta
Hangman Game
"""
import time


class HangmanPlay:

    def __init__(self, user_name, category):
        """ Constructor of HangmanPlay with user name and game category.
        Assign default value to number of guesses"""
        self.__user_name = user_name
        self.category = category
        self.limit = 7

    def __str__(self):
        """ Return player name, chosen category and number of allowed wrong
        guess """
        return "Hangman game play with {} in category {} with {} guesses"\
            .format(self.__user_name, self.category, self.limit)

    def play_game(self, word):
        """ Function that takes user input as a letter and find that letter
        in random chosen word. If user guess the word under allowed wrong
        guess limit, he wins else loses"""
        count = 0
        length = len(word)
        display = '_' * length
        already_guessed = []
        win = False

        print("Only {} wrong guess are allowed".format(self.limit))
        time.sleep(1)

        while(self.limit > count):
            guess = input("This is the Hangman Word of length " + str(length) +
                          ": " + display + " Enter your guess: \n")
            guess = guess.strip().lower()
            if (len(guess.strip()) == 0 or len(guess.strip()) >= 2 or
                    not guess.isalpha()):
                print("Invalid Input, Try a valid letter\n")
            elif guess in already_guessed:
                print("You have already guessed this letter.\n")
            elif guess in word:
                already_guessed.extend([guess])
                display = self.__get_updated_display(display, guess, word)

                if word == display:
                    print("Congrats! You have guessed the word correctly!")
                    win = True
                    break
            else:
                already_guessed.extend([guess])
                count += 1
                self.__print_wrong_guess(count, word)

        return win

    def __get_updated_display(self, display, guess, word):
        """ Function to update display to user after each guess """
        for i, ch in enumerate(word):
            if guess == ch:
                display = display[:i] + guess + display[i + 1:]

        return display

    def __print_wrong_guess(self, count, word):
        """ Function to print wrong guess """
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(self.limit - count) +
                  " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(self.limit - count) +
                  " guesses remaining\n")
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(self.limit - count) +
                  " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(self.limit - count) +
                  " guesses remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |     | \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess. " + str(self.limit - count) +
                  " guesses remaining\n")
        elif count == 6:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |   //|\\ \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess. " + str(self.limit - count) +
                  " last guess remaining\n")
        elif count == 7:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |   //|\\ \n"
                  "  |   // \\ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", word)
