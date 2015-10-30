import pygame
from pygame.locals import *
import sys

class Sprite(pygame.sprite.Sprite):
    def __init__(self, imagefile, rect):
        pygame.sprite.Sprite.__init__(self)

        self.setPosition(0, 0)

        self.spritesheet = pygame.image.load(imagefile)
        self.setRect(rect)

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



def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

def dibujar_mapa():
    mapa = []

    archivo = open('mapa.txt', 'r')

    for line in archivo:
        mapa.append(line)

    return mapa

#Hero 
hero_mov_down = [ pygame.Rect(3, 3, 18, 30), \
              pygame.Rect(23, 4, 17, 29), \
              pygame.Rect(42, 4, 17, 29), ]

hero_mov_left = [ pygame.Rect(61, 3, 16, 30), \
              pygame.Rect(79, 4, 20, 29), \
              pygame.Rect(101, 4, 20, 29), ]

hero_mov_right = [ pygame.Rect(123, 3, 16, 30), \
              pygame.Rect(141, 4, 20, 29), \
              pygame.Rect(163, 4, 20, 29), ]

hero_mov_up = [ pygame.Rect(185, 4, 16, 29), \
              pygame.Rect(203, 5, 16, 28), \
              pygame.Rect(221, 5, 16, 28), ]

#rival1
rival1_mov_up = [ pygame.Rect(3, 8, 19, 25), \
              pygame.Rect(24, 6, 19, 27), \
              pygame.Rect(45, 3, 19, 30), \
              pygame.Rect(66, 6, 19, 27)]

rival1_mov_right = [ pygame.Rect(3, 8, 19, 25), \
              pygame.Rect(24, 6, 19, 27), \
              pygame.Rect(45, 3, 19, 30), \
              pygame.Rect(66, 6, 19, 27)]

rival1_mov_left = [ pygame.Rect(87, 8, 18, 25), \
              pygame.Rect(108, 6, 19, 27), \
              pygame.Rect(129, 3, 19, 30), \
              pygame.Rect(150, 6, 19, 27)]

rival1_mov_down = [ pygame.Rect(87, 8, 18, 25), \
              pygame.Rect(108, 6, 19, 27), \
              pygame.Rect(129, 3, 19, 30), \
              pygame.Rect(150, 6, 19, 27)]

rival1_muerto = [ pygame.Rect(171, 7, 20, 22), \
              pygame.Rect(193, 7, 18, 20), \
              pygame.Rect(213, 9, 14, 16), \
              pygame.Rect(229, 10, 12, 14), \
              pygame.Rect(243, 8, 16, 18) ]

#rival2
rival2_mov_up = [ pygame.Rect(3, 42, 20, 23), \
              pygame.Rect(25, 41, 19, 24), \
              pygame.Rect(46, 42, 20, 23), \
              pygame.Rect(68, 41, 19, 24) ]

rival2_mov_right = [ pygame.Rect(3, 42, 20, 23), \
              pygame.Rect(25, 41, 19, 24), \
              pygame.Rect(46, 42, 20, 23), \
              pygame.Rect(68, 41, 19, 24) ]

rival2_mov_left = [ pygame.Rect(89, 42, 20, 23), \
              pygame.Rect(111, 41, 19, 24), \
              pygame.Rect(132, 42, 20, 23), \
              pygame.Rect(154, 41, 19, 24) ]

rival2_mov_down = [ pygame.Rect(89, 42, 20, 23), \
              pygame.Rect(111, 41, 19, 24), \
              pygame.Rect(132, 42, 20, 23), \
              pygame.Rect(154, 41, 19, 24) ]

rival2_muerto = [ pygame.Rect(175, 38, 20, 24), \
              pygame.Rect(197, 42, 18, 20), \
              pygame.Rect(217, 44, 14, 16), \
              pygame.Rect(233, 45, 12, 14), \
              pygame.Rect(247, 44, 16, 18) ]


#................................PANTALLA..................................

#Dimensiones
ANCHO = 648
ALTO = 657
#Iniciar Pygame
pygame.init()
#Creacion de ventana
screen = pygame.display.set_mode((ANCHO, ALTO))
#Titulo de la pantalla de seleccion
pygame.display.set_caption("...Laberinto...")

#Cargar fondo y Sprites estaticos
fondo = pygame.image.load("fondo.png").convert()
screen.blit(fondo, (0,-9))

  #Personajes
hero = Sprite("hero.png", pygame.Rect(3, 3, 18, 30))
bloque = Sprite("bloque.png", pygame.Rect(0, 0, 18, 18))
pasto = Sprite("pasto.png", pygame.Rect(0, 0, 18, 18))
cemento = Sprite("cemento.png", pygame.Rect(0, 0, 18, 18))
rival1 = Rival("rival1.png")
rival2 = Rival("rival2.png")
corazon = Sprite("objetos.png", pygame.Rect(71, 5, 16, 16))

clock = pygame.time.Clock()

#Posicionamiento de los Sprites estaticos
  #Personajes
hero.setPosition(0, 0)

tux_x = 0
tux_y = 0

#Posicionamiento del fondo de pantalla
screen.blit(fondo, (0,0))
  #Mostrar Sprites en pantalla
