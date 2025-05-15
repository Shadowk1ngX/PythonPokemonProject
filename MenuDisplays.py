import sys
import time
import os
import PokemonData as Pokemon

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


def Display_Starting_Pokemon(Game):
    print(" 1: Bulbasaur")
    print(" 2: Charmander")
    print(" 3: Squirtle")
    print(" 4: Pikachu")
    print(" 5: Eevee")
    print(" 6: Chikorita")
    print(" 7: Cyndaquil")
    print(" 8: Totodile")
    print(" 9: Treecko")
    print("10: Torchic")
    print("11: Mudkip")
    print("12: Turtwig")
    print("13: Chimchar")
    print("14: Piplup")
    print("15: Snivy")
    print("16: Tepig")
    print("17: Oshawott")
    print("18: Chespin")
    print("19: Fennekin")
    print("20: Froakie")
    print("21: Rowlet")
    print("22: Litten")
    print("23: Popplio")
    print("24: Grookey")
    print("25: Scorbunny")
    print("26: Sobble")
    print("27: Cyndaquil")
    print("28: Rowlet")
    print("29: Oshawott")
    print("30: Sprigatito")
    print("31: Fuecoco")
    print("32: Quaxly")


    choice = input("Please enter the number next to your choice to display more info\n")

    match choice:
        case "1":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory(Pokemon.Bulbasaur())
                    Type_Text_Effect("Great Choice! Now go out and catch them all!",Game.TextSpeed)
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "2":
            Game.ClearScreen()
            Type_Text_Effect("Charmander, a Fire type lizard Pokémon whose tail flame indicates its life .", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)           
        case "3":
            Game.ClearScreen()
            Type_Text_Effect("Squirtle, a Water type pokemon. A tiny turtle Pokémon that sprays water to protect itself.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "4":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "5":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "6":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "7":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "8":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "9":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "10":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "11":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "12":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "13":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "14":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "15":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "16":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "17":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "18":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "19":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "20":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "21":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "22":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "23":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "24":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "25":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "26":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "27":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "28":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "29":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "30":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "31":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)
        case "32":
            Game.ClearScreen()
            Type_Text_Effect("Bulbasaur, a Grass/Poison seed type Pokémon with a bulb on its back that grows into a plant.", Game.TextSpeed)
            time.sleep(1)
            Type_Text_Effect("Would you like to choose this Pokémon? Enter Y or N...\n", Game.TextSpeed)
            
            choice2 = input()
            match choice2:
                case "Y"|"y":
                    Game.Player.PlayerInventory.Add_Pokemon_To_Inventory()
                case "N"|"n":
                    Display_Starting_Pokemon(Game)
                case _:
                    Type_Text_Effect("Please enter a valid responce...",Game.TextSpeed)
                    Display_Starting_Pokemon(Game)    