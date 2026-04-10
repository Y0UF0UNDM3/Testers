# main.py
import asyncio
import pygame
import random

# --- CONFIGURATION ---
WIDTH, HEIGHT = 800, 600
GROUND_Y = HEIGHT - 80
GRAVITY = 0.6

async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("GitHub Explorer")
    clock = pygame.time.Clock()

    # --- FIELDS ---
    player_rect = pygame.Rect(100, GROUND_Y - 50, 40, 50)
    vel_y, speed, jump_power = 0, 5, -13
    is_grounded = False
    trees = [(random.randint(100, 2000), GROUND_Y) for _ in range(15)]

    # --- MUSIC ---
    try:
        pygame.mixer.init()
        # MUST MATCH YOUR UPLOADED FILE NAME EXACTLY
        pygame.mixer.music.load("melodigne-symphony-of-legends-192455.ogg") 
        pygame.mixer.music.play(-1)
    except:
        print("Music file not found in repo.")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player_rect.x -= speed
        if keys[pygame.K_RIGHT]: player_rect.x += speed
        if keys[pygame.K_SPACE] and is_grounded: vel_y = jump_power

        vel_y += GRAVITY
        player_rect.y += vel_y

        if player_rect.bottom >= GROUND_Y:
            player_rect.bottom, vel_y, is_grounded = GROUND_Y, 0, True
        else:
            is_grounded = False

        screen.fill((135, 206, 235))
        pygame.draw.rect(screen, (34, 139, 34), (0, GROUND_Y, WIDTH, 80))
        for tx, ty in trees:
            pygame.draw.rect(screen, (80, 50, 20), (tx, ty - 40, 15, 40))
            pygame.draw.circle(screen, (20, 80, 20), (tx + 7, ty - 50), 30)
        pygame.draw.rect(screen, (200, 30, 30), player_rect) 

        pygame.display.flip()
        await asyncio.sleep(0) # Critical for web
        clock.tick(60)

asyncio.run(main())
