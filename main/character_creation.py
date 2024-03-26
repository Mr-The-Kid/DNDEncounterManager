# Author(s): CJ Roedel
# Last update: 03/26/24 - 2:23

#imports
import csv

def create():
    character_values = ["name", "total_hp", "current_hp", "ac"]
    save_character = True
    values_index = 0

    while values_index < len(character_values):

        input_value = input("Please enter the ", character_values[values_index], " for this character: ")
        input_value = input_value.lower()

        if input_value == "cancel":
                print("Are you sure you want to cancel creating this character? Nothing will be saved.\n" + 
                      "Enter 'yes' to cancel or anything else to continue.")
                
                cancel_input = input("\nCancel? ")
                cancel_input.lower()

                if cancel_input == "yes":
                    save_character = False
                    break

                else:
                    continue
        else:
            print("else")
            

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
                create()
            case "exit":
                print("Mode changed from character upload to menu.")
                creation_running = False
            case default:
                print("Invalid command entered. Please enter a valid command.")
