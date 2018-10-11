# -*- coding : utf-8 -*-

from player import Player
from game import Game
from displayMenu import DisplayMenu

""" Main file containing the game """
keepPlaying = True

while keepPlaying == True:
    endGame = False
    
    #The player chose his/her pseudonyme
    pseudoPlayer = input("Choisissez un pseudonyme : ")
    player = Player(pseudoPlayer)

    #The player chose the difficulty of the game
    difficultyList = ["Facile", "Normal", "Difficile"]
    difficultyAsking = "Choisissez votre niveau de difficulté : "
    difficultyMenu = DisplayMenu(difficultyList, difficultyAsking)
    difficultyChosen = difficultyMenu.display()

    #We create the current game
    game = Game(difficultyChosen, player)
    game._get_word_chosen().selectRandomWord()

    #While the game is not over, the player keeps playing (chosing a letter)
    while endGame == False:
        endGame = game.play()

    game.endGameMessage()



