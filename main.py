import pygame
import sys
import time
import random

pygame.init()
screen = pygame.display.set_mode((760, 900))
pygame.display.set_caption('Pong')

events = [False, False, False, False, False] #z, x, left, right

#parametres
vitesse_plaquette = 12.5
vitesse_ball = 1
acceleration_ball = 0.1
fps = 1/60
initial_time = pygame.time


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


class Ball:
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.s_rect = screen.get_rect()
        self.screen = screen
        self.rect.centery = 0.5*self.screen.get_height()
        self.rect.centerx = random.randint(self.s_rect.left + self.image.get_height(), self.s_rect.right -self.image.get_height())
        self.angle = random.randint(0, 360)

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def move(self):  

    def checkwall(self):
        if self.rect.left < self.s_rect.left and 0 <= self.angle < 90: #frappe le mur gauche venant du haut
            self.rect.left = self.s_rect.left
            self.angle = self.angle - 2*abs(self.angle) - 180
            vitesse_ball = vitesse_ball + acceleration_ball

        elif self.rect.left < self.s_rect.left and 90 <= self.angle < 180: #frappe le mur gauche venant du bas
            self.rect.left = self.s_rect.left
            self.angle = self.angle + 2*abs(self.angle) + 180
            vitesse_ball = vitesse_ball + acceleration_ball

        elif self.rect.right > self.s_rect.right and 180 <= self.angle < 270: #frappe le mur droit venant du bas
            self.rect.right = self.s_rect.right
            self.angle = self.angle - 2*abs(self.angle) - 180
            vitesse_ball = vitesse_ball + acceleration_ball

        elif self.rect.right > self.s_rect.right and 270 <= self.angle < 360: #frappe le mur droit venant du haut
            self.rect.right = self.s_rect.right
            self.angle = self.angle + 2*abs(self.angle) + 180
            vitesse_ball = vitesse_ball + acceleration_ball
    
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
                self.rect.centerx = self.rect.centerx - vitesse_plaquette

            if userinput[1]:
                self.rect.centerx = self.rect.centerx + vitesse_plaquette

        if self.position == "bas":
            if userinput[2]:
                self.rect.centerx = self.rect.centerx - vitesse_plaquette

            if userinput[3]:
                self.rect.centerx = self.rect.centerx + vitesse_plaquette

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
             
