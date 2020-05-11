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
        print('\n\n')
        print('#'*50)
        print('\n       Welcome to the Phrase Guessing Game\n')
        print('#'*50)
        print('\n')


    def print_phrase(self):
        print('Your phrase to guess is...\n')
        self.correct_phrase.display_phrase()
        print('\n')

    def get_guess(self):
        return Character(input('Enter your guess:  ').upper())


    def check_lives(self, is_correct):
        if is_correct == False:
            self.lives -= 1
            if self.lives == 0:
                print('GAME OVER - YOU HAVE NO LIVES LEFT')
                return False
            print('You have {} lives remaining.\n'.format(self.lives))
            return True


    def check_phrase(self):
        #print(self.correct_phrase)
        #print(self.correct_phrase.display_phrase())
        #if self.correct_phrase == self.correct_phrase.display_phrase():
        #    print('yay')


    def start(self):
        while True:
            self.print_phrase()
            guess = self.get_guess()
            print('\n')
            is_correct = self.correct_phrase.contains_char(guess)
            continue_game = self.check_lives(is_correct)
            if continue_game == False:
                break
            self.check_phrase()
