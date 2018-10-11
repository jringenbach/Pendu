# -*- coding : utf-8 -*-


class Options:
    """Options of the game """

    def __init__(self):
        self._pseudoOptions = True
        self._difficultyOptions = True
        self._playAgain = True
        
# -----------------------------------------------------------------------
#                           GETTERS AND SETTERS
# -----------------------------------------------------------------------

    def _get_pseudo_options(self):
        """Getters for the pseudo Options """
        return self._pseudoOptions

    def _set_pseudo_options(self, pseudoOptions):
        """ Setters for the pseudo Options"""
        self._pseudoOptions = pseudoOptions

    def _get_difficulty_options(self):
        """ getters for the difficulty options"""
        return self._difficultyOptions

    def _set_difficulty_options(self, difficultyOptions):
        """ setters for the difficulty options """
        self._difficultyOptions = difficultyOptions

    def _get_play_again(self):
        """ getters for the play again options"""
        return self._playAgain

    def _set_play_again(self, playAgain):
        """ setters for the play again options """
        self._playAgain = playAgain
