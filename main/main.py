# Author(s): CJ Roedel
# Last update: 03/26/24 - 2:23

#imports
import character_creation as cc

def display_help():
    print("upload:  Begins the process to upload characters to the encounter manager")
    print("create:  Begins the process of creating an encounter")
    print("start:   Starts the encounter that has been created")
    print("exit:    Exits the program")


def main():
    #Welcome Screen
    print("\n*****************************************************************")
    print("Welcome to DND Encounter Manager -by CJ Roedel and Michael Natoli")
    print("*****************************************************************\n")

    print("To add new characters enter 'upload', to create an encounter enter 'create'," +
      " to see all commands enter 'help', to exit program enter 'exit'.")

    program_running = True

    while program_running:
        command_input = input("\nCommand: ")
        print("")
        command_input = command_input.lower()

        match command_input:
            case "help":
                display_help()
            case "upload":
                cc.upload_characters()
            case "create":
                next
            case "start":
                next
            case "exit":
                program_running = False
            case default:
                print("Please enter a valid command. For a list of valid commands enter 'help'.")


if __name__ == "__main__":
    main()