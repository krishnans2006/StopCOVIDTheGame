from datetime import datetime
from random import uniform

import pygame


class Player:
    def __init__(self, x, y, img1, img2, width, height):
        self.x = x
        self.y = y
        self.movementx = 0
        self.movementy = 0
        self.imgs = [img1, img2]
        self.img_cnt = 0
        self.img_max = 10
        self.img = self.imgs[self.img_cnt // 5]
        self.speed = 10
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.health = 10
        self.is_alive = True
        self.infected = False
        self.infect_time = None
        self.infect_end = None

    def dead(self):
        self.is_alive = False
        print("dead")

    def infect(self):
        self.infected = True
        self.infect_time = datetime.now()
        self.infect_end = uniform(0.5, 1.5)
        print("You will be cured in", self.infect_end, "seconds")

    def handle_key_pressed(self, key):
        if key == pygame.K_RIGHT or key == pygame.K_d:
            self.movementx = self.speed
        elif key == pygame.K_LEFT or key == pygame.K_a:
            self.movementx = - self.speed
        elif key == pygame.K_UP or key == pygame.K_w:
            self.movementy = - self.speed
        elif key == pygame.K_DOWN or key == pygame.K_s:
            self.movementy = self.speed

    def handle_key_unpressed(self, key):
        if key == pygame.K_RIGHT or key == pygame.K_d or key == pygame.K_LEFT or key == pygame.K_a:
            self.movementx = 0
        if key == pygame.K_UP or key == pygame.K_w or key == pygame.K_DOWN or key == pygame.K_s:
            self.movementy = 0

    def move(self):
        if self.x < 20 and self.movementx < 0:
            self.movementx = 0
        if self.x + self.width > 980 and self.movementx > 0:
            self.movementx = 0
        if self.y < 20 and self.movementy < 0:
            self.movementy = 0
        if self.y + self.height > 780 and self.movementy > 0:
            self.movementy = 0
        self.x += self.movementx
        self.y += self.movementy

    def update(self):
        self.move()
        self.img_cnt += 1
        if self.img_cnt >= self.img_max:
            self.img_cnt = 0
        self.img = self.imgs[self.img_cnt // (self.img_max // 2)]
        if self.infected:
            current = datetime.now()
            if (current - self.infect_time).seconds > self.infect_end:
                self.infected = False
                self.infect_time = None
                print("You have been cured!")
            self.health -= 0.1
        else:
            self.health -= 0.01
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        if not self.is_alive:
            return False
        return True

