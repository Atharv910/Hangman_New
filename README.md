Hangman Game

Hangman is a popular paper and pencil game, where one player thinks of a word and the other tries to guess it by suggesting letters within a certain number of guesses. As soon as the player loses all of his guesses, he is hanged. That is an old way to play Hangman. The new advancement in technologies allows us to play hangman using our own computer without any other player.

Project
The objective of my project is to implement the hangman game using Python. The project is developed using core python and doesn’t require any specific modules other than random and time.  
The project is built on object-oriented programming. The core functionality of the project is divided into a couple of classes. This abstraction hides the complexity and implementation from the main program and can be enhanced in future without changing the main program logic.
Project execution can be summarized in few steps.

Welcome 
The game starts with a welcome message. The user provides his name and the game displays a message at the start of the game.   

Category Selection
The game asks the user to select a category. The current supported categories are 'movie', 'actor', 'country', 'sport' and maintained in the program. As a future enhancement, they can be stored in a database.

Word Selection
Based on the user input category, the game picks a random word in that category. All words with their categories are currently stored in a file. As a future enhancement, they can be stored in a database.
The game displays the length of the random word and draws a line for the user to guess the word.

Guess
The user enters a letter, and the game validates the input. If the user provides anything other than a letter or enters a previously provided letter, the game displays an error and asks for another input.
The game checks if the user has correctly guessed a letter in the word. If guessed correctly, the display adds that letter in the given space according to its index or where it belongs in the given word. However, for incorrect guesses, the hangman starts to appear which also tells the user how many guesses are left.
This keeps on going until the user guesses the correct word or guesses 7 wrong letters. If the user incorrectly guesses 7 times, the game ends by showing the correct word and message that the user is hanged!!
If the word is guessed correctly, user wins the game
