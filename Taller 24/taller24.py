'''
Taller 24
1- Mover una imagen por la pantalla usando el teclado

2- Permitirque una imagen (2) se mueva de forma aleatoria
por la pantalla
 
3- En el momento en que las dos imagenes se choquen, se debe producir un sonido

http://developeando.net/tutorial-pygame-colisiones/
http://developeando.net/tutorial-pygame-musica-sonidos/
'''
import pygame,time,random
from pygame.locals import *
import sys

ANCHO = 1066
ALTO = 600


pygame.init()
#Creacion de ventana
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Movimiento")

#Cargar fondo
fondo = pygame.image.load("Fondo.jpg").convert()
tux = pygame.image.load("tux.png").convert_alpha()
tux2 = pygame.image.load("tux2.png").convert_alpha()

tux_x= 300  
tux_y= 200
tux_x2= 300  
tux_y2= 200

sprite1 = pygame.sprite.Sprite()
sprite1.image = tux
sprite1.rect = tux.get_rect()

sprite2 = pygame.sprite.Sprite()
sprite2.image = tux2
sprite2.rect = tux2.get_rect()

sprite1.rect.top = tux_y
sprite1.rect.left = tux_x
sprite2.rect.top = tux_y2
sprite2.rect.left = tux_x2

screen.blit(fondo, (0,0))
screen.blit(tux, (sprite1.rect.left, sprite1.rect.top))

screen.blit(fondo, (0,0))
screen.blit(tux2, (sprite2.rect.left, sprite2.rect.top))
pygame.display.flip()

 
pygame.mixer.music.load("sables.mp3")


while True:
    tecla = pygame.key.get_pressed()

    for event in pygame.event.get():
        sprite2.rect.left = random.randint(0, 1066)
        sprite2.rect.top = random.randint(0, 600)
        screen.blit(fondo, (0,0))
        screen.blit(tux, (sprite1.rect.left, sprite1.rect.top))
        screen.blit(tux2, (sprite2.rect.left,sprite2.rect.top))
        pygame.mixer.music.stop()
        pygame.display.flip()

        if tecla[K_LEFT]:
            sprite1.rect.left = sprite1.rect.left - 20
            if sprite1.rect.left < 0:
                sprite1.rect.left = 1066

        if tecla[K_RIGHT]:
            sprite1.rect.left = sprite1.rect.left+20
            if sprite1.rect.left > 1066:
                sprite1.rect.left = 0
        
        if tecla[K_UP]:
            sprite1.rect.top = sprite1.rect.top-20
            if sprite1.rect.top < 0:
                sprite1.rect.top = 600

        if tecla[K_DOWN]:
            sprite1.rect.top = sprite1.rect.top+20
            if sprite1.rect.top > 600:
                sprite1.rect.top = 0

        if pygame.sprite.collide_rect(sprite1, sprite2):
            pygame.mixer.music.play(1)

        if tecla[K_ESCAPE] or event.type == pygame.QUIT:
            raise SystemExit
	

if __name__ == "__main__":
    main()