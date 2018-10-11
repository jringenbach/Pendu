# -*- coding : utf-8 -*-

# -----------------------------------------------------------------------
#                       MAIN FILE CONTAINING THE GAME
# -----------------------------------------------------------------------

from displayMenu import DisplayMenu
from game import Game
from options import Options
from player import Player
from word import Word

import os

# -----------------------------------------------------------------------
#                       VARIABLES AND OBJECTS
# -----------------------------------------------------------------------
game = Game()
options = Options()
game._set_options(options)
player = Player()

# -----------------------------------------------------------------------
#                       CORE OF THE GAME
# -----------------------------------------------------------------------

while game._get_options()._get_play_again() == True:
    endGame = False
    game.resetGame()
    
    #The player chose his/her pseudonyme
    if game._get_options()._get_pseudo_options() == True:
        player.pseudoSelection()

    #The player chose the difficulty of the game
    if game._get_options()._get_difficulty_options() == True:
        difficultyList = ["Facile", "Normal", "Difficile"]
        difficultyAsking = "Choisissez votre niveau de difficulté : "
        difficultyMenu = DisplayMenu(difficultyList, difficultyAsking)
        difficultyChosen = difficultyMenu.display()
        
    word = Word(difficultyChosen)
    
    #We create the current game
    game.player = player
    game._set_word_chosen(word)
    game._get_word_chosen().selectRandomWord()

    #While the game is not over, the player keeps playing (chosing a letter)
    while game.endGame == False:
        game.play()

    game.endGameMessage()
    replayOptions = ["Rejouer", "Revenir au choix du pseudo", "Revenir au choix de la difficulté", "Quitter"]
    replayAsking = "Que souhaitez-vous faire?"
    replayMenu = DisplayMenu(replayOptions, replayAsking)
    replayOptionSelected = replayMenu.display()

    game.replay(replayOptionSelected)




