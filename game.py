# Create your Game class logic in here.
import random
from phrases import PHRASE_LIST
from phrase import Phrase
from character import Character

class Game:
    def __init__(self):
        self.lives = 5
        self.phrase_list = [Phrase(phrase) for phrase in PHRASE_LIST]
        self.correct_phrase = random.choice(self.phrase_list)


    def game_welcome(self):
        print('#'*50)
        print('\n       Welcome to the Phrase Guessing Game\n')
        print('#'*50)

    def start(self):

        while True:
            print('\nYour phrase to guess is...\n')
            self.correct_phrase.display_phrase()
            guess = Character(input('\nEnter your first letter to guess:  ').upper())
            self.correct_phrase.contains_char(guess)
            self.correct_phrase.display_phrase()
            break
