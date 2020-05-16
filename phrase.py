from character import Character


class Phrase:
    """
    This class is to store a phrase which is a collection of Character objects.

    Attributes:
        phrase ([Character]): list of characters that make up the phrase.
        max (int): the number of Characters and spaces in the phrase.
    """

    def __init__(self, phrase):
        """
        The constructor for the Phrase class.

        Parameters:
        self.phrase = [Character(char) for char in phrase]
        """

        self.phrase = [Character(char) for char in phrase]
        self.max = len(self.phrase)

    def display_phrase(self):
        """
        The function to obtain the display state for each character in the
        phrase, store them in a list and then join and print them into a
        single output.
        """

        phrase_to_display = []
        for char in self.phrase:
            phrase_to_display.append(char.display_char())
        print(''.join(phrase_to_display))


    def contains_char(self, char):
        """
        The function to check whether or not the user guessed character is in
        the phrase that the user is trying to guess.

        Parameters:
            char (Character): The user inputted character.

        Returns:
            is_correct (bool): True or False, depending on whether or not the
            phrase contains the user inputted guess.
        """
        count = 0
        is_correct = False
        while count < self.max:
            if self.phrase[count] == char:
                is_correct = True
                self.phrase[count].guess()
            count += 1
        return is_correct


    def check_phrase(self):
        """
        The function that checks whether the user has guessed all the
        characters in the phrase.

        Returns:
            The function returns either True or False, depending on whether all
            of the characters in the phrase have been guessed or not.
        """
        displayed_phrase = []
        for char in self.phrase:
            displayed_phrase.append(char.display_char_for_comparison())
        phrase_joined = ''.join(displayed_phrase)
        if ((''.join(self.phrase)) == (phrase_joined)):
            return True
        else:
            return False


    def reset_phrase(self):
        """
        The function that resets the Character.was_guessed attribute in the
        phrase back to false for each character in the phrase.
        """
        for char in self.phrase:
            char.was_guessed = False
