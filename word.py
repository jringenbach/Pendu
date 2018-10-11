# -*- coding : utf-8 -*-

import random

class Word:
    """The word the player has to find """

    def __init__(self, difficultyChosen):
        self._randomWord = ""
        self._letterDiscovered = [False]

        #If the player wrote a number in the difficulty Options
        if difficultyChosen == "1":
            self._difficulty = "Facile"

        elif difficultyChosen == "2":
            self._difficulty = "Normal"

        elif difficultyChosen == "3":
            self._difficulty = "Difficile"

        else:
            self._difficulty = difficultyChosen    

# -----------------------------------------------------------------------
#                           GETTERS AND SETTERS
# -----------------------------------------------------------------------


    def _get_random_word(self):
        """Getters for the random word generated"""
        return self._randomWord

    def _set_random_word(self, wordChosen):
        """Setters for the word"""
        initializationLetterDiscovered = True
        self._randomWord = wordChosen
        self._set_letter_discovered(initializationLetterDiscovered, -1)

    def _get_letter_discovered(self):
        """ Getters for the list of letters that have been discovered"""
        return self._letterDiscovered

    def _set_letter_discovered(self, initialization, index):
        """We create a list that indicates which letter has been discovered
            At the beginning, none of them has been."""

        #We initialize a list that has the same length as the word
        #Each letter that hasn't been discovered is set to false in the list
        if initialization == True:
            wordLength = len(self._get_random_word())
            self._letterDiscovered = [False] * wordLength

        #We set to true the index in the list where the letter has been
        #discovered
        else:
            self._letterDiscovered[index] = True

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

# -----------------------------------------------------------------------
#                                  FUNCTIONS
# -----------------------------------------------------------------------

    def checkLetterInWord(self, letterChosen):
        """We check if the letter chosen by the player is in the word """
        i = -1
        for letter in self._get_random_word():
            i = i + 1
            if letterChosen.upper() == letter.upper():
                self._set_letter_discovered(False, i)

    def displayWord(self):
        """Display the word with the letters discovered and not discovered.
        Letters not discovered are displayed with a _"""
        i = -1
        for letterStatus in self._get_letter_discovered():
            i = i + 1
            if letterStatus == False:
                print("_ ", end="")

            else:
                print(self._get_random_word()[i], end="")

        print("\n")

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
        self._set_random_word(word)

    difficulty = property(_get_difficulty, _set_difficulty)
    letterDiscovered = property(_get_letter_discovered, _set_letter_discovered)
    randomWord = property(_get_random_word, _set_random_word)
    

