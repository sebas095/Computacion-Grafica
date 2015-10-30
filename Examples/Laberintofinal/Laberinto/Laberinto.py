#Alejandro Esteban Rendon Diosa
#Laberinto - Bomberman
#Computacion Grafica
#INGENIERIA DE SISTEMAS Y COMPUTACION
#UNIVERSIDAD TECNOLOGICA DE PEREIRA

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


#-------------------------------------------------------------------
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

hero_muerto = [ pygame.Rect(3, 75, 20, 27), \
              pygame.Rect(25, 75, 20, 27), \
              pygame.Rect(47, 75, 20, 27), \
              pygame.Rect(69, 74, 20, 26), \
              pygame.Rect(91, 75, 20, 24), \
              pygame.Rect(113, 73, 20, 25), \
              pygame.Rect(135, 78, 20, 19),]

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
rival2_mov_up = [ pygame.Rect(3, 8, 19, 25), \
              pygame.Rect(24, 6, 19, 27), \
              pygame.Rect(45, 3, 19, 30), \
              pygame.Rect(66, 6, 19, 27)]

rival2_mov_right = [ pygame.Rect(3, 8, 19, 25), \
              pygame.Rect(24, 6, 19, 27), \
              pygame.Rect(45, 3, 19, 30), \
              pygame.Rect(66, 6, 19, 27)]

rival2_mov_left = [ pygame.Rect(87, 8, 18, 25), \
              pygame.Rect(108, 6, 19, 27), \
              pygame.Rect(129, 3, 19, 30), \
              pygame.Rect(150, 6, 19, 27)]

rival2_mov_down = [ pygame.Rect(87, 8, 18, 25), \
              pygame.Rect(108, 6, 19, 27), \
              pygame.Rect(129, 3, 19, 30), \
              pygame.Rect(150, 6, 19, 27)]

rival2_muerto = [ pygame.Rect(171, 7, 20, 22), \
              pygame.Rect(193, 7, 18, 20), \
              pygame.Rect(213, 9, 14, 16), \
              pygame.Rect(229, 10, 12, 14), \
              pygame.Rect(243, 8, 16, 18) ]

#rival3
rival3_mov_up = [ pygame.Rect(3, 42, 20, 23), \
              pygame.Rect(25, 41, 19, 24), \
              pygame.Rect(46, 42, 20, 23), \
              pygame.Rect(68, 41, 19, 24) ]

rival3_mov_right = [ pygame.Rect(3, 42, 20, 23), \
              pygame.Rect(25, 41, 19, 24), \
              pygame.Rect(46, 42, 20, 23), \
              pygame.Rect(68, 41, 19, 24) ]

rival3_mov_left = [ pygame.Rect(89, 42, 20, 23), \
              pygame.Rect(111, 41, 19, 24), \
              pygame.Rect(132, 42, 20, 23), \
              pygame.Rect(154, 41, 19, 24) ]

rival3_mov_down = [ pygame.Rect(89, 42, 20, 23), \
              pygame.Rect(111, 41, 19, 24), \
              pygame.Rect(132, 42, 20, 23), \
              pygame.Rect(154, 41, 19, 24) ]

rival3_muerto = [ pygame.Rect(175, 38, 20, 24), \
              pygame.Rect(197, 42, 18, 20), \
              pygame.Rect(217, 44, 14, 16), \
              pygame.Rect(233, 45, 12, 14), \
              pygame.Rect(247, 44, 16, 18) ]

#Boss muerto
boss_muerto = [ pygame.Rect(3, 53, 50, 45), \
              pygame.Rect(56, 53, 49, 45), \
              pygame.Rect(108, 53, 49, 45), \
              pygame.Rect(160, 54, 44, 39), \
              pygame.Rect(207, 58, 44, 32), \
              pygame.Rect(254, 61, 34, 25), \
              pygame.Rect(291, 62, 19, 22), \
              pygame.Rect(313, 59, 26, 27) ]

