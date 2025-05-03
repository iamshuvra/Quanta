import pygame

#configurations

GRID_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 50
SCREEN_WIDTH = GRID_SIZE*GRID_WIDTH
SCREEN_HEIGHT = GRID_SIZE*GRID_HEIGHT

#colors
WHITE = (255, 255, 255)
BLUE = (0, 102, 204)
GREY = (200, 200, 200)

#initialize
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scout Bot - A world")
clock = pygame.time.Clock()

#where to start the robo
roboX = 1
roboY = 1

running = True

while running:
    for event in pygame.event.get():
        if(event.type) == pygame.QUIT:
            running = False
    
    # draw background
    screen.fill(WHITE)

    # draw grid
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            rectg = pygame.Rect(x*GRID_SIZE, y*GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, GREY, rectg, 1)
    
    # draw the robot
    roboRectg = pygame.Rect(roboX*GRID_SIZE, roboY*GRID_SIZE, GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, BLUE, roboRectg, 0)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()


