import pygame
pygame.init()
screen = pygame.display.set_mode([500, 600])
pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption('PyPaint')
running = True
currentColour = (0,0,0)
brush = "circle"
cursorX = 0
cursorY = 0
size = 15
isEraser = False
canvas = screen.subsurface(0,0,500,500)
pygame.font.init()
text = pygame.font.SysFont('Courier New', 45)
def ui():
    screen.fill((150,150,150), rect=(0,500,500,100))
    screen.fill((currentColour), rect=(0,500,100,100))
    if brush == "circle":
        pygame.draw.circle(screen, currentColour, (250,550), 25,25)
    elif brush == "square":
        pygame.draw.rect(screen, currentColour, pygame.Rect(225,525,50,50))
    elif brush == "line":
        pygame.draw.rect(screen, currentColour, pygame.Rect(225,550,50,10))
    if isEraser == True:
        pygame.draw.circle(screen, (255,255,255), (250,550), 25,25)

    screen.blit(text.render(str(size), False, (0, 0, 0)), (425,525))

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

            if event.key == pygame.K_BACKSPACE:
                screen.fill((255,255,255))
            if event.key == pygame.K_s:
                if brush == "square":
                    brush = "circle"
                elif brush == "circle":
                    brush = "line"
                elif brush == "line":
                    brush = "square"
            if event.key == pygame.K_EQUALS:
                size += 2
            if event.key == pygame.K_MINUS:
                size -= 2
            if event.key == pygame.K_e:
                if isEraser == False:
                    isEraser = True
                elif isEraser == True:
                    isEraser = False
            if event.key == pygame.K_SPACE:
                pygame.image.save(canvas, "art.jpeg")

    buttons = pygame.mouse.get_pressed()
    if any(buttons):
        if brush == "circle" and isEraser == False:
            pygame.draw.circle(screen, currentColour, cursor, size)
        if brush == "square" and isEraser == False:
            pygame.draw.rect(screen, currentColour, pygame.Rect(cursorX-(0.5*size), cursorY-(0.5*size), size, size))
        if brush == "line" and isEraser == False:
            pygame.draw.line(screen, currentColour, cursor, (cursorX + size, cursorY), int((size/2)))
        if isEraser == True:
            pygame.draw.circle(screen, (255,255,255), cursor, size)


    ui()
    cursorX = pygame.mouse.get_pos()[0]
    cursorY = pygame.mouse.get_pos()[1]
    cursor = pygame.mouse.get_pos()



    pygame.display.flip()
pygame.quit()