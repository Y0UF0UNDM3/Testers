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

    # --- FIELDS (PLAYER STATS) ---
    player_rect = pygame.Rect(100, GROUND_Y - 50, 40, 50)
    vel_y = 0
    speed = 5
    jump_power = -13
    is_grounded = False
    
    # Scenery
    trees = [(random.randint(200, 1500), GROUND_Y) for _ in range(12)]

    # --- MUSIC SETUP ---
    # Put your "exploration_theme.ogg" in the same folder on GitHub!
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("exploration_theme.ogg")
        pygame.mixer.music.play(-1)
    except:
        print("Note: exploration_theme.ogg not found. Playing without music.")

    running = True
    while running:
        # 1. INPUT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player_rect.x -= speed
        if keys[pygame.K_RIGHT]: player_rect.x += speed
        if keys[pygame.K_SPACE] and is_grounded:
            vel_y = jump_power

        # 2. PHYSICS (GRAVITY)
        vel_y += GRAVITY
        player_rect.y += vel_y

        if player_rect.bottom >= GROUND_Y:
            player_rect.bottom = GROUND_Y
            vel_y = 0
            is_grounded = True
        else:
            is_grounded = False

        # 3. DRAWING
        screen.fill((135, 206, 235)) # Sky
        
        # Draw Grass & Soil
        pygame.draw.rect(screen, (34, 139, 34), (0, GROUND_Y, WIDTH, 20)) # Grass
        pygame.draw.rect(screen, (100, 65, 23), (0, GROUND_Y + 20, WIDTH, 60)) # Soil
        
        # Draw Trees
        for tx, ty in trees:
            pygame.draw.rect(screen, (80, 50, 20), (tx, ty - 40, 15, 40)) # Trunk
            pygame.draw.circle(screen, (20, 80, 20), (tx + 7, ty - 50), 30) # Leaves

        # Draw Player
        pygame.draw.rect(screen, (200, 30, 30), player_rect) 

        pygame.display.flip()
        
        # --- WEB REQUIREMENT ---
        # This prevents the browser tab from crashing
        await asyncio.sleep(0) 
        clock.tick(60)

asyncio.run(main())
