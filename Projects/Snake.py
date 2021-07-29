import pygame
import sys
import random

pygame.init()

runing = True
size_block = 20
count_block_r, count_block_c = 32, 46
screen_color = (0, 250, 200)
white = (255, 255, 255)
blue = (200, 255, 255)
red = (255, 0, 0)
head_color = (0, 200,150)
snake_color = (0, 100, 0)
head_margin = 70
margin = 1
size_x, size_y = [size_block * count_block_c + 2 * size_block + margin * count_block_c,
        size_block * count_block_r + 2 * size_block + margin * count_block_r + head_margin]
size = [size_block * count_block_c + 2 * size_block + margin * count_block_c,
        size_block * count_block_r + 2 * size_block + margin * count_block_r + head_margin]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
arial = pygame.font.SysFont('Arial', 36)
b_arial = pygame.font.SysFont('Arial', 80)

class snakeblock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < count_block_r and 0 <= self.y < count_block_c
    
    def __eq__(self, other):
        return isinstance(other, snakeblock) and self.x == other.x and self.y == other.y

def draw_block(color, r, c):
    pygame.draw.rect(screen, color, [size_block + c * size_block + margin * (c + 1),
                                             head_margin + size_block + r * size_block + margin * (r + 1),
                                             size_block, size_block])

def get_random_empty_block():
        x = random.randint(0, count_block_r - 1)
        y = random.randint(0, count_block_c - 1)
        empty_block = snakeblock(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, count_block_r - 1)
            empty_block.y = random.randint(0, count_block_c - 1)
        return empty_block

def menu_game(runing, score):
    while not runing:
        screen.fill(screen_color)
        game_over = b_arial.render('GAME OVER', 1, red)
        result_game = arial.render(f'Your Score: {score}', True, white)
        quit_game = arial.render('Press Q to Quit or exit', True, white)

        screen.blit(game_over, (size_x / 2 - 200, size_y / 2 - 100))
        screen.blit(result_game, (size_x / 2 - 100, size_y / 2))
        screen.blit(quit_game, (size_x / 2 - 150, size_y / 2 + 60))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                if event.key == pygame.K_q or event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()            

snake_blocks = [snakeblock(15, 22), snakeblock(15, 23), snakeblock(15, 24)]
apple = get_random_empty_block()
dr = br = 0
dc = bc = 1
score = 0
speed = 1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dc != 0:
                br = -1
                bc = 0
            elif event.key == pygame.K_RIGHT and dr != 0:
                br = 0
                bc = 1
            elif event.key == pygame.K_DOWN and dc != 0:
                br = 1
                bc = 0
            elif event.key == pygame.K_LEFT and dr != 0:
                br = 0
                bc = -1
    
    screen.fill(screen_color)
    pygame.draw.rect(screen, head_color, [0, 0, size[0], head_margin])
    text_score = arial.render(f"Score: {score}", 0, white)
    text_speed = arial.render(f"Speed: {speed}", 0, white)
    screen.blit(text_score, (size_block, size_block))
    screen.blit(text_speed, (size_block + 300, size_block))

    for r in range(count_block_r):
        for c in range(count_block_c):
            color = blue if (c + r) % 2 == 0 else white
            draw_block(color, r, c)

    head = snake_blocks[-1]
    if not head.is_inside():
        runing = False
        menu_game(runing, score)

    draw_block(red, apple.x, apple.y)
    for block in snake_blocks:   
        draw_block(snake_color, block.x, block.y)

    if apple == head:
        speed = score // 5 + 1
        score += 1
        snake_blocks.append(apple)
        apple = get_random_empty_block()  

    dr = br
    dc = bc
    new_head = snakeblock(head.x + dr, head.y + dc)

    if new_head in snake_blocks:
        runing = False
        menu_game(runing, score)
        
    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    pygame.display.flip()
    clock.tick(10 + speed)
