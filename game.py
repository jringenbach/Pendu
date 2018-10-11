# -*- coding: utf-8 -*-

from word import Word

class Game:
    """Class that contains information of the different games that have
    been played."""

    def __init__(self, difficultyChosen, player):
        #We initialize the attributes of Game class
        self.player = player
        self.win = False
        self.endGame = False
        self._wordChosen = Word(difficultyChosen)
        self.errorAllowed = 6                  

# -----------------------------------------------------------------------
#                           GETTERS AND SETTERS
# -----------------------------------------------------------------------

    def _get_word_chosen(self):
        """ Getters for the word that has been chosen randomly"""
        return self._wordChosen

    def _set_word_chosen(self, wordChosen):
        """Setters for the word that has been chosen randomly"""
        self._wordChosen._set_random_word(wordChosen)


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
    
        return self.endGame
        

        
