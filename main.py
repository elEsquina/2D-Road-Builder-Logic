import pygame
import pickle
import time

n = 25
matrix = {}
run = True

x, y = 500, 500
display = pygame.display.set_mode((x,y))
display.fill('grey')


red = False


def calc(X,Y):
    global x,y,n
    return (int(X/(x/n)),int(Y/(x/n)))

def draw_rectt(X,Y, color):
    global x,y,n
    pygame.draw.rect(display, color, ((x/n)*X,(x/n)*Y,x/n,x/n))

def draw_grid(x,y,n):
    for i in range(1,n):
        pygame.draw.rect(display,'black', ((x/n)*i-0.5,0,1,x))
        pygame.draw.rect(display,'black', (0,(y/n)*i-0.5,y,1))


def draw_path(start, end):
    pass

click_timout = 0

while run:
    if pygame.mouse.get_pressed()[0]:
        s = calc(pygame.mouse.get_pos()[0] ,pygame.mouse.get_pos()[1])
        if time.time() - click_timout > 0.5:
            click_timout = time.time()
            matrix[s[0], s[1]] = red
            red = not red
   

    for key, Kcolor in matrix.items():
        Lcolor = "red" if Kcolor else "green"
        draw_rectt(key[0], key[1], Lcolor)

    draw_grid(x,y,n)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break


pygame.quit()