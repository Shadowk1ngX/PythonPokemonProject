import tkinter as tk
from tkinter import ttk
import random
import PokemonData
import PokemonBattleHandler as BattleHandler

Inbattle = False
PlayerHealthBar = ""
PlayerHealthLabel = ""
EnemyHealthBar = ""
EnemyHealthLabel = ""

def UpdateHealthBar(PlayerPokemon,EnemyPokemon):
    PlayerPokemon.Health = max(0, PlayerPokemon.Health)
    PlayerHealthBar["value"] = PlayerPokemon.Health
    PlayerHealthLabel.config(text=f"HP: {PlayerPokemon.Health}/{PlayerPokemon.MaxHealth}")

    EnemyPokemon.Health = max(0, EnemyPokemon.Health)
    EnemyHealthBar["value"] = EnemyPokemon.Health
    EnemyHealthLabel.config(text=f"HP: {EnemyPokemon.Health}/{EnemyPokemon.MaxHealth}")


def StartMain(Game):
    TILE_SIZE = 50
    MAP_WIDTH = 10
    MAP_HEIGHT = 10
    player_pos = [5, 5]

    root = tk.Tk()
    canvas = tk.Canvas(root, width=TILE_SIZE * MAP_WIDTH, height=TILE_SIZE * MAP_HEIGHT)
    canvas.pack()

    # Bring game window to front temporarily
    root.attributes("-topmost", True)
    root.after(100, lambda: root.attributes("-topmost", False))
    root.resizable(False, False)
    

    # Load image sprites
    grass_img = tk.PhotoImage(file="Assets/Images/SmallGrass.png")     # 50x50 sprite
    player_img = tk.PhotoImage(file="Assets/Images/Player.png")        # 50x50 sprite

    # Prevent garbage collection
    canvas.grass_img = grass_img
    canvas.player_img = player_img

    tile_map = [["G" for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

    def draw_map():
        canvas.delete("all")
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                canvas.create_image(x * TILE_SIZE, y * TILE_SIZE, image=grass_img, anchor="nw")
        canvas.create_image(player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE, image=player_img, anchor="nw")

    def CheckInteraction():
        tile = tile_map[player_pos[1]][player_pos[0]]
        if tile == "G" and not Inbattle:
            if random.random() < 0.1:
                StartPokemonBattleGui(Game)

    def move(event):
        global Inbattle
        if Inbattle:
            return
        if event.keysym == "Up" and player_pos[1] > 0:
            player_pos[1] -= 1
        elif event.keysym == "Down" and player_pos[1] < MAP_HEIGHT - 1:
            player_pos[1] += 1
        elif event.keysym == "Left" and player_pos[0] > 0:
            player_pos[0] -= 1
        elif event.keysym == "Right" and player_pos[0] < MAP_WIDTH - 1:
            player_pos[0] += 1
        draw_map()
        CheckInteraction()

    root.bind("<KeyPress>", move)
    draw_map()
    root.mainloop()

def StartPokemonBattleGui(Game):
    global Inbattle
    Inbattle = True

    battle_win = tk.Toplevel()
    battle_win.title("Pokémon Battle")
    battle_win.geometry("400x400")
    battle_win.resizable(False, False)
    battle_win.attributes("-topmost", True)

    def disable_close_warning():
        popup = tk.Toplevel()
        popup.attributes("-topmost", True)
        popup.title("Cannot Exit")
        tk.Label(popup, text="You can't leave a battle like that!", padx=20, pady=10).pack()
        tk.Button(popup, text="OK", command=popup.destroy).pack(pady=10)

    battle_win.protocol("WM_DELETE_WINDOW", disable_close_warning)

    top_frame = tk.Frame(battle_win)
    top_frame.pack(pady=10)

    # Get enemy
    PickedEnemyPokemon = random.choice(PokemonData.PokemonList)
    EnemyPokemon = PickedEnemyPokemon()
    EnemyName = EnemyPokemon.Name

    Player = Game.Player
    PlayerPokemon = Player.PlayerInventory.EquippedPokemon
    

    opponent_name = tk.Label(top_frame, text=f"🌿 Wild {EnemyName}", font=("Arial", 12, "bold"))
    #opponent_name.pack()
    opponent_name.grid(row=0, column=1, sticky="w")
    enemy_health_label = tk.Label(top_frame, text=f"HP: {EnemyPokemon.Health}/{EnemyPokemon.MaxHealth}")
    enemy_health_label.grid(row=1, column=1, sticky="w")
    enemy_health_bar = ttk.Progressbar(top_frame, length=200, maximum=EnemyPokemon.MaxHealth)
    enemy_health_bar.grid(row=2, column=1, pady=(0, 10))
    enemy_health_bar["value"] = EnemyPokemon.Health

    player_name = tk.Label(top_frame, text=f"🔥 You sent out {PlayerPokemon.Name}!", font=("Arial", 12))
    #player_name.pack()
    player_name.grid(row=0, column=0, sticky="e")
    player_health_label = tk.Label(top_frame, text=f"HP: {PlayerPokemon.Health}/{PlayerPokemon.MaxHealth}")
    player_health_label.grid(row=1, column=0, sticky="e")
    player_health_bar = ttk.Progressbar(top_frame, length=200, maximum=PlayerPokemon.MaxHealth)
    player_health_bar.grid(row=2, column=0, pady=(0, 10))
    player_health_bar["value"] = PlayerPokemon.Health

    global PlayerHealthBar
    global PlayerHealthLabel
    PlayerHealthBar = player_health_bar
    PlayerHealthLabel = player_health_label

    global EnemyHealthBar
    global EnemyHealthLabel

    EnemyHealthBar = enemy_health_bar
    EnemyHealthLabel = enemy_health_label


    battle_log = tk.Text(battle_win, height=8, width=45, state="disabled", bg="#f4f4f4")
    battle_log.pack(pady=10)

    def log(text):
        battle_log.config(state="normal")
        battle_log.insert(tk.END, text + "\n")
        battle_log.see(tk.END)
        battle_log.config(state="disabled")

    # === Button Frames ===
    btn_frame = tk.Frame(battle_win)  # TEMP: red for visibility
    move_frame = tk.Frame(battle_win)  # TEMP: blue for visibility

    btn_frame.pack(pady=5)
    move_frame.pack(pady=5)

    def on_bag():
        log("You looked in your bag. It's empty!")

    def on_run():
        log("You ran away safely.")
        global Inbattle
        Inbattle = False
        battle_win.after(1000, battle_win.destroy)

    def on_wild_win():
        log(f"You defeated a wild {EnemyName}!.") #Add exp awarded
        global Inbattle
        Inbattle = False
        battle_win.after(1000, battle_win.destroy)

    # === Button Actions ===
    def on_fight():
        btn_frame.pack_forget()
        for widget in move_frame.winfo_children():
            widget.destroy()

        #log("Choose a move:")

        moves = PlayerPokemon.Moves

        def make_move_command(move): # Get speed
            def action():
                #log(f"{PlayerPokemon.Name} used {move.Name}!")
                for widget in move_frame.winfo_children():
                    widget.destroy()
                
                btn_frame.pack_forget()
                btn_frame.pack(pady=5, before=move_frame)
                battle_win.update_idletasks()

                BattleHandler.HandleAttackTurn(Game,PlayerPokemon,move,player_health_bar,player_health_label,EnemyPokemon,enemy_health_bar,enemy_health_label, on_wild_win)

            return action
        
        def return_to_defualt_Menu():
            def action():
                for widget in move_frame.winfo_children():
                    widget.destroy()
                
                btn_frame.pack_forget()
                btn_frame.pack(pady=5, before=move_frame)
                battle_win.update_idletasks()

            return action
        
        MoveInfoTracker = 0
        for i, move in enumerate(moves):
            move = move()
            btn = tk.Button(move_frame, text=move.Name, width=15, command=make_move_command(move))
            btn.grid(row=i // 2, column=i % 2, padx=5, pady=3)
            MoveInfoTracker = i + 1

        btn = tk.Button(move_frame, text="Back", width=15, command=return_to_defualt_Menu())
        btn.grid(row=MoveInfoTracker // 2, column=MoveInfoTracker % 2, padx=5, pady=3)



    

    # === Main Buttons ===
    tk.Button(btn_frame, text="Fight", width=10, command=on_fight).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(btn_frame, text="Bag", width=10, command=on_bag).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(btn_frame, text="Run", width=10, command=on_run).grid(row=0, column=2, padx=5, pady=5)

    log(f"A wild {EnemyName} appeared!")
    log("Go! Bulbasaur!")