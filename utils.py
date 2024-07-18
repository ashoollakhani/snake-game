import pygame
from constants import dis_width, dis_height, black, white, font_style, score_font, menu_font

def gradient_background(surface, color1, color2):
    """Create a gradient background from color1 to color2."""
    for y in range(dis_height):
        ratio = y / dis_height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (dis_width, y))

def draw_snake(dis, snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def draw_score(dis, score):
    value = score_font.render("Score: " + str(score), True, white)
    dis.blit(value, [dis_width / 2 - value.get_width() / 2, 0])

def message(dis, msg, color, y_displace=0):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2 - mesg.get_width() / 2, dis_height / 3 + y_displace])

def menu_message(dis, msg, color, y_displace=0):
    mesg = menu_font.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2 - mesg.get_width() / 2, dis_height / 3 + y_displace])
