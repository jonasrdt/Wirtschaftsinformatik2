import pygame
import os
from random import randrange, choice

os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 800, 800
FPS = 60

pygame.init()
screen = pygame.display.set_mode(RES)
pygame.display.set_caption("Christmas tree")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 30, bold=True)

ball_surface = pygame.image.load('/Users/jonasreinhardt/Desktop/_Desktop/Studium/_Module_FH/_SoSe_21/_Wirtschaftsinformatik-2a/Uebungen/Repo/Wirtschaftsinformatik2/WiSe-2122/Uebung-11/Gruppe-C/ball.png').convert_alpha()
ball_position = (150, 150)
ball_mask = pygame.mask.from_surface(ball_surface)

snowflake_surf = pygame.image.load('/Users/jonasreinhardt/Desktop/_Desktop/Studium/_Module_FH/_SoSe_21/_Wirtschaftsinformatik-2a/Uebungen/Repo/Wirtschaftsinformatik2/WiSe-2122/Uebung-11/Gruppe-C/snowflake.png').convert_alpha()
snowflake_overlay_surf = pygame.image.load('/Users/jonasreinhardt/Desktop/_Desktop/Studium/_Module_FH/_SoSe_21/_Wirtschaftsinformatik-2a/Uebungen/Repo/Wirtschaftsinformatik2/WiSe-2122/Uebung-11/Gruppe-C/snowflake.png').convert_alpha()

snowflakes = []

# Snowflakes
for _ in range(100):
    xs0 = randrange(0, WIDTH, 25)
    ys0 = randrange(0, HEIGHT, 15)
    snowflake_rect = snowflake_surf.get_rect(center=(xs0, ys0))
    snowflake_mask = pygame.mask.from_surface(snowflake_surf)
    snowflakes.append([snowflake_rect, snowflake_mask, xs0, ys0])


def text_display(x, y, char, color):
    text = font.render(str(char), True, color)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


tree = []
trunk = []

tree_height_temp = 14
tree_height = 14
tree_base = 19
dx, dy = 15, 25


def tree_generation(tree_base, tree_height_temp):
    x, y = 0, 0
    # Tree
    x0 = WIDTH // 2 - (tree_base * dx) / 2 + 5
    y0 = HEIGHT // 2 + (tree_height_temp * dy) / 2 - 50

    chars = ['0', '0', '0', '0', '1']
    while tree_height_temp != 0:
        for i in range(tree_height_temp):
            y = y0
            for j in range(tree_base):
                x = x0 + dx * j
                if i % 2 == 0:
                    char = choice(chars)
                else:
                    char = '0'
                tree.append((x, y, char))
            if tree_height_temp % 5 != 0:
                x0 += dx
                tree_base -= 2
            else:
                x0 -= dx
                tree_base += 2
            y0 -= dy
            tree_height_temp -= 1

    # Trunk
    xt0 = x - dx
    yt0 = y + tree_height * dy

    for _ in range(3):
        yt = yt0
        for j in range(3):
            xt = xt0 + dx * j
            trunk.append((xt, yt))
        yt0 += dy


k = 0
running = True
while running:
    clock.tick(FPS)
    screen.fill('black')

    pygame.draw.circle(screen, 'white', (WIDTH // 2, HEIGHT // 2), 255, 6)

    for i in tree:
        if i[2] == '0':
            color = 'green'
        else:
            color = 'red'
        text_display(i[0], i[1], i[2], color)

    for i in trunk:
        text_display(i[0], i[1], '0', 'yellow')

    for snowflake in snowflakes:
        snowflake_rect = snowflake[0]
        snowflake_mask = snowflake[1]

        snowflake_rect[1] += 1

        if snowflake_rect[1] > HEIGHT:
            snowflake_rect[0] = randrange(0, WIDTH, 25)
            snowflake_rect[1] = randrange(-50, 0, 15)

        offset_x = ball_position[0] - snowflake_rect.left
        offset_y = ball_position[1] - snowflake_rect.top
        if snowflake_mask.overlap(ball_mask, (offset_x, offset_y)):
            new_mask = snowflake_mask.overlap_mask(ball_mask, (offset_x, offset_y))
            new_surface = new_mask.to_surface()
            new_surface.set_colorkey('black')
            screen.blit(new_surface, snowflake_rect)

    if k == 0 or k == 20:
        tree = []
        trunk = []
        tree_generation(tree_base, tree_height_temp)
        k = 0

    pygame.display.update()
    k += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False