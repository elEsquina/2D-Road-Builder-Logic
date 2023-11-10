from manager import *

myMouse = Mouse()
gameLoop = GameLoop.GetInstance()
grid = Grid(25, 500, 500)
logicalGrid = {}

class example:
    
    def __init__(self):
        myMouse.OnMouseButton1Clicked.connect(self.detectMouseClick)
        self.xy = None
        self.clicked = 0
        
        
    def detectMouseClick(self) -> None:
        if self.clicked == 1:
            self.drawPath(self.xy, grid.calc(*myMouse.GetXY()))
            self.clicked = 0
            return
        
        self.xy = grid.calc(*myMouse.GetXY())
        self.clicked = 1
    
    def drawPath(self, start, end):
        xMin, yMin = min(start[0], end[0]), min(start[1], end[1])
        xMax, yMax = max(start[0], end[0]), max(start[1], end[1])
        
        for x in range(xMin, xMax + 1):
            logicalGrid[(x, yMin)] = 'yellow'
            grid.draw_rect(x, yMin, 'yellow')
            
        for y in range(yMin, yMax + 1):
            logicalGrid[(xMax, y)] = 'yellow'
            grid.draw_rect(xMin, y, 'yellow')


Example()


run = True
while run:

    gameLoop.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            break