boss_mov = [ pygame.Rect(3, 3, 47, 45), \
              pygame.Rect(53, 3, 40, 45), \
              pygame.Rect(96, 4, 34, 41), \
              pygame.Rect(133, 3, 27, 43), \
              pygame.Rect(163, 3, 17, 43), \
              pygame.Rect(183, 3, 28, 43), \
              pygame.Rect(214, 4, 36, 40), \
              pygame.Rect(253, 3, 40, 41), \
              pygame.Rect(296, 3, 48, 41), \
              pygame.Rect(347, 3, 40, 41), \
              pygame.Rect(390, 4, 36, 40), \
              pygame.Rect(429, 3, 28, 43), \
              pygame.Rect(460, 3, 17, 43), \
              pygame.Rect(480, 3, 27, 43), \
              pygame.Rect(510, 4, 34, 41), \
              pygame.Rect(547, 3, 40, 45)]

#Explosion
explosion_mov  = [ pygame.Rect(65, 107, 20, 20), \
              pygame.Rect(87, 108, 19, 18), \
              pygame.Rect(108, 107, 18, 19), \
              pygame.Rect(128, 107, 18, 19), \
              pygame.Rect(148, 107, 17, 19), \
              pygame.Rect(167, 109, 16, 16), \
              pygame.Rect(185, 109, 15, 17)]

#................................PANTALLA..................................

aux = 0

#Dimensiones
ANCHO = 648
ALTO = 694
#Reloj
clock = pygame.time.Clock()

#Iniciar Pygame
pygame.init()
#Creacion de ventana
screen = pygame.display.set_mode((ANCHO, ALTO))
#Titulo de la pantalla de seleccion
pygame.display.set_caption("...Laberinto...")

#Cargar fondo y Sprites estaticos
pygame.mixer.music.load("intro.mp3")
pygame.mixer.music.play(1)
fondo_intro = pygame.image.load("intro.png").convert()
screen.blit(fondo_intro, (0,-9))
pygame.display.flip()
pygame.time.wait(1000)

fondo_instrucciones = pygame.image.load("instrucciones.png").convert()
screen.blit(fondo_instrucciones, (0,-9))
pygame.display.flip()
pygame.time.wait(2000)

pygame.mixer.music.stop()
fondo_fin = pygame.image.load("fin.png").convert()

pygame.mixer.music.load("inicio.mp3")
pygame.mixer.music.play(1)

fondo = pygame.image.load("fondo.png").convert()
screen.blit(fondo, (0,-9))

#Fuente
fuente = pygame.font.Font(None, 36)


  #Personajes
hero = Sprite("hero.png", pygame.Rect(3, 3, 18, 30))
bloque = Sprite("bloque.png", pygame.Rect(0, 0, 18, 18))
pasto = Sprite("pasto.png", pygame.Rect(0, 0, 18, 18))
cemento = Sprite("cemento.png", pygame.Rect(0, 0, 18, 18))

boss = Sprite("boss.png", pygame.Rect(3, 3, 46, 45))

rival1 = Sprite("rivales.png", pygame.Rect(4, 8, 18, 25))
rival2 = Sprite("rivales.png", pygame.Rect(4, 8, 18, 25))
rival3 = Sprite("rivales.png", pygame.Rect(3, 42, 20, 23))

corazon2 = Sprite("objetos.png", pygame.Rect(71, 5, 16, 16))
corazon3 = Sprite("objetos.png", pygame.Rect(71, 5, 16, 16))
corazon4 = Sprite("objetos.png", pygame.Rect(71, 5, 16, 16))
corazon5 = Sprite("objetos.png", pygame.Rect(71, 5, 16, 16))

time1 = corazon1 = Sprite("objetos.png", pygame.Rect(94, 6, 14, 14))
time2 = corazon1 = Sprite("objetos.png", pygame.Rect(94, 6, 14, 14))
time3 = corazon1 = Sprite("objetos.png", pygame.Rect(94, 6, 14, 14))

bala = Sprite("objetos.png", pygame.Rect(27, 6, 14, 14))

bala1 = Sprite("objetos.png", pygame.Rect(27, 6, 14, 14))
bala2 = Sprite("objetos.png", pygame.Rect(27, 6, 14, 14))
bala3 = Sprite("objetos.png", pygame.Rect(27, 6, 14, 14))

explosion = Sprite("hero.png", pygame.Rect(65, 107, 20, 20))


#Posicionamiento de los Sprites estaticos
#Personajes
hero.setPosition(0, 0)

#Posicion del jugador
tux_x = 0
tux_y = 0
#Posicion de la bala
pos_bala_x = 0
pos_bala_y = 0

#Posicionamiento del fondo de pantalla
screen.blit(fondo, (0,0))
  #Mostrar Sprites en pantalla
