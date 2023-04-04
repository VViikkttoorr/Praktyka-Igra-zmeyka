from tkinter import *
import random
# Ширина экрана
WIDTH = 800
# Высота экрана
HEIGHT = 600
# Размер сегмента змеи
SEG_SIZE = 20
# Переменная, отвечающая за состояние игры
IN_GAME = True
# Вспомогательная функция
def create_block():
 """ Создаем еду для змейки """
 global BLOCK
 posx = SEG_SIZE * random.randint(1, (WIDTH - SEG_SIZE) / SEG_SIZE)
 posy = SEG_SIZE * random.randint(1, (HEIGHT - SEG_SIZE) / SEG_SIZE)
 BLOCK = c.create_oval(posx, posy,
 posx + SEG_SIZE, posy + SEG_SIZE,
 fill="green")
# Функция для управления игровым процессом
def main():
 """ Моделируем игровой процесс """
 global IN_GAME
 if IN_GAME:
 s.move()
 # Определяем координаты головы
 head_coords = c.coords(s.segments[-1].instance)
 x1, y1, x2, y2 = head_coords
 # столкновения с краями игрового поля
 if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
 IN_GAME = False
 # Поедание яблока
 elif head_coords == c.coords(BLOCK):
 s.add_segment()
 c.delete(BLOCK)
 create_block()
 # Поедание змейки
 else:
 for index in range(len(s.segments) - 1):
 if head_coords == c.coords(s.segments[index].instance):
 IN_GAME = False
 # скорость змейки
 root.after(100, main)
 # Не IN_GAME -> останавливаем игру и выводим сообщения
 else:
 set_state(game_over_text, 'normal')

class Segment(object):
 """ Сегмент змейки """
 def __init__(self, x, y):
 self.instance = c.create_rectangle(x, y,
 x + SEG_SIZE, y + SEG_SIZE,
 fill="green")

class Snake(object):
 """ Класс змейки """
 def __init__(self, segments):
 self.segments = segments
 # Варианты движения
 self.mapping = {"Down": (0, 1), "Right": (1, 0),
 "Up": (0, -1), "Left": (-1, 0)}
 # инициируем направление движения
 self.vector = self.mapping["Right"]
 def move(self):
 """ Двигаем змейку в заданном направлении """
 for index in range(len(self.segments) - 1):
 segment = self.segments[index].instance
 x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
 c.coords(segment, x1, y1, x2, y2)
 x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
 c.coords(self.segments[-1].instance,
 x1 + self.vector[0] * SEG_SIZE, y1 + self.vector[1] * SEG_SIZE,
 x2 + self.vector[0] * SEG_SIZE, y2 + self.vector[1] * SEG_SIZE)
 def add_segment(self):
 """ Добавляем сегмент змейки """
 last_seg = c.coords(self.segments[0].instance)
 x = last_seg[2] - SEG_SIZE
 y = last_seg[3] - SEG_SIZE
 self.segments.insert(0, Segment(x, y))
 def change_direction(self, event):
 """ Изменение направления движения змейки """
 if event.keysym in self.mapping:
 self.vector = self.mapping[event.keysym]
 # Функция обновления змейки при старте новой игры
 def reset_snake(self):
 for segment in self.segments:
 c.delete(segment.instance)
# функция для вывода сообщения
def set_state(item, state):
 c.itemconfigure(item, state=state)
 c.itemconfigure(BLOCK, state='hidden')
# Функция для старта игры
def start_game():
 global s
 create_block()
 s = create_snake()
 # Реагируем на нажатие клавиш
 c.bind("<KeyPress>", s.change_direction)
 main()
# Создаем сегменты и змейку
def create_snake():
 segments = [Segment(SEG_SIZE, SEG_SIZE),
 Segment(SEG_SIZE * 2, SEG_SIZE),
 Segment(SEG_SIZE * 3, SEG_SIZE)]
 return Snake(segments)

# Настройка главного окна
root = Tk()
root.title("Змейка")
# Создаем экземпляр класса Canvas
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#000000")
c.grid()
# Захватываем фокус для отлавливания нажатий клавиш
c.focus_set()
# Текст результата игры
game_over_text = c.create_text(WIDTH / 2, HEIGHT / 2, text="Игра окончена!",
 font='Arial 20', fill='red', state='hidden')

# Запускаем игру
start_game()
# запускаем окно
root.mainloop()
