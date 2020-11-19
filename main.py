import pygame
import sys
import time

pygame.init()
screen = pygame.display.set_mode((960, 760))
pygame.display.set_caption('Pong')

events = [False, False, False, False, False] #z, x, left, right


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
        if hautoubas == "haut":
            if userinput[0]:
                self.rect.centerx = self.rect.centerx - 1

            if userinput[1]:
                self.rect.centerx = self.rect.centerx + 1

         if hautoubas == "bas":
            if userinput[2]:
                self.rect.centerx = self.rect.centerx - 1

            if userinput[3]:
                self.rect.centerx = self.rect.centerx + 1
                
