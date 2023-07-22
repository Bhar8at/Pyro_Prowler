# Libraries used
import pygame
import os
import random as r

pygame.init()
pygame.font.init()
from pygame import mixer
import time


# Predefined functions


def create_window(WIDTH, HEIGHT, CAPTION):
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTION)
    return window


# To create window w/ dimensions and caption
window = create_window(900, 900, " Pyro Prowler ")

# Variables declared
speedoffb = 5
FPS = 60  # Frame rate
score = 0
text_font = pygame.font.SysFont("monospace", 50)
clock = pygame.time.Clock()
multiplier = 1
game_time = 0
# Background
space = pygame.image.load(os.path.join("dodge_boms_assets", "space.png"))
space = pygame.transform.scale(space, (1800, 1800))
space_1 = space
space_rage = pygame.image.load(os.path.join("dodge_boms_assets", "space_rage.png"))
space_rage = pygame.transform.scale(space_rage, (900, 900))
space_y = [0, 900, 1800]
scroll = 0
speedofbg = 5

# Sprites
mc_c = pygame.image.load(os.path.join("dodge_boms_assets", "mc.png"))  # Main character
mc = pygame.transform.scale(mc_c, (50, 45))
boost = pygame.image.load(os.path.join("dodge_boms_assets", "boost.png"))
boost = pygame.transform.scale(boost, (40, 35))
spofmc = 10
act_jetpack = False

# COLORS
BLACK = (0, 0, 0)

# FIREBALLS
max_balls = 3
balls_v = []
balls_h = []
ball_v = pygame.image.load(os.path.join("dodge_boms_assets", "fireball-png-pic-25.png"))
ball_v = pygame.transform.scale(ball_v, (100, 90))
ball_counter = 5
v_Fb = h_Fb = False

# Orbs
orb1_img = pygame.image.load(os.path.join("dodge_boms_assets", "orb1.png"))
orb1_img = pygame.transform.scale(orb1_img, (100, 100))
orbing = r.randrange(10, 15)
activate_orb1 = False
continue_orb1 = False
orbs = []
booster_timer = 0
activate_booster_status = False

# Main page sprites
mainpage = pygame.image.load(os.path.join("dodge_boms_assets", "Mainpage.png"))
playbutton = pygame.image.load(os.path.join("dodge_boms_assets", "playbutton.png"))
playbutton = pygame.transform.scale(playbutton, (200, 100))


# Power up functions

def activate_booster():
    global spofmc, mc, FPS, multiplier, activate_booster_status, space, space_rage, speedoffb
    spofmc = 15
    speedoffb = 20
    FPS = 80
    multiplier = 5
    mc_c = pygame.image.load(os.path.join("dodge_boms_assets", "mc_rage.png"))  # Main character
    mc = pygame.transform.scale(mc_c, (50, 45))
    activate_booster_status = True
    space = space_rage


def deactivate_booster():  # Gets activated by mistake ?
    global spofmc, mc, FPS, multiplier, space_1, space, activate_booster_status
    activate_booster_status = False
    spofmc = 10
    FPS = 60
    multiplier = 1
    mc_c = pygame.image.load(os.path.join("dodge_boms_assets", "mc.png"))  # Main character
    mc = pygame.transform.scale(mc_c, (50, 45))
    space = space_1


# Window Paint

def game_window(mc_hit, mcc, balls, score, orbs):
    global ball, continue_orb1, activate_orb1, space_y, scroll, speedofbg, ball_counter, boost, act_jetpack, v_Fb, h_Fb, balls_h

    # to have infinite scrolling display
    if v_Fb:
        window.blit(space, (0, 0 + scroll))
        window.blit(space, (0, -900 + scroll))
        window.blit(space, (0, -1800 + scroll))
    elif h_Fb:
        window.blit(space, (0 - scroll, 0))
        window.blit(space, (900 - scroll, 0))
        window.blit(space, (1800 - scroll, 0))

    if scroll >= 900:
        scroll = 0
    scroll += speedofbg

    # To provide animating fireball and switch between differently oriented fireballs
    if round(ball_counter) == 8:
        ball_counter = 5
    else:
        ball_counter += 0.15
    if v_Fb:
        ball = pygame.image.load(os.path.join("dodge_boms_assets", f"fireball-png-pic-2{round(ball_counter)}.png"))
        ball = pygame.transform.scale(ball, (100, 90))
        for i in balls_v:
            window.blit(ball, (i.x, i.y))
    elif h_Fb:
        ball = pygame.image.load(os.path.join("dodge_boms_assets", f"fireball-png-pic-2{round(ball_counter)}l.png"))
        ball = pygame.transform.scale(ball, (100, 90))
        for i in balls_h:
            window.blit(ball, (i.x, i.y))
    # for main character
    if act_jetpack:
        window.blit(boost, (mc_hit.x, mc_hit.y + 35))
    window.blit(mcc, (mc_hit.x, mc_hit.y))
    # for scorecard
    window.blit(score, (800, 800))
    # to display orb
    for i in orbs:
        window.blit(orb1_img, (i.x, i.y))
    pygame.display.update(())


