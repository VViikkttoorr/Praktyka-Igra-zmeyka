import pygame
import time
import random

pygame.init()

# цвета, используемые в игре
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# ширина и высота экрана
width = 600
height = 400

# создаем окно
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game by VViikkttoorr')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 30)


def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])


# рисуем змейку
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


# выводим сообщение на экран
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])


# класс, описывающий яблоко
class Apple:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.new_position()

    def draw(self):
        pygame.draw.rect(dis, red, [self.x, self.y, snake_block, snake_block])

    def new_position(self):
        self.x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0


# функция, реализующая саму игру
def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1

    # создаем первое яблоко
    apple = Apple()
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # обрабатываем нажатия клавиш
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # проверяем, не вышла ли змейка за границы экрана
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # обновляем координаты головы змейки
        x1 += x1_change
        y1 += y1_change

        # проверяем, не столкнулась ли змейка с собой
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        # проверяем, не съела ли змейка яблоко
        if x1 == apple.x and y1 == apple.y:
            apple.new_position()
            Length_of_snake += 1

        # рисуем змейку и яблоко
        dis.fill(blue)
        apple.draw()
        our_snake(snake_block, snake_list)
        Your_score(Length_of_snake - 1)

        # обновляем экран
        pygame.display.update()

        # ограничиваем скорость змейки
        clock.tick(snake_speed)

    # завершаем игру и выходим из Pygame
    pygame.quit()
    quit()

gameLoop()
