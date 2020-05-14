class Character(str):
    """
    This class is for storing a single character of a phrase.

    Attributes:
        char (character): The character to be stored.
        was_guessed (bool): Whether the user guessed the char yet.
    """

    def __init__(self, char):
        """
        The constructor for Character.

        Attributes:
            char (character): The character to be stored.
            was_guessed (bool): Whether the user guessed the char yet.
        """

        super().__init__()
        self.char = char
        self.was_guessed = False


    def guess(self):
        """
        The function to change the value of was_guessed from False to True.
        """

        self.was_guessed = True


    def display_char(self):
        """
        The function to display the phrase's character.

        Returns:
            Returns the character or '_' depending on the value of the
            characters's was_guessed attribute or a ' ' to represent a space.
            This function adds a ' ' (space) after each return for readability.
        """

        if self.was_guessed == True:
            return self.char + ' '
        elif self.char == ' ':
            return '  '
        else:
            return '_ '


    def display_char_for_comparison(self):
        """
        This function is identical to display_char() but without the extra
        space after each return. This is needed for comparison to the phrase
        being guessed.

        Returns:
            Returns the character or '_' depending on the value of the
            characters's was_guessed attribute or a ' ' to represent a space.
        """

        if self.was_guessed == True:
            return self.char
        elif self.char == ' ':
            return ' '
        else:
            return '_'
