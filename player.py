import pygame

class Player:
    def __init__(self, x, y, img1, img2, width, height):
        self.x = x
        self.y = y
        self.movement = 0
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

    def dead(self):
        self.is_alive = False

    def handle_key_pressed(self, key):
        if key == pygame.K_RIGHT or key == pygame.K_d:
            self.movement = self.speed
        elif key == pygame.K_LEFT or key == pygame.K_a:
            self.movement = - self.speed

    def handle_key_unpressed(self, key):
        if key == pygame.K_RIGHT or key == pygame.K_d or key == pygame.K_LEFT or key == pygame.K_a:
            self.movement = 0

    def move(self):
        if self.x < 20 and self.movement < 0:
            self.movement = 0
        if self.x + self.width > 980 and self.movement > 0:
            self.movement = 0
        self.x += self.movement

    def update(self):
        self.move()
        self.img_cnt += 1
        if self.img_cnt >= self.img_max:
            self.img_cnt = 0
        self.img = self.imgs[self.img_cnt // (self.img_max // 2)]

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        if not self.is_alive:
            return False
        return True