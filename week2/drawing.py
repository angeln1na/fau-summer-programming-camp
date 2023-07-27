import pygame#import the library 
pygame.init()#intailize the pygame library


screen = pygame.display.set_mode([500, 500])


running = True# set running equals to True
while running:

    
    for event in pygame.event.get():#create a for loop where event in pygame.event.get()
        if event.type == pygame.QUIT:
            running = False#set running equals to False

   
    screen.fill((255, 255, 255)) #pass 255 three times in screen.fill

   
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    #
    pygame.display.flip()


pygame.quit()#quit pygam 