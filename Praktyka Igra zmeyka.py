import tkinter as tk
import random

MOVE_INCREMENT = 10
MOVES_PER_SECOND = 8
GAME_SPEED = 1000 // MOVES_PER_SECOND

WIDTH = 500
HEIGHT = 500


def start_game():
    global snake, apple, score
    score = 0

# Создаем змею и яблоко
snake = Snake()
apple = Apple()

# Главный игровой цикл
def main():
    global score
    # Проверяем, не столкнулась ли змея с препятствием или с собственным телом
    if snake.check_collision() == True:
        messagebox.showinfo("Game Over", f"Your score is {score}")
        answer = messagebox.askquestion("Game Over", "Do you want to play again?")
        if answer == "yes":
            # Если пользователь хочет начать новую игру, перезагружаем игру
            snake.restart()
            apple.new_position()
            main()
        else:
            # Если пользователь не хочет играть, закрываем окно
            root.destroy()
    else:
        # Если змея не столкнулась с препятствием или с собственным телом, продолжаем игру
        snake.move()
        if snake.eat_apple(apple):
            # Если змея съела яблоко, обновляем позицию яблока и увеличиваем счет
            apple.new_position()
            score += 1
            score_label.config(text="Score: " + str(score))
        canvas.delete("all")
        snake.draw(canvas)
        apple.draw(canvas)
        root.after(100, main)

# Обработка нажатий клавиш
def on_key_press(event):
    snake.change_direction(event.keysym)

# Создание окна и элементов управления
root = tk.Tk()
root.title("Snake")
root.resizable(False, False)

canvas = tk.Canvas(root, width=500, height=500, bg="#003300")
canvas.pack()

score_label = tk.Label(root, text="Score: " + str(score), font=("Arial", 16))
score_label.pack()

reset_button = tk.Button(root, text="Reset Score", font=("Arial", 16), command=reset_score)
reset_button.pack()

start_button = tk.Button(root, text="Start Game", font=("Arial", 16), command=main)
start_button.pack()

# Привязка обработчика событий к клавиатуре
root.bind("<KeyPress>", on_key_press)

root.mainloop()

