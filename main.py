import pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])
running = True
currentColour = (0,0,0)

screen.fill((255, 255, 255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                currentColour = (0,0,0)
            if event.key == pygame.K_2:
                currentColour = (255,0,0)
            if event.key == pygame.K_3:
                currentColour = (0,255,0)
            if event.key == pygame.K_1:
                currentColour = (0,0,255)
            
    cursor = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()


    if any(buttons): 
        pygame.draw.circle(screen, currentColour, cursor, 15)
        
    pygame.display.flip()

pygame.quit()