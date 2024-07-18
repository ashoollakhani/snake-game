import pygame

# Screen dimensions
dis_width = 600
dis_height = 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
yellow = (255, 255, 102)
dark_blue = (50, 50, 255)
light_blue = (100, 100, 255)
dark_red = (255, 0, 0)
light_red = (255, 100, 100)
dark_yellow = (255, 255, 0)
light_yellow = (255, 255, 150)
dark_green = (0, 155, 0)
light_green = (100, 255, 100)

# Game settings
snake_block = 10
snake_speed = 15

# Initialize font
pygame.font.init()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
menu_font = pygame.font.SysFont("comicsansms", 50)

# Background gradient
background_gradient = (dark_blue, light_blue)
clock = pygame.time.Clock()
