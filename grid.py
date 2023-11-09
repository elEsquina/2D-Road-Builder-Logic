import pygame
import time


class Grid:
    
    def __init__(self, n, x, y):
        self.width, self.height = x, y
        self.display = pygame.display.set_mode((x,y))
        self.display.fill('grey')
        self.size = n

    def calc(self, X,Y):
        return (int(X/(self.width/self.size)),int(Y/(self.height/self.size)))

    def draw_rect(self, X,Y, color):
        pygame.draw.rect(self.display, color, ((self.width/self.size)*X,(self.width/self.size)*Y,self.width/self.size,self.width/self.size))

    def draw_grid(self):
        for i in range(1, self.size):
            pygame.draw.rect(self.display,'black', ((self.width/self.size)*i-0.5, 0, 1, self.width))
            pygame.draw.rect(self.display,'black', (0,(self.height/self.size)*i-0.5, self.height, 1))


