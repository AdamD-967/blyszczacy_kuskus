import pygame as pg
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from random import randint
from time import time
import tkinter as tk

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pg.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    def update(self, keys):
        if keys[K_UP]:
            self.rect.move_ip(0, -2)
        if keys[K_DOWN]:
            self.rect.move_ip(0, 2)
        if keys[K_LEFT]:
            self.rect.move_ip(-2, 0)
        if keys[K_RIGHT]:
            self.rect.move_ip(2, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
        

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pg.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(800, randint(0, 600)))
    def update(self):
        self.rect.move_ip((-1, 0))
        if self.rect.right < 0:
            self.kill()

level = list()
while len(level) < 1:
    window = tk.Tk()
    lev = tk.Label(text="Level(1-3):")
    lev.pack()
    ent = tk.Entry()
    ent.pack()
    ok = tk.Button(text='submit')
    ok.pack()

    def submit(click, obj=level):
        try:
            m = int(ent.get())
            obj.append(m)
            window.destroy()
        except ValueError:
            pass

    ok.bind("<Button-1>", submit)

    window.mainloop()

pg.init()

screen = pg.display.set_mode((800, 600))
player = Player()
enemies = pg.sprite.Group()
_all = pg.sprite.Group()
_all.add(player)

enemydelta = None
if level[len(level)-1] <= 1:
    enemydelta = 500
elif level[len(level)-1] == 2:
    enemydelta = 300
else:
    enemydelta = 100

ADDENEMY = pg.USEREVENT+1
pg.time.set_timer(ADDENEMY, enemydelta)

running = True

ts = time()

while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            enemy = Enemy()
            enemies.add(enemy)
            _all.add(enemy)
    pressed = pg.key.get_pressed()
    player.update(pressed)
    enemies.update()
    if pg.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False
    screen.fill((0, 0, 0))
    for one in _all:
        screen.blit(one.surf, one.rect)
    pg.display.flip()

t = time()-ts

pg.quit()

print("you survived: "+str(t)+" seconds")
