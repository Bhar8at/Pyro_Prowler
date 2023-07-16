# Libraries used
import pygame
import os
import random as r


# Predefined functions

def create_window(WIDTH, HEIGHT, CAPTION):
    print(WIDTH, HEIGHT)
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTION)
    return window


# To create window w/ dimensions and caption

window = create_window(900, 900, " bharat's game")

# Variables declared
speedoffb = 15
FPS = 60  # Frame rate
score = 0
# Sprites
mc_c = pygame.image.load(os.path.join("dodge_boms_assets", "mc.png"))  # Main character
print(mc_c)
mc = pygame.transform.scale(mc_c, (50, 45))
# COLORS
BLACK = (0, 0, 0)
# Bullets
max_balls = 4
balls = []
ball = pygame.image.load(os.path.join("dodge_boms_assets", "fireball-png-pic-25.png"))
ball = pygame.transform.scale(ball, (50, 45))


# Window Paint

def first_window(mc_hit, mcc, balls):
    global ball
    window.fill(BLACK)
    window.blit(mcc, (mc_hit.x, mc_hit.y))
    for i in balls:
        window.blit(ball, (i.x, i.y))
    pygame.display.update(())


# End page
end = pygame.image.load(os.path.join("dodge_boms_assets", "loserpage.png"))
end = pygame.transform.scale(end, (500, 400))


def endgame(score):
    run = True
    print(score)
    while run:
        # to check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window.fill(BLACK)
        window.blit(end, (200, 200))
        pygame.display.update()
    pygame.quit()


# Game loop

def main():
    global balls, score
    mc_hit = pygame.Rect(400, 700, 50, 45)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)  # To fix fps

        # to check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Fireballs
        while len(balls) < max_balls:
            x = r.randrange(0, 900)
            y = pygame.Rect(x, 0, 50, 45)
            balls.append(y)
        for i in balls:
            i.y += speedoffb
            if i.y > 900:
                balls.remove(i)
                score += 0.25
            if i.colliderect(mc_hit):
                run = False
                endgame(score)

        # Keyboard movements for mc
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            mc_hit.x += 10

        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            mc_hit.x -= 10
        # To paint window and update
        first_window(mc_hit, mc, balls)
        pygame.display.update()
    # to quit
    pygame.quit()


if __name__ == "__main__":
    main()
