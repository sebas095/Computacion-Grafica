import pygame
from pygame.locals import *
import sys

class Sprite(pygame.sprite.Sprite):
    def __init__(self, imagefile, rect):
        pygame.sprite.Sprite.__init__(self)

        self.setPosition(0, 0)
        self.spritesheet = pygame.image.load(imagefile)
        self.setRect(rect)
        self.rect = self.image.get_rect()

    def setPosition(self, x, y):
        self.x = x
        self.y = y
        
    def setRect(self, rect):
        self.image = self.spritesheet.subsurface(rect)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Rival(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()

def load_image(filename, transparent = False):
    try:
        image = pygame.load.image(filename)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    if transparent:
        color = image.get_at((0,0),RLEACCEL)
    return image

def draw_map():
    mapa = []

    archivo = open('mapa.txt','r')
    for line in archivo:
        mapa.append(line)

    return mapa

#-------------------------------------------------------------------
#personaje
personaje_down = [  pygame.Rect(3, 3, 18, 30), \
                    pygame.Rect(23, 4, 17, 29), \
                    pygame.Rect(42, 4, 17, 29), ]

personaje_left = [  pygame.Rect(61, 3, 16, 30), \
                    pygame.Rect(79, 4, 20, 29), \
                    pygame.Rect(101, 4, 20, 29), ]

personaje_right = [   pygame.Rect(123, 3, 16, 30), \
                      pygame.Rect(141, 4, 20, 29), \
                      pygame.Rect(163, 4, 20, 29), ]

personaje_up = [  pygame.Rect(185, 4, 16, 29), \
                  pygame.Rect(203, 5, 16, 28), \
                  pygame.Rect(221, 5, 16, 28), ]

#................................PANTALLA..................................
aux = 0
#Dimensiones
ANCHO = 648
ALTO = 694
#Reloj
clock = pygame.time.Clock()

pygame.init()
#creacion de ventana y titulo de la ventana
pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("LABERINTO :D")

#Cargar fondo y sonidos
pygame.mixer.music.load("intro.mp3")
pygame.mixer.music.play(1)
fondo_intro = pygame.image.load("intro.png").convert()
pantalla.blit(fondo_intro,(0,-9))
pygame.display.flip()
pygame.time.wait(1000)

fondo_instrucciones = pygame.image.load("instrucciones.png").convert()
pantalla.blit(fondo_instrucciones,(0,-9))
pygame.display.flip()
pygame.time.wait(2000)

pygame.mixer.music.stop()
fondo_fin = pygame.image.load("fin.png").convert()

pygame.mixer.music.load("inicio.mp3")
pygame.mixer.music.play(1)

fondo = pygame.image.load("fondo.png").convert()
pantalla.blit(fondo,(0,-9))

personaje = Sprite("hero.png",pygame.Rect(3, 3, 18, 30))
personaje.setPosition(0,0)

#Posicion del jugador y pantalla
personaje_x = 0
personaje_y = 0
pantalla.blit(fondo,(0,0))
personaje.draw(pantalla)
pygame.display.flip()

num_frame = 0

#..........................MAPA...............................

laberinto = draw_map()
pos_x = 0
pos_y = 0
fin = False

while not fin:
    tecla = pygame.key.get_pressed()

    #Movimiento a la izquierda
    if tecla[K_LEFT]:
        if num_frame >= len(personaje_left):
            num_frame = 0
        personaje.setRect(personaje_left[num_frame])
        pygame.display.flip()
        num_frame += 1
        if(personaje.rect.x/18)-1 >= 0 and laberinto[personaje.rect.y/18][(personaje.rect.x/18)-1] == '.' or laberinto[personaje.rect.y/18][(personaje.rect.x/18)-1] == '*':
            personaje.rect.x -= 18

        if personaje.rect.x < 0:
            personaje.rect.x = 0
        clock.tick(7)
        pantalla.blit(fondo,(0,0))
        personaje.setPosition(personaje.rect.x,personaje.rect.y)
        personaje.draw(pantalla)
        pos = "LEFT"
        pygame.display.flip()

    #Movimiento a la derecha
    if tecla[K_RIGHT]:
        if num_frame >= len(personaje_right):
            num_frame = 0
        personaje.setRect(personaje_right[num_frame])
        pygame.display.flip()
        num_frame += 1
        if laberinto[personaje.rect.y/18][(personaje.rect.x/18)+1] == '.' or laberinto[personaje.rect.y/18][(personaje.rect.x/18)+1] == '*':
            personaje.rect.x += 18

        if personaje.rect.x > 630:
            personaje.rect.x = 630
        clock.tick(7)
        pantalla.blit(fondo,(0,0))
        personaje.setPosition(personaje.rect.x,personaje.rect.y)
        personaje.draw(pantalla)
        pos = "RIGHT"
        pygame.display.flip()

    #Movimiento hacia abajo
    if tecla[K_DOWN]:
        if num_frame >= len(personaje_down):
            num_frame = 0
        personaje.setRect(personaje_down[num_frame])
        pygame.display.flip()
        num_frame += 1

        if laberinto[(personaje.rect.y/18)+1][personaje.rect.x/18] == '.' or laberinto[(personaje.rect.y/18)+1][personaje.rect.x/18] == '*':
            personaje.rect.y = personaje.rect.y+18

        if personaje.rect.y > 648:
            personaje.rect.y = 648
        clock.tick(7)
        pantalla.blit(fondo,(0,0))
        personaje.setPosition(personaje.rect.x,personaje.rect.y)
        personaje.draw(pantalla)
        pos = "DOWN"
        pygame.display.flip()

    #Movimiento hacia arriba
    if tecla[K_UP]:
        if num_frame >= len(personaje_up):
            num_frame = 0
        personaje.setRect(personaje_up[num_frame])
        pygame.display.flip()
        num_frame += 1

        if laberinto[(personaje.rect.y/18)-1][personaje.rect.x/18] == '.' or laberinto[(personaje.rect.y/18)-1][personaje.rect.x/18] == '*':
            personaje.rect.y = personaje.rect.y-18

        if personaje.rect.y < 0:
            personaje.rect.y = 0
        clock.tick(7)
        pantalla.blit(fondo,(0,0))
        personaje.setPosition(personaje.rect.x,personaje.rect.y)
        personaje.draw(pantalla)
        pos = "UP"
        pygame.display.flip()

    if personaje.rect.x >= 532 and personaje.rect.y >= 630:
        pantalla.blit(fondo_fin,(0,0))
        pygame.display.flip()
        pygame.mixer.music.load("fin.mp3")
        pygame.mixer.music.play(1)
        pygame.time.wait(6000)
        fin = True
        raise SystemExit

    for event in pygame.event.get():
          
        #Salida
        if event.type == pygame.QUIT or tecla[K_ESCAPE]:
            pantalla.blit(fondo_fin,(0,0))
            pygame.display.flip()
            pygame.mixer.music.load("fin.mp3")
            pygame.mixer.music.play(1)
            pygame.time.wait(6000)
            fin = True
            raise SystemExit 