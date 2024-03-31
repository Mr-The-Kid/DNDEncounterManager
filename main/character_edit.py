# Author(s): CJ Roedel
# Last update: 03/28/24 - 1:11

#imports
import os
import csv

#globals
characters_folder = ""
character_fields = []

def set_characters_folder(path):
    global characters_folder
    characters_folder = path

def set_characters_field(field):
   global character_fields
   character_fields = field

#Get the list of all saved characters and prints them to the screen
#param(s)
#no param(s)
#return(s)
#list of saved character names
def get_characters_list():
    files_list = os.listdir(characters_folder)

    if len(files_list) == 0:
        print("\nThere are no characters to edit.")
        return None

    character_names = files_list

    for i in range(len(files_list)):
        character_names[i] = str(files_list[i]).removesuffix(".csv")

    print("\nHere is the list of all saved characters:")
    for name in character_names:
        print(name)
    print(character_fields)
    
    return character_names
         

#Get the values of the currently selected character for editing
#param(s)
#character_name: the name of the character to edit
#return(s)
#list of character values
def get_character_values(character_name):
    character_file = characters_folder + character_name + ".csv"
    
    character_values = [None] * len(character_fields)

    with open(character_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            for i in range(len(character_fields)):
                character_values[i] = row[character_fields[i]]
        
    print(character_values)

#Save the changes made by the user to the characters file
#param(s)
#new_values: the updated values for the character
#return(s)
#no return(s)
def update_character_values(new_values):
    next

#Updates the existing character with the edited values
#param(s)
#character_name: the name of the character to edit
#return(s)
#no return(s)
def edit_character(character_name):
    print("You have selected to edit " + character_name + ". Select a field to edit or enter done to finish.")

    field_values = get_character_values(character_name)

    edit_running = True

    while edit_running:
        edit_field = input("\nField: ")
        edit_field = edit_field.lower()
        print("")

        if edit_field in character_fields:
            next
        elif edit_field == "done":
            edit_running = False
            print("Saving character now.")
            update_character_values()
        else:
            print("Please enter a valid field name or 'done'")

#Edit mode which allows for the user to edit the values of a character
#param(s)
#no param(s)
#return(s)
#no return(s)
def edit():
    #Tool explanation
    print("Mode changed from menu to character edit.")
    print("In character edit you will be given the list of all characters that are currently.\n" + 
          "saved. You will then input the name of the character that you would like to edit.\n" + 
          "From here you will be given the list of values that you can edit. Select a value\n" + 
          "and then enter the new value that you want for the character. When you are done\n" + 
          "editing a character enter 'done' to finish.\n")
    print("To edit a character enter the characters name. To return to the menu enter 'exit'.")

    edit_running = True

    #While the user wants to be in character creation
    while edit_running:

        character_list = get_characters_list()

        if character_list == None:
            print("\nMode changed from character edit to menu.")
            return

        character_name = input("\nCharacter: ")
        print("")
        character_name = character_name.lower()

        if character_name in character_list:
            edit_character(character_name)
        elif character_name == "exit":
            print("Mode changed from character edit to menu.")
            edit_running = False
        else:
            print("Invalid name. Please enter a valid name or exit.\n")