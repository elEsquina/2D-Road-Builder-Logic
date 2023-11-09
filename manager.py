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
        self.OnUpdate()


    @staticmethod
    def GetInstance():
        return GameLoop() if GameLoop._instance is None else GameLoop._instance
    

class Mouse:

    def __init__(self):
        self.mouse = pygame.mouse
        self.OnMouseButton1Clicked = EventSignal()
        GameLoop.GetInstance().OnUpdate.connect(self.update)

    def GetXY(self):
        return self.mouse.get_pos()[0] , self.mouse.get_pos()[1]

    def update(self):
        if pygame.mouse.get_pressed()[0]:
            self.OnMouseButton1Clicked()


class EventSignal():
    def __init__(self) -> None:
        self.timeout = 0
        self.timeout_time = 0.1
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