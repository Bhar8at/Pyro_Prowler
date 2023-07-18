# Libraries used
import pygame
import os
import random as r
import time
pygame.init()
pygame.font.init()
from pygame import mixer

# Predefined functions



def create_window(WIDTH, HEIGHT, CAPTION):
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTION)
    return window


# To create window w/ dimensions and caption
window = create_window(900, 900, " Pyro Prowler ")

# Variables declared
speedoffb = 15
FPS = 60  # Frame rate
score = 0
text_font = pygame.font.SysFont("monospace", 50)
clock = pygame.time.Clock()

# Background
space = pygame.image.load(os.path.join("dodge_boms_assets", "space.png"))
space = pygame.transform.scale(space, (900, 900))
# Sprites
mc_c = pygame.image.load(os.path.join("dodge_boms_assets", "mc.png"))  # Main character
mc = pygame.transform.scale(mc_c, (50, 45))
spofmc = 10

# COLORS
BLACK = (0, 0, 0)

# Bullets
max_balls = 3
balls = []
ball = pygame.image.load(os.path.join("dodge_boms_assets", "fireball-png-pic-25.png"))
ball = pygame.transform.scale(ball, (100, 90))

# Orbs
orb1_img = pygame.image.load(os.path.join("dodge_boms_assets", "orb1.png"))
orb1_img = pygame.transform.scale(orb1_img, (100, 100))
activate_orb1 = False
continue_orb1 = False
orb1_activator = r.randrange(2, 5)
# Main page sprites
mainpage = pygame.image.load(os.path.join("dodge_boms_assets", "Mainpage.png"))
playbutton = pygame.image.load(os.path.join("dodge_boms_assets", "playbutton.png"))
playbutton = pygame.transform.scale(playbutton, (200, 100))

# Power up functions

def activate_booster():
    print("THIS HAPPENEED ENOWENFEWIFNWEIFONWF")
    global spofmc, mc
    spofmc = 20
    mc = pygame.transform.scale(mc_c, (10, 10))
    activate_booster_status = True

# Window Paint

def game_window(mc_hit, mcc, balls, score):
    global ball, continue_orb1, activate_orb1
    window.blit(space, (0,0))
    window.blit(mcc, (mc_hit.x, mc_hit.y))
    for i in balls:
        window.blit(ball, (i.x, i.y))
    window.blit(score, (800, 800))
    global activate_orb1
    if activate_orb1:
        global orb1_hit
        orb1_hit = pygame.Rect(100, 100, r.randrange(0, 900), 0)
        window.blit(orb1_img, (orb1_hit.x, orb1_hit.y))
        activate_orb1 = False
        continue_orb1 = True
    if continue_orb1:
        orb1_hit.y += 10
        window.blit(orb1_img, (orb1_hit.x, orb1_hit.y))
        if orb1_hit.colliderect(mc_hit):
            print("IT HIT THE ORBN")
            activate_booster()
        if orb1_hit.y > 900:
            continue_orb1 = False

    pygame.display.update(())


# End page
end = pygame.image.load(os.path.join("dodge_boms_assets", "loserpage.png"))
end = pygame.transform.scale(end, (600, 400))
tryagain = pygame.image.load(os.path.join("dodge_boms_assets", "tryagain.png"))
tryagain = pygame.transform.scale(tryagain, (200, 100))
mainmenu = pygame.image.load(os.path.join("dodge_boms_assets", "mainmenu.png"))
mainmenu = pygame.transform.scale(mainmenu, (200, 100))


def endgame(score):
    mixer.Sound("dodge_boms_assets/gameover.wav").play()
    global balls
    balls = []
    tryagain_hit = pygame.Rect(365, 600, 200, 100)
    mainmenu_hit = pygame.Rect(365, 750, 200, 100)
    run = True
    while run:
        clock.tick(FPS)
        window.fill(BLACK)
        window.blit(end, (200, 200))
        window.blit(score, (450, 500))
        window.blit(tryagain, (tryagain_hit.x, tryagain_hit.y))
        window.blit(mainmenu, (mainmenu_hit.x, mainmenu_hit.y))
        pygame.display.update()

        # to check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if int(event.type) == 1025 and event.button == 1:
                print("WORKED", int(event.type)) # THIs PRINT COMMAND IS NECESARY FOR GAME TO WORK FOR SOME REASON IDK WHY
                if tryagain_hit.collidepoint(pygame.mouse.get_pos()):
                    print("This worked too ig")
                    run = False
                    mixer.music.stop()
                    main()
                if mainmenu_hit.collidepoint(pygame.mouse.get_pos()):
                    run = False
                    mixer.music.stop()
                    main_page()
    print("This worked too")
    pygame.quit()


# Title Page

def main_page():
    mixer.music.load("dodge_boms_assets/mainmenubgm.wav")
    mixer.music.play(-1)
    time.sleep(0.25)
    global score
    score = 0
    run = True
    while run:
        clock.tick(FPS)
        window.blit(space, (0,0))
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
                    run = False
                    mixer.music.stop()
                    main()
        pygame.display.update()
    pygame.quit()


# Game loop

def main():
    global balls, score, text_font, Scoreboard
    score = 0
    mc_hit = pygame.Rect(400, 700, 50, 45)
    mc_hit.x = 450
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
            y = pygame.Rect(x, 0, 100, 90)
            balls.append(y)
        for i in balls:
            i.y += speedoffb
            if i.y > 900:
                ball_dodge_sound = mixer.Sound("dodge_boms_assets/scored.mp3")
                ball_dodge_sound.play()
                balls.remove(i)
                score += max_balls ** -1
            if i.colliderect(mc_hit):
                run = False
                endgame(Scoreboard)

        # Power ups
        if score % orb1_activator == 0 and score != 0:
            global activate_orb1
            activate_orb1 = True

        # Scoreboard

        Scoreboard = text_font.render(f"{round(score)}", 1, (255, 255, 255))

        # Keyboard movements for mc
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            mc_hit.x += spofmc

        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            mc_hit.x -= spofmc

        # To check if out of boundary
        if mc_hit.x not in range(0, 900):
            endgame(Scoreboard)
            score = 0

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
