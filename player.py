# -*- coding: utf-8 -*-

class Player:
    """Information about the players """

    def __init__(self, pseudo):
        self._pseudo = pseudo

# -----------------------------------------------------------------------
#                           GETTERS AND SETTERS
# -----------------------------------------------------------------------

    def _get_pseudo(self):
        """ getters for the pseudonyme of the player"""
        return self._pseudo

    def _set_pseudo(self, new_pseudo):
        """ setters for the pseudonyme of the player"""
        self._pseudo = new_pseudo

    pseudo = property(_get_pseudo, _set_pseudo)

# -----------------------------------------------------------------------
#                                  FUNCTIONS
# -----------------------------------------------------------------------
    def choseALetter(self):
        """The player chooses a letter """
        letterChosen = input("Choisissez une lettre : ")

        return letterChosen
