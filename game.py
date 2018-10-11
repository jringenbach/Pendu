# -*- coding: utf-8 -*-

from word import Word

class Game:
    """Class that contains information of the different games that have
    been played."""

    def __init__(self, difficultyChosen):
        #We initialize the attributes of Game class
        
        self._wordChosen = Word(difficultyChosen)
        self.errorAllowed = 6                  

    def _get_word_chosen(self):
        """ Getters for the word that has been chosen randomly"""
        return self._wordChosen

    def _set_word_chosen(self, wordChosen):
        """Setters for the word that has been chosen randomly"""
        self._wordChosen._set_random_word(wordChosen)


    wordChosen = property(_get_word_chosen, _set_word_chosen)

        
