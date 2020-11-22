import pygame
import sys
import time
import random
import math

pygame.init()
screen = pygame.display.set_mode((760, 900))
pygame.display.set_caption('Pong')

events = [False, False, False, False, False] #z, x, left, right

#parametres #test
vitesse_plaquette = 12.5
vitesse_ball = 3
acceleration_ball = 0.3
fps = 1/60
initial_time = time.time()
angle_attaque = 0.02

score_bottom = 0
score_top = 0

def resetall():
    global initial_time

    time.sleep(1)
    ball.y = 0.5*ball.screen.get_height()
    ball.x = 380
    ball.angle = random.randint(0, 360)
    plaquette_up.rect.centerx = 380
    plaquette_down.rect.centerx = 380
    initial_time = time.time()


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
        self.angle = 0 #pointé vers le haut sens horaire
        self.x = self.rect.centerx
        self.y = self.rect.centery

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        self.x -= math.cos(((self.angle+90)/180)*math.pi) * (vitesse_ball + acceleration_ball * (time.time() - initial_time))
        self.y -= math.sin(((self.angle+90)/180)*math.pi) * (vitesse_ball + acceleration_ball * (time.time() - initial_time))
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def checkwall(self):
        if (self.rect.left < self.s_rect.left) and (180 < self.angle) and (self.angle < 270): #frappe le mur gauche venant du haut
            self.x = self.s_rect.left + 5
            self.angle = self.angle - 2*self.angle

        elif (self.rect.left < self.s_rect.left) and (270 < self.angle) and (self.angle < 360): #frappe le mur gauche venant du bas
            self.x = self.s_rect.left + 5
            self.angle = 360 - self.angle

        elif (self.rect.right > self.s_rect.right) and (0 < self.angle) and (self.angle < 90): #frappe le mur droit venant du bas
            self.x = self.s_rect.right - 5
            self.angle = 360 - self.angle

        elif (self.rect.right > self.s_rect.right) and (90 < self.angle) and (self.angle < 180): #frappe le mur droit venant du haut
            self.x = self.s_rect.right - 5
            self.angle = self.angle + 2*(180-self.angle)

        if self.angle > 360:
            self.angle -= 360

        if self.angle < 0:
            self.angle = 360 + self.angle
            
    def checkend (self):
        global score_bottom
        global score_top
        
        if self.rect.bottom > self.s_rect.bottom:
            score_top += 1
            resetall()
        elif self.rect.top < self.s_rect.top:
            score_bottom += 1
            resetall()  

    def check_plaquette(self):
        if (self.rect.top < plaquette_up.rect.bottom) and (abs(self.rect.centerx - plaquette_up.rect.centerx) < 41.5) and (self.rect.top > plaquette_up.rect.top):
            distance = self.rect.centerx - plaquette_up.rect.centerx
            denominateur = 2*angle_attaque*distance
            if denominateur == 0:
                angle_board = 0
            else:
                angle_board = math.atan(abs(denominateur)/3) * 180 / math.pi

            if denominateur < 0:
                angle_board = angle_board*-1

            if self.angle > 270:
                self.angle = 540 - self.angle - angle_board

            elif self.angle < 90:
                self.angle = 180 - self.angle - angle_board

            if self.angle < 100:
                self.angle = 100

            elif self.angle > 260:
                self.angle = 260

            self.y = plaquette_up.rect.bottom + 5

        elif (self.rect.bottom > plaquette_down.rect.top) and (abs(self.rect.centerx - plaquette_down.rect.centerx) < 41.5) and (
                self.rect.bottom < plaquette_down.rect.bottom):
            distance = self.rect.centerx - plaquette_down.rect.centerx
            denominateur = 2 * -1 * angle_attaque * distance
            if denominateur == 0:
                angle_board = 0
            else:
                angle_board = math.atan(abs(denominateur) / 3) * 180 / math.pi

            if denominateur < 0:
                angle_board = angle_board * -1

            if self.angle > 180:
                self.angle = 540 - self.angle - angle_board

            elif self.angle < 180:
                self.angle = 180 - self.angle - angle_board

            if self.angle >= 360:
                self.angle -= 360

            elif self.angle < 0:
                self.angle = 360 + self.angle

            if (self.angle > 80) and (self.angle <= 180):
                self.angle = 80

            elif (self.angle < 280) and (self.angle >= 90):
                self.angle = 280

            self.y = plaquette_down.rect.top - 5


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
ball = Ball("Balle.jpg")
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

while True:
    time.sleep(fps)
    get_input()
    plaquette_down.move(events)
    plaquette_up.move(events)
    ball.move()
    ball.checkwall()
    ball.check_plaquette()
    ball.checkend()
    screen.fill((255, 255, 255))
    plaquette_down.blit()
    plaquette_up.blit()
    ball.blit()
    up = myfont.render(str(score_top), False, (0, 0, 0))
    down = myfont.render(str(score_bottom), False, (0, 0, 0))
    screen.blit(up, (50, 400))
    screen.blit(down, (50, 500))
    pygame.display.flip()
    print(ball.angle)
