from manager import *
import numpy as np

myMouse = Mouse()
gameLoop = GameLoop.GetInstance()
logicalGrid = {}
grid = Grid(25, 500, 500, logicalGrid)

myGraph = []

class BaseRoad:
    class _WayPoint:
        def __init__(self, XY) -> None:
            self.position = XY
            self.connections = []


class RoadTile(BaseRoad):

    def __init__(self, start, end):
        self.start = start 
        self.end = end 
        self.waypoints = []
        self.occupiedGrid = []
        self.drawPath(self.start, self.end)

    def drawPath(self, start, end):
        xMin, yMin = min(start[0], end[0]), min(start[1], end[1])
        xMax, yMax = max(start[0], end[0]), max(start[1], end[1])
        
        if (xMax  - xMin) > (yMax - yMin):
            starty = self._WayPoint((xMin, start[1]))
            endy  =  self._WayPoint((xMax, start[1]))
            self.waypoints.append(starty)
            self.waypoints.append(endy)

            for x in range(xMin, xMax + 1):
                if x == xMin or x == xMax:
                    self.draw(x, start[1], "red")
                self.draw(x, start[1])
            return

        starty = self._WayPoint((end[0], yMin))
        endy  =  self._WayPoint((end[0], yMax))
        self.waypoints.append(endy)
        self.waypoints.append(starty)
        
        for y in range(yMin,  yMax + 1):
            if y == yMin or y == yMax:
                self.draw(end[0], y, "red")
            self.draw(end[0], y)

    def draw(self, x, y, color='black'):
        if not (x, y) in grid.logicalGrid:
            grid.logicalGrid[(x, y)] = (color, self)
            self.occupiedGrid.append((x,y))

        if (x,y) in grid.logicalGrid:
            a = self._WayPoint(x, y)
            grid.logicalGrid[(x,y)][1].waypoints.append(a)
            self.waypoints.append(a)
            self.occupiedGrid.append((x,y))
               



class example:
    ignorelist = ('black', 'red')

    def __init__(self):
        gameLoop.OnUpdate.connect(self.update)
        myMouse.OnMouseButton1Clicked.connect(self.detectMouseClick)
        myMouse.OnMouseButton1Released.connect(self.detectMouseUp)
        self.xy = None
        self.clicked = False
        self.release = False
        
        
    def detectMouseClick(self) -> None:
        self.clicked = True
        self.xy = grid.calc(*myMouse.GetXY())


    def detectMouseUp(self) -> None:
        self.clicked = False 
        self.release = True


    def cleanselections(self):
        for key, color in grid.logicalGrid.copy().items():
            if color[0] == 'green': 
                grid.logicalGrid.pop(key)


    def makeselection(self, start, end):
        xMin, yMin = min(start[0], end[0]), min(start[1], end[1])
        xMax, yMax = max(start[0], end[0]), max(start[1], end[1])

        if (xMax  - xMin) > (yMax - yMin):
            for x in range(xMin, xMax + 1):
                self.draw(x, start[1])
            return

        for y in range(yMin,  yMax + 1):
            self.draw(end[0], y)


    def draw(self, x, y):
        if not (x, y) in grid.logicalGrid or not grid.logicalGrid[(x, y)] in self.ignorelist:
            grid.logicalGrid[(x, y)] = ('green', None)


    def update(self):
        self.cleanselections()
        if self.clicked:
            self.makeselection(self.xy, grid.calc(*myMouse.GetXY()))
        elif self.release:
            RoadTile(self.xy, grid.calc(*myMouse.GetXY()))
            self.release = False


example()


run = True
while run:
    gameLoop.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            break
