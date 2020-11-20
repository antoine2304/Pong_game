import pygame
import sys
import time

pygame.init()
screen = pygame.display.set_mode((760, 900))
pygame.display.set_caption('Pong')

events = [False, False, False, False, False] #z, x, left, right

#parametres
vitesse = 12.5
fps = 1/60


def get_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                events[0] = False

            if event.key == pygame.K_x:
                events[1] = False

            if event.key == pygame.K_LEFT:
                events[2] = False

            if event.key == pygame.K_RIGHT:
                events[3] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                events[0] = True
                events[1] = False

            if event.key == pygame.K_x:
                events[1] = True
                events[0] = False

            if event.key == pygame.K_LEFT:
                events[2] = True
                events[3] = False

            if event.key == pygame.K_RIGHT:
                events[3] = True
                events[2] = False


class Plaquette:

    def __init__(self, image, x, y, hautoubas):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.s_rect = screen.get_rect()
        self.screen = screen
        self.rect.centerx = x
        self.rect.centery = y
        self.position = hautoubas

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def move(self, userinput):

        if self.position == "haut":
            if userinput[0]:
                self.rect.centerx = self.rect.centerx - vitesse

            if userinput[1]:
                self.rect.centerx = self.rect.centerx + vitesse

        if self.position == "bas":
            if userinput[2]:
                self.rect.centerx = self.rect.centerx - vitesse

            if userinput[3]:
                self.rect.centerx = self.rect.centerx + vitesse

        if self.rect.left < self.s_rect.left:
            self.rect.left = self.s_rect.left

        elif self.rect.right > self.s_rect.right:
            self.rect.right = self.s_rect.right


plaquette_down = Plaquette("Plaquette.jpg", 580, 810, "bas")
plaquette_up = Plaquette("Plaquette.jpg", 580, 90, "haut")

while True:
    time.sleep(fps)
    get_input()
    plaquette_down.move(events)
    plaquette_up.move(events)
    screen.fill((255, 255, 255))
    plaquette_down.blit()
    plaquette_up.blit()
    pygame.display.flip()
             
