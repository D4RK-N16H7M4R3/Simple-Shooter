import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colorsimport pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Shooter")

# Load images
player_img = pygame.image.load('ship.jpg')
bullet_img = pygame.image.load('bullet.jpg')

# Scale images
player_width = 50
player_height = 50
player_img = pygame.transform.scale(player_img, (player_width, player_height))
bullet_width = 5
bullet_height = 20
bullet_img = pygame.transform.scale(bullet_img, (bullet_width, bullet_height))

# Player variables
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 5

# Enemy variables
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemies = []

# Bullet variables
bullet_speed = 7
bullets = []

# Power-up variables
powerup_width = 30
powerup_height = 30
powerup_speed = 5
powerups = []

# Score
score = 0
missed_enemies = 0
font = pygame.font.Font(None, 36)

def spawn_enemy():
    enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
    enemy_y = -enemy_height
    enemies.append([enemy_x, enemy_y])

def spawn_powerup():
    powerup_x = random.randint(0, SCREEN_WIDTH - powerup_width)
    powerup_y = -powerup_height
    powerups.append([powerup_x, powerup_y])

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def check_collision(rect1, rect2):
    return (
        rect1[0] < rect2[0] + rect2[2] and
        rect1[0] + rect1[2] > rect2[0] and
        rect1[1] < rect2[1] + rect2[3] and
        rect1[1] + rect1[3] > rect2[1]
    )

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullets.append([bullet_x, bullet_y])

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # Spawn enemies randomly
    if random.randint(1, 100) == 1:
        spawn_enemy()

    # Move and draw enemies
    for enemy in enemies[:]:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))
        enemy[1] += enemy_speed

        # Collision with player
        if check_collision([player_x, player_y, player_width, player_height], [enemy[0], enemy[1], enemy_width, enemy_height]):
            running = False  # End game if enemy collides with player

        # Remove enemies if they go off screen and increment missed counter
        if enemy[1] > SCREEN_HEIGHT:
            enemies.remove(enemy)
            missed_enemies += 1
            if missed_enemies > 5:
                running = False  # End game if more than 5 enemies are missed

    # Spawn power-ups randomly
    if random.randint(1, 1000) == 1:
        spawn_powerup()

    # Move and draw power-ups
    for powerup in powerups[:]:
        pygame.draw.rect(screen, WHITE, (powerup[0], powerup[1], powerup_width, powerup_height))
        powerup[1] += powerup_speed

        # Collision with player for power-ups (example)
        if check_collision([player_x, player_y, player_width, player_height], [powerup[0], powerup[1], powerup_width, powerup_height]):
            powerups.remove(powerup)
            # Implement power-up effect here (example)

        # Remove power-ups if they go off screen
        if powerup[1] > SCREEN_HEIGHT:
            powerups.remove(powerup)

    # Move and draw bullets
    for bullet in bullets[:]:
        screen.blit(bullet_img, (bullet[0], bullet[1]))
        bullet[1] -= bullet_speed

        # Remove bullets if they go off screen
        if bullet[1] < 0:
            bullets.remove(bullet)

        # Check for collision with enemies
        for enemy in enemies[:]:
            if check_collision([bullet[0], bullet[1], bullet_width, bullet_height], [enemy[0], enemy[1], enemy_width, enemy_height]):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Display score
    draw_text(f"Score: {score}", font, WHITE, screen, 10, 10)
    draw_text(f"Missed: {missed_enemies}", font, WHITE, screen, 10, 50)

    # Update display
    pygame.display.update()
    clock.tick(60)

# Quit Pygame
pygame.quit()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Shooter")

# Load images
player_img = pygame.image.load('ship.jpg')
bullet_img = pygame.image.load('bullet.jpg')

# Scale images
player_width = 50
player_height = 50
player_img = pygame.transform.scale(player_img, (player_width, player_height))
bullet_width = 5
bullet_height = 20
bullet_img = pygame.transform.scale(bullet_img, (bullet_width, bullet_height))

# Player variables
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 5

# Enemy variables
enemy_width = 50
enemy_height = 50
enemy_speed = 2
enemies = []

# Bullet variables
bullet_speed = 7
bullets = []

# Power-up variables
powerup_width = 30
powerup_height = 30
powerup_speed = 5
powerups = []

# Score
score = 0
font = pygame.font.Font(None, 36)

def spawn_enemy():
    enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
    enemy_y = -enemy_height
    enemies.append([enemy_x, enemy_y])

def spawn_powerup():
    powerup_x = random.randint(0, SCREEN_WIDTH - powerup_width)
    powerup_y = -powerup_height
    powerups.append([powerup_x, powerup_y])

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullets.append([bullet_x, bullet_y])

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # Spawn enemies randomly
    if random.randint(1, 100) == 1:
        spawn_enemy()

    # Move and draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))
        enemy[1] += enemy_speed

        # Collision with player
        if (enemy[1] + enemy_height) > player_y and enemy[0] > player_x and enemy[0] < (player_x + player_width):
            enemies.remove(enemy)
            score += 1

        # Remove enemies if they go off screen
        if enemy[1] > SCREEN_HEIGHT:
            enemies.remove(enemy)

    # Spawn power-ups randomly
    if random.randint(1, 1000) == 1:
        spawn_powerup()

    # Move and draw power-ups
    for powerup in powerups:
        pygame.draw.rect(screen, WHITE, (powerup[0], powerup[1], powerup_width, powerup_height))
        powerup[1] += powerup_speed

        # Collision with player for power-ups (example)
        if (powerup[1] + powerup_height) > player_y and powerup[0] > player_x and powerup[0] < (player_x + player_width):
            powerups.remove(powerup)
            # Implement power-up effect here (example)

        # Remove power-ups if they go off screen
        if powerup[1] > SCREEN_HEIGHT:
            powerups.remove(powerup)

    # Move and draw bullets
    for bullet in bullets:
        screen.blit(bullet_img, (bullet[0], bullet[1]))
        bullet[1] -= bullet_speed

        # Remove bullets if they go off screen
        if bullet[1] < 0:
            bullets.remove(bullet)

        # Check for collision with enemies
        for enemy in enemies:
            if (bullet[1] < (enemy[1] + enemy_height) and
                (bullet[1] + bullet_height) > enemy[1] and
                bullet[0] > enemy[0] and
                bullet[0] < (enemy[0] + enemy_width)):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Display score
    draw_text(f"Score: {score}", font, WHITE, screen, 10, 10)

    # Update display
    pygame.display.update()
    clock.tick(60)

# Quit Pygame
pygame.quit()
