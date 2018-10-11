class Game:
    """Class that contains information of the different games that have
    been played."""

    def __init__(self, difficulty, wordChosen):
        self.difficulty = difficulty
        self._wordChosen = wordChosen

    def _get_word_chosen(self):
        """ Getters for the word that has been chosen randomly"""
        return self._wordChosen

    def _set_word_chosen(self, wordChosen):
        """Setters for the word that has been chosen randomly"""
        self._wordChosen = wordChosen

    wordChosen = property(_get_word_chosen, _set_word_chosen)
        
