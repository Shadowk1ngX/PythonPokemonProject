import random


def HandleBattle(Winner,Game,PlayerPokemon,PlayerAttack,EnemyPokemon,EnemyAttack): #Move atttack handling and death handling in pokemon class?
    if Winner == "Player":
        PlayerAttackPower = PlayerAttack.Power
        EnemyAttackPower = EnemyAttack.Power

        EnemyPokemon.Health -= PlayerAttackPower

        if EnemyPokemon.Health <= 0:
            ...
        
        PlayerAttack.Health -= EnemyAttackPower
        
        if PlayerPokemon.Health <= 0:
            ...

    else:
        ...

def HandleAttackTurn(Game,PlayerPokemon,PlayerAttack,EnemyPokemon):
    PlayerPokemonPriority = PlayerAttack.Priority
    EnemyAttack = random.choice(EnemyPokemon.Moves)()

    EnemyPokemonPriority = EnemyAttack.Priority

    if PlayerPokemonPriority == EnemyPokemonPriority: #if same priority hen check speed next
        PlayerPokemonSpeed = PlayerPokemon.Speed
        EnemyPokemonSpeed = EnemyPokemon.Speed

        if PlayerPokemonSpeed == EnemyPokemonSpeed: #if speed is the same then pick random to go first
            LuckyNumber = random.randint(0,1)
            if LuckyNumber == 1:
                HandleBattle("Player",Game,PlayerPokemon,PlayerAttack,EnemyPokemon)
            else:
                HandleBattle("Enemy",Game,PlayerPokemon,PlayerAttack,EnemyPokemon)

        elif PlayerPokemonSpeed > EnemyPokemonSpeed:
            HandleBattle("Player",Game,PlayerPokemon,PlayerAttack,EnemyPokemon)
        else:
            HandleBattle("Enemy",Game,PlayerPokemon,PlayerAttack,EnemyPokemon)

    elif PlayerPokemonPriority > EnemyPokemonPriority:
        HandleBattle("Player",Game,PlayerPokemon,PlayerAttack,EnemyPokemon)
    else:
        HandleBattle("Enemy",Game,PlayerPokemon,PlayerAttack,EnemyPokemon)