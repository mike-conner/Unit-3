# Create your Character class logic in here.

class Character(str):

    def __init__(self, char):
        super().__init__()
        self.char = char
        self.was_guessed = False


    def guess(self):
        self.was_guessed = True


    def display_char(self):
        if self.was_guessed == True:
            return self.char + ' '
        elif self.char == ' ':
            return '  '
        else:
            return '_ '
