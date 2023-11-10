from manager import *

myMouse = Mouse()
gameLoop = GameLoop.GetInstance()
grid = Grid(25, 500, 500)

logicalGrid = {}
"""
logicalGrid:
    key: (x,y) -> grid.calc() return
    value: color
"""

class example:
    pass


run = True
while run:

    gameLoop.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            break
