from GameEngine import Engine
from PlayerClass import PlayerObj
import MenuDisplays
import TypeingTextEffect
import os
import re
import time
import Gui

def ensure_directory_exists(SaveParam):
    if SaveParam == "SavePath":
        appdata_local = os.getenv("LOCALAPPDATA")
        game_data_path = os.path.join(appdata_local, "PokemonTextAdventures", "Data")
        os.makedirs(game_data_path, exist_ok=True)
        return game_data_path

Game = Engine()

while True:
    MenuDisplays.Display_Main_Menu(Game)

    if Game.GameMode == "New":
        TypeingTextEffect.Type_Text_Effect("Welcome adventurer!", Game.TextSpeed)
        TypeingTextEffect.Type_Text_Effect("\nWhat is your name?", Game.TextSpeed)
        AbsPath = ensure_directory_exists("SavePath")
        PlayerName = input("\n")

        while not bool(re.match("^[A-Za-z]+$", PlayerName)):
            PlayerName = input("Please Enter at least one character and no special characters \n")

        while os.path.exists(f"{AbsPath}\{PlayerName}") or not bool(re.match("^[A-Za-z]+$", PlayerName)):
            PlayerName = input("A character with this name already exist! Please choose another name. \n")

        Player = PlayerObj(PlayerName, Game)
        Game.Update_Player(Player) #Update engine to have new player
       # Game.Save_Game(Player)
        Game.Update_GameMode("New")#Must be switched back so game continues as normal or else game mode will be set to load due to save function

        TypeingTextEffect.Type_Text_Effect("Welcome to Pokemon Text Adventures! Get ready for an exciting journey with your favorite Pokemon!",Game.TextSpeed)
        TypeingTextEffect.Type_Text_Effect("Firstly, you need to choose a starting pokemon!",Game.TextSpeed)
        time.sleep(.5)
        MenuDisplays.Display_Starting_Pokemon(Game)
        Gui.StartMain(Game)