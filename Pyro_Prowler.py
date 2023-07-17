# Libraries used
import pygame
import os
import random as r
pygame.init()
import time
# Predefined functions

def create_window(WIDTH, HEIGHT, CAPTION):
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTION)
    return window


# To create window w/ dimensions and caption
window = create_window(900, 900, " bharat's game")

# Variables declared
speedoffb = 15
FPS = 60  # Frame rate
score = 0
text_font = pygame.font.SysFont("monospace", 50)

# Sprites
mc_c = pygame.image.load(os.path.join("dodge_boms_assets", "mc.png"))  # Main character
mc = pygame.transform.scale(mc_c, (50, 45))

# COLORS
BLACK = (0, 0, 0)

# Bullets
max_balls = 3
balls = []
ball = pygame.image.load(os.path.join("dodge_boms_assets", "fireball-png-pic-25.png"))
ball = pygame.transform.scale(ball, (50, 45))

# Main page sprites
mainpage = pygame.image.load(os.path.join("dodge_boms_assets", "Mainpage.png"))
playbutton = pygame.image.load(os.path.join("dodge_boms_assets","playbutton.png"))
playbutton = pygame.transform.scale(playbutton, (200,100))


# Window Paint

def game_window(mc_hit, mcc, balls, score):
    global ball
    window.fill(BLACK)
    window.blit(mcc, (mc_hit.x, mc_hit.y))
    for i in balls:
        window.blit(ball, (i.x, i.y))
    window.blit(score, (800, 800))
    pygame.display.update(())


# End page
end = pygame.image.load(os.path.join("dodge_boms_assets", "loserpage.png"))
end = pygame.transform.scale(end, (500, 400))


def endgame(score):
    run = True
    while run:
        # to check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window.fill(BLACK)
        window.blit(end, (200, 200))
        window.blit(score, (400, 400))
        pygame.display.update()
    pygame.quit()

# Title Page

def main_page():
    key_pressed = pygame.mouse.get_pressed()
    print(key_pressed)
    run = True
    while run:
        window.fill(BLACK)
        window.blit(mainpage, (0, 0))
        playbutton_hit = pygame.Rect(350, 700, 200, 100)
        window.blit(playbutton, (playbutton_hit.x, playbutton_hit.y))

        for event in pygame.event.get():
            # To check for quit
            if event.type == pygame.QUIT:
                run = False
            # To check if the left button is down
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if playbutton_hit.collidepoint(pygame.mouse.get_pos()):
                    main()

        pygame.display.update()
    pygame.quit()


# Game loop

def main():
    global balls, score, text_font, Scoreboard
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
                score += max_balls**-1
            if i.colliderect(mc_hit):
                run = False
                endgame(Scoreboard)
        # Scoreboard

        Scoreboard = text_font.render(f"{round(score)}", 1, (255, 255, 255))

        # Keyboard movements for mc
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            mc_hit.x += 10

        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            mc_hit.x -= 10
        # To paint window and update
        game_window(mc_hit, mc, balls, Scoreboard)
        pygame.display.update()
    # to quit
    pygame.quit()

# Start Page

def Start():
    window.fill(BLACK)
    Title = text_font.render(f"{score}", 1, (255, 255, 255))

if __name__ == "__main__":
    main_page()
