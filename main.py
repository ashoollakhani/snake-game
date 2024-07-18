import pygame
import random
from settings import show_settings
from utils import gradient_background, menu_message, draw_snake, draw_score, message
from constants import dis_width, dis_height, background_gradient, green, white, yellow, red, black, snake_block, snake_speed, clock

# Initialize Pygame and font module
pygame.init()

# Create the game window
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

def game_loop(background_gradient):
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            gradient_background(dis, *background_gradient)
            message(dis, "You Lost! Press Q-Quit or C-Play Again", red, -50)
            draw_score(dis, Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop(background_gradient)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        gradient_background(dis, *background_gradient)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(dis, snake_block, snake_List)
        draw_score(dis, Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def game_menu(background_gradient):
    menu = True
    while menu:
        gradient_background(dis, *background_gradient)
        menu_message(dis, "Snake Game", green, -130)
        menu_message(dis, "1. Play", white, -20)
        menu_message(dis, "2. Settings", white, 30)
        menu_message(dis, "3. Quit", white, 80)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_loop(background_gradient)
                elif event.key == pygame.K_2:
                    background_gradient = show_settings(dis)
                elif event.key == pygame.K_4:
                    menu = False

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_menu(background_gradient)
