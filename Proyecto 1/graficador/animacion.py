import pygame,sys,time
from pygame.locals import *
pygame.init()
finish = False
#import py_compile
#Comando para crear ejecutables
#py_compile.compile('animacion.py')

#colisiones:
#http://www.taringa.net/posts/linux/14655133/Colision-de-Objetos-en-Pygame.html
#http://developeando.net/tutorial-pygame-colisiones/
#http://pygamesbardella.blogspot.com/2012/05/control-del-teclado-y-colisiones-pygame.html

#--------------------------------------------------------------------------------------------------
#Clase para usar en cualquier sprite

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
        
    def invert(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def scale2(self):
      self.image = pygame.transform.scale2x(self.image)

    def scale(self,ax,ay):
      self.image = pygame.transform.scale(self.image, (self.image.get_width() * ax, self.image.get_height() * ay))

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

#--------------------------------------------------------------------------------------------------
#definimos la pantalla

colorfondo = 255, 255, 255
tamano = ancho, alto = 865, 321
pantalla = pygame.display.set_mode(tamano)
pygame.display.set_caption('ANIMACION')
fondo = pygame.image.load("../imagenes/mundo2.png")
fondo2 = pygame.image.load("../imagenes/letrero.png")
pantalla.blit(fondo,(0,0))
pygame.display.flip()
 
pygame.mixer.music.load("tema3.mp3")
pygame.mixer.music.play(1)
#--------------------------------------------------------------------------------------------------
#definimos sprites de los personajes y explosiones

personaje = Sprite("../imagenes/zero2.png",pygame.Rect(414,7,37,41))
personaje.setPosition(520,220)
personaje.draw(pantalla)


personaje2 = Sprite("../imagenes/megaman.png",pygame.Rect(140,13,37,38))
personaje2.setPosition(450,220)
personaje2.invert()
personaje2.draw(pantalla)

personaje3 = Sprite("../imagenes/purprill.png",pygame.Rect(729,665,65,54))
personaje3.setPosition(765,200)
personaje3.draw(pantalla)

personaje4 = Sprite("../imagenes/malo2.png",pygame.Rect(261,225,49,66))
personaje4.setPosition(140,200)
personaje4.invert()
personaje4.draw(pantalla)

balas = Sprite("../imagenes/dispa.png",pygame.Rect(455,600,46,32))
balas.setPosition(710,220)
pygame.display.flip()

balas2 = Sprite("../imagenes/balas.gif",pygame.Rect(101,401,42,35))
balas2.setPosition(214,215)
balas2.invert()
pygame.display.flip()

explosion1 = Sprite("../imagenes/explo.png",pygame.Rect(42,67,18,18))
explosion1.setPosition(765,200)
explosion1.scale(4,4)

explosion2 = Sprite("../imagenes/explo.png",pygame.Rect(42,67,18,18))
explosion2.setPosition(140,200)
explosion2.scale(4,4)

#--------------------------------------------------------------------------------------------------
#Definimos los pasos de zero

num_frame_zero = 0
caminando_zero = [  pygame.Rect(452,7,35,41), \
                    pygame.Rect(486,7,31,41), \
                    pygame.Rect(517,10,38,38), \
                    pygame.Rect(555,8,42,40), \
                    pygame.Rect(597,9,34,39), \
                    pygame.Rect(631,10,24,38), \
                    pygame.Rect(656,8,32,40), \
                    pygame.Rect(687,9,38,39), \
                    pygame.Rect(725,7,39,40), \
                    pygame.Rect(764,8,37,40), \
                    pygame.Rect(801,9,34,39), \
                    pygame.Rect(414,7,37,41)
                ]

#--------------------------------------------------------------------------------------------------
#Definimos los disparos de zero

num_frame_zero2 = 0
disparo_zero = [ pygame.Rect(222,1128,47,41), \
                 pygame.Rect(222,1128,47,41), \
                 pygame.Rect(329,1078,49,41), \
                 pygame.Rect(329,1078,49,41), \
               ]
                
#--------------------------------------------------------------------------------------------------
#Definimos los pasos de megaman 

num_frame_megaman = 0
caminando_megaman = [ pygame.Rect(292,13,33,38), \
                      pygame.Rect(324,13,29,38), \
                      pygame.Rect(353,16,38,35), \
                      pygame.Rect(392,14,42,37), \
                      pygame.Rect(433,15,35,36), \
                      pygame.Rect(469,16,24,36), \
                      pygame.Rect(492,15,32,37), \
                      pygame.Rect(524,15,38,36), \
                      pygame.Rect(562,13,36,38), \
                      pygame.Rect(598,14,32,38), \
                      pygame.Rect(630,16,26,36), \
                      pygame.Rect(140,13,37,38)
                    ]
#--------------------------------------------------------------------------------------------------
#Definimos los disparos de zero

num_frame_megaman2 = 0
disparo_megaman = [ pygame.Rect(195,973,41,40), \
                    pygame.Rect(195,973,41,40), \
                    pygame.Rect(236,972,41,41), \
                    pygame.Rect(236,972,41,41), \
                  ]

#--------------------------------------------------------------------------------------------------
#Definimos los pasos de purprill

num_frame_purprill = 0
mov_purprill = [ pygame.Rect(729,665,65,56), \
                 pygame.Rect(794,665,65,55)
               ]

#Purprill destruyendose

num_frame_purprill2 = 0
mov_purprill2 = [ pygame.Rect(729,665,65,56), \
                  pygame.Rect(794,665,65,55), \
                  pygame.Rect(751,730,84,78), \
                  pygame.Rect(835,730,114,78)
                ] 

#--------------------------------------------------------------------------------------------------
#Definimos los pasos del malo 2 

num_frame_malo2 = 0
mov_malo2 = [ pygame.Rect(357,224,77,68), \
              pygame.Rect(439,225,43,63), 
            ]

#malo2 destruyendose
num_frame_malo22 = 0
mov_malo22 = [ #pygame.Rect(357,224,77,68), \
               pygame.Rect(439,225,43,63), \
               pygame.Rect(658,298,47,71), \
               pygame.Rect(415,309,53,51)
             ]

#--------------------------------------------------------------------------------------------------
#Definimos las explosiones

num_frame_explo1 = 0
mov_explo1 = [ pygame.Rect(59,63,30,26), \
               pygame.Rect(90,62,33,29), \
               pygame.Rect(124,59,35,32), \
               pygame.Rect(161,65,34,27), \
               pygame.Rect(204,71,34,21), 
            ]

num_frame_explo2 = 0
mov_explo2 = [ pygame.Rect(59,63,30,26), \
               pygame.Rect(90,62,33,29), \
               pygame.Rect(124,59,35,32), \
               pygame.Rect(161,65,34,27), \
               pygame.Rect(204,71,34,21), 
            ]

#--------------------------------------------------------------------------------------------------
clock = pygame.time.Clock()
bandera = True
run = True
k = 0
k2 = 0
i = 0
i2 = 0
band = False
band2 = True
band3 = False
band4 = True
bandfinal1 = False
bandfinal2 = False
cont_dead = len(mov_purprill2)-1
cont_disp = 0
cont_dead2 = len(mov_malo22)-1
cont_disp2 = 0
contaux = 0
contaux2 = 0

while run:
    if bandfinal1 and bandfinal2:
        run = False

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

#--------------------------------------------------------------------------------------------------
# ZERO Y PURPRILL 
    if num_frame_zero >= len(caminando_zero):
        num_frame_zero = 0

    personaje.setRect(caminando_zero[num_frame_zero])
    num_frame_zero += 1

    #Hace que aparezca el cargando 
    if bandera:
        pantalla.blit(fondo,(0,0))
    if not bandera:
        pantalla.blit(fondo2,(0,0))

   #Zero caminando
    if k < 175:
        x = 520+k
        personaje.setPosition(x,220)
        k+=15

    #zero disparando
    if k>=175 and num_frame_purprill2 < 4:
       band = True
       personaje.setPosition(x-15,220)
       personaje.setRect(pygame.Rect(112,7,37,41))

       if num_frame_zero2 >= len(disparo_zero):
            num_frame_zero2 = 0

       personaje.setRect(disparo_zero[num_frame_zero2])
       num_frame_zero2 += 1

       #Desplazamiento de la bala
       i += 30
       if 710+i > ancho-75:
            i = 0
   
       balas.setPosition(710+i,220)
       balas.draw(pantalla)
       clock.tick(35)

    #Deja a zero quieto y sin disparar
    elif num_frame_purprill2 >= 4:
        personaje.setRect(disparo_zero[0])

    #Purprill moviendose
    if band2:
        if num_frame_purprill >= len(mov_purprill):
            num_frame_purprill = 0
        personaje3.setRect(mov_purprill[num_frame_purprill])
        num_frame_purprill += 1

    #Purprill recibiendo el disparo
    if  balas.rect.colliderect(personaje3.rect) and band:
        if num_frame_purprill2 < 4:
            if num_frame_purprill2 >= cont_dead:
                num_frame_purprill2 = 0
            personaje3.setRect(mov_purprill2[num_frame_purprill2])
            num_frame_purprill2 += 1
            cont_disp += 1
            if cont_disp == 15:
                cont_dead = len(mov_purprill2)
        band2 = False

        #efecto de destruccion
        if num_frame_purprill2 == cont_dead:
            contaux += 1
            if contaux > 5:
              personaje3.setPosition(900,0)
              if num_frame_explo1 >= len(mov_explo1):
                  num_frame_explo1 = len(mov_explo1)-1
              explosion1.setRect(mov_explo1[num_frame_explo1])
              num_frame_explo1 += 1
              explosion1.scale(3,3)
              explosion1.draw(pantalla)
              if num_frame_explo1 == len(mov_explo1)-1:
                  bandfinal1 = True


#--------------------------------------------------------------------------------------------------
#MEGAMAN Y MALO 2

    #megaman caminando
    if num_frame_megaman >= len(caminando_megaman):
        num_frame_megaman = 0

    personaje2.setRect(caminando_megaman[num_frame_megaman])
    personaje2.invert()
    num_frame_megaman+= 1

    if k2 < 175:
        x2 = 450-k
        personaje2.setPosition(x2,220)
        k2+=15

    #megaman disparando
    if k>=175 and num_frame_malo22 < 3:
       band3 = True
       personaje2.setPosition(x2-15,220)

       if num_frame_megaman2 >= len(disparo_megaman):
            num_frame_megaman2 = 0

       personaje2.setRect(disparo_megaman[num_frame_megaman2])
       personaje2.invert()
       num_frame_megaman2 += 1

       #Desplazamiento de la bala
       i2 -= 35
       if 214+i2 < 142:
            i2 = 0
   
       balas2.setPosition(214+i2,215)
       balas2.draw(pantalla)
       clock.tick(35)

    #Deja a zero quieto y sin disparar
    elif num_frame_malo22 >= 3:
        personaje2.setRect(disparo_megaman[0])
        personaje2.invert()

    #malo moviendose
    if band4:
      if num_frame_malo2 >= len(mov_malo2):
          num_frame_malo2 = 0
      personaje4.setRect(mov_malo2[num_frame_malo2])
      personaje4.invert()
      num_frame_malo2 += 1

    #malo2 recibiendo el disparo
    if balas2.rect.colliderect(personaje4.rect) and band3:
      if num_frame_malo22 < 3:
          if num_frame_malo22 >= cont_dead2:
              num_frame_malo22 = 0
          personaje4.setRect(mov_malo22[num_frame_malo22])
          personaje4.invert()
          num_frame_malo22 += 1
          cont_disp2 += 1
          if cont_disp2 == 15:
              cont_dead2 = len(mov_malo22)
      band4 = False

      #efecto de destruccion
      if num_frame_malo22 == cont_dead2:
          contaux2 += 1
          if contaux2 > 8:
            personaje4.setPosition(900,0)
            if num_frame_explo2 >= len(mov_explo2):
                  num_frame_explo2 = len(mov_explo2)-1
            explosion2.setRect(mov_explo2[num_frame_explo2])
            num_frame_explo2 += 1
            explosion2.scale(3,3)
            explosion2.draw(pantalla)
            if num_frame_explo2 == len(mov_explo2)-1:
                bandfinal2 = True

    bandera = not bandera
    personaje.draw(pantalla)
    personaje2.draw(pantalla)
    personaje3.draw(pantalla)
    personaje4.draw(pantalla)
    time.sleep(0.4)
    pygame.display.flip()

#Mensaje se bienvenida
pygame.display.set_caption('SALUDOS')
fondob = pygame.image.load("../imagenes/bienvenidos.png").convert()
pantalla.blit(fondob,(0,0))
pygame.display.flip()
time.sleep(3)
finish = True
pygame.mixer.music.stop()