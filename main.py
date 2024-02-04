"""
Atharv Gupta
Hangman Game Main
"""
import time
from hangman_selector import HangmanSelector
from hangman_play import HangmanPlay


def play_game(user_name):
    """ Function to start Hangman game. User select game category and then
    provide guess for a random word """
    print("The game is about to start.....")
    time.sleep(1)
    print("Best of Luck!!", user_name)

    hs = HangmanSelector(user_name)
    # get game categories for user selection
    categories = hs.get_categories()
    print("Please select a category:", categories)

    user_input_required = True
    while user_input_required:
        user_category = input("Enter your choice : ")
        if user_category not in categories:
            print("Error: Invalid input.Please try again")
            continue
        else:
            user_input_required = False

    print("Selecting a word to guess....")
    time.sleep(1)
    # fetch random word in user input category
    word = hs.fetch_random_word(user_category)
    hp = HangmanPlay(user_name, user_category)

    return hp.play_game(word)


# Program starting
if __name__ == '__main__':
    print("Welcome to Hangman game")
    name = ''

    while name == '':
        name = input("Enter your name: ")
        if name == '':
            print("Error: Invalid input.Please try again")
            continue

    print("Hello " + name + ", Let's play Hangman!!")
    win = play_game(name)

    if win:
        print("Thanks For Playing! We expect you back again!")
    else:
        print("Sorry you lost. Please try again!!")
