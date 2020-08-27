import pygame

class Virus:
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
            return False
        self.y += self.movement
        return True

    def update(self):
        self.img_cnt += 1
        if self.img_cnt >= self.img_max:
            self.img_cnt = 0
        self.img = self.imgs[self.img_cnt // (self.img_max // 4)]
        return self.move()

    def draw(self, win):
        if self.is_alive:
            win.blit(self.img, (self.x, self.y))