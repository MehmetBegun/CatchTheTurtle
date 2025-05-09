import turtle
import random

# ——— Pencere Ayarları ———
screen = turtle.Screen()
screen.title("Catch The Turtle")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# ——— Kaplumbağa ve Durum ———
t = turtle.Turtle("turtle")
t.penup()

score = 0
remaining_time = 30
game_over = False

# ——— Skor ve Sayaç ———
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(0, 260)

timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(0, 230)

def update_scoreboard():
    scoreboard.clear()
    scoreboard.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

def update_timer():
    timer_turtle.clear()
    timer_turtle.write(f"Time: {remaining_time}", align="center", font=("Arial", 24, "normal"))

def move_turtle():
    if game_over:
        return
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    screen.ontimer(move_turtle, 1000)

def catch_turtle(x, y):
    global score
    if game_over:
        return
    score += 1
    update_scoreboard()
    if score >= 10:
        win_game()

def countdown():
    global remaining_time
    if game_over:
        return
    if remaining_time <= 0:
        end_game()
    else:
        update_timer()
        remaining_time -= 1
        screen.ontimer(countdown, 1000)

def end_game():
    global game_over
    game_over = True
    # Kaplumbağayı gizle, ekranı bozmadan son skoru göster
    t.hideturtle()
    scoreboard.clear()
    timer_turtle.clear()
    scoreboard.goto(0, 0)
    scoreboard.write(f"Final Score: {score}", align="center",
                     font=("Arial", 36, "bold"))

def win_game():
    global game_over
    game_over = True
    t.hideturtle()
    scoreboard.clear()
    timer_turtle.clear()
    winner = turtle.Turtle()
    winner.hideturtle()
    winner.penup()
    winner.goto(0, 0)
    winner.write("You Won!", align="center",
                 font=("Arial", 48, "bold"))

# ——— Olayları Bağla ve Başlat ———
t.onclick(catch_turtle)
update_scoreboard()
update_timer()
move_turtle()
countdown()

screen.mainloop()