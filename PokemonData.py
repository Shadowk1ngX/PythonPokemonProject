
class Pokemon:
    def __init__(self,name,health,attack,defense,sp_attack,sp_defense,speed,poke_id,level,catch_rate,base_exp,current_exp,egg_cycle,shiny,growth_rate):
        self.Name = name
        self.Health = health
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


class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__(
        name = "Bulbasaur",
        health = 45,
        attack = 49,
        defense = 49,
        sp_attack = 65,
        sp_defense = 65,
        speed = 45,
        poke_id = 1,
        base_exp = 64,
        current_exp = 0,
        level = 1,
        catch_rate = 45,
        egg_cycle = 20,
        shiny = False,
        GrowthRate = "Medium-Slow"
        )
