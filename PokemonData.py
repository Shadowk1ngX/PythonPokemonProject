import PokemonType as PokeTypes
import PokemonTraits as PokeTraits
import PokemonMoves as PokeMoves
import random



class Pokemon:
    def __init__(self,name,base_max_health,base_attack,base_defense,base_sp_attack,base_sp_defense,base_speed,poke_id,level,catch_rate,base_exp,current_exp,egg_cycle,shiny,growth_rate,poke_type,gender,moves,description):
        self.Name = name
        self.BaseMaxHealth = base_max_health
        self.BaseAttack = base_attack
        self.BaseDefense = base_defense
        self.BaseSpAttack = base_sp_attack
        self.BaseSpDefense = base_sp_defense
        self.BaseSpeed = base_speed
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
        self.ExpToNextLevel = self.CalculateExpToNextLevel()
        self.Attack = self.CalculateNewStat(base_attack,self.Ivs["Attack"],self.Evs["Attack"],self.Level,"Attack")
        self.Defense = self.CalculateNewStat(base_defense,self.Ivs["Defense"],self.Evs["Defense"],self.Level,"Defense")
        self.SpAttack = self.CalculateNewStat(base_sp_attack,self.Ivs["SpAttack"],self.Evs["SpAttack"],self.Level,"SpAttack")
        self.SpDefense = self.CalculateNewStat(base_sp_defense,self.Ivs["SpDefense"],self.Evs["SpDefense"],self.Level,"SpDefense")
        self.Speed = self.CalculateNewStat(base_speed,self.Ivs["Speed"],self.Evs["Speed"],self.Level,"Speed")
        self.Moves = moves

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
    
    def CalculateExpToNextLevel(self):
        level = self.Level + 1
        if self.GrowthRate == "Fast":
            return int(4 * (level ** 3) / 5)
        elif self.GrowthRate == "Medium-Fast":
            return int(level ** 3)
        elif self.GrowthRate == "Medium-Slow":
            return int(1.2 * (level ** 3) - 15 * (level ** 2) + 100 * level - 140)
        elif self.GrowthRate == "Slow":
            return int(5 * (level ** 3) / 4)
        elif self.GrowthRate == "Erratic":
            if level <= 50:
                return int((level ** 3) * (100 - level) / 50)
            elif level <= 68:
                return int((level ** 3) * (150 - level) / 100)
            elif level <= 98:
                return int((level ** 3) * ((1911 - 10 * level) / 3) / 500)
            else:
                return int((level ** 3) * (160 - level) / 100)
        elif self.GrowthRate == "Fluctuating":
            if level <= 15:
                return int((level ** 3) * ((level + 1) / 3 + 24) / 50)
            elif level <= 36:
                return int((level ** 3) * (level + 14) / 50)
            else:
                return int((level ** 3) * ((level / 2) + 32) / 50)
        else:
            return int(level ** 3)  # Default to Medium-Fast

    
    def LevelUp(self):
        #Should have made stats a dict so i could loop though them instead
        print("LEVEL UP!")
        self.Level += 1
        self.MaxHealth = self.CalculateNewStat(self.BaseMaxHealth,self.Ivs["Health"],self.Evs["Health"],self.Level,"Health")
        self.Health = self.MaxHealth
        self.Attack = self.CalculateNewStat(self.BaseAttack,self.Ivs["Attack"],self.Evs["Attack"],self.Level,"Attack")
        self.Defense = self.CalculateNewStat(self.BaseDefense,self.Ivs["Defense"],self.Evs["Defense"],self.Level,"Defense")
        self.SpAttack = self.CalculateNewStat(self.BaseSpAttack,self.Ivs["SpAttack"],self.Evs["SpAttack"],self.Level,"SpAttack")
        self.SpDefense = self.CalculateNewStat(self.BaseSpDefense,self.Ivs["SpDefense"],self.Evs["SpDefense"],self.Level,"SpDefense")
        self.Speed = self.CalculateNewStat(self.BaseSpeed,self.Ivs["Speed"],self.Evs["Speed"],self.Level,"Speed") 
        self.ExpToNextLevel = self.CalculateExpToNextLevel()    

    def TakeDamage(self, EnemyPokemon, EnemyAttack):

        STABMultiplier = 1
        TypeEffctivenessMultiplier = PokeTypes.GetEffectivenessMulitpier(EnemyAttack.Type, self.PokeType)
        RandomMultiplier = random.uniform(0.85,1.00)

        for ClassType in self.PokeType:
            Type = ClassType().PokeType
            if EnemyAttack.Type == Type:
                print("Type match!")
                STABMultiplier = 1.5
                break

        
        if EnemyAttack.Category == "Physical":
            Damage = (((2 * EnemyPokemon.Level / 5+2) * EnemyAttack.Power * (EnemyPokemon.Attack / self.Defense)) / 50 + 2 ) * STABMultiplier * TypeEffctivenessMultiplier * RandomMultiplier
        elif EnemyAttack.Category == "Special":
            Damage = (((2 * EnemyPokemon.Level / 5+2) * EnemyAttack.Power * (EnemyPokemon.SpAttack / self.SpDefense)) / 50 + 2 ) * STABMultiplier * TypeEffctivenessMultiplier * RandomMultiplier
        else:
            print("Handle status attack")
            Damage = 0

        if Damage == 0:
            print("NO DAMAGE")
            return True
        
        print(f"Calculated Damage: {Damage}")
        self.Health -= Damage
        if self.Health <= 0:
            return False#Choose true or false for death
        return True
    
    def AddExp(self, Amount):
        self.CurrentExp += Amount
        while self.CurrentExp >= self.ExpToNextLevel:
            self.CurrentExp -= self.ExpToNextLevel
            self.LevelUp()

    def CalculateExpReward(self, base_exp, defeated_level, receiver_level, is_trainer_battle=False): #is_traded=False, has_lucky_egg=False, has_affection=False):
        
        term1 = (base_exp * defeated_level) / 5
        level_factor = ((2 * defeated_level + 10) / (defeated_level + receiver_level + 10)) ** 2.5
        exp = (term1 * level_factor) + 1  # +1 is added to round up small amounts

        if is_trainer_battle:
            exp *= 1.5
    
        self.AddExp(int(exp))

    

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
        poke_type = [PokeTypes.Grass,PokeTypes.Poison],
        gender= PokeTraits.GenerateGender(1,7),
        moves = [PokeMoves.Tackle, PokeMoves.Growl],
        description= "Bulbasaur is a small, quadrupedal, amphibian Pokémon with blue-green skin and darker spots. It has red eyes, a wide mouth, and pointed, ear-like structures on top of its head. A notable feature is the plant bulb on its back, which is present from birth. This bulb grows alongside Bulbasaur, absorbing sunlight to provide energy through photosynthesis. This process allows Bulbasaur to sustain itself without food for extended periods.",
        )
        



PokemonList = [Bulbasaur] #For wild pokemon