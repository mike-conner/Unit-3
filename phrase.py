# Create your Phrase class logic here.
from character import Character

class Phrase:

    def __init__(self, phrase):
        self.phrase = [Character(char) for char in phrase]
        self.max = len(self.phrase)


    '''def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration'''


    def display_phrase(self):
        phrase_to_display = []
        for char in self.phrase:
            phrase_to_display.append(char.display_char())
        print(''.join(phrase_to_display))


    def contains_char(self, char):
        count = 0
        is_correct = False
        while count < self.max:
            if self.phrase[count] == char:
                is_correct = True
                self.phrase[count].guess()
            count += 1
        return is_correct
