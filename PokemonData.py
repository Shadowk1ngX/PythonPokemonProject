import PokemonType as PokemonType
import PokemonTraits as PokeTraits
import random

class Pokemon:
    def __init__(self,name,base_max_health,base_attack,base_defense,base_sp_attack,base_sp_defense,base_speed,max_health,attack,defense,sp_attack,sp_defense,speed,poke_id,level,catch_rate,base_exp,current_exp,egg_cycle,shiny,growth_rate,poke_type,current_health,description,gender):
        self.Name = name
        self.BaseMaxHealth = base_max_health
        self.BaseAttack = base_attack
        self.BaseDefense = base_defense
        self.BaseSpAttack = base_sp_attack
        self.BaseSpDefense = base_sp_defense
        self.BaseSpeed = base_speed
        base_exp
        self.MaxHealth = max_health
        self.Health = current_health
        self.Attack = attack
        self.Defense = defense
        self.SpAttack = sp_attack
        self.SpDefense = sp_defense
        self.Speed = speed
        self.PokeId = poke_id
        self.BaseExp = base_exp
        self.CurrentExp = current_exp
        self.Level = level
        self.CatchRate = catch_rate #The lower the harder, the higher the easier to catch
        self.EggCycle = egg_cycle
        self.Shiny = shiny
        self.GrowthRate = growth_rate
        self.PokeType = poke_type
        self.Description = description
        self.Gender = gender
        self.Ivs = PokeTraits.GenerateIvs()
        self.HeldItem = None
        self.Nature = PokeTraits.GenerateNature()

    def LevelUp(self):
        #print(self.Ivs.items())
        for x in self.Ivs.keys():
            if str(x)=="Attack":
                ...



    def __str__(self):
        PokeTypeString = ""
        for index, x in enumerate(self.PokeType):
            ToString = str(x().PokeType)
            PokeTypeString += ToString
            if index < len(self.PokeType) - 1:
                PokeTypeString += ", "
        return (
            f"Name: {self.Name}\n"
            f"Type: {PokeTypeString}\n"
            f"Pokemon Id: {self.PokeId}\n"
            f"Sex: {self.Gender}\n"
            f"Level: {self.Level}\n"
            f"Exp: {self.CurrentExp}(put / max)\n"
            f"Health: {self.Health}/{self.MaxHealth}\n"
            f"Attack: {self.Attack}\n"
            f"Defense: {self.Defense}\n"
            f"Special Attack: {self.SpAttack}\n"
            f"Special Defense: {self.SpDefense}\n"
            f"Speed: {self.Speed}\n"
            f"Holding: {self.HeldItem}\n"
            f"Nature: {self.Nature}\n"
            f"\nDescription:\n"
            f"{self.Description}"
        )
     

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__(
        name = "Bulbasaur",
        base_max_health = 45,
        base_attack = 49,
        base_defense = 49,
        base_sp_attack = 65,
        base_sp_defense = 65,
        base_speed = 45,
        base_exp = 64,
        max_health = 45,
        current_health= 45,
        attack = 49,
        defense = 49,
        sp_attack = 65,
        sp_defense = 65,
        speed = 45,
        poke_id = 1,
        current_exp = 0,
        level = 1,
        catch_rate = 45,
        egg_cycle = 20,
        shiny = False,
        growth_rate= "Medium-Slow",
        poke_type = [PokemonType.Grass,PokemonType.Poison],
        gender= PokeTraits.GenerateGender(1,7),
        description= "Bulbasaur is a small, quadrupedal, amphibian Pokémon with blue-green skin and darker spots. It has red eyes, a wide mouth, and pointed, ear-like structures on top of its head. A notable feature is the plant bulb on its back, which is present from birth. This bulb grows alongside Bulbasaur, absorbing sunlight to provide energy through photosynthesis. This process allows Bulbasaur to sustain itself without food for extended periods.",
        )

Bulb = Bulbasaur()
print(Bulb.LevelUp())