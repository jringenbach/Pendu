# -*- coding : utf-8 -*-

class DisplayMenu:
    """ class containing the method to display different menus"""
    
    def __init__(self, options, askingOption):
        self.options = options
        self.nbOptions = len(options)
        self.askingOption = askingOption

    def display(self):
        """ Display a menu with the different options offered to the player"""
        validOption = False
        optionSelected = ""
        
        i = 1

        #We display the options offered to the player
        for option in self.options:
            print(str(i)+ ". "+self.options[i-1])
            i = i + 1

        while validOption == False:
            optionSelected = input(self.askingOption)

            #We check if the player has chosen a number
            try:
                int(optionSelected)
                if int(optionSelected) >= 1:
                    if int(optionSelected) <= self.nbOptions:
                        validOption = True

                    else:
                        print("L'option choisie n'est pas valide.\n")

            
            except:
                print("Vous devez tapez le nombre correspondant à votre choix.\n")
                    
        #Returning the choice made by the player
        return optionSelected
