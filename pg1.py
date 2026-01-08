# coding=utf-8
import pygame
import sys
import time
from typing import List

pygame.init()
screen=pygame.display.set_mode([800, 600])
pygame.display.set_caption("Robot Spin")

screen.fill("white")
pygame.display.update()

clock=pygame.time.Clock()
running=True
print("game start")
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill("white")

    pygame.draw.circle(
        surface=screen,
        color="red",
        center=(400,300),
        radius=100,
        width=10
    )

    clock.tick(60)
    pygame.display.update()

print("game end")
pygame.quit()
sys.exit()