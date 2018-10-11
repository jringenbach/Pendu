# -*- coding: utf-8 -*-

from word import Word
from options import Options

class Game:
    """Class that contains information of the different games that have
    been played."""

    def __init__(self):
        #We initialize the attributes of Game class
        self.player = ""
        self.win = False
        self.endGame = False
        self._wordChosen = ""
        self.errorAllowed = 6
        self._options = Options()

# -----------------------------------------------------------------------
#                           GETTERS AND SETTERS
# -----------------------------------------------------------------------

    def _get_word_chosen(self):
        """ Getters for the word that has been chosen randomly"""
        return self._wordChosen

    def _set_word_chosen(self, wordChosen):
        """Setters for the word that has been chosen randomly"""
        self._wordChosen = wordChosen

    def _get_options(self):
        """Getters for the options of the game """
        return self._options

    def _set_options(self, options):
        """Setters for the options of the game """
        self._options = options
        

    options = property(_get_options, _set_options)
    wordChosen = property(_get_word_chosen, _set_word_chosen)

# -----------------------------------------------------------------------
#                                  FUNCTIONS
# -----------------------------------------------------------------------

    def checkEndGame(self):
        """We check if the player has won or not"""

        if self.errorAllowed == 0:
            endGame = True

    def checkLose(self):
        """ We check if the player has lost by checking if the number of errors
        allowed left is equal to 0"""

        playerLose = False

        if self.errorAllowed == 0:
            playerLose = True

        return playerLose

    def checkWin(self):
        """We check every argument in letter discovered. If each of them is set
        to true, then it means the player has won"""
        letterDiscovered = self._get_word_chosen()._get_letter_discovered()
        playerWins = True
        
        for statusLetter in letterDiscovered:
            if statusLetter == False:
                playerWins = False

        return playerWins

    def endGameMessage(self):
        """Display the endgame message depending if the player has won or not """
        if self.win == True:
            print("Vous avez gagné!")

        else:
            print("Vous avez perdu!")

    def play(self):
        """function where the game is happening """
        
        letterFound = False
        
        self._get_word_chosen().displayWord()
        letterChosen = self.player.choseALetter()
        letterFound = self._get_word_chosen().checkLetterInWord(letterChosen)

        if letterFound == False:
            self.errorAllowed = self.errorAllowed - 1
            
        print("Il vous reste "+str(self.errorAllowed)+" essais")
        
        #We check if the player has won or lost the game
        if self.checkWin() == False:
            if self.checkLose() == True:
                self.endGame = True

        else:
            self.win = True
            self.endGame = True

    def replay(self, optionSelected):
        """Select the right action depending on what the player has selected
        in the replay options at the endgame"""

        if optionSelected == "1":
            self._get_options()._set_pseudo_options(False)
            self._get_options()._set_difficulty_options(False)
            self._get_options()._set_play_again(True)

        elif optionSelected == "2":
            self._get_options()._set_pseudo_options(True)
            self._get_options()._set_difficulty_options(True)
            self._get_options()._set_play_again(True)

        elif optionSelected == "3":
            self._get_options()._set_pseudo_options(False)
            self._get_options()._set_difficulty_options(True)
            self._get_options()._set_play_again(True)

        else:
            self._get_options()._set_play_again(False)

    def resetGame(self):
        """Reset the attributes of the game """
        self.win = False
        self.endGame = False
        self.errorAllowed = 6
            
        
        
