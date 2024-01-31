import pygame
import sys

pygame.init()

width, height = 640, 480
Red = (255, 0, 0)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")
Paddle_Width = 10
paddle_height = 100
paddle_x = 50
paddle_y = (height - paddle_height) // 2

paddle2_x = width - 50 - Paddle_Width
paddle2_y = (height - paddle_height) // 2
paddle_veloz1 = 0
paddle_veloz2 = 0
ball_size = 20
ball_x = width // 2
ball_y = height // 2
ball_veloz_x = 7
ball_veloz_y = 7
ponto1 = 0
ponto2 = 0
font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle_veloz1 = -7
            elif event.key == pygame.K_s:
                paddle_veloz1 = 7
            elif event.key == pygame.K_UP:
                paddle_veloz2 = -7
            elif event.key == pygame.K_DOWN:
                paddle_veloz2 = 7
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                paddle_veloz1 = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle_veloz2 = 0

    paddle_y += paddle_veloz1
    paddle2_y += paddle_veloz2
    paddle_y = max(min(paddle_y, height - paddle_height), 0)
    paddle2_y = max(min(paddle2_y, height - paddle_height), 0)

    ball_x += ball_veloz_x
    ball_y += ball_veloz_y

    if ball_y <= 0 or ball_y >= height - ball_size:
        ball_veloz_y = -ball_veloz_y

    if (ball_x <= paddle_x + Paddle_Width and paddle_y <= ball_y <= paddle_y + paddle_height) or \
       (ball_x >= paddle2_x - ball_size and paddle2_y <= ball_y <= paddle2_y + paddle_height):
        ball_veloz_x = -ball_veloz_x

    if ball_x <= 0:
        ponto2 += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_veloz_x = -ball_veloz_x
    elif ball_x >= width - ball_size:
        ponto1 += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_veloz_x = -ball_veloz_x

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, Red, (paddle_x, paddle_y, Paddle_Width, paddle_height))
    pygame.draw.rect(screen, Red, (paddle2_x, paddle2_y, Paddle_Width, paddle_height))
    pygame.draw.ellipse(screen, Red, (ball_x, ball_y, ball_size, ball_size))

    ponto_text = font.render(f"{ponto1} - {ponto2}", True, Red)
    screen.blit(ponto_text, (width // 2 - ponto_text.get_width() // 2, 20))

    pygame.display.flip()
    pygame.time.Clock().tick(60)
