# Author(s): CJ Roedel
# Last update: 03/28/24 - 1:11

#imports

#globals

#This is going to be a version 2.0 feature
def feature_selection():
    next

def select_characters():
    next

def create():
    #Tool explanation
    print("Mode changed from menu to encounter creation.")
    print("In encounter creation you will select the list of characters you have uploaded that\n" + 
          "will take place in the encounter. The encounter will be saved for quick access to the\n" + 
          "to give quick access to all relevant data without having to use as many menus during and\n" + 
          "encounter. Each character you add to the list can be given a classification of friendly,\n" + 
          "enemy, or neutral.\n")
    print("To create an encounter, enter a name for the encounter. To return to the menu enter 'exit'")

    creation_running = True

    #While the user wants to be in character creation
    while creation_running:

        encounter_name = input("\Encounter Name: ")
        print("")
        encounter_name = encounter_name.lower()

        if not encounter_name.isalnum():
            print("Invalid encounter name, please enter a name that only consits of letters and numbers.")

        #TO DO: set up an encounter folder and a system to get the encounter_list
        if encounter_name in encounter_list:
            print("An enounter of that name already exists, please enter another encounter name.")
        elif encounter_name == "exit":
            print("Mode changed from character edit to menu.")
            creation_running = False