hero.draw(screen)

pygame.display.flip()
num_frame = 0 
puntos = 0

#..........................MAPA...............................

laberinto = dibujar_mapa() 
pos_x = 0
pos_y = 9

'''for i in laberinto:
    print i
    for j in i:
        if j == '#':
            bloque.setPosition(pos_x, pos_y)
            bloque.draw(screen)
            pygame.display.flip()
        else:
            if j == '.':
                pasto.setPosition(pos_x, pos_y)
                pasto.draw(screen)
                pygame.display.flip()
            else:
                cemento.setPosition(pos_x, pos_y)
                cemento.draw(screen)
                pygame.display.flip()
        pos_x += 18
    pos_x = 0
    pos_y += 18'''

while True:
    tecla = pygame.key.get_pressed()

    if tecla[K_LEFT]:
        if num_frame >= len(hero_mov_left):
            num_frame = 0
        hero.setRect(hero_mov_left[num_frame])
        pygame.display.flip()
        num_frame += 1
        if (tux_x/18)-1 >= 0 and laberinto[tux_y/18][(tux_x/18)-1] == '.' or laberinto[tux_y/18][(tux_x/18)-1] == '*':
            tux_x = tux_x-18
        '''else:
            if laberinto[tux_y/18][(tux_x/18)-1] == '1':
                puntos += 10
                laberinto[tux_y/18].replace("1", ".")
                tux_x = tux_x-18
            else:
                if laberinto[tux_y/18][(tux_x/18)-1] == '2':
                    puntos += 20
                    laberinto[tux_y/18].replace("2", ".")
                    tux_x = tux_x-18'''

        if tux_x < 0:
            tux_x = 0
        clock.tick(7)
        screen.blit(fondo, (0,0))
        hero.setPosition(tux_x,tux_y)
        hero.draw(screen)  
        pos = "LEFT"                       
        pygame.display.flip()

    if tecla[K_RIGHT]:
        if num_frame >= len(hero_mov_right):
            num_frame = 0
        hero.setRect(hero_mov_right[num_frame])
        pygame.display.flip()
        num_frame += 1
        if laberinto[tux_y/18][(tux_x/18)+1] == '.' or laberinto[tux_y/18][(tux_x/18)+1] == '*':
            tux_x = tux_x+18

        '''else:
            if laberinto[tux_y/18][(tux_x/18)+1] == '1':
                puntos += 10
                laberinto[(tux_x/18)+1].replace("1", ".")

                tux_x = tux_x+18
            else:
                if laberinto[tux_y/18][(tux_x/18)+1] == '2':
                    puntos += 20
                    laberinto[tux_y/18].replace("2", ".")
                    tux_x = tux_x+18 '''

        if tux_x > 630:
            tux_x = 630
        clock.tick(7)
        screen.blit(fondo, (0,0))
        hero.setPosition(tux_x,tux_y)
        hero.draw(screen)  
        pos = "RIGHT"                       
        pygame.display.flip()
        print puntos


    if tecla[K_DOWN]:
        if num_frame >= len(hero_mov_down):
            num_frame = 0
        hero.setRect(hero_mov_down[num_frame])
        pygame.display.flip()
        num_frame += 1

        if laberinto[(tux_y/18)+1][tux_x/18] == '.' or laberinto[(tux_y/18)+1][tux_x/18] == '*':
            tux_y = tux_y+18
        '''else:
            if laberinto[(tux_y/18)+1][tux_x/18] == '1':
                puntos += 10
                laberinto[(tux_y/18)+1].replace("1", ".")
                tux_y = tux_y+18
            else:
                if laberinto[(tux_y/18)+1][tux_x/18] == '2':
                    puntos += 20
                    laberinto[(tux_y/18)+1].replace("2", ".")
                    tux_y = tux_y+18'''
        
        if tux_y > 648:
            tux_y = 648
        clock.tick(7)
        screen.blit(fondo, (0,0))
        hero.setPosition(tux_x,tux_y)
        hero.draw(screen)  
        pos = "DOWN"                       
        pygame.display.flip()

    if tecla[K_UP]:
        if num_frame >= len(hero_mov_up):
            num_frame = 0
        hero.setRect(hero_mov_up[num_frame])
        pygame.display.flip()
        num_frame += 1

        if laberinto[(tux_y/18)-1][tux_x/18] == '.' or laberinto[(tux_y/18)-1][tux_x/18] == '*':
            tux_y = tux_y-18
        '''else:
            if laberinto[(tux_y/18)-1][tux_x/18] == '1':
                puntos += 10
                laberinto[(tux_y/18)-1].replace("1", ".")
                tux_y = tux_y-18
            else:
                if laberinto[(tux_y/18)-1][tux_x/18] == '2':
                    puntos += 20
                    laberinto[(tux_y/18)-1].replace("2", ".")
                    tux_y = tux_y-18'''

        if tux_y < 0:
            tux_y = 0
        clock.tick(7)
        screen.blit(fondo, (0,0))
        hero.setPosition(tux_x,tux_y)
        hero.draw(screen)  
        pos = "UP"                       
        pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT or tecla[K_ESCAPE]: 
            raise SystemExit











