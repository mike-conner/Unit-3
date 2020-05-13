from character import Character

class Phrase:

    def __init__(self, phrase):
        self.phrase = [Character(char) for char in phrase]
        self.max = len(self.phrase)


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


    # TODO: needs refractoring...
    def check_phrase(self):
        displayed_phrase = []
        for char in self.phrase:
            displayed_phrase.append(char.display_char_for_comparison())
        phrase_joined = ''.join(displayed_phrase)
        if ((''.join(self.phrase)) == (phrase_joined)):
            return True
        else:
            return False


    def reset_phrase(self):
        for char in self.phrase:
            char.was_guessed = False
