import sys
import time
import os

BoldText = "\033[1m"
ResetText = "\033[0m"

TextColorList = {
    "RED" : "\033[31m",
    "GREEN" : "\033[32m",
    "YELLOW" : "\033[33m",
    "RESET" : "\033[0m",
    }


GameVersion = "0.1 ALPHA"

def Type_Text_Effect(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def ensure_directory_exists(SaveParam):
    if SaveParam == "SavePath":
        appdata_local = os.getenv("LOCALAPPDATA")
        game_data_path = os.path.join(appdata_local, "TextAdeventures", "Data")
        os.makedirs(game_data_path, exist_ok=True)
        return game_data_path
    elif SaveParam == "DeathList":
        appdata_local = os.getenv("LOCALAPPDATA")
        game_data_path = os.path.join(appdata_local, "TextAdeventures", "Deaths")
        os.makedirs(game_data_path, exist_ok=True)
        return game_data_path

def Display_Load_Menu(Game):
 
    SaveFolder = ensure_directory_exists("SavePath")
    print(f"Save Path: {SaveFolder}")
    
    if not os.path.isdir(SaveFolder):
        try:
            os.makedirs(SaveFolder)
            print(f"Created directory: {SaveFolder}")
        except OSError as e:
            print(f"Error creating directory {SaveFolder}: {e}")
            return
        

    SaveFiles = [f for f in os.listdir(SaveFolder) if os.path.isfile(os.path.join(SaveFolder, f))]
    LastNumber = 0

    print("------------------- Choose A Save File -------------------")
    for i, save_file in enumerate(SaveFiles, start=1):
        LastNumber = i
        print(f"{i}. {save_file}")
    print(f"{LastNumber + 1}. Back")
    print("---------------------------------------------------------")
    
    choice = input("Please enter the number next to your choice:\n")

    if int(choice) == LastNumber + 1:
        Game.Update_GameMode(None)
        return

    
    choice_index = int(choice) - 1  # Convert choice to zero-based index
    if 0 <= choice_index < len(SaveFiles):
        SelectedSave = SaveFiles[choice_index]
        Type_Text_Effect(f"Loading save file for the adeventurer: {SelectedSave}....", Game.TextSpeed)
        time.sleep(2)
        SelectedSavePath = os.path.join(SaveFolder, SaveFiles[choice_index])
        LoadedPlayer = Game.Load_Game(SelectedSavePath)
        print("Player Loaded")
        time.sleep(2)
        return LoadedPlayer
    else:
        print(f"Invalid selection: {choice}")
        Game.Update_GameMode(None)
        Display_Load_Menu(Game)


def Display_Delete_Menu(Game):
    SaveFolder = ensure_directory_exists("SavePath")
    print(f"Save Path: {SaveFolder}")
    
    SaveFiles = [f for f in os.listdir(SaveFolder) if os.path.isfile(os.path.join(SaveFolder, f))]
    LastNumber = 0

    print("------------------- Choose A Save File To Delete -------------------")
    for i, save_file in enumerate(SaveFiles, start=1):
        LastNumber = i
        print(f"{i}. {save_file}")
    print(f"{LastNumber + 1}. Back")
    print("---------------------------------------------------------")
    
    choice = input("Please enter the number next to your choice:\n")

    if int(choice) == LastNumber + 1:#HERE
        return

    choice_index = int(choice) - 1  # Convert choice to zero-based index
    if 0 <= choice_index < len(SaveFiles):
        SelectedSave = SaveFiles[choice_index]
        Type_Text_Effect(f"Deleting save file for the adeventurer: {SelectedSave}....", Game.TextSpeed)
        SelectedSavePath = os.path.join(SaveFolder, SaveFiles[choice_index])
        os.remove(SelectedSavePath)
        time.sleep(2)
        print("Save Deleted")
        time.sleep(2)
        Display_Main_Menu(Game)
    else:
        print(f"Invalid selection: {choice}")
        Game.Update_GameMode(None)
        Display_Load_Menu(Game)


def Display_Play_Menu(Game):
    Game.ClearScreen()
    print("\n-------------------Text Adventures!-------------------")
    print("\n1: Load Game")
    print("\n2: New Game")
    print('\n3: Delete Save')
    print("\n4: Main menu")
    print("\n-------------------Text Adventures!-------------------")

    choice = input("Please enter the number next to your choice\n")


    match choice:
        case "1":
            Game.Update_GameMode("Load")
        case "2":
            Game.ClearScreen()
            Game.Update_GameMode("New")
        case "3":
            Display_Delete_Menu(Game)
        case "4":
            Display_Main_Menu(Game)
        case _:
            print("Selection does not exist for: " + choice)
            Display_Play_Menu(Game)


def Display_Text_Speed_Options(Game):
    print("\n-------------------Text Speeds-------------------")
    print("\n1: Slow")
    print("\n2: Medium")
    print("\n3: Fast")
    print("\n4: No type effect")
    print("\n-------------------Text Speeds-------------------")

    choice = input("Please enter the number next to your choice\n")

    match choice:
        case "1":
            Game.Update_Text_Speed(.12)
            Display_Options_Menu(Game)
        case "2":
            Game.Update_Text_Speed(.05)
            Display_Options_Menu(Game)
        case "3":
            Game.Update_Text_Speed(.01)
            Display_Options_Menu(Game)
        case "4":
            Game.Update_Text_Speed(0)
            Display_Options_Menu(Game)
        case _:
            print("Selection does not exist for: " + choice)
            Display_Text_Speed_Options(Game)



def Display_Options_Menu(Game):
    Game.ClearScreen()
    print("\n-------------------Game Options-------------------")
    print("\n1: Text Speed")
    print("\n2: Main menu")
    print("\n-------------------Game Options-------------------")

    choice = input("Please enter the number next to your choice\n")

    match choice:
        case "1":
            Game.ClearScreen()
            Display_Text_Speed_Options(Game)
        case "2":
            Game.ClearScreen()
            Display_Main_Menu(Game)
        case _:
            Game.ClearScreen()
            print("Selection does not exist for: " + choice)
            Display_Options_Menu(Game)




def Display_Update_Log(Game):#Updates
    Game.ClearScreen()

    print("\n-------------------Update Log-------------------")
    print(f"{BoldText}----Version 0.70 ALPHA----{ResetText}")
    print(f"{BoldText}Updates{ResetText}")
    print("-Added Gold")
    print("-Added Armors (Hemlet, Body Armor, and boots)")
    print("-Removed option to manually save and game now auto saves for you. Replaced with option to change game options")
    print("-Adventurer Graveyard added to main menu that shows past attempts")
    print("-Added Show Player stats option in dungeon menu")
    print("-Items (Weapons and armor etc) can now affect more than one stat")
    print("-Added very basic shop functionality and random events (Shop is one of the random events)")

    print(f"\n{BoldText}Balance Changes{ResetText}")

    print(f"{BoldText}Bug Fixes{ResetText}")
    print("-Fixed stat points giving a lot (I actually just forgot to reset the spent ones lol)")



    print(f"\n{BoldText}----Version 0.65 ALPHA----{ResetText}")
    print(f"{BoldText}Updates{ResetText}")
    print("-Added credits option")
    print("-Added Update Log option")
    print("-Added Discard Menu for Inventory (Currently only weapons and consumables work)")
    print("-Each Race now has their own sarting weapons.")
    print("-Race Menu now shows the starting stats and weapon along with a description")
    

    print(f"\n{BoldText}Balance Changes{ResetText}")
    print("-Increased base inventory space from 6 to 10")

    print("\n-------------------Update Log-------------------")
    
    choice = input("Enter Y when ready to return\n")
    match choice:
            case "Y":
                Display_Main_Menu(Game)
            case "y":
                Display_Main_Menu(Game)
            case _:
                print("Invalid Input")
                time.sleep(1.5)
                Display_Update_Log(Game)

def Display_Credits(Game):
    Game.ClearScreen()

    print("\n-------------------Credits-------------------")
    print(f"{BoldText}Creator{ResetText}: Shadowking\nDiscord Name: Shadowking\nDiscord Server Link: https://discord.gg/bCpZHZURVG\n")
    print(f"{BoldText}Testers{ResetText} (Discord Names):\nDva_rocks\nOmniMan\nNoyaDevs\nZomb")

    print("\n-------------------Credits-------------------")
    
    choice = input("Enter Y when ready to return\n")
    match choice:
            case "Y":
                Display_Main_Menu(Game)
            case "y":
                Display_Main_Menu(Game)
            case _:
                print("Invalid Input")
                time.sleep(1.5)
                Display_Update_Log(Game)



def Display_Main_Menu(Game):
    Game.ClearScreen()
    print("\n-------------------Text Adventures!-------------------")
    print("\n1: Play")
    print("\n2: Options")
    print("\n3: Update Log")
    print("\n4: Credits")
    print("\n5: Quit")
    print("\n-------------------Text Adventures!-------------------")
    print(f"\nGame Version: {GameVersion}")

    choice = input("Please enter the number next to your choice\n")

    match choice:
        case "1":
            Display_Play_Menu(Game)
        case "2":
            Display_Options_Menu(Game)
        case "3":
            Display_Update_Log(Game)
        case "4":
            Display_Credits(Game)
        case "5":
            Type_Text_Effect("Till we meet again adventurer...", Game.TextSpeed)
            quit()
        case _:
            print(f"{TextColorList['RED']}Selection does not exist for: {TextColorList['RESET']}" + choice)
            Display_Main_Menu(Game)