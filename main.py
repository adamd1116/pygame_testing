import pygame, sys
pygame.init()

size = width, height = 1000, 1000
black = 0, 100, 0 #Black screens with fast moving images make the trail more noticeable. This color is dark green
speed = [1,1]

screen = pygame.display.set_mode(size)

funnyimage = pygame.image.load("lolol.png")
funnyimagerect = funnyimage.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    funnyimagerect = funnyimagerect.move(speed)
    if funnyimagerect.left < 0 or funnyimagerect.right > width:
        speed[0] = -speed[0]
    if funnyimagerect.top < 0 or funnyimagerect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(funnyimage, funnyimagerect)
    pygame.display.flip()
    
