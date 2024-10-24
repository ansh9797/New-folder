import pygame

pygame.init()

screen = pygame.display.set_mode((400,300))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            done = True

    pygame.draw.rect(screen,(0,200,14),pygame.Rect(30,30,60,60))
    pygame.draw.circle(screen,(0,255,0),(300,150),50)
    pygame.draw.circle(screen,(0,255,0),(200,150),50,3)
    pygame.draw.line(screen,(255,0,0),(0,50),(100,150),3)
    pygame.display.flip()
