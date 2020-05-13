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
            print('You have {} our of 5 lives remaining!\n'.format(self.lives))
            return True


    def play_again(self):
        answer = input('Want to play again (Y/N):  ').upper()
        if answer == 'Y':
            return True
        return False


    def reset_game(self):
        self.correct_phrase.reset_phrase()
        self.lives = 5
        self.correct_phrase = random.choice(self.phrase_list)


    def start(self):
        while True:
            self.print_phrase()
            guess = self.get_guess()
            print('\n')
            is_correct = self.correct_phrase.contains_char(guess)
            continue_game = self.check_lives(is_correct)
            if continue_game == False:
                if (self.play_again()):
                    self.reset_game()
                else:
                    print('GOOD BYE')
                    break
            if (self.correct_phrase.check_phrase()):
                self.print_phrase()
                print('solved')
                if (self.play_again()):
                    self.reset_game()
                else:
                    print('GOOD BYE')
                    break
