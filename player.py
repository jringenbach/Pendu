# -*- coding: utf-8 -*-

import re

class Player:
    """Information about the players """

    def __init__(self):
        self._pseudo = ""

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

    def pseudoSelection(self):
        """The player writes his/her pseudonyme.  """
        wrongPseudo = True

        #The pseudo must not contain numbers or special characters
        while wrongPseudo == True:
            wrongPseudo = False
            pseudoSelected = input("Choisissez un pseudonyme : ")

            #We check if there is a special character in the pseudo
            if re.search(r"\W", pseudoSelected) is not None:
                wrongPseudo = True
                print("WrongPseudo : "+str(wrongPseudo))
                
            #We check if there is a number in the pseudo
            if re.search(r"\d", pseudoSelected) is not None:
                wrongPseudo = True
                print("WrongPseudo : "+str(wrongPseudo))

        self._set_pseudo(pseudoSelected)

    def choseALetter(self):
        """The player chooses a letter """
        letterChosen = input("Choisissez une lettre : ")

        return letterChosen
