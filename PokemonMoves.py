class PokemonMove():
    def __init__(self,name,id,pp,power,accuracy,priority,move_type,category, description):
        self.Name = name
        self.ID = id
        self.PP = pp
        self.Power = power
        self.Accuracy = accuracy
        self.Priority = priority
        self.Type = move_type
        self.Category = category
        self.Description = description

    def __str__(self):
        return (
            f"Name: {self.Name}\n"
            f"Move ID: {self.ID}\n"
            f"PP: {self.PP}\n"
            f"Power: {self.Power}\n"
            f"Accuracy: {self.Accuracy}"
            f"Type: {self.Type}\n"
            f"Category: {self.Category}\n"
            f"Description: {self.Description}\n"
        )


class Tackle(PokemonMove):
    def __init__(self):
        super().__init__(
            name = "Tackle",
            id = 33,
            pp = 35,
            power = 40, 
            accuracy = 1, #Percentage based so do 0-1 or 0-100 1 being 100% or 100 being 100%
            priority = 0,
            move_type = "Normal", 
            category = "Physical",
            description = "A physical attack in which the user charges and slams into the target with its whole body."
        )

class Growl(PokemonMove):
    def __init__(self):
        super().__init__(
            name = "Growl",
            id = 45,
            pp = 40,
            power = 0, 
            accuracy = 1,
            priority = 0,
            move_type = "Normal", 
            category = "Status",
            description = "The user growls in an endearing way, making opposing Pokémon less wary. This lowers their Attack stats."
        )