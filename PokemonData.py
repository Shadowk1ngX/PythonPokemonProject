import PokemonType as PokemonType
import PokemonTraits as PokeTraits
import random



class Pokemon:
    def __init__(self,name,base_max_health,base_attack,base_defense,base_sp_attack,base_sp_defense,base_speed,poke_id,level,catch_rate,base_exp,current_exp,egg_cycle,shiny,growth_rate,poke_type,description,gender):
        self.Name = name
        self.BaseMaxHealth = base_max_health
        self.BaseAttack = base_attack
        self.BaseDefense = base_defense
        self.BaseSpAttack = base_sp_attack
        self.BaseSpDefense = base_sp_defense
        self.BaseSpeed = base_speed
        base_exp
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
        self.Evs = PokeTraits.CreateEvsData()
        self.MaxHealth = self.CalculateNewStat(base_max_health,self.Ivs["Health"],self.Evs["Health"],self.Level,"Health")
        self.Health = self.MaxHealth
        self.Attack = self.CalculateNewStat(base_attack,self.Ivs["Attack"],self.Evs["Attack"],self.Level,"Attack")
        self.Defense = self.CalculateNewStat(base_defense,self.Ivs["Defense"],self.Evs["Defense"],self.Level,"Defense")
        self.SpAttack = self.CalculateNewStat(base_sp_attack,self.Ivs["SpAttack"],self.Evs["SpAttack"],self.Level,"SpAttack")
        self.SpDefense = self.CalculateNewStat(base_sp_defense,self.Ivs["SpDefense"],self.Evs["SpDefense"],self.Level,"SpDefense")
        self.Speed = self.CalculateNewStat(base_speed,self.Ivs["Speed"],self.Evs["Speed"],self.Level,"Speed")

    def GetGrowthRateMultiplier(self, RateType):
        if RateType == "Fluctuating":
            return 1.1
        elif  RateType == "Erratic":
            return 0.9
        elif  RateType == "Slow":
            return 1.25
        elif  RateType == "Erratic":
            return 0.9
        elif  RateType == "Medium-Slow":
            return 1.2
        elif  RateType == "Medium-Fast":
            return 1.0
        elif  RateType == "Fast":
            return 0.8
        else:
            return 1
    
    def CalculateNewStat(self, BaseStat,IV,EV,Level,NatureModifierName):
        NatureModifier = 1
        NatrueData = PokeTraits.GetNatureValues(self.Nature)
        
        if NatureModifierName in NatrueData:
            NatureModifier += NatrueData[NatureModifierName]

        NewStat = round((((2 * BaseStat + IV + (EV / 4)) * Level) / 100 + 5) * NatureModifier)
        return NewStat
    

    def LevelUp(self):
        #Should have made stats a dict so i could loop though them instead
        self.Level += 1
        self.MaxHealth = self.CalculateNewStat(self.BaseMaxHealth,self.Ivs["Health"],self.Evs["Health"],self.Level,"Health")
        self.Health = self.MaxHealth
        self.Attack = self.CalculateNewStat(self.BaseAttack,self.Ivs["Attack"],self.Evs["Attack"],self.Level,"Attack")
        self.Defense = self.CalculateNewStat(self.BaseDefense,self.Ivs["Defense"],self.Evs["Defense"],self.Level,"Defense")
        self.SpAttack = self.CalculateNewStat(self.BaseSpAttack,self.Ivs["SpAttack"],self.Evs["SpAttack"],self.Level,"SpAttack")
        self.SpDefense = self.CalculateNewStat(self.BaseSpDefense,self.Ivs["SpDefense"],self.Evs["SpDefense"],self.Level,"SpDefense")
        self.Speed = self.CalculateNewStat(self.BaseSpeed,self.Ivs["Speed"],self.Evs["Speed"],self.Level,"Speed")     



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
        poke_id = 1,
        current_exp = 0,
        level = random.randint(1,5),
        catch_rate = 45,
        egg_cycle = 20,
        shiny = random.randint(1,4096) == 1 or False,
        growth_rate= "Medium-Slow",
        poke_type = [PokemonType.Grass,PokemonType.Poison],
        gender= PokeTraits.GenerateGender(1,7),
        description= "Bulbasaur is a small, quadrupedal, amphibian Pokémon with blue-green skin and darker spots. It has red eyes, a wide mouth, and pointed, ear-like structures on top of its head. A notable feature is the plant bulb on its back, which is present from birth. This bulb grows alongside Bulbasaur, absorbing sunlight to provide energy through photosynthesis. This process allows Bulbasaur to sustain itself without food for extended periods.",
        )
        



PokemonList = [Bulbasaur]