#Alejandro Esteban Rendon Diosa
#Proyecto Final
#Computacion Grafica
#INGENIERIA DE SISTEMAS Y COMPUTACION
#UNIVERSIDAD TECNOLOGICA DE PEREIRA

import pygame
import math
from pygame.locals import *
import sys
import py_compile

#Comando para crear ejecutables
#py_compile.compile('GP.py')


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



def seguir(hero_x, hero_y, rival_x, rival_y):
    ls = []

    if abs(hero_x-rival_x) <=120:
        if rival_x > hero_x:
            rival_x -= 4
        elif rival_x < hero_x:
            rival_x += 4

        if rival_y > hero_y:
            rival_y -= 4
        elif rival_y < hero_y:
            rival_y += 4

    ls.append(rival_x)
    ls.append(rival_y)

    return ls


#................................PANTALLA..................................

#Iniciar Pygame
pygame.init()
#Creacion de ventana

#Titulo de la pantalla de seleccion
pygame.display.set_caption("...1-1...")

colorfondo = 255, 255, 255
tamano = ancho, alto = 1019, 400
pantalla = pygame.display.set_mode(tamano)
fondo = pygame.image.load("fondo1.png").convert()

#Personajes
personaje = Sprite("hero1.png", pygame.Rect(14, 150, 48, 85))
rival1 = Sprite("rival1.png", pygame.Rect(589, 7, 33, 77))
rival2 = Sprite("rival1.png", pygame.Rect(589, 7, 33, 77))
boss = Sprite("boss.gif", pygame.Rect(11, 92, 59, 101))


clock = pygame.time.Clock()

rival1_lista = pygame.sprite.Group()
rival2_lista = pygame.sprite.Group()
boss_lista = pygame.sprite.Group()
tl = pygame.sprite.Group()


#Rivales
rival1.rect.x = 700
rival1.rect.y = 150
rival1_lista.add(rival1)
rival1.setPosition(700, 150)
tl.add(rival1)

rival2.rect.x = 220
rival2.rect.y = 200
rival2_lista.add(rival2)
rival2.setPosition(220, 200)
tl.add(rival2)

boss.rect.x = 100
boss.rect.y = 150
boss.setPosition(100, 150)

colision = True





      



#.................MOVIMIENTOS HERO1.........................
hero1_caminando_right = [ pygame.Rect(182, 147, 45, 88), \
              pygame.Rect(233, 146, 37, 89), \
              pygame.Rect(283, 145, 19, 90), \
              pygame.Rect(314, 146, 33, 89), \
              pygame.Rect(358, 146, 45, 89), \
              pygame.Rect(410, 145, 37, 90), \
              pygame.Rect(460, 144, 18, 91), \
              pygame.Rect(489, 145, 33, 89), ]

hero1_caminando_left = [ pygame.Rect(529, 147, 33, 89), \
              pygame.Rect(573, 146, 18, 90), \
              pygame.Rect(604, 147, 37, 89), \
              pygame.Rect(648, 148, 45, 88), \
              pygame.Rect(704, 148, 33, 89), \
              pygame.Rect(749, 147, 19, 90), \
              pygame.Rect(781, 148, 37, 89), \
              pygame.Rect(824, 149, 45, 88),]

hero1_correr_right = [ pygame.Rect(23, 248, 56, 76), \
              pygame.Rect(87, 247, 55, 76), \
              pygame.Rect(151, 248, 51, 75), \
              pygame.Rect(212, 249, 51, 75), \
              pygame.Rect(282, 247, 53, 77), \
              pygame.Rect(119, 1026, 18, 35), \
              pygame.Rect(142, 1031, 18, 30), \
              pygame.Rect(165, 1038, 18, 23),]

hero1_caminando_down_right = [ pygame.Rect(4, 132, 26, 35), \
              pygame.Rect(35, 133, 27, 34), \
              pygame.Rect(67, 132, 26, 35), \
              pygame.Rect(98, 131, 20, 36), \
              pygame.Rect(123, 132, 18, 35), \
              pygame.Rect(146, 134, 23, 33), \
              pygame.Rect(174, 132, 18, 35), \
              pygame.Rect(197, 131, 20, 36),]  

hero1_puno_right = [ pygame.Rect(14, 150, 48, 85),\
              pygame.Rect(13, 474, 47, 88), \
              pygame.Rect(64, 473, 63, 89), \
              pygame.Rect(140, 477, 50, 84), \
              pygame.Rect(201, 481, 73, 80), \
              pygame.Rect(286, 481, 54, 80), \
              pygame.Rect(356, 480, 65, 81), ]

hero1_puno_left = [ pygame.Rect(989, 152, 48, 85),\
              pygame.Rect(963, 477, 65, 81), \
              pygame.Rect(1044, 478, 54, 80), \
              pygame.Rect(1110, 478, 73, 80), \
              pygame.Rect(1194, 474, 50, 84), \
              pygame.Rect(1257, 470, 63, 89), \
              pygame.Rect(1275, 373, 47, 88), ]

hero1_patada_right = [ pygame.Rect(14, 150, 48, 85),
              pygame.Rect(432, 485, 47, 76), \
              pygame.Rect(485, 480, 41, 79), \
              pygame.Rect(537, 465, 34, 94), \
              pygame.Rect(587, 459, 47, 100), \
              pygame.Rect(652, 467, 37, 92), ] 

hero1_patada_left = [ pygame.Rect(989, 152, 48, 85),\
              pygame.Rect(905, 482, 47, 76), \
              pygame.Rect(858, 477, 41, 79), \
              pygame.Rect(813, 462, 34, 94), \
              pygame.Rect(750, 456, 47, 100), \
              pygame.Rect(696, 464, 37, 92), ]

hero1_caminando_down_left = [ pygame.Rect(221, 131, 20, 36), \
              pygame.Rect(246, 132, 18, 35), \
              pygame.Rect(269, 134, 23, 33), \
              pygame.Rect(297, 132, 18, 35), \
              pygame.Rect(320, 131, 20, 36), \
              pygame.Rect(345, 132, 26, 35), \
              pygame.Rect(376, 133, 27, 34), \
              pygame.Rect(408, 132, 26, 34),] 

hero1_caminando_up_right = [ pygame.Rect(4, 215, 20, 35), \
              pygame.Rect(29, 216, 23, 34), \
              pygame.Rect(57, 215, 20, 35), \
              pygame.Rect(82, 214, 21, 36), \
              pygame.Rect(108, 215, 24, 35), \
              pygame.Rect(137, 216, 25, 34), \
              pygame.Rect(167, 215, 24, 35), \
              pygame.Rect(196, 214, 21, 36),] 

hero1_caminando_up_left = [ pygame.Rect(222, 214, 21, 36), \
              pygame.Rect(248, 215, 24, 35), \
              pygame.Rect(277, 216, 25, 34), \
              pygame.Rect(307, 215, 24, 35), \
              pygame.Rect(336, 214, 21, 36), \
              pygame.Rect(362, 215, 20, 35), \
              pygame.Rect(387, 216, 23, 34), \
              pygame.Rect(415, 215, 20, 35),] 

hero1_muerte_left = [ pygame.Rect(16, 1209, 35, 85), \
              pygame.Rect(54, 1209, 41, 85), \
              pygame.Rect(97, 1209, 77, 85), \
              pygame.Rect(97, 1209, 77, 85), \
              pygame.Rect(178, 1209, 86, 85), \
              pygame.Rect(178, 1209, 86, 85), \
              pygame.Rect(178, 1209, 86, 85), \
              pygame.Rect(178, 1209, 86, 85),] 

hero1_muerte_right = [ pygame.Rect(763, 1211, 35, 85), \
              pygame.Rect(719, 1211, 41, 85), \
              pygame.Rect(640, 1211, 77, 85), \
              pygame.Rect(640, 1211, 77, 85), \
              pygame.Rect(550, 1211, 86, 85), \
              pygame.Rect(550, 1211, 86, 85), \
              pygame.Rect(550, 1211, 86, 85), \
              pygame.Rect(550, 1211, 86, 85),] 



#Movimientos rivales
rival2_muere_derecha = [ pygame.Rect(618, 251, 36, 80), \
              pygame.Rect(532, 252, 77, 79), \
              pygame.Rect(440, 252, 83, 82), \
              pygame.Rect(440, 252, 83, 82), \
              pygame.Rect(343, 252, 88, 84), \
              pygame.Rect(343, 252, 88, 84), \
              pygame.Rect(343, 252, 88, 84), \
              pygame.Rect(343, 252, 88, 84),] 

