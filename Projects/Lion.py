import pygame
import sys
import random

pygame.init()
fps = 60
size_x = 800
size_y = 500
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 255, 0)
blue = (150, 150, 255)
blue_block_x = size_x / 2
blue_block_y = 400
size = [size_x, size_y]
red_blocks = []
green_blocks = []

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Hungry Lion')
clock = pygame.time.Clock()
arial = pygame.font.SysFont('Arial', 36)

for _ in range(50):
    red_block_x = random.randint(0, size_x)
    red_block_y = random.randint(-size_y / 2, size_y / 2)
    red_block = pygame.Rect((red_block_x, red_block_y, 20, 15))
    red_blocks.append((screen, red, red_block))

for _ in range(10):
    green_block_x = random.randint(0, size_x)
    green_block_y = random.randint(0, size_y / 2)
    green_block = pygame.Rect((green_block_x, green_block_y, 20, 15))
    green_blocks.append((screen, green, green_block))

dr = br = 0
dc = bc = 1
cnt = 0
score = 0
speed = 3

while True:

    blue_block = pygame.Rect(blue_block_x, blue_block_y, 15, 15)
    key_press = pygame.key.get_pressed()
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if key_press[pygame.K_UP]:
        blue_block_y -= speed
    if key_press[pygame.K_RIGHT]:
        blue_block_x += speed
    if key_press[pygame.K_DOWN]:
        blue_block_y += speed
    if key_press[pygame.K_LEFT]:
        blue_block_x -= speed

    for i in red_blocks:
        pygame.draw.rect(i[0], i[1], i[2])
        i[2][1] += 1
        if i[2][1] > size_y:
            i[2][1] = -20
        elif blue_block.colliderect(i[2]):
            i[2][1] = 10000
            i[2][0] = 10000
            score -= 1

    for i in green_blocks:
        pygame.draw.rect(i[0], i[1], i[2])
        if blue_block.colliderect(i[2]):
            cnt += 1
            score += 1
            i[2][1] = 10000
            i[2][0] = 10000
        else:
            i[2][1] += random.randint(-2, 2)
            i[2][0] += random.randint(-2, 2)

    if not (0 <= blue_block_y <= size_y or 0 <= blue_block_x <= size_x):
        speed = -speed

    text_score = arial.render(f"Score: {score}", 0, black)
    screen.blit(text_score, (20, 20)) 
    pygame.draw.rect(screen, blue, blue_block)
    clock.tick(fps)
    pygame.display.flip()