hero.draw(screen)

pygame.display.flip()
num_frame = 0 
puntos = 0
balas = 0
corazon_recolec = 0
division = 1000
flag = True



balas_premio = pygame.sprite.Group()
corazones_premio = pygame.sprite.Group()
rivales = pygame.sprite.Group()
boss_lista = pygame.sprite.Group()
rival1_lista = pygame.sprite.Group()
rival2_lista = pygame.sprite.Group()
rival3_lista = pygame.sprite.Group()
time = pygame.sprite.Group()
tl = pygame.sprite.Group()

#Boss
boss.rect.x = 31*18
boss.rect.y = (32*18)
boss_lista.add(boss)
boss.setPosition(31*18, 32*18)
tl.add(boss)

#Rivales
rival1.rect.x = 17*18
rival1.rect.y = (15*18)
rival1_lista.add(rival1)
rival1.setPosition(17*18, 15*18)
tl.add(rival1)

rival2.rect.x = 19*18
rival2.rect.y = (33*18)
rival2_lista.add(rival2)
rival2.setPosition(19*18, 33*18)
tl.add(rival2)

rival3.rect.x = 17*18
rival3.rect.y = (31*18)
rival3_lista.add(rival3)
rival3.setPosition(17*18, 31*18)
tl.add(rival3)

#Balas para recolectar

bala1.rect.x = 3*18
bala1.rect.y = (2*18)+9
balas_premio.add(bala1)
tl.add(bala1)

bala2.rect.x = 5*18
bala2.rect.y = (5*18)+9
balas_premio.add(bala2)
tl.add(bala2)

bala3.rect.x = 19*18
bala3.rect.y = (18*18)+9
balas_premio.add(bala3)
tl.add(bala3)


#Corazones para recolectar
corazon5.rect.x = 11*18
corazon5.rect.y = (16*18)-9
corazones_premio.add(corazon5)
tl.add(corazon5)

corazon2.rect.x = 11*18
corazon2.rect.y = (20*18)-9
corazones_premio.add(corazon2)
tl.add(corazon2)

corazon3.rect.x = 33*18
corazon3.rect.y = (18*18)-9
corazones_premio.add(corazon3)
tl.add(corazon3)

corazon4.rect.x = 5*18
corazon4.rect.y = (16*18)-9
corazones_premio.add(corazon4)
tl.add(corazon4)

#Tiempo
time1.rect.x = 17*18
time1.rect.y = (10*18)-9
time.add(time1)
tl.add(time1)

time2.rect.x = 7*18
time2.rect.y = (36*18)-9
time.add(time2)
tl.add(time2)

time3.rect.x = 23*18
time3.rect.y = (24*18)-9
time.add(time3)
tl.add(time3)

tl.add(hero)

#..........................MAPA...............................

laberinto = dibujar_mapa() 
pos_x = 0
pos_y = 9

