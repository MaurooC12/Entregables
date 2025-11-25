import tkinter as tk
import threading
import time
import random

# --- Configuración base ---
WIDTH = 800
HEIGHT = 300
GROUND_Y = 250
DINO_W = 40
DINO_H = 50

# --- Estado global ---
game_running = False
game_over = False
obstacles = []
trophy = None
timer_value = 0
OBSTACLE_SPEED = 6
GAME_DURATION = 60

# --- Tkinter setup ---
root = tk.Tk()
root.title("Juego del Dino")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# --- Dino ---
dino = None
dino_state = {"x": 80, "y": GROUND_Y - DINO_H, "vy": 0, "jumping": False, "crouching": False}

# --- UI ---
status_text = canvas.create_text(WIDTH // 2, HEIGHT // 2 - 40,
                                 text="Selecciona dificultad y presiona 'Iniciar'",
                                 font=("Consolas", 14), fill="#555")
info_text = canvas.create_text(10, 10, anchor="nw", text="", font=("Consolas", 12), fill="#333")

start_btn = tk.Button(root, text="Iniciar", font=("Consolas", 12))
restart_btn = tk.Button(root, text="Reiniciar", font=("Consolas", 12), state="disabled")

# --- Selector de dificultad ---
difficulty_var = tk.StringVar(value="easy")
tk.Radiobutton(root, text="Easy", variable=difficulty_var, value="easy").pack(side="left")
tk.Radiobutton(root, text="Medium", variable=difficulty_var, value="medium").pack(side="left")
tk.Radiobutton(root, text="Hard", variable=difficulty_var, value="hard").pack(side="left")

# --- Funciones ---
def create_dino():
    global dino
    dino = canvas.create_rectangle(dino_state["x"], dino_state["y"],
                                   dino_state["x"] + DINO_W, dino_state["y"] + DINO_H,
                                   fill="limegreen")

def reset_game():
    global game_running, game_over, obstacles, trophy, timer_value
    canvas.delete("all")
    obstacles.clear()
    trophy = None
    dino_state.update({"x": 80, "y": GROUND_Y - DINO_H, "vy": 0, "jumping": False, "crouching": False})
    game_running = False
    game_over = False
    create_dino()
    canvas.create_line(0, GROUND_Y, WIDTH, GROUND_Y, fill="#888", width=2)
    canvas.itemconfig(status_text, text="Selecciona dificultad y presiona 'Iniciar'", fill="#555")
    restart_btn.config(state="disabled")
    start_btn.config(state="normal")
    canvas.itemconfig(info_text, text="")

def start_game():
    global game_running, GAME_DURATION, timer_value, OBSTACLE_SPEED
    if game_running:
        return
    # Configurar dificultad
    level = difficulty_var.get()
    if level == "easy":
        GAME_DURATION = 60
        OBSTACLE_SPEED = 6
        spawn_delay = (2.0, 3.5)
    elif level == "medium":
        GAME_DURATION = 180
        OBSTACLE_SPEED = 6
        spawn_delay = (1.8, 3.2)
    else:  # hard
        GAME_DURATION = 300
        OBSTACLE_SPEED = 8
        spawn_delay = (1.2, 2.5)

    timer_value = GAME_DURATION
    game_running = True
    canvas.itemconfig(status_text, text="")
    start_btn.config(state="disabled")
    restart_btn.config(state="disabled")
    threading.Thread(target=generate_obstacles, args=(spawn_delay,), daemon=True).start()
    threading.Thread(target=game_timer, daemon=True).start()
    game_loop()

def end_game(msg="Game Over"):
    global game_running, game_over
    game_running = False
    game_over = True
    canvas.itemconfig(status_text, text=f"{msg}\nClic en 'Reiniciar' para jugar de nuevo", fill="red")
    restart_btn.config(state="normal")