rival2_muere_izquierda = [ pygame.Rect(55, 167, 36, 79), \
              pygame.Rect(100, 167, 77, 79), \
              pygame.Rect(186, 167, 83, 81), \
              pygame.Rect(186, 167, 83, 81), \
              pygame.Rect(278, 167, 88, 83), \
              pygame.Rect(278, 167, 88, 83), \
              pygame.Rect(278, 167, 88, 83), \
              pygame.Rect(278, 167, 88, 83),] 


boss_muere_derecha = [ pygame.Rect(11, 92, 59, 101), \
              pygame.Rect(12, 776, 64, 105), \
              pygame.Rect(79, 776, 63, 105), \
              pygame.Rect(149, 776, 103, 105), \
              pygame.Rect(149, 776, 103, 105), \
              pygame.Rect(261, 776, 112, 105), \
              pygame.Rect(261, 776, 112, 105), \
              pygame.Rect(380, 776, 110, 105), \
              pygame.Rect(380, 776, 110, 105),] 

boss_muere_izquierda = [ pygame.Rect(216, 93, 60, 98), \
              pygame.Rect(532, 3, 64, 105), \
              pygame.Rect(466, 4, 63, 105), \
              pygame.Rect(356, 4, 103, 105), \
              pygame.Rect(356, 4, 103, 105), \
              pygame.Rect(235, 2, 112, 88), \
              pygame.Rect(235, 2, 112, 88), \
              pygame.Rect(118, 2, 110, 88), \
              pygame.Rect(118, 2, 110, 88),] 






num_frame = 0
walking = True
clock = pygame.time.Clock()
personaje.rect.x = 0
personaje.rect.y = 190
pos = "RIGHT"
diagonal = True

personaje.setPosition(0,180)
personaje.draw(pantalla)

rival1.setPosition(700, 150)
rival1.draw(pantalla)

rival2.setPosition(220, 200)
rival2.draw(pantalla)

fondo1 = pygame.image.load("fin1.png").convert()
fondo2 = pygame.image.load("fin2.png").convert()
opcion1 = pygame.image.load("menu1.png").convert()
opcion2 = pygame.image.load("menu2.png").convert()
opcion3 = pygame.image.load("menu3.png").convert()
instruccion = pygame.image.load("instruccion.png").convert()

pygame.mixer.music.load("ff.mp3")
pygame.mixer.music.play(1)
pygame.time.wait(500)


#Fuente
fuente = pygame.font.Font(None, 36)

pygame.display.flip()

muerte = 10
flag_boss = False
round2 = False
boss_muerte = 5

vida = "**********"
opc_menu = 1

menu_activo = True

pantalla.blit(opcion1, (0,0))
pygame.display.flip()

#..............................INICIA EL JUEGO.......................


while walking:
    tecla = pygame.key.get_pressed()


    if tecla[K_1] == 1 and menu_activo == True:
        opc_menu = 1
        menu_activo = False
        pantalla.blit(fondo, (0,0))
        personaje.draw(pantalla)
        tl.draw(pantalla)
        
        pygame.display.flip()
        pygame.mixer.music.load("round.wav")
        pygame.mixer.music.play(1)
        pygame.time.wait(500)
        pygame.mixer.music.load("uno.wav")
        pygame.mixer.music.play(1)
        pygame.time.wait(500)
        pygame.mixer.music.load("pelear.wav")
        pygame.mixer.music.play(1)     

    elif tecla[K_2] == 1 and menu_activo == True:
        opc_menu = 2
        pantalla.blit(opcion2, (0,0))
        pygame.display.flip()
        clock.tick(2)
        pantalla.blit(instruccion, (0,0))
        pygame.display.flip()
        clock.tick(0.1)
        menu_activo = False
        pantalla.blit(fondo, (0,0))
        personaje.draw(pantalla)
        tl.draw(pantalla)

        pygame.display.flip()
        pygame.mixer.music.load("round.wav")
        pygame.mixer.music.play(1)
        pygame.time.wait(500)
        pygame.mixer.music.load("uno.wav")
        pygame.mixer.music.play(1)
        pygame.time.wait(500)
        pygame.mixer.music.load("pelear.wav")
        pygame.mixer.music.play(1) 

    elif tecla[K_3] == 1 and menu_activo == True:
        pantalla.blit(opcion3, (0,0))
        pygame.display.flip()
        raise SystemExit
            


    if len(rival1_lista) == 0 and len(rival2_lista) == 0 and flag_boss == False and boss_muerte > 0:
        if round2 == False:
	        pygame.mixer.music.load("round.wav")
	        pygame.mixer.music.play(1)
	        pygame.time.wait(500)
	        pygame.mixer.music.load("dos.wav")
	        pygame.mixer.music.play(1)
	        pygame.time.wait(500)
	        pygame.mixer.music.load("pelear.wav")
	        pygame.mixer.music.play(1)
	        pygame.display.set_caption("...1-2   BOSS...")
	        pygame.time.wait(1000)
	        pygame.mixer.music.load("boss.wav")
	        pygame.mixer.music.play(1)
	        round2 == True
        elif round2 == True:
	    	pygame.mixer.music.load("boss.wav")
	        pygame.mixer.music.play(1)
	        pygame.display.set_caption("...1-2   BOSS...")

        boss_lista.add(boss)
        tl.add(boss)
        tl.draw(pantalla)
        pygame.display.flip()
        flag_boss = True

    if muerte == 0:
        pygame.mixer.music.load("ff.mp3")
        pygame.mixer.music.play(1)
        pygame.time.wait(500)
        pygame.display.flip()
        pantalla.blit(fondo1, (0,0))
        pygame.display.flip()
        clock.tick(0.1)
        raise SystemExit

    elif boss_muerte == 0:
        pygame.mixer.music.load("ff.mp3")
        pygame.mixer.music.play(1)
        pygame.time.wait(500)
        pygame.display.flip()
        pantalla.blit(fondo2, (0,0))
        pygame.display.flip()
        clock.tick(0.1)
        raise SystemExit

    

