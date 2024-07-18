import pygame
from constants import white, light_blue, dark_blue, light_red, dark_red, light_yellow, dark_yellow, light_green, dark_green, dis_width, dis_height, menu_font
from utils import gradient_background, menu_message

def show_settings(screen):
    settings = True
    selected_gradient = (dark_blue, light_blue)
    while settings:
        gradient_background(screen, *selected_gradient)
        menu_message(screen, "Background Color", white, -100)
        menu_message(screen, "1. Blue", white, -40)
        menu_message(screen, "2. Red", white, 10)
        menu_message(screen, "3. Yellow", white, 60)
        menu_message(screen, "4. Green", white, 110)
        menu_message(screen, "5. Back to Menu", white, 150)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_gradient = (dark_blue, light_blue)
                elif event.key == pygame.K_2:
                    selected_gradient = (dark_red, light_red)
                elif event.key == pygame.K_3:
                    selected_gradient = (dark_yellow, light_yellow)
                elif event.key == pygame.K_4:
                    selected_gradient = (dark_green, light_green)
                elif event.key == pygame.K_5:
                    return selected_gradient
    return selected_gradient
