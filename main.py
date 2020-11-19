import pygame

pygame.init()
screen = pygame.display.set_mode((960, 760))
pygame.display.set_caption('Pong')


class Plaquette:
    
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.s_rect = screen.get_rect()
        self.screen = screen

    def blit(self):
        self.screen.blit(self.image, self.rect)
