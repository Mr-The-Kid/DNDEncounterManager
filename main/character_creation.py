# Author(s): CJ Roedel
# Last update: 03/26/24 - 2:23

#imports
import csv

#globals
character_fields = ["name", "total_hp", "current_hp", "ac"]

def create_character(field_values):
    next

def value_inputs():
    field_values = [None] * len(character_fields)
    save_character = True
    values_index = 0

    while values_index < len(character_fields):

        input_value = input("\nPlease enter the " + character_fields[values_index] +" for this character: ")
        input_value = input_value.lower()

        if input_value == "cancel":
                print("\nAre you sure you want to cancel creating this character? Nothing will be saved.\n" + 
                      "Enter 'yes' to cancel or anything else to continue.")
                
                cancel_input = input("\nCancel? ")
                cancel_input.lower()
                print("")

                if cancel_input == "yes":
                    save_character = False
                    break

                else:
                    continue
        else:
            if character_fields[values_index] != "name":
                if input_value.isnumeric():
                    print("Character " + character_fields[values_index] + " saved as " + input_value)
                    field_values[values_index] = input_value
                    values_index += 1
                else:
                    print("Please only input integers for values that are not names.")
            else:
                if input_value.isalnum():
                    print("Character " + character_fields[values_index] + " saved as " + input_value)
                    field_values[values_index] = input_value
                    values_index += 1
                else:
                    print("Please only input letters and digits for a characters name.")
    
    print("\nCharacter completed. Here is your character: ")
    for i in range(len(character_fields)):
        print("Character " + character_fields[i] + ": " + field_values[i])
    print("\nIf you would like to edit your character enter 'edit'. If you are satisfied\n" + 
          "with your current character enter anything else.")

            

def upload_characters():
    print("Mode changed from menu to character upload.")
    print("In character upload you will be prompted to enter information for a character.\n" + 
          "Each prompt will tell you what information to enter. Once you have entered all\n" + 
          "of the information for a character it will be saved. If at any point you wish\n" + 
          "to cancel creation of a character enter 'cancel'. If you enter an incorrect value\n" + 
          "you will have a chance to rectify your error before saving the character, or you\n" + 
          "will be able to fix the error in charcter edit mode.\n")
    
    creation_running = True

    while creation_running:
        print("To create a new character enter 'create'. To return to the normal command space enter 'exit'.")

        character_command = input("\nCommand: ")
        print("")
        character_command = character_command.lower()

        match character_command:
            case "create":
                value_inputs()
            case "exit":
                print("Mode changed from character upload to menu.")
                creation_running = False
            case default:
                print("Invalid command entered. Please enter a valid command.")
