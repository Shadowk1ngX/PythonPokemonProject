from InventoryClass import Inventory

BoldText = "\033[1m"
ResetText = "\033[0m"

TextColorList = {
    "RED" : "\033[31m",
    "GREEN" : "\033[32m",
    "YELLOW" : "\033[33m",
    "RESET" : "\033[0m",
    }

class PlayerObj:
    def __init__(self, Name, Game):
       
        PlayerInventory = Inventory() 

        if Game.Get_GameMode() != "Load": #If Game Mode = New
            self.Name = Name
            self.PlayerInventory = PlayerInventory
            self.Gold = 0
        else:
            self.Name = Name
            self.PlayerInventory = None
            self.Gold = 0

    def Add_Gold(self, FoundGold):
        self.Gold += FoundGold
        print(f"{TextColorList['GREEN']}You found {FoundGold} Gold{TextColorList['RESET']}")
    
    def Remove_Gold(self, Amount):
        self.Gold -= Amount
        print(f"{TextColorList['RED']}You spent {Amount} Gold{TextColorList['RESET']}")
    
    def Get_Player(self):
        return self
    
    def Get_Player_Name(self):
        return self.Name

    def __str__(self) -> str:
        return f"{'Player Name : '+ self.Name}\n"
