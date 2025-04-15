import os
import pickle
import datetime
import time
import TypeingTextEffect

def ensure_directory_exists(SaveParam):
    if SaveParam == "SavePath":
        appdata_local = os.getenv("LOCALAPPDATA")
        game_data_path = os.path.join(appdata_local, "PokemonTextAdventures", "Data")
        os.makedirs(game_data_path, exist_ok=True)
        return game_data_path

class Engine:
    def __init__(self,):
        self.GameMode = None
        self.TextSpeed = 0.03
        self.Player = None


    def Update_Player(self, Player):
        self.Player = Player

    def Update_GameMode(self, Mode):
        self.GameMode = Mode

    def Get_GameMode(self):
        return self.GameMode

    def Update_Text_Speed(self, Speed):
        self.TextSpeed = Speed
    
    def Delete_Save(self):
        AbsPath = ensure_directory_exists("SavePath")
        SavePath = os.path.join(AbsPath, self.Player.Name)
        if os.path.exists(SavePath):
            os.remove(SavePath)
        else:
            print("Could not find save file")

    def Auto_Save_Game(self, CurrentPlayer):
       
        self.Update_GameMode("Load") #Needed or gamemode will load in as new and be treated as such

        CurrentGame = self
        FileSaveName = self.Player.Name
        AbsPath = ensure_directory_exists("SavePath")
        FileSavePath = f"{AbsPath}\{FileSaveName}"

        DataToSave = (CurrentGame, CurrentPlayer)

        with open(FileSavePath, 'wb') as f:
            pickle.dump(DataToSave, f)
        f.close()
        

    def Save_Game(self, CurrentPlayer):
       
        self.Update_GameMode("Load") #Needed or gamemode will load in as new and be treated as such

        CurrentGame = self
        FileSaveName = self.Player.Name
        AbsPath = ensure_directory_exists("SavePath")
        FileSavePath = f"{AbsPath}\{FileSaveName}"

        DataToSave = (CurrentGame, CurrentPlayer)

        with open(FileSavePath, 'wb') as f:
            pickle.dump(DataToSave, f)
        f.close()

        TypeingTextEffect.Type_Text_Effect("Saving game...", self.TextSpeed)
        time.sleep(1.5)
        TypeingTextEffect.Type_Text_Effect("Game Saved", self.TextSpeed)

    def Load_Game(self, SaveFile):
    
        with open(SaveFile, 'rb') as f:
            Data = pickle.load(f)
        f.close()


        if isinstance(Data[0], Engine):
                saved_engine = Data[0]
                self.GameMode = saved_engine.GameMode
                self.Difficulty = saved_engine.Difficulty
                self.DungeonLevel = saved_engine.DungeonLevel
                self.TextSpeed = saved_engine.TextSpeed
                self.CurrentEnimies = saved_engine.CurrentEnimies
                
        
        
        if isinstance(Data[1], Player):
                saved_hero = Data[1]
                Player = Player("Loading")
                Player.Name = saved_hero.Name
                Player.Race = saved_hero.Race
                Player.Level = saved_hero.Level
                Player.EXP = saved_hero.EXP
                Player.StatPoints = saved_hero.StatPoints
                Player.MaxHealth = saved_hero.MaxHealth
                Player.Health = saved_hero.Health
                Player.Attack = saved_hero.Attack
                Player.Defence = saved_hero.Defence
                Player.Intellect = saved_hero.Intellect
                Player.PlayerInventory = saved_hero.PlayerInventory
                Player.Luck = saved_hero.Luck
                Player.Description = saved_hero.Description
                Player.Weapon = saved_hero.Weapon
                Player.Gold = saved_hero.Gold
                Player.Helmet = saved_hero.Helmet
                Player.BodyArmor = saved_hero.BodyArmor
                Player.Boots = saved_hero.Boots
                return Player
        
    def Get_GraveYard_Data(self):
        AbsPath = ensure_directory_exists("DeathList")
        SavePath = os.path.join(AbsPath, "DeathList")

        with open(SavePath, 'rb') as f:
            Data = pickle.load(f)
        f.close()

        return Data
    
    def Get_Date_Time(self):
        CurrentDateTime = datetime.datetime.now()
        CurrentDate = CurrentDateTime.date()
        CurrentTime = CurrentDateTime.time()
        CurrentTimeFormatted = CurrentTime.strftime("%I:%M %p")

        return CurrentDate, CurrentTimeFormatted


    def ClearScreen(self):
        os.system('cls||clear')