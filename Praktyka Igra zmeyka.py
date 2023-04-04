import pygame
import random


pygame.init()

# создание окна
screen_width = 500
screen_height = 500
game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake game')
game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True


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
        self.snake_list = [[x, y]]

    def draw(self):
        for block in self.snake_list:
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

        self.snake_list.append([self.x, self.y])

        if len(self.snake_list) > snake_length:
            del self.snake_list[0]
#11111111111111111
    def check_collision(self, apple):
        for block in self.snake_list[:-1]:
            if block == [self.x, self.y]:
                return True
     
        if self.x < 0 or self.x >= screen_width or self.y < 0 or self.y >= screen_height:
            return True
     
        if self.x == apple.x and self.y == apple.y:
            self.snake_list.append([self.x, self.y])
            return False
     
        return False
 
 
# Game Loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "left"
                x_change = -block_size
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                direction = "right"
                x_change = block_size
                y_change = 0
            elif event.key == pygame.K_UP:
                direction = "up"
                x_change = 0
                y_change = -block_size
            elif event.key == pygame.K_DOWN:
                direction = "down"
                x_change = 0
                y_change = block_size
 
    # Move the snake
    snake.move(x_change, y_change)
 
    # Check for collision
    game_over = snake.check_collision(apple)
 
    # Generate a new apple if the previous one was eaten
    if game_over == False:
        if apple.x == snake.x and apple.y == snake.y:
            apple.generate_new_location()
        pygame.display.update()
 
    # Draw the snake and apple
    draw_snake(snake)
    draw_apple(apple)
 
    # Update the display
    pygame.display.update()
 
    # Wait for a short amount of time before moving the snake again
    clock.tick(snake_speed)
 
# Quit the game
pygame.quit()
quit()
