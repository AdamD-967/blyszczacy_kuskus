import pygame as pg
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_RETURN, 
)
from random import randint

class Head(pg.sprite.Sprite):
    def __init__(self):
        super(Head, self).__init__()
        self.surf = pg.Surface((24, 24))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect()
        self.rect.move_ip((400, 400))
        self.dir = "RIGHT"
        self.num = 0

    def update(self, keys):
        if keys[K_UP] and self.dir != "DOWN":
            self.dir = "UP"
        elif keys[K_DOWN] and self.dir != "UP":
            self.dir = "DOWN"
        elif keys[K_LEFT] and self.dir != "RIGHT":
            self.dir = "LEFT"
        elif keys[K_RIGHT] and self.dir != "LEFT":
            self.dir = "RIGHT"

        if self.dir == "UP":
            self.rect.move_ip(0, -1)
        elif self.dir == "DOWN":
            self.rect.move_ip(0, 1)
        elif self.dir == "LEFT":
            self.rect.move_ip(-1, 0)
        else:
            self.rect.move_ip(1, 0)

    def check(self, group):
        if self.rect.left < 0:
            return False
        if self.rect.right > 800:
            return False
        if self.rect.top <= 0:
            return False
        if self.rect.bottom >= 800:
            return False
        else:
            return not any(map(lambda n: n.rect.center == self.rect.center, group))

    def eat(self, food, body):
        if pg.sprite.spritecollideany(self, food):
            food.pop(0)
            body.extend([Node() for _ in range(10)])
            self.num+=1

sneak = [Head()]

class Node(pg.sprite.Sprite):
    def __init__(self):
        super(Node, self).__init__()
        self.surf = pg.Surface((24, 24))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect()
        self.rect.center = sneak[len(sneak)-1].rect.center

    def update(self, nnode):
        self.rect.center = nnode.rect.center


class Food(pg.sprite.Sprite):
    def __init__(self):
        super(Food, self).__init__()
        self.surf = pg.Surface((24, 25))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.move_ip((randint(12, 788), randint(12, 788)))

pg.init()

def main():
    screen = pg.display.set_mode((800, 800))
    sneak.extend([Node(), Node()])
    sneak.extend([Node() for _ in range(100)])
    food = [Food()]
    clock = pg.time.Clock()
    running = True

    while running:
        for event in pg.event.get():
            if event.type == QUIT:
                running = False
        
        sneak[0].eat(food, sneak)
        if len(food) == 0:
            food.append(Food())

        pressed = pg.key.get_pressed()
        sneak[0].update(pressed)
        for n in range(len(sneak)-1, 0, -1):
            sneak[n].update(sneak[n-1])

        running = sneak[0].check(sneak[2::])

        screen.fill((0, 0, 0))
        for m in sneak:
            screen.blit(m.surf, m.rect)
        screen.blit(food[0].surf, food[0].rect)
        pg.display.flip()
        clock.tick(300)
    print(f"Score: {sneak[0].num}")

main()
pg.quit()
