import random
from phrases import PHRASE_LIST
from phrase import Phrase
from character import Character


class Game:
    """
    The class is used for the instance of the game that creates a list of
    phrases from the phrase.py file and then randomly selects one of them for
    the user to guess. The class is responsible for creating Phrase objects as
    well as contrlling the logic and state of the game.

    Attributes:
        guessed_letters [Character]: List of user guessed characters.
        lives (int): Number of lives (available guesses) that remain in the
        current game.
        phrases [Phrase]: List of Phrase objects.
        correct_phrase (phrase): randomly selected Phrase object for the user
        to guess.
    """

    def __init__(self):
        """
        The constructor for the Game class.
        """

        self.guessed_letters = []
        self.lives = 5
        self.phrases = [Phrase(phrase) for phrase in PHRASE_LIST]
        self.correct_phrase = random.choice(self.phrases)


    def game_welcome(self):
        """
        The function that displays a welcome message to the user.
        """

        print('\n\n')
        print('#'*50)
        print('\n       Welcome to the Phrase Guessing Game\n')
        print('#'*50)
        print('\n')


    def print_phrase(self):
        """
        The function that prints the phrase out that the user is to guess with
        the characters of the phrase in their current state based on each of
        their was_guessed values.
        """

        print('Your phrase to guess is...\n')
        self.correct_phrase.display_phrase()
        print('\n')


    def get_guess(self):
        """
        The function that gets the user's guess and returns that value as a
        Character.

        Returns:
            The user inputted character as a Character object.
        """

        return Character(input('Enter your guess:  ').upper())


    def check_lives(self, is_correct):
        """
        The function that checks how many lives (turns) the user has remaining.

        Parameters:
            is_correct (bool): Whether or not the user's guess was correct.

        Returns:
            True or False depending on if the user has any lives (turns) left.
        """

        if is_correct == False:
            self.lives -= 1
            if self.lives == 0:
                print('GAME OVER - YOU HAVE NO LIVES LEFT\n')
                return False
            print('You have {} our of 5 lives remaining!\n'.format(self.lives))
            return True


    def play_again(self):
        """
        The function to prompt the user to play again if they solved the phrase
        or if they have run out of lives.

        Returns:
            True or False depending on whether they want to play again or not.
        """

        play_again = False
        while True:
            try:
                answer = input('\nWant to play again (Y/N):  ').upper()
                if answer != 'Y' and answer != 'N':
                    raise ValueError
            except ValueError:
                print("\nYou must enter either 'Y' or 'N'")
            else:
                if answer == 'Y':
                    play_again = True
                    print('\n')
                break
        return play_again


    def reset_game(self):
        """
        The funtion to reset all of the Game class instance's attributes to
        their default values and to randomly select a new phrase to guess.
        """

        self.correct_phrase.reset_phrase()
        self.lives = 5
        self.correct_phrase = random.choice(self.phrases)
        self.guessed_letters = []


    def start(self):
        """
        The function to print the welcome message and begin the game loop.
        """

        self.game_welcome()
        while True:
            self.print_phrase()
            # Get user's guess and validate their input.
            while True:
                try:
                    guess = self.get_guess()
                    if len(guess) != 1 or guess < 'A' or guess > 'Z':
                        raise ValueError
                except ValueError:
                    print("\nThat is not a valid option. Please try again.\n")
                else:
                    if guess in self.guessed_letters:
                        print('\nWait, you already guess that... try again.\n')
                    else:
                        self.guessed_letters.append(guess)
                        break
            print('\n')

            # Check to see if the user guess is in the phrase.
            is_correct = self.correct_phrase.contains_char(guess)

            # Check to see if the user has any lives left
            continue_game = self.check_lives(is_correct)

            # If the user is out of lives, see if they want to play again.
            if continue_game == False:
                if (self.play_again()):
                    self.reset_game()
                else:
                    print('\nGOOD BYE\n')
                    break

            # Check to see if the user guessed all the characters in the phrase.
            if (self.correct_phrase.check_phrase()):
                self.print_phrase()
                print('Congrats! You solved the phrase!!!\n')

                # If they guessed all characters, see if they want to play more.
                if (self.play_again()):
                    self.reset_game()
                else:
                    print('\nGOOD BYE\n')
                    break
