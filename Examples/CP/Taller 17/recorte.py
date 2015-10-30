import sys, pygame, time
pygame.init()

size = alto, ancho = 300, 300
color = 255,255,255

Pantalla = pygame.display.set_mode(size)

imagenFondo = pygame.image.load("gatos.jpg")
imagenrect = imagenFondo.get_rect()

Pantalla.fill(color)

Pantalla.blit(imagenFondo, imagenrect)
pygame.display.flip()


def corte(Xmin, Xmax, Ymin, Ymax):
    i = 0
    f = 0
    for i in range(alto):
        for f in range(ancho):
            if ((f < Ymin) or (f > Ymax) or (i < Xmin) or (i > Xmax)):
                Pantalla.set_at((i, f), color)
                
        k = 0

    
pygame.time.delay(1000)
corte (0, 150, 0, 150)
pygame.display.flip()
pygame.time.delay(1000)

Pantalla.blit(imagenFondo, imagenrect)
pygame.display.flip()
pygame.time.delay(1000)

corte (150, 300, 0, 150)
pygame.display.flip()
pygame.time.delay(1000)

Pantalla.blit(imagenFondo, imagenrect)
pygame.display.flip()
pygame.time.delay(1000)

corte (0, 150, 150, 300)
pygame.display.flip()
pygame.time.delay(1000)

Pantalla.blit(imagenFondo, imagenrect)
pygame.display.flip()
pygame.time.delay(1000)

corte (150, 300, 150, 300)
pygame.display.flip()
pygame.time.delay(1000)

Pantalla.blit(imagenFondo, imagenrect)
pygame.display.flip()
pygame.time.delay(1000)

corte (50, 250, 50, 250)
pygame.display.flip()
pygame.time.delay(1000)

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