# End page
end = pygame.image.load(os.path.join("dodge_boms_assets", "loserpage.png"))
end = pygame.transform.scale(end, (600, 400))
tryagain = pygame.image.load(os.path.join("dodge_boms_assets", "tryagain.png"))
tryagain = pygame.transform.scale(tryagain, (200, 100))
mainmenu = pygame.image.load(os.path.join("dodge_boms_assets", "mainmenu.png"))
mainmenu = pygame.transform.scale(mainmenu, (200, 100))


def endgame(score):
    mixer.music.stop()
    mixer.Sound("dodge_boms_assets/gameover.wav").play()
    global balls, act_jetpack, balls_h, balls_v
    balls_h = balls_v = []
    act_jetpack = False
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
                print("WORKED",
                      int(event.type))  # THIs PRINT COMMAND IS NECESARY FOR GAME TO WORK FOR SOME REASON IDK WHY
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
    global score, space_y
    score = 0
    run = True
    while run:
        clock.tick(FPS)
        window.blit(space, (0, 0))
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
    mixer.music.load("dodge_boms_assets/gliding.mp3")
    mixer.music.play()
    global balls_v, balls_h, score, text_font, Scoreboard, activate_orb1, booster_timer, activate_booster_status, FPS, speedoffb, speedofbg, game_time, act_jetpack, v_Fb, h_Fb
    FPS = 60
    v_Fb = True
    speedofbg = speedoffb = 5
    score = 0
    game_time = 0
    mc_hit = pygame.Rect(400, 800, 50, 45)
    mc_hit.x = 450
    clock = pygame.time.Clock()
    run = True
    start_time = time.time()
    while run:
        current_time = time.time()
        time_taken = round(current_time - start_time)  # To find time taken
        print(time_taken)
        clock.tick(FPS)  # To fix fps

        # to check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Fireballs
        if v_Fb:
            while len(balls_v) < max_balls:
                x = r.randrange(0, 900)
                y = pygame.Rect(x, 0, 100, 90)
                balls_v.append(y)
            for i in balls_v:
                i.y += speedoffb
                if i.y > 900:
                    ball_dodge_sound = mixer.Sound("dodge_boms_assets/scored.mp3")
                    ball_dodge_sound.play()
                    balls_v.remove(i)
                    score += multiplier * max_balls ** -1
                    if activate_booster_status:
                        booster_timer += 1
                if i.colliderect(mc_hit):
                    run = False
                    booster_timer = 0
                    deactivate_booster()
                    endgame(Scoreboard)
        elif h_Fb:
            while len(balls_h) < max_balls:
                x = r.randrange(0, 900)
                y = pygame.Rect(900, x, 100, 90)
                balls_h.append(y)
            for i in balls_h:
                i.x -= speedoffb
                if i.x < 0:
                    ball_dodge_sound = mixer.Sound("dodge_boms_assets/scored.mp3")
                    ball_dodge_sound.play()
                    balls_h.remove(i)
                    score += multiplier * max_balls ** -1
                    if activate_booster_status:
                        booster_timer += 1
                if i.colliderect(mc_hit):
                    run = False
                    booster_timer = 0
                    deactivate_booster()
                    endgame(Scoreboard)

        # Hype from song
        if time_taken in range(15, 41):
            FPS = 65
            speedoffb = 15
            speedofbg = 10
            act_jetpack = True
        elif time_taken in range(41, 44):
            balls_h = balls_v = []
            v_Fb = False
            h_Fb = True
            if mc_hit.x > 100:
                mc_hit.x -= 10
            if mc_hit.y > 450:
                mc_hit.y -= 10
        elif time_taken in range(44, 51):
            v_Fb = False
            h_Fb = True
        elif time_taken in range(51, 58):
            v_Fb = False
            h_Fb = True
            speedoffb = 7
        elif time_taken in range(58, 70): # switch to left !!
            pass

        else:
            v_Fb = True
            h_Fb = False
            FPS = 60
            speedoffb = 7
            speedofbg = 5
            act_jetpack = False

        # Power ups

        if round(score) % orbing == 0 and score != 0 and len(orbs) < 1:
            orbs.append(pygame.Rect(r.randrange(0, 900), 0, 50, 50))

        for i in orbs:
            i.y += 10
            if i.y > 900:
                orbs.remove(i)
            if i.colliderect(mc_hit):
                booster_timer = 0
                activate_booster()
        if booster_timer > 15 and activate_booster_status:
            deactivate_booster()
            booster_timer = 0

        # Scoreboard
        Scoreboard = text_font.render(f"{round(score)}", 1, (255, 255, 255))

        # Keyboard movements for mc
        key_pressed = pygame.key.get_pressed()
        if v_Fb:
            if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
                mc_hit.x += spofmc

            if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
                mc_hit.x -= spofmc
        elif h_Fb:
            if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
                mc_hit.y -= spofmc

            if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
                mc_hit.y += spofmc

        # To check if out of boundary
        if mc_hit.x not in range(0, 900):
            deactivate_booster()
            booster_timer = 0
            score = 0
            mixer.music.stop()
            endgame(Scoreboard)
        # To check if song is done, so game finishes
        if not mixer.music.get_busy() and run == True:
            endgame(Scoreboard)

        # To paint window and update
        game_window(mc_hit, mc, balls_h, Scoreboard, orbs)
        pygame.display.update()

    # to quit
    pygame.quit()


# Start Page

def Start():
    window.fill(BLACK)
    text_font.render(f"{score}", 1, (255, 255, 255))


if __name__ == "__main__":
    main_page()
