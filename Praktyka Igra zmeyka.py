import pygame
import random
import time


pygame.init()

# создание окна
screen_width = 500
screen_height = 500
game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake game')

# цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

# фоновый цвет
bg_color = white

# размер блока
block_size = 10

# настройки змейки
snake_speed = 15




class Snake:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.direction = "right"
        self.update_snake_position = []

    def draw(self):
        for block in self.update_snake_position:
            pygame.draw.rect(game_display, black, [block[0], block[1], self.size, self.size])

    def update(self):
        if self.direction == "right":
            self.x += self.size
        elif self.direction == "left":
            self.x -= self.size
        elif self.direction == "up":
            self.y -= self.size
        elif self.direction == "down":
            self.y += self.size

        self.update_snake_position.append([self.x, self.y])

        if len(self.update_snake_position) > snake_length:
            del self.update_snake_position[0]

    def check_collision(self):
        for block in self.update_snake_position[:-1]:
            if block == [self.x, self.y]:
                return True
        if self.x >= screen_width or self.x < 0 or self.y >= screen_height or self.y < 0:
            return True
        return False

class Apple:
    def __init__(self, size):
        self.size = size
        self.x = round(random.randrange(0, screen_width - self.size) / 10.0) * 10.0
        self.y = round(random.randrange(0, screen_height - self.size) / 10.0) * 10.0

    def draw(self):
        pygame.draw.rect(game_display, red, [self.x, self.y, self.size, self.size])

    def update(self):
        self.x = round(random.randrange(0, screen_width - self.size) / 10.0) * 10.0
        self.y = round(random.randrange(0, screen_height - self.size) / 10.0) * 10.0


def score_system(score):
    value = pygame.font.SysFont("arial", 25).render("Score: " + str(score), True, black)
    game_display.blit(value, [0, 0])

# инициализация змейки и яблока
snake_length = 1
snake = Snake(0, 0, block_size)
apple = Apple(block_size)

# основной игровой цикл
game_over = False
game_close = False

while not game_over:

    while game_close == True:
        game_display.fill(bg_color)
        message = pygame.font.SysFont("arial", 30).render("You lost! Press Q to Quit or C to Play Again", True, black)
        message_rect = message.get_rect()
        message_rect.center = (screen_width / 2, screen_height / 2)
        game_display.blit(message_surface, message_rect)

        pygame.display.update()

        # Задержка перед завершением программы
        pygame.time.wait(3000)

        # Закрываем окно игры и завершаем работу Pygame
        pygame.quit()
        quit()

# Основной игровой цикл
game_exit = False
while not game_exit:
# тело цикла
    while not game_exit:

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            # Обработка нажатий клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")
                elif event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")

        # Рисуем фон
        game_display.fill(bg_color)

        # Рисуем яблоко
        apple.draw(game_display)

        # Обновляем змею
        snake.update()

        # Проверяем столкновение змеи с яблоком
        if snake.check_collision(apple):
            apple.move()
            snake.grow()
            score += 10

        # Рисуем змею
        snake.draw(game_display)

        # Рисуем счетчик очков
        score_surface = font.render("Score: " + str(score), True, font_color)
        game_display.blit(score_surface, (10, 10))

        # Обновляем экран
        pygame.display.update()

        # Устанавливаем задержку
        clock.tick(10)

    # Закрываем окно игры и завершаем работу Pygame
    pygame.quit()
    quit()

# Запускаем игру
game_loop()

