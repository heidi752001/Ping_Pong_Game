import pygame
from pygame import gfxdraw
import random

pygame.init()
display_info = pygame.display.Info()
screen_width, screen_height = display_info.current_w, display_info.current_h
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

bg_color = pygame.Color("#001219")
prop_color = pygame.Color("#fefae0")

ball_radius = 15
player_width, player_height = 10, 150

ball = pygame.Rect(screen_width//2-ball_radius, screen_height//2-ball_radius, ball_radius*2, ball_radius*2)
player1 = pygame.Rect(0, screen_height//2-player_height//2, player_width, player_height)
player2 = pygame.Rect(screen_width-player_width, screen_height//2-player_height//2, player_width, player_height)

ball_speed_x, ball_speed_y = 5, 5
player_speed = 5
player1_delta, player2_delta = 0, 0
player1_score, player2_score = 0, 0

clock = pygame.time.Clock()
font = pygame.font.SysFont("inkfree", 35)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player1_delta = player_speed
            if event.key == pygame.K_w:
                player1_delta = -player_speed
            if event.key == pygame.K_DOWN:
                player2_delta = player_speed
            if event.key == pygame.K_UP:
                player2_delta = -player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s or event.key == pygame.K_w:
                player1_delta = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player2_delta = 0
    
    player1.y += player1_delta
    player2.y += player2_delta
    player1.top = max(0, player1.top)
    player2.top = max(0, player2.top)
    player1.bottom = min(screen_height, player1.bottom)
    player2.bottom = min(screen_height, player2.bottom)

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        if ball.left <= 0: player2_score += 1
        else: player1_score += 1
        ball.center = (screen_width//2, screen_height//2)
        ball_speed_x *= random.choice([-1, 1])
        ball_speed_y *= random.choice([-1, 1])
    
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    screen.fill(bg_color)
    player1_text = font.render('Player 1: {}'.format(player1_score), True, prop_color)
    player1_text_rect = player1_text.get_rect()
    player1_text_rect.center = (screen_width//4, 20)
    screen.blit(player1_text, player1_text_rect)
    player2_text = font.render('Player 2: {}'.format(player2_score), True, prop_color)
    player2_text_rect = player2_text.get_rect()
    player2_text_rect.center = (screen_width-screen_width//4, 20)
    screen.blit(player2_text, player2_text_rect)
    pygame.draw.aaline(screen, prop_color, (screen_width//2, 0), (screen_width//2, screen_height))
    gfxdraw.aacircle(screen, screen_width//2, screen_height//2, 200, prop_color)
    pygame.draw.rect(screen, prop_color, player1)
    pygame.draw.rect(screen, prop_color, player2)
    gfxdraw.filled_circle(screen, ball.centerx, ball.centery, ball_radius, prop_color)
    pygame.display.update()
    clock.tick(60)