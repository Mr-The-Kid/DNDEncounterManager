# Author(s): CJ Roedel
# Last update: 03/28/24 - 1:11

#imports
import DND_Encounter_Manager as dnd
import os

#Get the list of all saved characters and prints them to the screen
#param(s)
#no params
#return(s)
#list of saved character names
def get_characters_list():
    characters_folder = dnd.get_characters_folder()
    files_list = os.listdir(characters_folder)

#Get the values of the currently selected character for editing
#param(s)
#character_name: the name of the character to edit
#return(s)
#list of edited character values
def get_character_values(character_name):
    next

#Updates the existing character with the edited values
#param(s)
#character_name: the name of the character to edit
#return(s)
#no return(s)
def edit_character(character_name):
    next

#Edit mode which allows for the user to edit the values of a character
#param(s)
#characters_folder: the path to the characters folder
#return(s)
#no return(s)
def edit(characters_folder):
    #Tool explanation
    print("Mode changed from menu to character edit.")
    print("In character edit you will be given the list of all characters that are currently.\n" + 
          "saved. You will then input the name of the character that you would like to edit.\n" + 
          "From here you will be given the list of values that you can edit. Select a value\n" + 
          "and then enter the new value that you want for the character. When you are done\n" + 
          "editing a character enter 'done' to finish.\n")
    
    get_characters_list()

    edit_running = True

    #While the user wants to be in character creation
    while edit_running:
        print("To edit a character enter the characters name. To return to the menu enter 'exit'.")

        character_name = input("\nCharacter: ")
        print("")
        character_name = character_name.lower()

        character_list = get_characters_list(characters_folder)

        if character_name in character_list:
                edit(character_name)
        elif character_name == "exit":
            print("Mode changed from character edit to menu.")
            edit_running = False
        else:
            print("Invalid name. Please enter a valid name or exit.\n")