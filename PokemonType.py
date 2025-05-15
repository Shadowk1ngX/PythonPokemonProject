
class PokemonType():
    def __init__(self,poke_type):
        self.PokeType = poke_type


class Grass(PokemonType):
    def __init__(self):
        super().__init__(
            poke_type="Grass"
        )

class Poison(PokemonType):
    def __init__(self):
        super().__init__(
            poke_type="Poison"
        )


Effectiveness = {
        ("Grass", "Ground"): 2,
        ("Grass", "Rock"): 2,
        ("Grass", "Water"): 2,
        ("Grass", "Flying"): .5,
        ("Grass", "Poison"): .5,
        ("Grass", "Bug"): .5,
        ("Grass", "Steel"): .5,
        ("Grass", "Fire"): .5,
        ("Grass", "Grass"): .5,
        ("Grass", "Dragon"): .5,
    }   


def GetEffectivenessMulitpier(AttackMoveType,DefenderPokeTypes):
    multiplier = 1
    for defender_type in DefenderPokeTypes:
        multiplier *= Effectiveness.get((AttackMoveType, defender_type), 1)
    return multiplier