def generate_obstacles(spawn_delay):
    while game_running:
        tipo = random.choice(["floor", "air", "tall"])
        if tipo == "floor":
            obs = canvas.create_rectangle(WIDTH, GROUND_Y - 40, WIDTH + 30, GROUND_Y, fill="red")
        elif tipo == "air":
            obs = canvas.create_rectangle(WIDTH, GROUND_Y - 70, WIDTH + 40, GROUND_Y - 40, fill="blue")
        else:
            obs = canvas.create_rectangle(WIDTH, GROUND_Y - 60, WIDTH + 35, GROUND_Y, fill="purple")
        obstacles.append(obs)
        time.sleep(random.uniform(*spawn_delay))

def game_timer():
    global timer_value, trophy
    while game_running and timer_value > 0:
        time.sleep(1)
        timer_value -= 1
    if game_running and timer_value <= 0:
        trophy = canvas.create_oval(WIDTH, GROUND_Y - 60, WIDTH + 40, GROUND_Y - 20, fill="gold")
        obstacles.append(("trophy", trophy))

def jump(event=None):
    if not dino_state["jumping"] and not dino_state["crouching"]:
        dino_state["jumping"] = True
        dino_state["vy"] = -12

def crouch(event=None):
    if not dino_state["jumping"]:
        dino_state["crouching"] = True
        canvas.coords(dino, dino_state["x"], dino_state["y"] + 20,
                      dino_state["x"] + DINO_W, dino_state["y"] + DINO_H)

def uncrouch(event=None):
    if dino_state["crouching"]:
        dino_state["crouching"] = False
        canvas.coords(dino, dino_state["x"], dino_state["y"],
                      dino_state["x"] + DINO_W, dino_state["y"] + DINO_H)

def update_dino():
    if dino_state["jumping"]:
        dino_state["vy"] += 0.8
        dino_state["y"] += dino_state["vy"]
        if dino_state["y"] >= GROUND_Y - DINO_H:
            dino_state["y"] = GROUND_Y - DINO_H
            dino_state["vy"] = 0
            dino_state["jumping"] = False
        canvas.coords(dino, dino_state["x"], dino_state["y"],
                      dino_state["x"] + DINO_W, dino_state["y"] + DINO_H)

def move_obstacles():
    for obs in obstacles[:]:
        if isinstance(obs, tuple):
            _, obj = obs
            canvas.move(obj, -OBSTACLE_SPEED, 0)
            coords = canvas.coords(obj)
            if coords[2] < 0:
                canvas.delete(obj)
                obstacles.remove(obs)
        else:
            canvas.move(obs, -OBSTACLE_SPEED, 0)
            coords = canvas.coords(obs)
            if coords[2] < 0:
                canvas.delete(obs)
                obstacles.remove(obs)

def check_collisions():
    dino_box = canvas.coords(dino)
    for obs in obstacles:
        if isinstance(obs, tuple):
            tipo, obj = obs
            obs_box = canvas.coords(obj)
            overlap = not (dino_box[2] < obs_box[0] or dino_box[0] > obs_box[2] or
                           dino_box[3] < obs_box[1] or dino_box[1] > obs_box[3])
            if overlap and tipo == "trophy":
                end_game("¡Winner! 🏆")
                return True
        else:
            obs_box = canvas.coords(obs)
            overlap = not (dino_box[2] < obs_box[0] or dino_box[0] > obs_box[2] or
                           dino_box[3] < obs_box[1] or dino_box[1] > obs_box[3])
            if overlap:
                end_game()
                return True
    return False

def update_info():
    canvas.itemconfig(info_text, text=f"Tiempo restante: {timer_value} segundos")

def game_loop():
    if not game_running:
        return
    update_dino()
    move_obstacles()
    update_info()
    if check_collisions():
        return
    root.after(16, game_loop)

# --- Eventos y botones ---
start_btn.config(command=start_game)
restart_btn.config(command=reset_game)
start_btn.pack(side="left", padx=10, pady=5)
restart_btn.pack(side="left", padx=10, pady=5)

root.bind("<space>", jump)
root.bind("<Down>", crouch)
root.bind("<Up>", uncrouch)

# --- Inicializar ---
reset_game()
root.mainloop()