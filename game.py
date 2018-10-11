# -*- coding: utf-8 -*-

from word import Word

class Game:
    """Class that contains information of the different games that have
    been played."""

    def __init__(self, difficultyChosen, player):
        #We initialize the attributes of Game class
        self.player = player
        self._wordChosen = Word(difficultyChosen)
        self.errorAllowed = 6                  

    def _get_word_chosen(self):
        """ Getters for the word that has been chosen randomly"""
        return self._wordChosen

    def _set_word_chosen(self, wordChosen):
        """Setters for the word that has been chosen randomly"""
        self._wordChosen._set_random_word(wordChosen)

    def play(self):
        """function where the game is happening """
        
        self._get_word_chosen().displayWord()
        letterChosen = self.player.choseALetter()
        self._get_word_chosen().checkLetterInWord(letterChosen)


    wordChosen = property(_get_word_chosen, _set_word_chosen)

        
