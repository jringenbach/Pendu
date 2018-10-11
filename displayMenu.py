# -*- coding : utf-8 -*-

class DisplayMenu:
    """ class containing the method to display different menus"""
    
    def __init__(self, options):
        self.options = options
        self.nbOptions = len(options)

    def display(self):
        """ Display a menu with the different options offered to the player"""
        i = 1
        for option in self.options:
            print(str(i)+ ". "+self.options[i-1])
            i = i + 1
