import time
import pygame
from typing import Any

class GameLoop:
    _instance = None 

    def __init__(self) -> None:
        if GameLoop._instance is not None:
            raise ValueError()
        GameLoop._instance = self

        self.OnUpdate = EventSignal()


    def tick(self):
        pygame.display.flip()
        self.OnUpdate()


    @staticmethod
    def GetInstance():
        return GameLoop() if GameLoop._instance is None else GameLoop._instance
    

class Mouse:

    def __init__(self):
        self.mouse = pygame.mouse
        self.isClicking = False
        self.OnMouseButton1Clicked = EventSignal()
        self.OnMouseButton1Released = EventSignal()
        GameLoop.GetInstance().OnUpdate.connect(self.Update)

    def GetXY(self):
        return self.mouse.get_pos()[0] , self.mouse.get_pos()[1]

    def Update(self):
        if pygame.mouse.get_pressed()[0] and not self.isClicking:
            self.OnMouseButton1Clicked()
            self.isClicking = True
        elif not pygame.mouse.get_pressed()[0] and self.isClicking:
            self.OnMouseButton1Released()
            self.isClicking = False


class EventSignal():
    def __init__(self) -> None:
        self.timeout = 0
        self.timeout_time = 0.01
        self.subs = []

    def connect(self, func):
        self.subs.append(func)

    def disconnect(self, func):
        if func in self.subs:
            self.subs.remove(func)
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if time.time() - self.timeout < self.timeout_time:
            return 
        self.timeout = time.time()

        for func in self.subs:
            func(*args, **kwds)


class Grid:
    
    def __init__(self, n, x, y, logicalGrid):
        self.width, self.height = x, y
        self.display = pygame.display.set_mode((x,y))
        self.size = n
        self.logicalGrid = logicalGrid
        GameLoop.GetInstance().OnUpdate.connect(self.Update)

    def calc(self, X,Y):
        return (int(X/(self.width/self.size)),int(Y/(self.height/self.size)))

    def draw_rect(self, X,Y, color):
        pygame.draw.rect(self.display, color, ((self.width/self.size)*X,(self.width/self.size)*Y,self.width/self.size,self.width/self.size))

    def draw_grid(self):
        for i in range(1, self.size):
            pygame.draw.rect(self.display,'black', ((self.width/self.size)*i-0.5, 0, 1, self.width))
            pygame.draw.rect(self.display,'black', (0,(self.height/self.size)*i-0.5, self.height, 1))
    
    def draw_objects(self):
        for key, color in self.logicalGrid.items():
            self.draw_rect(*key, color[0])

    def Update(self):
        self.display.fill('grey')
        self.draw_grid()
        self.draw_objects()

