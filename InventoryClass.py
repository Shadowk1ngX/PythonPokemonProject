class Inventory:
   
    def __init__(self):
        MaxInventorySlots = 10
        CurrentSlotsTaken = 0
        Backpack = []

        self.PlayerInventory = Backpack
        self.MaxInventory = MaxInventorySlots
        self.CurrentlyUsedSlots = CurrentSlotsTaken


    def Get_Inventory(self):
        return self.PlayerInventory


    def Search_For_Item(self, ItemName):
        for x in self.PlayerInventory:
            if x.__class__.__name__ == ItemName.__class__.__name__:
                return True, x
            else:
                continue
        return False
       

    