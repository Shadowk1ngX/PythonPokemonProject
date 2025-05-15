import random
import Gui

def HandleBattle(Winner,Game,PlayerPokemon,PlayerAttack,EnemyPokemon,EnemyAttack): #Move atttack handling and death handling in pokemon class?
    if Winner == "Player":

        IsEnemyAlive = EnemyPokemon.TakeDamage(PlayerPokemon, PlayerAttack) #Enemy takes damage
        Gui.UpdateHealthBar(PlayerPokemon, EnemyPokemon)

        if not IsEnemyAlive:
            #print("Enemy Defeated!")
            return True
        
        IsPlayerAlive = PlayerPokemon.TakeDamage(EnemyPokemon, EnemyAttack)
        if not IsPlayerAlive:
            #print("Player Defeated!")
            return False

    else:

        IsPlayerAlive = PlayerPokemon.TakeDamage(EnemyPokemon, EnemyAttack) #Player takes damage
        Gui.UpdateHealthBar(PlayerPokemon, EnemyPokemon)
        if not IsPlayerAlive:
            #print("Player Defeated!")
            return False

        IsEnemyAlive = EnemyPokemon.TakeDamage(PlayerPokemon, PlayerAttack) 
        if not IsEnemyAlive:
            #print("Enemy Defeated!")
            return True
        

def HandlePlayerBattleWin(Game,PlayerPokemon,EnemyPokemon,GuiRemoveFunction):
    PlayerPokemon.CalculateExpReward(EnemyPokemon.BaseExp,EnemyPokemon.Level,PlayerPokemon.Level,is_trainer_battle = False)
    GuiRemoveFunction()

def HandlePlayerBattleLose(Game,PlayerPokemon,EnemyPokemon,GuiRemoveFunction):
    GuiRemoveFunction()

def HandleAttackTurn(Game,PlayerPokemon,PlayerAttack,PlayerHealthBar,PlayerHealthLabel,EnemyPokemon,EnemyHealthBar,EnemyHealthLabel,RemoveGuiFUnction):
    PlayerPokemonPriority = PlayerAttack.Priority
    EnemyAttack = random.choice(EnemyPokemon.Moves)()

    EnemyPokemonPriority = EnemyAttack.Priority

    if PlayerPokemonPriority == EnemyPokemonPriority: #if same priority hen check speed next
        PlayerPokemonSpeed = PlayerPokemon.Speed
        EnemyPokemonSpeed = EnemyPokemon.Speed

        if PlayerPokemonSpeed == EnemyPokemonSpeed: #if speed is the same then pick random to go first
            LuckyNumber = random.randint(0,1)
            if LuckyNumber == 1:
                BattleOutcome = HandleBattle("Player",Game,PlayerPokemon,PlayerAttack,EnemyPokemon,EnemyAttack)
            else:
               BattleOutcome = HandleBattle("Enemy",Game,PlayerPokemon,PlayerAttack,EnemyPokemon,EnemyAttack)
            
        elif PlayerPokemonSpeed > EnemyPokemonSpeed:
            BattleOutcome = HandleBattle("Player",Game,PlayerPokemon,PlayerAttack,EnemyPokemon,EnemyAttack)
        else:
           BattleOutcome = HandleBattle("Enemy",Game,PlayerPokemon,PlayerAttack,EnemyPokemon,EnemyAttack)

        if BattleOutcome == True:
            HandlePlayerBattleWin(Game,PlayerPokemon,EnemyPokemon,RemoveGuiFUnction)
        elif BattleOutcome == False:
            HandlePlayerBattleLose(Game,PlayerPokemon,EnemyPokemon,RemoveGuiFUnction)

    elif PlayerPokemonPriority > EnemyPokemonPriority:
        BattleOutcome = HandleBattle("Player",Game,PlayerPokemon,PlayerAttack,EnemyPokemon,EnemyAttack)
        if BattleOutcome == True:
            HandlePlayerBattleWin(Game,PlayerPokemon,EnemyPokemon,RemoveGuiFUnction)
        elif BattleOutcome == False:
            HandlePlayerBattleLose(Game,PlayerPokemon,EnemyPokemon,RemoveGuiFUnction)

    else:
        BattleOutcome = HandleBattle("Enemy",Game,PlayerPokemon,PlayerAttack,EnemyPokemon,EnemyAttack)
        if BattleOutcome == True:
            HandlePlayerBattleWin(Game,PlayerPokemon,EnemyPokemon,RemoveGuiFUnction)
        elif BattleOutcome == False:
            HandlePlayerBattleLose(Game,PlayerPokemon,EnemyPokemon,RemoveGuiFUnction)