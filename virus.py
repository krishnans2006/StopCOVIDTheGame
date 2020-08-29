import pygame

class Virus1:
    def __init__(self, x, y, img, width, height):
        self.x = x
        self.y = y
        self.movement = 5
        self.imgs = [img, pygame.transform.rotate(img, 90), pygame.transform.rotate(img, 270), pygame.transform.rotate(img, 180)]
        self.img_cnt = 0
        self.img_max = 20
        self.img = self.imgs[self.img_cnt // 5]
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_alive = True

    def move(self):
        if self.is_alive and self.y + self.height > 800:
            self.is_alive = False
        self.y += self.movement

    def update(self):
        self.img_cnt += 1
        if self.img_cnt >= self.img_max:
            self.img_cnt = 0
        self.img = self.imgs[self.img_cnt // (self.img_max // 4)]
        self.move()
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        if self.is_alive:
            win.blit(self.img, (self.x, self.y))

class Virus2:
    def __init__(self, x, y, img, width, height):
        self.x = x
        self.y = 800 - height - y
        self.movement = 5
        self.imgs = [img, pygame.transform.rotate(img, 90), pygame.transform.rotate(img, 270), pygame.transform.rotate(img, 180)]
        self.img_cnt = 0
        self.img_max = 20
        self.img = self.imgs[self.img_cnt // 5]
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_alive = True

    def move(self):
        if self.is_alive and self.y + self.height > 800:
            self.is_alive = False
        self.y -= self.movement

    def update(self):
        self.img_cnt += 1
        if self.img_cnt >= self.img_max:
            self.img_cnt = 0
        self.img = self.imgs[self.img_cnt // (self.img_max // 4)]
        self.move()
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        if self.is_alive:
            win.blit(self.img, (self.x, self.y))

class Virus3:
    def __init__(self, x, y, img, width, height):
        self.x = y
        self.y = x
        self.movement = 5
        self.imgs = [img, pygame.transform.rotate(img, 90), pygame.transform.rotate(img, 270), pygame.transform.rotate(img, 180)]
        self.img_cnt = 0
        self.img_max = 20
        self.img = self.imgs[self.img_cnt // 5]
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_alive = True

    def move(self):
        if self.is_alive and self.y + self.height > 800:
            self.is_alive = False
        self.x += self.movement

    def update(self):
        self.img_cnt += 1
        if self.img_cnt >= self.img_max:
            self.img_cnt = 0
        self.img = self.imgs[self.img_cnt // (self.img_max // 4)]
        self.move()
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        if self.is_alive:
            win.blit(self.img, (self.x, self.y))

class Virus4:
    def __init__(self, x, y, img, width, height):
        self.x = 1000 - width - y
        self.y = x
        self.movement = 5
        self.imgs = [img, pygame.transform.rotate(img, 90), pygame.transform.rotate(img, 270), pygame.transform.rotate(img, 180)]
        self.img_cnt = 0
        self.img_max = 20
        self.img = self.imgs[self.img_cnt // 5]
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_alive = True

    def move(self):
        if self.is_alive and self.y + self.height > 800:
            self.is_alive = False
        self.x -= self.movement

    def update(self):
        self.img_cnt += 1
        if self.img_cnt >= self.img_max:
            self.img_cnt = 0
        self.img = self.imgs[self.img_cnt // (self.img_max // 4)]
        self.move()
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        if self.is_alive:
            win.blit(self.img, (self.x, self.y))