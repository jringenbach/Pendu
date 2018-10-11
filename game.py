# -*- coding: utf-8 -*-

import random

class Game:
    """Class that contains information of the different games that have
    been played."""

    def __init__(self, difficultyChosen):
        #We initialize the attributes of Game class
        self._difficulty = ""
        self._wordChosen = ""
        
        #If the player wrote a number in the difficulty Options
        if difficultyChosen == "1":
            self._difficulty = "Facile"

        elif difficultyChosen == "2":
            self._difficulty = "Normal"

        elif difficultyChosen == "3":
            self._difficulty = "Difficile"

        else:
            self._difficulty = difficultyChosen       

    def _get_word_chosen(self):
        """ Getters for the word that has been chosen randomly"""
        return self._wordChosen

    def _set_word_chosen(self, wordChosen):
        """Setters for the word that has been chosen randomly"""
        self._wordChosen = wordChosen

    def _get_difficulty(self):
        """ Getters for the difficulty"""
        return self._difficulty

    def _set_difficulty(self, difficultyChosen):
        """ Setters for the difficulty"""
        
        #If the player wrote a number in the difficulty Options
        if difficultyChosen == "1":
            self._difficulty = "Facile"

        elif difficultyChosen == "2":
            self._difficulty = "Normal"

        elif difficultyChosen == "3":
            self._difficulty = "Difficile"

        else:
            self._difficulty = difficultyChosen

    def pathFileWordDifficulty(self):
        """Chose the file in which the word will be chosen depending on
            the difficulty """

        path = ""
        
        if self._get_difficulty() == "Facile":
            path = "resources/easyWords.txt"

        elif self._get_difficulty() == "Normal":
            path = "resources/normalWords.txt"

        elif self._get_difficulty() == "Difficile":
            path = "resources/hardWords.txt"

        else:
            print("Erreur dans le chargement du fichier de mots")

        return path
            

    def selectRandomWord(self):
        """ Chose a word randomly depending on the difficulty """

        #We get the path of the file depending on the difficulty
        path = self.pathFileWordDifficulty()
        word = ""

        #We open the file where all the words are
        with open(path, "r") as fileLoaded:
            file = fileLoaded.read()
            listOfWords = file.split()
            randomNumber = random.randint(0, len(listOfWords)-1)
            word = listOfWords[randomNumber]

        #We set the random word in the actual game
        self._set_word_chosen(word)
        return word

    wordChosen = property(_get_word_chosen, _set_word_chosen)
    difficulty = property(_get_difficulty, _set_difficulty)
        
