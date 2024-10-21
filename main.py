import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра: кликай по мишени')
icon = pygame.image.load('images/icon.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('images/target.png')
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

hits = 0
misses = 0

font = pygame.font.Font(None, 40)

running = True
while running:
    screen.fill('green')

    screen.blit(target_img, (target_x, target_y))

    hits_text = font.render(f'Попадания: {hits}', True, (255, 255, 255))
    misses_text = font.render(f'Промахи: {misses}', True, (255, 255, 255))
    screen.blit(hits_text, (20, SCREEN_HEIGHT - 50))
    screen.blit(misses_text, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                hits += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            else:
                misses += 1

    pygame.display.update()

pygame.quit()