#...Movimiento a la derecha-------------------------------------------------------------------------------------
    if tecla[K_RIGHT] == 1 and tecla[K_DOWN] == 0 and tecla[K_UP] == 0 and tecla[K_LEFT] == 0 and tecla[K_z] == 0 and menu_activo == False and tecla[K_x] == 0:
        if num_frame >= len(hero1_caminando_right):
            num_frame = 0
        personaje.setRect(hero1_caminando_right[num_frame])
        num_frame += 1
        personaje.rect.x += 10 
        if personaje.rect.x > 986:
            personaje.rect.x = 986
        clock.tick(12)
        pantalla.blit(fondo, (0,0))
        personaje.setPosition(personaje.rect.x, personaje.rect.y)
        personaje.draw(pantalla)  
        pos = "RIGHT"  

        if flag_boss == True:
        	lb = seguir(personaje.rect.x, personaje.rect.y, boss.rect.x, boss.rect.y)
	        boss.rect.x = lb[0]
	        boss.rect.y = lb[1]
	        boss.setPosition(boss.rect.x, boss.rect.y)        

        lp = seguir(personaje.rect.x, personaje.rect.y, rival1.rect.x, rival1.rect.y)
        rival1.rect.x = lp[0]
        rival1.rect.y = lp[1]
        rival1.setPosition(rival1.rect.x, rival1.rect.y)

        ls = seguir(personaje.rect.x, personaje.rect.y, rival2.rect.x, rival2.rect.y)
        rival2.rect.x = ls[0]
        rival2.rect.y = ls[1]
        rival2.setPosition(rival2.rect.x, rival2.rect.y)

        #Si hay colision con boss
        lista_boss = pygame.sprite.spritecollide(personaje, boss_lista, True)
        
        for rival in lista_boss:
            cont3 = 0
            num_frame3 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont3 < 1:
                if num_frame3 >= len(hero1_muerte_left):
                    num_frame3 = 0
                    cont3 += 1
                    personaje.setRect(hero1_muerte_left[0])
                    
                    boss_lista.add(boss)
                    boss.draw(pantalla)
                    tl.add(boss)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_left[num_frame3])

                    if personaje.rect.x >= 10:
                    	personaje.rect.x -= 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    boss.setPosition(boss.rect.x, boss.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    boss.draw(pantalla)
                    boss_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame3 += 1


        #Si hay colision con un rival2
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival2_lista, True)
        
        for rival in lista_rivales1:
            cont1 = 0
            num_frame1 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont1 < 1:
                if num_frame1 >= len(hero1_muerte_left):
                    num_frame1 = 0
                    cont1 += 1
                    personaje.setRect(hero1_muerte_left[0])
                    rival2_lista.add(rival2)
                    rival2.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_left[num_frame1])

                    if personaje.rect.x >= 10:
                    	personaje.rect.x -= 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival2.setPosition(rival2.rect.x, rival2.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival2.draw(pantalla)
                    rival2_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame1 += 1


        #Si hay colision con el rival1
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival1_lista, True)
        
        for rival in lista_rivales1:
            cont2 = 0
            num_frame2 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont2 < 1:
                if num_frame2 >= len(hero1_muerte_left):
                    num_frame2 = 0
                    cont2 += 1
                    personaje.setRect(hero1_muerte_left[0])
                    rival1_lista.add(rival1)
                    rival1.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_left[num_frame2])

                    if personaje.rect.x >= 10:
                    	personaje.rect.x -= 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival1.setPosition(rival1.rect.x, rival1.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival1.draw(pantalla)
                    rival1_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame2 += 1

        boss_lista.draw(pantalla)
        rival1_lista.draw(pantalla)
        rival2_lista.draw(pantalla)
        tl.draw(pantalla)

        pygame.display.flip()

#...Movimiento a la izquierda-------------------------------------------------------------------------------------
    if tecla[K_LEFT] == 1 and tecla[K_UP] == 0 and tecla[K_RIGHT] == 0 and tecla[K_DOWN] == 0 and tecla[K_z] == 0 and menu_activo == False and tecla[K_x] == 0:
        if num_frame >= len(hero1_caminando_left):
            num_frame = 0
        personaje.setRect(hero1_caminando_left[num_frame])
        num_frame += 1
        personaje.rect.x = personaje.rect.x-10
        if personaje.rect.x < 0:
            personaje.rect.x = 0
        clock.tick(12)
        pantalla.blit(fondo, (0,0))
        personaje.setPosition(personaje.rect.x,personaje.rect.y)
        personaje.draw(pantalla)  
        pos = "LEFT" 

        if flag_boss == True:
        	lb = seguir(personaje.rect.x, personaje.rect.y, boss.rect.x, boss.rect.y)
	        boss.rect.x = lb[0]
	        boss.rect.y = lb[1]
	        boss.setPosition(boss.rect.x, boss.rect.y)  

        lp = seguir(personaje.rect.x, personaje.rect.y, rival1.rect.x, rival1.rect.y)
        rival1.rect.x = lp[0]
        rival1.rect.y = lp[1]
        rival1.setPosition(rival1.rect.x, rival1.rect.y)

        ls = seguir(personaje.rect.x, personaje.rect.y, rival2.rect.x, rival2.rect.y)
        rival2.rect.x = ls[0]
        rival2.rect.y = ls[1]
        rival2.setPosition(rival2.rect.x, rival2.rect.y)


        #Si hay colision con boss
        lista_boss = pygame.sprite.spritecollide(personaje, boss_lista, True)
        
        for rival in lista_boss:
            cont3 = 0
            num_frame3 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont3 < 1:
                if num_frame3 >= len(hero1_muerte_right):
                    num_frame3 = 0
                    cont3 += 1
                    personaje.setRect(hero1_muerte_right[0])
                    
                    boss_lista.add(boss)
                    boss.draw(pantalla)
                    tl.add(boss)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_right[num_frame3])

                    if personaje.rect.x <= 976:
                    	personaje.rect.x += 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    boss.setPosition(boss.rect.x, boss.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    boss.draw(pantalla)
                    boss_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame3 += 1


        #Si hay colision con un rival2
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival2_lista, True)
        
        for rival in lista_rivales1:
            cont1 = 0
            num_frame1 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont1 < 1:
                if num_frame1 >= len(hero1_muerte_right):
                    num_frame1 = 0
                    cont1 += 1
                    personaje.setRect(hero1_muerte_right[0])
                    rival2_lista.add(rival2)
                    rival2.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_right[num_frame1])

                    if personaje.rect.x <= 976:
                    	personaje.rect.x += 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival2.setPosition(rival2.rect.x, rival2.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival2.draw(pantalla)
                    rival2_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame1 += 1

        #Si hay colision con el rival1
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival1_lista, True)
        
        for rival in lista_rivales1:
            cont2 = 0
            num_frame2 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont2 < 1:
                if num_frame2 >= len(hero1_muerte_right):
                    num_frame2 = 0
                    cont2 += 1
                    personaje.setRect(hero1_muerte_right[0])
                    rival1_lista.add(rival1)
                    rival1.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_right[num_frame2])

                    if personaje.rect.x <= 976:
                    	personaje.rect.x += 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival1.setPosition(rival1.rect.x, rival1.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival1.draw(pantalla)
                    rival1_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame2 += 1

        rival1_lista.draw(pantalla)
        rival2_lista.draw(pantalla)
        tl.draw(pantalla)

        pygame.display.flip()

#...Movimiento hacia abajo----------------------------------------------------------------------------------------------
    if tecla[K_DOWN] == 1 and tecla[K_UP] == 0 and tecla[K_LEFT] == 0 and tecla[K_RIGHT] == 0 and tecla[K_z] == 0 and pos == "LEFT" and menu_activo == False and tecla[K_x] == 0:
        if num_frame >= len(hero1_caminando_left):
            num_frame = 0
        personaje.setRect(hero1_caminando_left[num_frame])
        num_frame += 1
        personaje.rect.y = personaje.rect.y+10
        if personaje.rect.y > 190:
            personaje.rect.y = 190
        clock.tick(12)
        pantalla.blit(fondo, (0,0))
        personaje.setPosition(personaje.rect.x, personaje.rect.y)
        personaje.draw(pantalla) 

        if flag_boss == True:
        	lb = seguir(personaje.rect.x, personaje.rect.y, boss.rect.x, boss.rect.y)
	        boss.rect.x = lb[0]
	        boss.rect.y = lb[1]
	        boss.setPosition(boss.rect.x, boss.rect.y)         

        ls = seguir(personaje.rect.x, personaje.rect.y, rival1.rect.x, rival1.rect.y)
        rival1.rect.x = ls[0]
        rival1.rect.y = ls[1]
        rival1.setPosition(rival1.rect.x, rival1.rect.y)

        ls = seguir(personaje.rect.x, personaje.rect.y, rival2.rect.x, rival2.rect.y)
        rival2.rect.x = ls[0]
        rival2.rect.y = ls[1]
        rival2.setPosition(rival2.rect.x, rival2.rect.y)

         #Si hay colision con un rival2
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival2_lista, True)
        
        for rival in lista_rivales1:
            cont1 = 0
            num_frame1 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont1 < 1:
                if num_frame1 >= len(hero1_muerte_right):
                    num_frame1 = 0
                    cont1 += 1
                    personaje.setRect(hero1_muerte_right[0])
                    rival2_lista.add(rival2)
                    rival2.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_right[num_frame1])

                    if personaje.rect.x <= 976:
                    	personaje.rect.x += 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival2.setPosition(rival2.rect.x, rival2.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival2.draw(pantalla)
                    rival2_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame1 += 1

        #Si hay colision con el rival1
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival1_lista, True)
        
        for rival in lista_rivales1:
            cont2 = 0
            num_frame2 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont2 < 1:
                if num_frame2 >= len(hero1_muerte_right):
                    num_frame2 = 0
                    cont2 += 1
                    personaje.setRect(hero1_muerte_right[0])
                    rival1_lista.add(rival1)
                    rival1.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_right[num_frame2])

                    if personaje.rect.x <= 976:
                    	personaje.rect.x += 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival1.setPosition(rival1.rect.x, rival1.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival1.draw(pantalla)
                    rival1_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame2 += 1

        rival1_lista.draw(pantalla)
        rival2_lista.draw(pantalla)
        tl.draw(pantalla)

        pygame.display.flip()




    if tecla[K_DOWN] == 1 and tecla[K_UP] == 0 and tecla[K_LEFT] == 0 and tecla[K_RIGHT] == 0 and tecla[K_z] == 0 and pos == "RIGHT" and menu_activo == False and tecla[K_x] == 0:
        if num_frame >= len(hero1_caminando_right):
            num_frame = 0
        personaje.setRect(hero1_caminando_right[num_frame])
        num_frame += 1
        personaje.rect.y = personaje.rect.y+10
        if personaje.rect.y > 190:
            personaje.rect.y = 190
        clock.tick(12)
        pantalla.blit(fondo, (0,0))
        personaje.setPosition(personaje.rect.x, personaje.rect.y)
        personaje.draw(pantalla)  

        if flag_boss == True:
        	lb = seguir(personaje.rect.x, personaje.rect.y, boss.rect.x, boss.rect.y)
	        boss.rect.x = lb[0]
	        boss.rect.y = lb[1]
	        boss.setPosition(boss.rect.x, boss.rect.y) 

        lp = seguir(personaje.rect.x, personaje.rect.y, rival1.rect.x, rival1.rect.y)
        rival1.rect.x = lp[0]
        rival1.rect.y = lp[1]
        rival1.setPosition(rival1.rect.x, rival1.rect.y)

        ls = seguir(personaje.rect.x, personaje.rect.y, rival2.rect.x, rival2.rect.y)
        rival2.rect.x = ls[0]
        rival2.rect.y = ls[1]
        rival2.setPosition(rival2.rect.x, rival2.rect.y)

        #Si hay colision con un rival2
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival2_lista, True)
        
        for rival in lista_rivales1:
            cont1 = 0
            num_frame1 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont1 < 1:
                if num_frame1 >= len(hero1_muerte_left):
                    num_frame1 = 0
                    cont1 += 1
                    personaje.setRect(hero1_muerte_left[0])
                    rival2_lista.add(rival2)
                    rival2.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_left[num_frame1])

                    if personaje.rect.x >= 10:
                    	personaje.rect.x -= 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival2.setPosition(rival2.rect.x, rival2.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival2.draw(pantalla)
                    rival2_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame1 += 1


        #Si hay colision con el rival1
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival1_lista, True)
        
        for rival in lista_rivales1:
            cont2 = 0
            num_frame2 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont2 < 1:
                if num_frame2 >= len(hero1_muerte_left):
                    num_frame2 = 0
                    cont2 += 1
                    personaje.setRect(hero1_muerte_left[0])
                    rival1_lista.add(rival1)
                    rival1.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_left[num_frame2])

                    if personaje.rect.x >= 10:
                    	personaje.rect.x -= 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival1.setPosition(rival1.rect.x, rival1.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival1.draw(pantalla)
                    rival1_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame2 += 1

        rival1_lista.draw(pantalla)
        rival2_lista.draw(pantalla)
        tl.draw(pantalla)

        pygame.display.flip()
    
#...Movimiento hacia arriba------------------------------------------------------------------------------------------------------
    if tecla[K_UP] == 1 and tecla[K_LEFT] == 0 and tecla[K_RIGHT] == 0 and tecla[K_DOWN] == 0 and tecla[K_z] == 0 and pos == "RIGHT" and menu_activo == False and tecla[K_x] == 0:
        if num_frame >= len(hero1_caminando_right):
            num_frame = 0
        personaje.setRect(hero1_caminando_right[num_frame])
        num_frame += 1
        personaje.rect.y = personaje.rect.y-10
        if personaje.rect.y <= 130:
            personaje.rect.y = 130
        clock.tick(12)
        pantalla.blit(fondo, (0,0))
        personaje.setPosition(personaje.rect.x, personaje.rect.y)
        personaje.draw(pantalla)

        if flag_boss == True:
        	lb = seguir(personaje.rect.x, personaje.rect.y, boss.rect.x, boss.rect.y)
	        boss.rect.x = lb[0]
	        boss.rect.y = lb[1]
	        boss.setPosition(boss.rect.x, boss.rect.y) 

        lp = seguir(personaje.rect.x, personaje.rect.y, rival1.rect.x, rival1.rect.y)
        rival1.rect.x = lp[0]
        rival1.rect.y = lp[1]
        rival1.setPosition(rival1.rect.x, rival1.rect.y)

        ls = seguir(personaje.rect.x, personaje.rect.y, rival2.rect.x, rival2.rect.y)
        rival2.rect.x = ls[0]
        rival2.rect.y = ls[1]
        rival2.setPosition(rival2.rect.x, rival2.rect.y)

        #Si hay colision con un rival2
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival2_lista, True)
        
        for rival in lista_rivales1:
            cont1 = 0
            num_frame1 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont1 < 1:
                if num_frame1 >= len(hero1_muerte_left):
                    num_frame1 = 0
                    cont1 += 1
                    personaje.setRect(hero1_muerte_left[0])
                    rival2_lista.add(rival2)
                    rival2.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_left[num_frame1])

                    if personaje.rect.x >= 10:
                    	personaje.rect.x -= 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival2.setPosition(rival2.rect.x, rival2.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival2.draw(pantalla)
                    rival2_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame1 += 1


        #Si hay colision con el rival1
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival1_lista, True)
        
        for rival in lista_rivales1:
            cont2 = 0
            num_frame2 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont2 < 1:
                if num_frame2 >= len(hero1_muerte_left):
                    num_frame2 = 0
                    cont2 += 1
                    personaje.setRect(hero1_muerte_left[0])
                    rival1_lista.add(rival1)
                    rival1.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_left[num_frame2])

                    if personaje.rect.x >= 10:
                    	personaje.rect.x -= 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival1.setPosition(rival1.rect.x, rival1.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival1.draw(pantalla)
                    rival1_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame2 += 1

        rival1_lista.draw(pantalla)
        rival2_lista.draw(pantalla)
        tl.draw(pantalla)

        pygame.display.flip()

#...........
    if tecla[K_UP] == 1 and tecla[K_LEFT] == 0 and tecla[K_RIGHT] == 0 and tecla[K_DOWN] == 0 and tecla[K_z] == 0 and pos == "LEFT" and tecla[K_x] == 0:
        if num_frame >= len(hero1_caminando_left):
            num_frame = 0
        personaje.setRect(hero1_caminando_left[num_frame])
        num_frame += 1
        personaje.rect.y = personaje.rect.y-10
        if personaje.rect.y < 130:
            personaje.rect.y = 130
        clock.tick(12)
        pantalla.blit(fondo, (0,0))
        personaje.setPosition(personaje.rect.x, personaje.rect.y)
        personaje.draw(pantalla)  

        if flag_boss == True:
        	lb = seguir(personaje.rect.x, personaje.rect.y, boss.rect.x, boss.rect.y)
	        boss.rect.x = lb[0]
	        boss.rect.y = lb[1]
	        boss.setPosition(boss.rect.x, boss.rect.y)   

        lp = seguir(personaje.rect.x, personaje.rect.y, rival1.rect.x, rival1.rect.y)
        rival1.rect.x = lp[0]
        rival1.rect.y = lp[1]
        rival1.setPosition(rival1.rect.x, rival1.rect.y)

        ls = seguir(personaje.rect.x, personaje.rect.y, rival2.rect.x, rival2.rect.y)
        rival2.rect.x = ls[0]
        rival2.rect.y = ls[1]
        rival2.setPosition(rival2.rect.x, rival2.rect.y)

        #Si hay colision con un rival2
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival2_lista, True)
        
        for rival in lista_rivales1:
            cont1 = 0
            num_frame1 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont1 < 1:
                if num_frame1 >= len(hero1_muerte_right):
                    num_frame1 = 0
                    cont1 += 1
                    personaje.setRect(hero1_muerte_right[0])
                    rival2_lista.add(rival2)
                    rival2.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_right[num_frame1])

                    if personaje.rect.x <= 976:
                    	personaje.rect.x += 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival2.setPosition(rival2.rect.x, rival2.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival2.draw(pantalla)
                    rival2_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame1 += 1

        #Si hay colision con el rival1
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival1_lista, True)
        
        for rival in lista_rivales1:
            cont2 = 0
            num_frame2 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont2 < 1:
                if num_frame2 >= len(hero1_muerte_right):
                    num_frame2 = 0
                    cont2 += 1
                    personaje.setRect(hero1_muerte_right[0])
                    rival1_lista.add(rival1)
                    rival1.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_right[num_frame2])

                    if personaje.rect.x <= 976:
                    	personaje.rect.x += 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival1.setPosition(rival1.rect.x, rival1.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival1.draw(pantalla)
                    rival1_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame2 += 1

        rival1_lista.draw(pantalla)
        rival2_lista.draw(pantalla)
        tl.draw(pantalla)

        pygame.display.flip()

    

#...Movimiento diagonal derecha - abajo
    if tecla[K_DOWN] == 1 and tecla[K_RIGHT] == 1 and tecla[K_UP] == 0 and tecla[K_LEFT] == 0 and tecla[K_z] == 0 and tecla[K_x] == 0 and menu_activo == False:

        if num_frame >= len(hero1_caminando_right):
            num_frame = 0
        personaje.setRect(hero1_caminando_right[num_frame])
        num_frame += 1
        personaje.rect.y = personaje.rect.y+10
        personaje.rect.x = personaje.rect.x+10
        if personaje.rect.y >= 190:
            personaje.rect.y = 190
        if personaje.rect.x > 986:
            personaje.rect.x = 986
        clock.tick(12)
        pantalla.blit(fondo, (0,0))
        personaje.setPosition(personaje.rect.x, personaje.rect.y)
        personaje.draw(pantalla)  
        pos = "RIGHT"        

        if flag_boss == True:
        	lb = seguir(personaje.rect.x, personaje.rect.y, boss.rect.x, boss.rect.y)
	        boss.rect.x = lb[0]
	        boss.rect.y = lb[1]
	        boss.setPosition(boss.rect.x, boss.rect.y) 

        lp = seguir(personaje.rect.x, personaje.rect.y, rival1.rect.x, rival1.rect.y)
        rival1.rect.x = lp[0]
        rival1.rect.y = lp[1]
        rival1.setPosition(rival1.rect.x, rival1.rect.y)

        ls = seguir(personaje.rect.x, personaje.rect.y, rival2.rect.x, rival2.rect.y)
        rival2.rect.x = ls[0]
        rival2.rect.y = ls[1]
        rival2.setPosition(rival2.rect.x, rival2.rect.y)

        #Si hay colision con un rival2
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival2_lista, True)
        
        for rival in lista_rivales1:
            cont1 = 0
            num_frame1 = 0

            while cont1 < 1:
                if num_frame1 >= len(hero1_muerte_left):
                    num_frame1 = 0
                    cont1 += 1
                    personaje.setRect(hero1_muerte_left[0])
                    rival2_lista.add(rival2)
                    rival2.draw(pantalla)
                else:
                    personaje.setRect(hero1_muerte_left[num_frame1])

                    if personaje.rect.x >= 10:
                    	personaje.rect.x -= 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival2.setPosition(rival2.rect.x, rival2.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival2.draw(pantalla)
                    rival2_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame1 += 1

        #Si hay colision con el rival1
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival1_lista, True)
        
        for rival in lista_rivales1:
            cont2 = 0
            num_frame2 = 0

            while cont2 < 1:
                if num_frame2 >= len(hero1_muerte_left):
                    num_frame2 = 0
                    cont2 += 1
                    personaje.setRect(hero1_muerte_left[0])
                    rival1_lista.add(rival1)
                    rival1.draw(pantalla)
                else:
                    personaje.setRect(hero1_muerte_left[num_frame2])

                    if personaje.rect.x >= 10:
                    	personaje.rect.x -= 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival1.setPosition(rival1.rect.x, rival1.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival1.draw(pantalla)
                    rival1_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame2 += 1

        rival1_lista.draw(pantalla)
        rival2_lista.draw(pantalla)
        tl.draw(pantalla)

        pygame.display.flip()

#...Movimiento diagonal izquierda - abajo---------------------------------------------------------------------------
    if tecla[K_DOWN] == 1 and tecla[K_RIGHT] == 0 and tecla[K_UP] == 0 and tecla[K_LEFT] == 1 and tecla[K_z] == 0 and tecla[K_x] == 0 and menu_activo == False:

        if num_frame >= len(hero1_caminando_left):
            num_frame = 0
        personaje.setRect(hero1_caminando_left[num_frame])
        num_frame += 1
        personaje.rect.y = personaje.rect.y+10
        personaje.rect.x = personaje.rect.x-10
        if personaje.rect.y > 190:
            personaje.rect.y = 190
        if personaje.rect.x < 0:
            personaje.rect.x = 0
        clock.tick(12)
        pantalla.blit(fondo, (0,0))
        personaje.setPosition(personaje.rect.x, personaje.rect.y)
        personaje.draw(pantalla) 

        if flag_boss == True:
        	lb = seguir(personaje.rect.x, personaje.rect.y, boss.rect.x, boss.rect.y)
	        boss.rect.x = lb[0]
	        boss.rect.y = lb[1]
	        boss.setPosition(boss.rect.x, boss.rect.y)   

        lp = seguir(personaje.rect.x, personaje.rect.y, rival1.rect.x, rival1.rect.y)
        rival1.rect.x = lp[0]
        rival1.rect.y = lp[1]
        rival1.setPosition(rival1.rect.x, rival1.rect.y)

        ls = seguir(personaje.rect.x, personaje.rect.y, rival2.rect.x, rival2.rect.y)
        rival2.rect.x = ls[0]
        rival2.rect.y = ls[1]
        rival2.setPosition(rival2.rect.x, rival2.rect.y)

        #Si hay colision con un rival2
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival2_lista, True)
        
        for rival in lista_rivales1:
            cont1 = 0
            num_frame1 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont1 < 1:
                if num_frame1 >= len(hero1_muerte_right):
                    num_frame1 = 0
                    cont1 += 1
                    personaje.setRect(hero1_muerte_right[0])
                    rival2_lista.add(rival2)
                    rival2.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_right[num_frame1])

                    if personaje.rect.x <= 976:
                    	personaje.rect.x += 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival2.setPosition(rival2.rect.x, rival2.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival2.draw(pantalla)
                    rival2_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame1 += 1

        #Si hay colision con el rival1
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival1_lista, True)
        
        for rival in lista_rivales1:
            cont2 = 0
            num_frame2 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont2 < 1:
                if num_frame2 >= len(hero1_muerte_right):
                    num_frame2 = 0
                    cont2 += 1
                    personaje.setRect(hero1_muerte_right[0])
                    rival1_lista.add(rival1)
                    rival1.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_right[num_frame2])

                    if personaje.rect.x <= 976:
                    	personaje.rect.x += 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival1.setPosition(rival1.rect.x, rival1.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival1.draw(pantalla)
                    rival1_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame2 += 1

        rival1_lista.draw(pantalla)
        rival2_lista.draw(pantalla)
        tl.draw(pantalla)

        pygame.display.flip()

#...Movimiento diagonal derecha - arriba-------------------------------------------------------------------------
    if tecla[K_DOWN] == 0 and tecla[K_RIGHT] == 1 and tecla[K_UP] == 1 and tecla[K_LEFT] == 0 and tecla[K_z] == 0 and tecla[K_x] == 0 and menu_activo == False:

        if num_frame >= len(hero1_caminando_right):
            num_frame = 0
        personaje.setRect(hero1_caminando_right[num_frame])
        num_frame += 1
        personaje.rect.y = personaje.rect.y-10
        personaje.rect.x = personaje.rect.x+10
        if personaje.rect.y < 130:
            personaje.rect.y = 130
        if personaje.rect.x >986:
            personaje.rect.x = 986
        clock.tick(12)
        pantalla.blit(fondo, (0,0))
        personaje.setPosition(personaje.rect.x, personaje.rect.y)
        personaje.draw(pantalla)  

        if flag_boss == True:
        	lb = seguir(personaje.rect.x, personaje.rect.y, boss.rect.x, boss.rect.y)
	        boss.rect.x = lb[0]
	        boss.rect.y = lb[1]
	        boss.setPosition(boss.rect.x, boss.rect.y) 

        lp = seguir(personaje.rect.x, personaje.rect.y, rival1.rect.x, rival1.rect.y)
        rival1.rect.x = lp[0]
        rival1.rect.y = lp[1]
        rival1.setPosition(rival1.rect.x, rival1.rect.y)

        ls = seguir(personaje.rect.x, personaje.rect.y, rival2.rect.x, rival2.rect.y)
        rival2.rect.x = ls[0]
        rival2.rect.y = ls[1]
        rival2.setPosition(rival2.rect.x, rival2.rect.y)

        #Si hay colision con un rival2
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival2_lista, True)
        
        for rival in lista_rivales1:
            cont1 = 0
            num_frame1 = 0

            while cont1 < 1:
                if num_frame1 >= len(hero1_muerte_left):
                    num_frame1 = 0
                    cont1 += 1
                    personaje.setRect(hero1_muerte_left[0])
                    rival2_lista.add(rival2)
                    rival2.draw(pantalla)
                else:
                    personaje.setRect(hero1_muerte_left[num_frame1])

                    if personaje.rect.x >= 10:
                    	personaje.rect.x -= 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival2.setPosition(rival2.rect.x, rival2.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival2.draw(pantalla)
                    rival2_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame1 += 1

        #Si hay colision con el rival1
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival1_lista, True)
        
        for rival in lista_rivales1:
            cont2 = 0
            num_frame2 = 0

            while cont2 < 1:
                if num_frame2 >= len(hero1_muerte_left):
                    num_frame2 = 0
                    cont2 += 1
                    personaje.setRect(hero1_muerte_left[0])
                    rival1_lista.add(rival1)
                    rival1.draw(pantalla)
                else:
                    personaje.setRect(hero1_muerte_left[num_frame2])

                    if personaje.rect.x >= 10:
                    	personaje.rect.x -= 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival1.setPosition(rival1.rect.x, rival1.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival1.draw(pantalla)
                    rival1_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame2 += 1

        rival1_lista.draw(pantalla)
        rival2_lista.draw(pantalla)
        tl.draw(pantalla)

        pygame.display.flip()


#...Movimiento diagonal izquierda - arriba--------------------------------------------------------------------
    if tecla[K_DOWN] == 0 and tecla[K_RIGHT] == 0 and tecla[K_UP] == 1 and tecla[K_LEFT] == 1 and tecla[K_z] == 0 and tecla[K_x] == 0 and menu_activo == False:

        if num_frame >= len(hero1_caminando_left):
            num_frame = 0
        personaje.setRect(hero1_caminando_left[num_frame])
        num_frame += 1
        personaje.rect.y = personaje.rect.y-10
        personaje.rect.x = personaje.rect.x-10
        if personaje.rect.y < 130:
            personaje.rect.y = 130
        if personaje.rect.x < 0:
            personaje.rect.x = 0
        clock.tick(12)
        pantalla.blit(fondo, (0,0))
        personaje.setPosition(personaje.rect.x, personaje.rect.y)
        personaje.draw(pantalla)   

        if flag_boss == True:
        	lb = seguir(personaje.rect.x, personaje.rect.y, boss.rect.x, boss.rect.y)
	        boss.rect.x = lb[0]
	        boss.rect.y = lb[1]
	        boss.setPosition(boss.rect.x, boss.rect.y)  

        lp = seguir(personaje.rect.x, personaje.rect.y, rival1.rect.x, rival1.rect.y)
        rival1.rect.x = lp[0]
        rival1.rect.y = lp[1]
        rival1.setPosition(rival1.rect.x, rival1.rect.y)

        ls = seguir(personaje.rect.x, personaje.rect.y, rival2.rect.x, rival2.rect.y)
        rival2.rect.x = ls[0]
        rival2.rect.y = ls[1]
        rival2.setPosition(rival2.rect.x, rival2.rect.y)

        #Si hay colision con un rival2
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival2_lista, True)
        
        for rival in lista_rivales1:
            cont1 = 0
            num_frame1 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont1 < 1:
                if num_frame1 >= len(hero1_muerte_right):
                    num_frame1 = 0
                    cont1 += 1
                    personaje.setRect(hero1_muerte_right[0])
                    rival2_lista.add(rival2)
                    rival2.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_right[num_frame1])

                    if personaje.rect.x <= 976:
                    	personaje.rect.x += 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival2.setPosition(rival2.rect.x, rival2.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival2.draw(pantalla)
                    rival2_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame1 += 1

        #Si hay colision con el rival1
        lista_rivales1 = pygame.sprite.spritecollide(personaje, rival1_lista, True)
        
        for rival in lista_rivales1:
            cont2 = 0
            num_frame2 = 0
            pygame.mixer.music.load("hero.wav")
            pygame.mixer.music.play(1)

            while cont2 < 1:
                if num_frame2 >= len(hero1_muerte_right):
                    num_frame2 = 0
                    cont2 += 1
                    personaje.setRect(hero1_muerte_right[0])
                    rival1_lista.add(rival1)
                    rival1.draw(pantalla)
                    muerte -= 1
                    vida = vida[0:len(vida)-1]
                else:
                    personaje.setRect(hero1_muerte_right[num_frame2])

                    if personaje.rect.x <= 976:
                    	personaje.rect.x += 10 

                    personaje.setPosition(personaje.rect.x, personaje.rect.y)
                    rival1.setPosition(rival1.rect.x, rival1.rect.y)

                    clock.tick(12)
                    pantalla.blit(fondo, (0,0))
                    personaje.draw(pantalla)
                    rival1.draw(pantalla)
                    rival1_lista.draw(pantalla)
                    tl.draw(pantalla)
                    pygame.display.flip()
                    num_frame2 += 1

        rival1_lista.draw(pantalla)
        rival2_lista.draw(pantalla)
        tl.draw(pantalla)

        pygame.display.flip()      



    if menu_activo == False:
        texto = fuente.render("Vida:   "+str(muerte)+"0 %    "+vida, True, (255, 255, 255))
        area_texto = texto.get_rect()     
        texto_x = 200
        texto_y = 300
        pantalla.blit(texto, [texto_x, texto_y])
        pygame.display.flip()


#..........Punno y Patada--------------------------------------------------------------------------
    for event in pygame.event.get():

#.......Punno Derecho-------------------------------------------------------------------------
        if pos == "RIGHT" and tecla[K_z] == 1 and tecla[K_x] == 0 and menu_activo == False:
            cont = 0
            num_frame = 0
            pygame.mixer.music.load("punno.wav")
            pygame.mixer.music.play(1)

            while cont < 1:
            	if flag_boss == True:
		        	lb = seguir(personaje.rect.x, personaje.rect.y, boss.rect.x, boss.rect.y)
			        boss.rect.x = lb[0]
			        boss.rect.y = lb[1]
			        boss.setPosition(boss.rect.x, boss.rect.y) 

                lp = seguir(personaje.rect.x, personaje.rect.y, rival1.rect.x, rival1.rect.y)
                rival1.rect.x = lp[0]
                rival1.rect.y = lp[1]

                ls = seguir(personaje.rect.x, personaje.rect.y, rival2.rect.x, rival2.rect.y)
                rival2.rect.x = ls[0]
                rival2.rect.y = ls[1]

                if num_frame >= len(hero1_puno_right):
                    num_frame = 0
                    personaje.setRect(hero1_puno_right[0])
                    cont += 1
                    
                personaje.setRect(hero1_puno_right[num_frame])
                num_frame += 1

                #Si hay colision con boss
                
                if len(boss_lista) > 0:  
                	lista_boss = pygame.sprite.spritecollide(personaje, boss_lista, True)

	                for rival in lista_boss:
	                    cont3 = 0
	                    num_frame3 = 0
	                    pygame.mixer.music.load("boss.wav")
	                    pygame.mixer.music.play(1)

	                    while cont3 < 1:
	                        if num_frame3 >= len(boss_muere_izquierda):
	                            num_frame3 = 0
	                            cont3 += 1
	                            boss_muerte -= 1
	                            if boss_muerte > 0:
	                            	boss.setRect(boss_muere_izquierda[0])
	                            	boss_lista.add(boss)
	                            	tl.add(boss)
	                        else:
	                            boss.setRect(boss_muere_izquierda[num_frame3])
	                            if boss.rect.x <= 966:
	                            	boss.rect.x += 20
	                            
	                            boss.setPosition(boss.rect.x, boss.rect.y)

	                            clock.tick(12)
	                            pantalla.blit(fondo, (0,0))
	                            personaje.draw(pantalla)
	                            boss.draw(pantalla)
	                            tl.draw(pantalla)
	                            pygame.display.flip()
	                            num_frame3 += 1

                #Si hay colision con un rival
                lista_rivales1 = pygame.sprite.spritecollide(personaje, rival2_lista, True)

                for rival in lista_rivales1:
                    cont1 = 0
                    num_frame1 = 0
                    pygame.mixer.music.load("rival.wav")
                    pygame.mixer.music.play(1)

                    while cont1 < 1:
                        if num_frame1 >= len(rival2_muere_derecha):
                            num_frame1 = 0
                            cont1 += 1
                        else:
                            rival2.setRect(rival2_muere_derecha[num_frame1])
                            rival2.rect.x += 3 
                            rival2.rect.y += 2
                            rival2.setPosition(ls[0], ls[1])

                            clock.tick(12)
                            pantalla.blit(fondo, (0,0))
                            personaje.draw(pantalla)
                            rival2.draw(pantalla)
                            tl.draw(pantalla)
                            pygame.display.flip()
                            num_frame1 += 1

                #Colision con el rival 1
                lista_rivales2 = pygame.sprite.spritecollide(personaje, rival1_lista, True)
                
                for rival in lista_rivales2:
                    cont2 = 0
                    num_frame2 = 0
                    pygame.mixer.music.load("rival.wav")
                    pygame.mixer.music.play(1)

                    while cont2 < 1:
                        if num_frame2 >= len(rival2_muere_derecha):
                            num_frame2 = 0
                            cont2 += 1
                        else:
                            rival1.setRect(rival2_muere_derecha[num_frame2])
                            rival1.rect.x += 3 
                            rival1.rect.y += 2
                            rival1.setPosition(lp[0], lp[1])

                            clock.tick(12)
                            pantalla.blit(fondo, (0,0))
                            personaje.draw(pantalla)
                            rival1.draw(pantalla)
                            tl.draw(pantalla)
                            pygame.display.flip()
                            num_frame2 += 1



                clock.tick(12)
                pantalla.blit(fondo, (0,0))
                personaje.setPosition(personaje.rect.x, personaje.rect.y)
                personaje.draw(pantalla)
                boss_lista.draw(pantalla)
                rival1_lista.draw(pantalla)
                rival2_lista.draw(pantalla) 
                tl.draw(pantalla)
                pos = "RIGHT"                        
                pygame.display.flip()


#.......Punno Izquierdo-------------------------------------------------------------------------
        elif pos == "LEFT" and tecla[K_z] == 1 and tecla[K_x] == 0 and menu_activo == False:
            cont = 0
            num_frame = 0
            pygame.mixer.music.load("punno.wav")
            pygame.mixer.music.play(1)

            while cont < 1:
            	if flag_boss == True:
		        	lb = seguir(personaje.rect.x, personaje.rect.y, boss.rect.x, boss.rect.y)
			        boss.rect.x = lb[0]
			        boss.rect.y = lb[1]
			        boss.setPosition(boss.rect.x, boss.rect.y) 

                lp = seguir(personaje.rect.x, personaje.rect.y, rival1.rect.x, rival1.rect.y)
                rival1.rect.x = lp[0]
                rival1.rect.y = lp[1]

                ls = seguir(personaje.rect.x, personaje.rect.y, rival2.rect.x, rival2.rect.y)
                rival2.rect.x = ls[0]
                rival2.rect.y = ls[1]

                if num_frame >= len(hero1_puno_left):
                    num_frame = 0
                    personaje.setRect(hero1_puno_left[0])
                    cont += 1
                    
                personaje.setRect(hero1_puno_left[num_frame])
                num_frame += 1

                #Si hay colision con boss
                
                if len(boss_lista) > 0:  
                	lista_boss = pygame.sprite.spritecollide(personaje, boss_lista, True)

	                for rival in lista_boss:
	                    cont3 = 0
	                    num_frame3 = 0
	                    pygame.mixer.music.load("boss.wav")
	                    pygame.mixer.music.play(1)

	                    while cont3 < 1:
	                        if num_frame3 >= len(boss_muere_derecha):
	                            num_frame3 = 0
	                            cont3 += 1
	                            boss_muerte -= 1
	                            if boss_muerte > 0:
	                            	boss.setRect(boss_muere_derecha[0])
	                            	boss_lista.add(boss)
	                            	tl.add(boss)
	                        else:
	                            boss.setRect(boss_muere_derecha[num_frame3])

	                            if boss.rect.x >= 20:
	                            	boss.rect.x -= 20
	                            boss.setPosition(boss.rect.x, boss.rect.y)

	                            clock.tick(12)
	                            pantalla.blit(fondo, (0,0))
	                            personaje.draw(pantalla)
	                            boss.draw(pantalla)
	                            tl.draw(pantalla)
	                            pygame.display.flip()
	                            num_frame3 += 1


                #Si hay colision con un rival
                lista_rivales1 = pygame.sprite.spritecollide(personaje, rival2_lista, True)
                
                for rival in lista_rivales1:
                    cont1 = 0
                    num_frame1 = 0
                    pygame.mixer.music.load("rival.wav")
                    pygame.mixer.music.play(1)

                    while cont1 < 1:
                        if num_frame1 >= len(rival2_muere_izquierda):
                            num_frame1 = 0
                            cont1 += 1
                        else:
                            rival2.setRect(rival2_muere_izquierda[num_frame1])
                            rival2.rect.x -= 5 
                            rival2.rect.y -= 2
                            rival2.setPosition(ls[0], ls[1])

                            clock.tick(12)
                            pantalla.blit(fondo, (0,0))
                            personaje.draw(pantalla)
                            rival1_lista.draw(pantalla)
                            rival2_lista.draw(pantalla) 
                            tl.draw(pantalla)
                            pygame.display.flip()
                            num_frame1 += 1

                #Colision con el rival 1
                lista_rivales2 = pygame.sprite.spritecollide(personaje, rival1_lista, True)
                
                for rival in lista_rivales2:
                    cont2 = 0
                    num_frame2 = 0
                    pygame.mixer.music.load("rival.wav")
                    pygame.mixer.music.play(1)

                    while cont2 < 1:
                        if num_frame2 >= len(rival2_muere_izquierda):
                            num_frame2 = 0
                            cont2 += 1
                        else:
                            rival1.setRect(rival2_muere_izquierda[num_frame2])
                            rival1.rect.x -= 5 
                            rival1.rect.y -= 2
                            rival1.setPosition(lp[0], lp[1])

                            clock.tick(12)
                            pantalla.blit(fondo, (0,0))
                            personaje.draw(pantalla)
                            rival1.draw(pantalla)
                            tl.draw(pantalla)
                            pygame.display.flip()
                            num_frame2 += 1

                clock.tick(12)
                pantalla.blit(fondo, (0,0))
                personaje.setPosition(personaje.rect.x, personaje.rect.y)
                personaje.draw(pantalla) 
                rival1_lista.draw(pantalla)
                rival2_lista.draw(pantalla) 
                tl.draw(pantalla)
                pos = "LEFT"                        
                pygame.display.flip()

                
#.......Patada Derecha-------------------------------------------------------------------------
        if pos == "RIGHT" and tecla[K_x] == 1 and tecla[K_z] == 0 and menu_activo == False:
            cont = 0
            num_frame = 0
            pygame.mixer.music.load("patada.wav")
            pygame.mixer.music.play(1)

            while cont < 1:
            	if flag_boss == True:
		        	lb = seguir(personaje.rect.x, personaje.rect.y, boss.rect.x, boss.rect.y)
			        boss.rect.x = lb[0]
			        boss.rect.y = lb[1]
			        boss.setPosition(boss.rect.x, boss.rect.y) 

                lp = seguir(personaje.rect.x, personaje.rect.y, rival1.rect.x, rival1.rect.y)
                rival1.rect.x = lp[0]
                rival1.rect.y = lp[1]

                ls = seguir(personaje.rect.x, personaje.rect.y, rival2.rect.x, rival2.rect.y)
                rival2.rect.x = ls[0]
                rival2.rect.y = ls[1]

                if num_frame >= len(hero1_patada_right):
                    num_frame = 0
                    cont += 1
                    personaje.setRect(hero1_patada_right[0])
                personaje.setRect(hero1_patada_right[num_frame])
                num_frame += 1

                #Si hay colision con boss
                
                if len(boss_lista) > 0:  
                	lista_boss = pygame.sprite.spritecollide(personaje, boss_lista, True)

	                for rival in lista_boss:
	                    cont3 = 0
	                    num_frame3 = 0
	                    pygame.mixer.music.load("boss.wav")
	                    pygame.mixer.music.play(1)

	                    while cont3 < 1:
	                        if num_frame3 >= len(boss_muere_izquierda):
	                            num_frame3 = 0
	                            cont3 += 1
	                            boss_muerte -= 1
	                            if boss_muerte > 0:
	                            	boss.setRect(boss_muere_izquierda[0])
	                            	boss_lista.add(boss)
	                            	tl.add(boss)
	                        else:
	                            boss.setRect(boss_muere_izquierda[num_frame3])
	                            if boss.rect.x <= 966:
	                            	boss.rect.x += 20
	                            
	                            boss.setPosition(boss.rect.x, boss.rect.y)

	                            clock.tick(12)
	                            pantalla.blit(fondo, (0,0))
	                            personaje.draw(pantalla)
	                            boss.draw(pantalla)
	                            tl.draw(pantalla)
	                            pygame.display.flip()
	                            num_frame3 += 1
                
                #Colision con el rival2
                lista_rivales2 = pygame.sprite.spritecollide(personaje, rival2_lista, True)
                
                for rival in lista_rivales2:
                    cont2 = 0
                    num_frame2 = 0

                    while cont2 < 1:
                        if num_frame2 >= len(rival2_muere_derecha):
                            num_frame2 = 0
                            cont2 += 1
                            pygame.mixer.music.load("rival.wav")
                            pygame.mixer.music.play(1)
                        else:
                            rival2.setRect(rival2_muere_derecha[num_frame2])
                            rival2.rect.x += 5 
                            rival2.rect.y += 2
                            rival2.setPosition(ls[0], ls[1])

                            clock.tick(12)
                            pantalla.blit(fondo, (0,0))
                            personaje.draw(pantalla)
                            rival2.draw(pantalla)
                            tl.draw(pantalla)
                            pygame.display.flip()
                            num_frame2 += 1

                #Colision con el rival 1
                lista_rivales1 = pygame.sprite.spritecollide(personaje, rival1_lista, True)
                
                for rival in lista_rivales1:
                    cont1 = 0
                    num_frame1 = 0

                    while cont1 < 1:
                        if num_frame1 >= len(rival2_muere_derecha):
                            num_frame1 = 0
                            cont1 += 1
                            pygame.mixer.music.load("rival.wav")
                            pygame.mixer.music.play(1)
                        else:
                            rival1.setRect(rival2_muere_derecha[num_frame1])
                            rival1.rect.x += 5 
                            rival1.rect.y += 2
                            rival1.setPosition(lp[0], lp[1])

                            clock.tick(12)
                            pantalla.blit(fondo, (0,0))
                            personaje.draw(pantalla)
                            rival1.draw(pantalla)
                            tl.draw(pantalla)
                            pygame.display.flip()
                            num_frame1 += 1

                clock.tick(12)
                pantalla.blit(fondo, (0,0))
                personaje.setPosition(personaje.rect.x, personaje.rect.y)
                personaje.draw(pantalla) 
                rival1_lista.draw(pantalla)
                rival2_lista.draw(pantalla)
                tl.draw(pantalla)
                pos = "RIGHT"                        
                pygame.display.flip()

#.......Patada Izquierda-------------------------------------------------------------------------
        elif pos == "LEFT" and tecla[K_x] == 1 and tecla[K_z] == 0 and menu_activo == False:
            cont = 0
            num_frame = 0
            pygame.mixer.music.load("patada.wav")
            pygame.mixer.music.play(1)

            while cont < 1:
            	if flag_boss == True:
		        	lb = seguir(personaje.rect.x, personaje.rect.y, boss.rect.x, boss.rect.y)
			        boss.rect.x = lb[0]
			        boss.rect.y = lb[1]
			        boss.setPosition(boss.rect.x, boss.rect.y) 

                lp = seguir(personaje.rect.x, personaje.rect.y, rival1.rect.x, rival1.rect.y)
                rival1.rect.x = lp[0]
                rival1.rect.y = lp[1]

                ls = seguir(personaje.rect.x, personaje.rect.y, rival2.rect.x, rival2.rect.y)
                rival2.rect.x = ls[0]
                rival2.rect.y = ls[1]

                if num_frame >= len(hero1_patada_left):
                    num_frame = 0
                    cont += 1
                    personaje.setRect(hero1_patada_left[0])
                personaje.setRect(hero1_patada_left[num_frame])
                num_frame += 1

                #Si hay colision con boss
                
                if len(boss_lista) > 0:  
                	lista_boss = pygame.sprite.spritecollide(personaje, boss_lista, True)

	                for rival in lista_boss:
	                    cont3 = 0
	                    num_frame3 = 0
	                    pygame.mixer.music.load("boss.wav")
	                    pygame.mixer.music.play(1)

	                    while cont3 < 1:
	                        if num_frame3 >= len(boss_muere_derecha):
	                            num_frame3 = 0
	                            cont3 += 1
	                            boss_muerte -= 1
	                            if boss_muerte > 0:
	                            	boss.setRect(boss_muere_derecha[0])
	                            	boss_lista.add(boss)
	                            	tl.add(boss)
	                        else:
	                            boss.setRect(boss_muere_derecha[num_frame3])

	                            if boss.rect.x >= 20:
	                            	boss.rect.x -= 20
	                            boss.setPosition(boss.rect.x, boss.rect.y)

	                            clock.tick(12)
	                            pantalla.blit(fondo, (0,0))
	                            personaje.draw(pantalla)
	                            boss.draw(pantalla)
	                            tl.draw(pantalla)
	                            pygame.display.flip()
	                            num_frame3 += 1

                #Colision con el rival2
                lista_rivales2 = pygame.sprite.spritecollide(personaje, rival2_lista, True)
                
                for rival in lista_rivales2:
                    cont2 = 0
                    num_frame2 = 0

                    while cont2 < 1:
                        if num_frame2 >= len(rival2_muere_izquierda):
                            num_frame2 = 0
                            cont2 += 1
                            pygame.mixer.music.load("rival.wav")
                            pygame.mixer.music.play(1)
                        else:
                            rival2.setRect(rival2_muere_izquierda[num_frame2])
                            rival2.rect.x -= 5 
                            rival2.rect.y -= 2
                            rival2.setPosition(ls[0], ls[1])

                            clock.tick(12)
                            pantalla.blit(fondo, (0,0))
                            personaje.draw(pantalla)
                            rival2.draw(pantalla)
                            tl.draw(pantalla)
                            pygame.display.flip()
                            num_frame2 += 1

                #Colision con el rival 1
                lista_rivales1 = pygame.sprite.spritecollide(personaje, rival1_lista, True)
                
                for rival in lista_rivales1:
                    cont1 = 0
                    num_frame1 = 0

                    while cont1 < 1:
                        if num_frame1 >= len(rival2_muere_izquierda):
                            num_frame1 = 0
                            cont1 += 1
                            pygame.mixer.music.load("rival.wav")
                            pygame.mixer.music.play(1)
                        else:
                            rival1.setRect(rival2_muere_izquierda[num_frame1])
                            rival1.rect.x += 5 
                            rival1.rect.y += 2
                            rival1.setPosition(lp[0], lp[1])

                            clock.tick(12)
                            pantalla.blit(fondo, (0,0))
                            personaje.draw(pantalla)
                            rival1.draw(pantalla)
                            tl.draw(pantalla)
                            pygame.display.flip()
                            num_frame1 += 1

                clock.tick(12)
                pantalla.blit(fondo, (0,0))
                personaje.setPosition(personaje.rect.x, personaje.rect.y)
                personaje.draw(pantalla) 
                rival1_lista.draw(pantalla)
                rival2_lista.draw(pantalla) 
                tl.draw(pantalla)
                pos = "LEFT"                        
                pygame.display.flip()



        if event.type == pygame.QUIT or tecla[K_ESCAPE]:
            pygame.mixer.music.load("ff.mp3")
            pygame.mixer.music.play(1)
            pygame.time.wait(500)
            pygame.display.flip()
            pantalla.blit(fondo1, (0,0))
            pygame.display.flip()
            clock.tick(0.1)
            walking = False