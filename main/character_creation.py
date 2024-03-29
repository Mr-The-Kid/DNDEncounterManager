# Author(s): CJ Roedel
# Last update: 03/28/24 - 1:11

#imports
import csv

#globals
#character_fields is the list of fields that a character needs to be created.
#Editing this list will update all processes to account for the new field values.
character_fields = []

def set_character_fields(fields):
    global character_fields
    character_fields = fields

#creates a new csv file for a character from the inputs provided for it.
#param(s)
#field_values: This is the list of values entered by the user to define this
#characters_folder: the path to the characters folder
#character
#return(s)
#no return value
def create_character(field_values, characters_folder):
    file_name = characters_folder + field_values[character_fields.index("name")] + ".csv"
    print(file_name)

    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=character_fields)

        writer.writeheader()
        writer.writerow(dict(zip(character_fields, field_values)))

#if a user decides that they want to change the values of their character before
#the character is saved to a file they can do so here
#param(s)
#field_values: This is the list of values entered by the user to define this
#character
#return(s)
#field_values: Returns the update list of field values
def edit_created_character(field_values):
    #Editing instructions
    print("\nYou have chosen to edit your character. When you are done enter 'done'. This will\n" +
          "exit edit mode and save your character. To edit later use edit mode from the menu.")
    
    editing = True

    
    while editing:
        #Print the field names that can be used
        print("The field values that you can edit are: ")
        for field in character_fields:
            print(field)
        print("Enter a field name as shown above. You will then be prompted to enter the new value.")

        edit_field = input("\nField: ")
        edit_field = edit_field.lower()
        print("")

        #Check if done
        if edit_field == "done":
            return field_values
        #Check if entered is valid option
        elif edit_field in character_fields:
            field_index = character_fields.index(edit_field)
            
            print("You are now editing the " + edit_field + " field. Current value is " + field_values[field_index])
            
            #Get value
            field_values[field_index] = input("\nUpdating " + field_values[field_index] + " to: ")

            #print new value and apply update to character
            print("\nUpdated value.")
            print("\nThis is now your character:")
            for i in range(len(character_fields)):
                print("Character " + character_fields[i] + ": " + field_values[i])
            print("")
        else:
            print("Please enter a field name or done.")
            continue
    return field_values
        

#This is the main function where the user must input the information for their
#character
#param(s)
#no param(s)
#return(s)
#no return(s)
def value_inputs(characters_folder):
    #Create an empy list the same size as character_fields
    field_values = [None] * len(character_fields)
    values_index = 0

    #Until the user has satisfied every required value
    while values_index < len(character_fields):
        
        #Users input for current field value
        input_value = input("\nPlease enter the " + character_fields[values_index] +" for this character: ")
        input_value = input_value.lower()

        #If the user decides to cancel at any point, ask for confirmation, then cancel
        if input_value == "cancel":
                print("\nAre you sure you want to cancel creating this character? Nothing will be saved.\n" + 
                      "Enter 'yes' to cancel or anything else to continue.")
                
                cancel_input = input("\nCancel? ")
                cancel_input.lower()
                print("")

                if cancel_input == "yes":
                    return

                else:
                    continue
        else:
            #Check that only integers are used for values that are not the name
            if character_fields[values_index] != "name":
                if input_value.isnumeric():
                    print("Character " + character_fields[values_index] + " saved as " + input_value)
                    field_values[values_index] = input_value
                    values_index += 1
                else:
                    print("Please only input integers for values that are not names.")
            else:
                #Check that only letters and numbers are used for the name
                if input_value.isalnum():
                    if input_value == "done":
                        print("You have entered 'done' as a characters name, but done is a reserved word.")
                        continue
                    print("Character " + character_fields[values_index] + " saved as " + input_value)
                    field_values[values_index] = input_value
                    values_index += 1
                else:
                    print("Please only input letters and digits for a characters name.")

    #Print out the character that was entered for verification before saving to file
    print("\nCharacter completed. Here is your character: ")
    for i in range(len(character_fields)):
        print("Character " + character_fields[i] + ": " + field_values[i])
    print("\nIf you would like to edit your character enter 'yes'. If you are satisfied\n" + 
          "with your current character enter anything else.")
    
    edit_input = input("\nEdit?: ")
    print("")
    edit_input = edit_input.lower()

    if edit_input == "yes":
        field_values = edit_created_character(field_values)
    
    create_character(field_values, characters_folder)

            
#the main function of character creation which explains the tool and lets the user
#continue to create characters, or return to menu mode
#param(s)
#characters_folder: the path to the characters folder
#return(s)
#no return(s)
def upload_characters(characters_folder):
    #Tool explanation
    print("Mode changed from menu to character upload.")
    print("In character upload you will be prompted to enter information for a character.\n" + 
          "Each prompt will tell you what information to enter. Once you have entered all\n" + 
          "of the information for a character it will be saved. If at any point you wish\n" + 
          "to cancel creation of a character enter 'cancel'. If you enter an incorrect value\n" + 
          "you will have a chance to rectify your error before saving the character, or you\n" + 
          "will be able to fix the error in charcter edit mode.\n")
    
    creation_running = True

    #While the user wants to be in character creation
    while creation_running:
        print("To create a new character enter 'create'. To return to the menu enter 'exit'.")

        character_command = input("\nCommand: ")
        print("")
        character_command = character_command.lower()

        match character_command:
            case "create":
                value_inputs(characters_folder)
            case "exit":
                print("Mode changed from character upload to menu.")
                creation_running = False
            case default:
                print("Invalid command entered. Please enter a valid command.")