'''#Dibujar mapa desde archivo txt
for i in laberinto:
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

fin = False

while not fin:
    

    tecla = pygame.key.get_pressed()

    #Movimiento a la izquierda
    if tecla[K_LEFT]:
        
        if num_frame >= len(hero_mov_left):
            num_frame = 0
        hero.setRect(hero_mov_left[num_frame])
        pygame.display.flip()
        num_frame += 1
        if (hero.rect.x/18)-1 >= 0 and laberinto[hero.rect.y/18][(hero.rect.x/18)-1] == '.' or laberinto[hero.rect.y/18][(hero.rect.x/18)-1] == '*':
            #tux_x = tux_x-18
            hero.rect.x -= 12

        if hero.rect.x < 0:
            hero.rect.x = 0
        clock.tick(7)
        screen.blit(fondo, (0,0))
        hero.setPosition(hero.rect.x, hero.rect.y)
        #hero.draw(screen)  
        tl.draw(screen)
        pos = "LEFT"                       
        pygame.display.flip()

    #Moviento a la derecha
    if tecla[K_RIGHT]:
        if num_frame >= len(hero_mov_right):
            num_frame = 0
        hero.setRect(hero_mov_right[num_frame])
        pygame.display.flip()
        num_frame += 1
        if laberinto[hero.rect.y/18][(hero.rect.x/18)+1] == '.' or laberinto[hero.rect.y/18][(hero.rect.x/18)+1] == '*':
            hero.rect.x += 12


        if hero.rect.x > 630:
            hero.rect.x = 630
        clock.tick(7)
        screen.blit(fondo, (0,0))
        hero.setPosition(hero.rect.x,hero.rect.y)
        #hero.draw(screen)
        tl.draw(screen)  
        pos = "RIGHT"                       
        pygame.display.flip()

    #Movimiento hacia abajo
    if tecla[K_DOWN]:
        if num_frame >= len(hero_mov_down):
            num_frame = 0
        hero.setRect(hero_mov_down[num_frame])
        pygame.display.flip()
        num_frame += 1

        if laberinto[(hero.rect.y/18)+1][hero.rect.x/18] == '.' or laberinto[(hero.rect.y/18)+1][hero.rect.x/18] == '*':
            hero.rect.y = hero.rect.y+12

        
        if hero.rect.y > 648:
            hero.rect.y = 648
        clock.tick(7)
        screen.blit(fondo, (0,0))
        hero.setPosition(hero.rect.x,hero.rect.y)
        #hero.draw(screen)
        tl.draw(screen)  
        pos = "DOWN"                       
        pygame.display.flip()

    #Movimiento hacia arriba
    if tecla[K_UP]:
        if num_frame >= len(hero_mov_up):
            num_frame = 0
        hero.setRect(hero_mov_up[num_frame])
        pygame.display.flip()
        num_frame += 1

        if laberinto[(hero.rect.y/18)-1][hero.rect.x/18] == '.' or laberinto[(hero.rect.y/18)-1][hero.rect.x/18] == '*':
            hero.rect.y = hero.rect.y-12


        if hero.rect.y < 0:
            hero.rect.y = 0
        clock.tick(7)
        screen.blit(fondo, (0,0))
        hero.setPosition(hero.rect.x,hero.rect.y)
        #hero.draw(screen)
        tl.draw(screen)  
        pos = "UP"                       
        pygame.display.flip()


    #Recoger balas-------------------------------------------------------      
    lg = pygame.sprite.spritecollide(hero, balas_premio, True)
    for b in lg:
        pygame.mixer.music.load("bomba.wav")
        pygame.mixer.music.play(1)
        balas += 1
        print puntos

    #Recoger corazones---------------------------------------------------
    lista_corazon = pygame.sprite.spritecollide(hero, corazones_premio, True)
    for cor in lista_corazon:
        pygame.mixer.music.load("corazon.wav")
        pygame.mixer.music.play(1)
        puntos += 100
        corazon_recolec += 1
        print puntos

    if corazon_recolec == 3 and puntos >= 500 and flag:
        pygame.mixer.music.load("corazones_completos.wav")
        pygame.mixer.music.play(1)
        flag = False
    


    #Si se encuentra con el rival1
    lista_rivales = pygame.sprite.spritecollide(hero, rival1_lista, True)

    for riv in lista_rivales:
        cont = 0
        cont2 = 0
        cont3 = 0
        num_frame = 0

        if balas == 0:
            pygame.mixer.music.load("muerte.mp3")
            pygame.mixer.music.play(1)

            while cont < 1:
                if num_frame >= len(hero_muerto):
                    num_frame = 0
                    cont += 1
                else:
                    hero.setRect(hero_muerto[num_frame])
                    clock.tick(5)
                    screen.blit(fondo, (0,0))
                    hero.draw(screen)
                    rival1.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1
            while cont2 < 2:
                if num_frame >= len(rival1_mov_down):
                    num_frame = 0
                    cont2 += 1
                else:
                    rival1.setRect(rival1_mov_down[num_frame])
                    clock.tick(5)
                    screen.blit(fondo, (0,0))
                    rival1.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1

            pygame.mixer.music.load("fin.mp3")
            pygame.mixer.music.play(1)
            screen.blit(fondo_fin, (0,0))  
            pygame.display.flip() 
            pygame.time.wait(6000)  
            fin = True

        else:
            pygame.mixer.music.load("explosion.wav")
            pygame.mixer.music.play(1)
            
            while cont3 < 1:
                if num_frame >= len(explosion_mov):
                    num_frame = 0
                    cont3 += 1
                else:
                    explosion.setRect(explosion_mov[num_frame])
                    clock.tick(5)
                    screen.blit(fondo, (0,0))
                    hero.draw(screen)
                    explosion.setPosition(hero.rect.x, hero.rect.y)
                    explosion.draw(screen)
                    rival1.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1

            while cont < 1:
                if num_frame >= len(rival1_muerto):
                    num_frame = 0
                    cont += 1
                else:
                    rival1.setRect(rival1_muerto[num_frame])
                    clock.tick(7)
                    screen.blit(fondo, (0,0))
                    rival1.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1

            puntos += 200
            balas -= 1

    #Si se encuentra con el rival2
    lista_rivales2 = pygame.sprite.spritecollide(hero, rival2_lista, True)

    for riv in lista_rivales2:
        cont = 0
        cont2 = 0
        cont3 = 0
        num_frame = 0

        if balas == 0:
            pygame.mixer.music.load("muerte.mp3")
            pygame.mixer.music.play(1)

            while cont < 1:
                if num_frame >= len(hero_muerto):
                    num_frame = 0
                    cont += 1
                else:
                    hero.setRect(hero_muerto[num_frame])
                    clock.tick(5)
                    screen.blit(fondo, (0,0))
                    hero.draw(screen)
                    rival2.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1
            while cont2 < 2:
                if num_frame >= len(rival2_mov_down):
                    num_frame = 0
                    cont2 += 1
                else:
                    rival2.setRect(rival2_mov_down[num_frame])
                    clock.tick(5)
                    screen.blit(fondo, (0,0))
                    rival2.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1

            pygame.mixer.music.load("fin.mp3")
            pygame.mixer.music.play(1)
            screen.blit(fondo_fin, (0,0))  
            pygame.display.flip() 
            pygame.time.wait(6000)  
            fin = True

        else:
            pygame.mixer.music.load("explosion.wav")
            pygame.mixer.music.play(1)

            while cont3 < 1:
                if num_frame >= len(explosion_mov):
                    num_frame = 0
                    cont3 += 1
                else:
                    explosion.setRect(explosion_mov[num_frame])
                    clock.tick(5)
                    screen.blit(fondo, (0,0))
                    hero.draw(screen)
                    explosion.setPosition(hero.rect.x, hero.rect.y)
                    explosion.draw(screen)
                    rival1.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1


            while cont < 1:
                if num_frame >= len(rival2_muerto):
                    num_frame = 0
                    cont += 1
                else:
                    rival2.setRect(rival2_muerto[num_frame])
                    clock.tick(7)
                    screen.blit(fondo, (0,0))
                    rival2.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1

            puntos += 200
            balas -= 1        

    #Si se encuentra con el rival3
    lista_rivales3 = pygame.sprite.spritecollide(hero, rival3_lista, True)

    for riv in lista_rivales3:
        cont = 0
        cont2 = 0
        cont3 = 0
        num_frame = 0

        if balas == 0:
            pygame.mixer.music.load("muerte.mp3")
            pygame.mixer.music.play(1)

            while cont < 2:
                if num_frame >= len(hero_muerto):
                    num_frame = 0
                    cont += 1
                else:
                    hero.setRect(hero_muerto[num_frame])
                    clock.tick(5)
                    screen.blit(fondo, (0,0))
                    hero.draw(screen)
                    rival3.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1

            while cont2 < 2:
                if num_frame >= len(rival3_mov_down):
                    num_frame = 0
                    cont2 += 1
                else:
                    rival3.setRect(rival3_mov_down[num_frame])
                    clock.tick(5)
                    screen.blit(fondo, (0,0))
                    rival3.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1

            pygame.mixer.music.load("fin.mp3")
            pygame.mixer.music.play(1)
            screen.blit(fondo_fin, (0,0))  
            pygame.display.flip() 
            pygame.time.wait(6000)  
            fin = True

        else:
            pygame.mixer.music.load("explosion.wav")
            pygame.mixer.music.play(1)

            while cont3 < 1:
                if num_frame >= len(explosion_mov):
                    num_frame = 0
                    cont3 += 1
                else:
                    explosion.setRect(explosion_mov[num_frame])
                    clock.tick(5)
                    screen.blit(fondo, (0,0))
                    hero.draw(screen)
                    explosion.setPosition(hero.rect.x, hero.rect.y)
                    explosion.draw(screen)
                    rival1.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1


            while cont < 1:
                if num_frame >= len(rival3_muerto):
                    num_frame = 0
                    cont += 1
                else:
                    rival3.setRect(rival3_muerto[num_frame])
                    clock.tick(7)
                    screen.blit(fondo, (0,0))
                    rival3.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1

            puntos += 200
            balas -= 1  

    #Si se encuentra con el Boss
    lista_boss = pygame.sprite.spritecollide(hero, boss_lista, True)

    for b in lista_boss:
        cont = 0
        cont2 = 0
        num_frame = 0

        if corazon_recolec < 3 and puntos >= 500:
            pygame.mixer.music.load("muerte.mp3")
            pygame.mixer.music.play(1)

            while cont < 1:
                if num_frame >= len(hero_muerto):
                    num_frame = 0
                    cont += 1
                else:
                    hero.setRect(hero_muerto[num_frame])
                    clock.tick(5)
                    screen.blit(fondo, (0,0))
                    hero.draw(screen)
                    boss.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1

            while cont2 < 2:
                if num_frame >= len(boss_mov):
                    num_frame = 0
                    cont2 += 1
                else:
                    boss.setRect(boss_mov[num_frame])
                    clock.tick(5)
                    screen.blit(fondo, (0,0))
                    boss.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1

            pygame.mixer.music.load("fin.mp3")
            pygame.mixer.music.play(1)
            screen.blit(fondo_fin, (0,0))  
            pygame.display.flip() 
            pygame.time.wait(6000)  
            fin = True



        else:
            pygame.mixer.music.load("explosion.wav")
            pygame.mixer.music.play(1)

            while cont < 1:
                if num_frame >= len(boss_muerto):
                    num_frame = 0
                    cont += 1
                else:
                    boss.setRect(boss_muerto[num_frame])
                    clock.tick(7)
                    screen.blit(fondo, (0,0))
                    boss.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1

            pygame.mixer.music.load("fin.mp3")
            pygame.mixer.music.play(1)
            screen.blit(fondo_fin, (0,0))  
            pygame.display.flip() 
            pygame.time.wait(6000)  
            fin = True
            raise SystemExit
     



    screen.blit(fondo, (0,0))
    tl.draw(screen)
    #clock.tick(60)

    segundos = pygame.time.get_ticks()/division

    if segundos == 60:
        cont = 0

        pygame.mixer.music.load("tiempo.wav")
        pygame.mixer.music.play(1)
        clock.tick(0.5)

        while cont < 1:
            if num_frame >= len(hero_muerto):
                num_frame = 0
                cont += 1
            else:
                hero.setRect(hero_muerto[num_frame])
                clock.tick(5)
                screen.blit(fondo, (0,0))
                hero.draw(screen)
                tl.draw(screen)
                pygame.display.flip()
                num_frame += 1

        screen.blit(fondo_fin, (0,0))  
        pygame.display.flip() 
        pygame.mixer.music.load("fin.mp3")
        pygame.mixer.music.play(1)
        pygame.time.wait(6000)  
        fin = True
        raise SystemExit


    #Si se encuentra con un reloj disminuye la velocidad del conteo del tiempo
    lista_time = pygame.sprite.spritecollide(hero, time, True)
    for t in lista_time:
        pygame.mixer.music.load("corazon.wav")
        pygame.mixer.music.play(1)
        division += 500

    texto = fuente.render("Puntos:"+str(puntos)+"     Balas:"+str(balas)+"     Corazones:"+str(corazon_recolec)+"    Tiempo: "+str(segundos), True, (255, 255, 255))
    area_texto = texto.get_rect()     
    texto_x = 18
    texto_y = 660
    screen.blit(texto, [texto_x, texto_y])

    pygame.display.flip()
        


    for event in pygame.event.get():
          
        #Salida
        if event.type == pygame.QUIT or tecla[K_ESCAPE]: 
            cont = 0

            pygame.mixer.music.load("tiempo.wav")
            pygame.mixer.music.play(1)
            clock.tick(0.5)

            while cont < 1:
                if num_frame >= len(hero_muerto):
                    num_frame = 0
                    cont += 1
                else:
                    hero.setRect(hero_muerto[num_frame])
                    clock.tick(5)
                    screen.blit(fondo, (0,0))
                    hero.draw(screen)
                    tl.draw(screen)
                    pygame.display.flip()
                    num_frame += 1

            screen.blit(fondo_fin, (0,0))  
            pygame.display.flip() 
            pygame.mixer.music.load("fin.mp3")
            pygame.mixer.music.play(1)
            pygame.time.wait(6000)  
            fin = True
            raise SystemExit