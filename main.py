import random
from datetime import datetime

import pygame
from pygame.locals import *

from player import Player
from soap import Soap1, Soap2, Soap3, Soap4
from virus import Virus1, Virus2, Virus3, Virus4
from mask import Mask1, Mask2, Mask3, Mask4


def setup(W, H, caption):
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    win = pygame.display.set_mode((W, H))
    pygame.display.set_caption(caption)

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsans", 30, True)
    return win, clock, font


win, clock, font = setup(1000, 800, "Stay Healthy")


def update(*args, **kwargs):
    for arg in args:
        arg.update()
    for kw, arg in kwargs.items():
        if kw == "viruses":
            for virus in arg:
                virus.update()
                if not kwargs["player"].shield and virus.is_alive and virus.hitbox.colliderect(kwargs["player"].hitbox):
                    virus.is_alive = False
                    kwargs["player"].infect()
        elif kw == "soaps":
            for soap in arg:
                soap.update()
                if soap.is_alive and soap.hitbox.colliderect(kwargs["player"].hitbox):
                    soap.is_alive = False
                    kwargs["player"].heal()
        elif kw == "masks":
            for mask in arg:
                mask.update()
                if mask.is_alive and mask.hitbox.colliderect(kwargs["player"].hitbox):
                    mask.is_alive = False
                    kwargs["player"].activate_shield()
        else:
            arg.update()
    if kwargs["player"].health <= 0:
        kwargs["player"].dead()
    if kwargs["player"].health > 10:
        kwargs["player"].health = 10


def endgame(player, score):
    player.is_alive = True
    player.health = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    main()
        redraw(win, player=player, text=["Press q to quit and c to play again!", 200, 200], score=score)
        clock.tick(30)


def redraw_healthbar(win, player):
    drawing_x = player.x
    drawing_y = player.y + player.width + 5
    drawing_width = player.width
    drawing_height = 16
    drawing_sep = 2
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(drawing_x, drawing_y, drawing_width, drawing_height))
    pygame.draw.rect(win, (0, 255, 0), pygame.Rect(drawing_x + drawing_sep, drawing_y + drawing_sep,
                                                   (drawing_width - 2 * drawing_sep) * (player.health / 10),
                                                   drawing_height - 2 * drawing_sep))


def redraw(win, *args, **kwargs):
    win.fill((5, 5, 50))
    for arg in args:
        arg.draw(win)
    for kw, arg in kwargs.items():
        if kw == "player":
            alive = arg.draw(win)
            if not alive:
                endgame(kwargs["player"], kwargs["score"])
        elif kw == "text":
            text = font.render(arg[0], 1, (220, 220, 220))
            win.blit(text, (arg[1], arg[2]))
        elif kw == "score":
            text = font.render(arg[0], 1, (220, 220, 220))
            win.blit(text, (arg[1], arg[2]))
        else:
            arg.draw(win)
    if kwargs["player"].infected:
        text = font.render("You are infected with CoViD-19!", 1, (220, 0, 0))
        win.blit(text, (10, 800 - text.get_height() - 10))
    if kwargs["player"].shield:
        text = font.render(f"Mask activated! You will be protected from CoViD-19 for {kwargs['player'].shield_end - (datetime.now() - kwargs['player'].shield_time).seconds} more seconds!", 1, (0, 220, 0))
        win.blit(text, (1000 - text.get_width() - 10, 800 - text.get_height() - 10))
    redraw_healthbar(win, kwargs["player"])
    pygame.display.flip()


def main():
    pygame.time.set_timer(USEREVENT + 1, 1000)  # Timer for Virus spawn
    pygame.time.set_timer(USEREVENT + 2, 5000)  # Timer for Soap spawn
    pygame.time.set_timer(USEREVENT + 3, 10000)  # Timer for Mask spawn
    player = Player(468, 675, pygame.image.load("spaceship.png"), pygame.image.load("spaceship2.png"), 64, 64)
    Viruses = [Virus1, Virus2, Virus3, Virus4]
    viruses = []
    Soaps = [Soap1, Soap2, Soap3, Soap4]
    soaps = []
    Masks = [Mask1, Mask2, Mask3, Mask4]
    masks = []
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                player.handle_key_pressed(event.key)
            if event.type == pygame.KEYUP:
                player.handle_key_unpressed(event.key)
            if event.type == USEREVENT + 1:
                Virus = random.choice(Viruses)
                viruses.append(Virus(random.randint(10, 958), 10, pygame.image.load("virus.png"), 64, 64))
                score += 1
            if event.type == USEREVENT + 2:
                Soap = random.choice(Soaps)
                soaps.append(Soap(random.randint(10, 958), 10, pygame.image.load("soap.png"), 64, 64))
            if event.type == USEREVENT + 3:
                Mask = random.choice(Masks)
                masks.append(Mask(random.randint(10, 958), 10, pygame.image.load("mask.png"), 64, 64))
        update(player=player, viruses=viruses, soaps=soaps, masks=masks)
        redraw(win, *viruses, *soaps, *masks, player=player, score=["Score: " + str(score), 10, 10])
        clock.tick(30)


if __name__ == '__main__':
    main()
