import sys
import pygame
import math
import libreriaGraficaPaint
from pygame.locals import *
#-----------------------------------------------

def radio(cor1,cor2):
    x = cor1[0] - cor2[0]
    y = cor1[1] - cor2[1]
    d = 1.0 * math.sqrt((x * x)+(y * y))
    return int(d)

def cuadrante(cor):
    if(cor[0]<50 and cor[1]<50):
        return 0
    if(cor[0]<50 and cor[1]>50 and cor[1]<100):
        return 1
    if(cor[0]<50 and cor[1]>100 and cor[1]<150):
        return 2
    if(cor[0]<50 and cor[1]>150 and cor[1]<200):
        return 3
    if(cor[0]<50 and cor[1]>200 and cor[1]<250):
        return 4
    if(cor[0]<50 and cor[1]>250 and cor[1]<300):
        return 5
    if(cor[0]<50 and cor[1]>300 and cor[1]<350):
        return 6
    if(cor[0]<50 and cor[1]>350 and cor[1]<400):
        return 7
    if(cor[0]>200  and cor[1]<500): ##area de trabajo
        return 8
    #cuadrante lineas-----------------------------------------
    if(cor[0]>50 and cor[0]<100 and cor[1]>50  and cor[1]<100):
        return 9
    if(cor[0]>100 and cor[0]<150 and cor[1]>50  and cor[1]<100):
        return 10
    if(cor[0]>150 and cor[0]<200 and cor[1]>50  and cor[1]<100):
        return 11
    #cuadrante poligonos------------------------------------
    if(cor[0]>50 and cor[0]<100 and cor[1]>100  and cor[1]<150):
        return 12
    if(cor[0]>100 and cor[0]<150 and cor[1]>100  and cor[1]<150):
        return 13
    #cuadrante Elipses--------------------------------------
    if(cor[0]>50 and cor[0]<100 and cor[1]>150  and cor[1]<200):
        return 14
    if(cor[0]>100 and cor[0]<150 and cor[1]>150  and cor[1]<200):
        return 15
#-----------------------------------------------
def cuadrantecolor(cor):
    if(cor[0]>50 and cor[0]<100 and cor[1]>500 and cor[1]<550):
        return 0
    if(cor[0]>100 and cor[0]<150 and cor[1]>500 and cor[1]<550):
        return 1
    if(cor[0]>150 and cor[0]<200 and cor[1]>500 and cor[1]<550):
        return 2 
    if(cor[0]>50 and cor[0]<100 and cor[1]>550 and cor[1]<600):
        return 3
    if(cor[0]>100 and cor[0]<150 and cor[1]>550 and cor[1]<600):
        return 4
    if(cor[0]>150 and cor[0]<200 and cor[1]>550 and cor[1]<600):
        return 5
    else:
        return 10

    
pantalla = pygame.display.set_mode((800,600)) 
pantalla.fill((255,255,255))
relleno = 0
Panel_Botones = pygame.Surface((200, 500))
Panel_Botones.fill((193,193,193))

panelColores = pygame.Surface((800, 100))
panelColores.fill((193,193,193))

Area_Dibujo = pygame.Surface((600, 500))
Area_Dibujo.fill((255,255,255))
#---------------------------------------

#panel de colores
color = (0,0,0)
scolor = pygame.Surface((200, 100))
scolor.fill(color)
def panelcolor():
    pygame.draw.rect(scolor, color, [0,0,50, 100])
    pygame.draw.rect(scolor, (0,0,0), [0,0,50, 100],4)
    pygame.draw.rect(scolor, (255,100,100), [50,0,50, 50])
    pygame.draw.rect(scolor, (100,255,100), [50,50,50, 50])
    pygame.draw.rect(scolor, (100,100,255), [100,0,50, 50])
    pygame.draw.rect(scolor, (255,255,100), [100,50,50, 50])
    pygame.draw.rect(scolor, (0,0,0), [150,0,50,50])
    pygame.draw.rect(scolor, (255,255,255), [150,50,50, 50])
    panelColores.blit(scolor,(0,0))
    pantalla.blit(panelColores,(0,500))

panelcolor()



#-------------------imagenes botones
figura1 = pygame.image.load('punto.jpg')
figura2 = pygame.image.load('linea.jpg')
figura3 = pygame.image.load('poligono.jpg')
figura4 = pygame.image.load('circulo.jpg')
figura5 = pygame.image.load('tijeras.jpg')
figura6 = pygame.image.load('importar.jpg')
figura7 = pygame.image.load('borrar.jpg')
figura8 = pygame.image.load('relleno.jpg')
####figuras lineas
figura9 = pygame.image.load('BR.jpg')
figura10 = pygame.image.load('pm.jpg')
figura11 = pygame.image.load('Dda.jpg')
####POLIGONOS
figura12 = pygame.image.load('PR.jpg')
figura13 = pygame.image.load('PI.jpg')
## circunferencias
figura14 = pygame.image.load('Cr.jpg')
figura15 = pygame.image.load('elipse.jpg')

goku = pygame.image.load('goku.jpg')

#--------------------botones presionados
presion1 = pygame.image.load('punto1.jpg')
presion2 = pygame.image.load('linea1.jpg')
presion3 = pygame.image.load('poligono1.jpg')
presion4 = pygame.image.load('circulo1.jpg')
presion5 = pygame.image.load('tijeras1.jpg')
presion6 = pygame.image.load('importar1.jpg')
presion7 = pygame.image.load('borrar1.jpg')
presion8 = pygame.image.load('relleno1.jpg')
####figuras lineas
presion9 = pygame.image.load('BR1.jpg')
presion10 = pygame.image.load('pm1.jpg')
presion11 = pygame.image.load('Dda1.jpg')
####POLIGONOS
presion12 = pygame.image.load('PR1.jpg')
presion13 = pygame.image.load('PI1.jpg')
## circunferencias
presion14 = pygame.image.load('Cr1.jpg')
presion15 = pygame.image.load('elipse1.jpg')




#-------------panel botones
def pbotones(pantalla):
    pantalla.blit(figura1,(0,0))
    pantalla.blit(figura2,(0,50))
    pantalla.blit(figura3,(0,100))
    pantalla.blit(figura4,(0,150))
    pantalla.blit(figura5,(0,200))
    pantalla.blit(figura6,(0,250))
    pantalla.blit(figura7,(0,300))
    if(relleno == 0):
        pantalla.blit(figura8,(0,350))
    
    ####linea-----------------
    pantalla.blit(figura9,(50,50))
    pantalla.blit(figura10,(100,50))
    pantalla.blit(figura11,(151,50))
    ####poligono
    pantalla.blit(figura12,(50,100))
    pantalla.blit(figura13,(100,100))
    ####circunferencia
    pantalla.blit(figura14,(50,150))
    pantalla.blit(figura15,(100,150))
    
pbotones(Panel_Botones)
botonPunto = False
botonLinea = False
botonPoligono = False
botonCortar = False
botonCircunferencia = False
botonImportar = False
botonBorrar = False
botonRecorte = False


tipoLinea = 0 # 0=bresenham,1=puntomedio,2=dda
tipoPoligono = 0
tipoCirculo = 0
flagBoton = 0
lista_click = []
#### vector poligono irregular
vectorX = []
vectorY = []
#-----------------------


listaBotones = [botonPunto,botonLinea,botonPoligono,
                botonCircunferencia,botonCortar, botonImportar,botonBorrar]
pantalla.blit(Panel_Botones,(0,0))
pantalla.blit(Area_Dibujo,(200,0))
salir = False


while salir!= True:
#activo boton punto
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrante(pygame.mouse.get_pos())==0):
        pbotones(Panel_Botones)
        for i in range(1,len(listaBotones)):
            listaBotones[i]= False
        if(flagBoton <= 1):
            listaBotones[0] = True
            Panel_Botones.blit(presion1,(0,0))
            pantalla.blit(Panel_Botones,(0,0))
            flagBoton = flagBoton + 1
            print "activado"
        if (flagBoton > 1):
            listaBotones[0] = False
            Panel_Botones.blit(figura1,(0,0))
            pantalla.blit(Panel_Botones,(0,0))
            print "desactivado"
            flagBoton = 0
        pygame.time.delay(100)
#-------------------------------------------------------------
#activo boton linea
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrante(pygame.mouse.get_pos())==1):
        pbotones(Panel_Botones)
        for i in range(1,len(listaBotones)):
                listaBotones[i]= False
        if(flagBoton <= 1):
            listaBotones[1] = True
            Panel_Botones.blit(presion2,(0,50))
            pantalla.blit(Panel_Botones,(0,0))
            flagBoton = flagBoton + 1
            print "activado"
        if (flagBoton > 1):
            listaBotones[1] = False
            Panel_Botones.blit(figura2,(0,50))
            pantalla.blit(Panel_Botones,(0,0))
            print "desactivado"
            flagBoton = 0
        pygame.time.delay(100)
#activo boton linea Bressenham
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrante(pygame.mouse.get_pos())==9):
        pbotones(Panel_Botones)
        for i in range(1,len(listaBotones)):
                listaBotones[i]= False
        if(flagBoton <= 1):
            listaBotones[1] = True
            tipoLinea = 0
            Panel_Botones.blit(presion2,(0,50))
            Panel_Botones.blit(presion9,(50,50))
            pantalla.blit(Panel_Botones,(0,0))
            flagBoton = flagBoton + 1
            print "activado"
        if (flagBoton > 1):
            listaBotones[1] = False
            Panel_Botones.blit(figura9,(50,50))
            pantalla.blit(Panel_Botones,(0,0))
            print "desactivado"
            flagBoton = 0
        pygame.time.delay(100)
#activo boton linea punto medio
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrante(pygame.mouse.get_pos())==10):
        pbotones(Panel_Botones)
        for i in range(1,len(listaBotones)):
                listaBotones[i]= False
        if(flagBoton <= 1):
            listaBotones[1] = True
            tipoLinea = 1
            Panel_Botones.blit(presion2,(0,50))
            Panel_Botones.blit(presion10,(100,50))
            pantalla.blit(Panel_Botones,(0,0))
            flagBoton = flagBoton + 1
            print "activado"
        if (flagBoton > 1):
            listaBotones[1] = False
            Panel_Botones.blit(figura10,(100,50))
            pantalla.blit(Panel_Botones,(0,0))
            print "desactivado"
            flagBoton = 0
        pygame.time.delay(100)
#activo boton linea dda
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrante(pygame.mouse.get_pos())==11):
        pbotones(Panel_Botones)
        for i in range(1,len(listaBotones)):
                listaBotones[i]= False
        if(flagBoton <= 1):
            listaBotones[1] = True
            tipoLinea = 2
            Panel_Botones.blit(presion2,(0,50))
            Panel_Botones.blit(presion11,(150,50))
            pantalla.blit(Panel_Botones,(0,0))
            flagBoton = flagBoton + 1
            print "activado"
        if (flagBoton > 1):
            listaBotones[1] = False
            Panel_Botones.blit(figura11,(150,50))
            pantalla.blit(Panel_Botones,(0,0))
            print "desactivado"
            flagBoton = 0
        pygame.time.delay(100)

#----------------------------------------------------------------------------------------

#activo boton poligono        
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrante(pygame.mouse.get_pos())==2):
        pbotones(Panel_Botones)
        for i in range(1,len(listaBotones)):
            listaBotones[i]= False
        if(flagBoton <= 1):
            listaBotones[2] = True
            Panel_Botones.blit(presion3,(0,100))
            pantalla.blit(Panel_Botones,(0,0))
            flagBoton = flagBoton + 1
            print "activado"
        if (flagBoton > 1):
            listaBotones[2] = False
            Panel_Botones.blit(figura3,(0,100))
            pantalla.blit(Panel_Botones,(0,0))
            print "desactivado"
            flagBoton = 0
        pygame.time.delay(100)

#activo poligono regular
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrante(pygame.mouse.get_pos())==12):
        pbotones(Panel_Botones)
        for i in range(1,len(listaBotones)):
            listaBotones[i]= False
        if(flagBoton <= 1):
            listaBotones[2] = True
            tipoPoligono = 0
            Panel_Botones.blit(presion12,(50,100))
            Panel_Botones.blit(presion3,(0,100))
            pantalla.blit(Panel_Botones,(0,0))
            flagBoton = flagBoton + 1
            print "activado"
        if (flagBoton > 1):
            listaBotones[2] = False
            Panel_Botones.blit(figura12,(50,100))
            pantalla.blit(Panel_Botones,(0,0))
            print "desactivado"
            flagBoton = 0
        pygame.time.delay(100)
#activo poligono iregular
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrante(pygame.mouse.get_pos())==13):
        pbotones(Panel_Botones)
        for i in range(1,len(listaBotones)):
            listaBotones[i]= False
        if(flagBoton <= 1):
            listaBotones[2] = True
            tipoPoligono = 1
            Panel_Botones.blit(presion13,(100,100))
            Panel_Botones.blit(presion3,(0,100))
            pantalla.blit(Panel_Botones,(0,0))
            flagBoton = flagBoton + 1
            print "activado"
        if (flagBoton > 1):
            listaBotones[2] = False
            Panel_Botones.blit(figura13,(100,100))
            pantalla.blit(Panel_Botones,(0,0))
            print "desactivado"
            flagBoton = 0
        pygame.time.delay(100)

        
#----------------------------------------------------------------------------------------
#activo boton circunferencia
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrante(pygame.mouse.get_pos())==3):
        pbotones(Panel_Botones)
        for i in range(1,len(listaBotones)):
            listaBotones[i]= False
        if(flagBoton <= 1):
            listaBotones[3] = True
            Panel_Botones.blit(presion4,(0,150))
            pantalla.blit(Panel_Botones,(0,0))
            flagBoton = flagBoton + 1
            print "activado"
        if (flagBoton > 1):
            listaBotones[3] = False
            Panel_Botones.blit(figura4,(0,150))
            pantalla.blit(Panel_Botones,(0,0))
            print "desactivado"
            flagBoton = 0
        pygame.time.delay(100)
# circulo
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrante(pygame.mouse.get_pos())==14):
        pbotones(Panel_Botones)
        for i in range(1,len(listaBotones)):
            listaBotones[i]= False
        if(flagBoton <= 1):
            listaBotones[3] = True
            tipoCirculo = 0
            Panel_Botones.blit(presion14,(50,150))
            pantalla.blit(Panel_Botones,(0,0))
            flagBoton = flagBoton + 1
            print "activado"
        if (flagBoton > 1):
            listaBotones[3] = False
            Panel_Botones.blit(figura14,(50,150))
            pantalla.blit(Panel_Botones,(0,0))
            print "desactivado"
            flagBoton = 0
        pygame.time.delay(100)
        
# elipse 
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrante(pygame.mouse.get_pos())==15):
        pbotones(Panel_Botones)
        for i in range(1,len(listaBotones)):
            listaBotones[i]= False
        if(flagBoton <= 1):
            listaBotones[3] = True
            tipoCirculo = 1
            Panel_Botones.blit(presion15,(100,150))
            pantalla.blit(Panel_Botones,(0,0))
            flagBoton = flagBoton + 1
            print "activado"
        if (flagBoton > 1):
            listaBotones[3] = False
            Panel_Botones.blit(figura15,(100,150))
            pantalla.blit(Panel_Botones,(0,0))
            print "desactivado"
            flagBoton = 0
        pygame.time.delay(100)




#activo boton cortar
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrante(pygame.mouse.get_pos())==4):
        pbotones(Panel_Botones)
        for i in range(1,len(listaBotones)):
            listaBotones[i]= False
        if(flagBoton <= 1):
            listaBotones[4] = True
            Panel_Botones.blit(presion5,(0,200))
            pantalla.blit(Panel_Botones,(0,0))
            flagBoton = flagBoton + 1
            print "activado"
        if (flagBoton > 1):
            listaBotones[4] = False
            Panel_Botones.blit(figura5,(0,200))
            pantalla.blit(Panel_Botones,(0,0))
            print "desactivado"
            flagBoton = 0
        pygame.time.delay(100)

#activo boton importar
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrante(pygame.mouse.get_pos())==5):
        pbotones(Panel_Botones)
        for i in range(1,len(listaBotones)):
            listaBotones[i]= False
        if(flagBoton <= 1):
            listaBotones[5] = True
            Panel_Botones.blit(presion6,(0,250))
            pantalla.blit(Panel_Botones,(0,0))
            flagBoton = flagBoton + 1
            print "activado"
        if (flagBoton > 1):
            listaBotones[5] = False
            Panel_Botones.blit(figura6,(0,250))
            pantalla.blit(Panel_Botones,(0,0))
            print "desactivado"
            flagBoton = 0
        pygame.time.delay(100)
#activo boton borrar
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrante(pygame.mouse.get_pos())==6):
        pbotones(Panel_Botones)
        for i in range(1,len(listaBotones)):
            listaBotones[i]= False
        if(flagBoton <= 1):
            listaBotones[6] = True
            Panel_Botones.blit(presion7,(0,300))
            pantalla.blit(Panel_Botones,(0,0))
            flagBoton = flagBoton + 1
            print "activado"
        if (flagBoton > 1):
            listaBotones[6] = False
            Panel_Botones.blit(figura7,(0,300))
            pantalla.blit(Panel_Botones,(0,0))
            print "desactivado"
            flagBoton = 0
        pygame.time.delay(100)

#activo boton relleno
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrante(pygame.mouse.get_pos())==7):
        if(flagBoton <= 1):
            relleno = 1
            Panel_Botones.blit(presion8,(0,350))
            pantalla.blit(Panel_Botones,(0,0))
            flagBoton = flagBoton + 1
            print "activado"
        if (flagBoton > 1):
            relleno = 0
            Panel_Botones.blit(figura8,(0,350))
            pantalla.blit(Panel_Botones,(0,0))
            print "desactivado"
            flagBoton = 0
        pygame.time.delay(100)


#activo boton color
    if ((1,0,0)==pygame.mouse.get_pressed() and cuadrantecolor(pygame.mouse.get_pos())<=5):
        if (cuadrantecolor(pygame.mouse.get_pos())==0):
            color = (255,100,100)
            print "0"
        if(cuadrantecolor(pygame.mouse.get_pos())==1):
            color = (100,100,255)
            print "1"
        if(cuadrantecolor(pygame.mouse.get_pos())==2):
            color = (0,0,0)
            print "2"
        if(cuadrantecolor(pygame.mouse.get_pos())==3):
            color = (100,255,100)
            print "3"
        if(cuadrantecolor(pygame.mouse.get_pos())==4):
            color = (255,255,100)
            print "4"
        if(cuadrantecolor(pygame.mouse.get_pos())==5):
            color = (255,255,255)
            print "5"
        panelcolor()


 

            
#---------------------------------------------------------------
#dibujar punto
    if((1,0,0)==pygame.mouse.get_pressed() and listaBotones[0]!=False and cuadrante(pygame.mouse.get_pos())==8):
        Pos_Area = pygame.mouse.get_pos()
        Area_Dibujo.set_at((Pos_Area[0] - 200, Pos_Area[1]), color)
        pantalla.blit(Area_Dibujo, [200,0])
        pygame.display.flip()
#dibujar linea
    if((1,0,0)==pygame.mouse.get_pressed() and listaBotones[1]!=False and cuadrante(pygame.mouse.get_pos())==8):
        Pos_Area = pygame.mouse.get_pos()
        lista_click.append(Pos_Area)
        pygame.time.delay(100)
        if(len(lista_click) == 2):
            x1 = lista_click[0][0] - 200
            y1 = lista_click[0][1]
            x2 = lista_click[1][0] - 200
            y2 = lista_click[1][1]
            if(tipoLinea==0):
                libreriaGraficaPaint.Bresenham(Area_Dibujo, (x1, y1), (x2, y2), color)
                print "bressenham"
            if(tipoLinea==1):
                libreriaGraficaPaint.lineaPuntomedio(Area_Dibujo,x1,y1,x2,y2,color)
                print "punto medio"
            if(tipoLinea==2):
                libreriaGraficaPaint.lineaDDA(Area_Dibujo,x1,y1,x2,y2,color)
                print "dda"
            pantalla.blit(Area_Dibujo, [200,0])
            pygame.display.flip()
            lista_click = []
        
#dibujar poligono
    if((1,0,0)==pygame.mouse.get_pressed() and listaBotones[2]!=False and cuadrante(pygame.mouse.get_pos())==8):
        Pos_Area = pygame.mouse.get_pos()
        lista_click.append(Pos_Area)
        vectorX.append(Pos_Area[0]-200)
        vectorY.append(Pos_Area[1])
        pygame.time.delay(100)
        if(tipoPoligono == 0):
            if(len(lista_click) == 2):
                r = radio(lista_click[0],lista_click[1])
                centro = (lista_click[0][0]-200,lista_click[0][1])
                if(relleno == 0):
                    libreriaGraficaPaint.poligonoRegular(6,centro,r,Area_Dibujo,color)
                else:
                    libreriaGraficaPaint.poligonoRegularRelleno(6,centro,r,Area_Dibujo,color)
                pantalla.blit(Area_Dibujo, [200,0])
                pygame.display.flip()
                lista_click = []
        if(tipoPoligono == 1):
            if(len(lista_click) == 6):
                r = radio(lista_click[0],lista_click[1])
                centro = (lista_click[0][0]-200,lista_click[0][1])
                libreriaGraficaPaint.poligonoIrregular(Area_Dibujo, vectorX,vectorY,color)
                pantalla.blit(Area_Dibujo, [200,0])
                pygame.display.flip()
                vectorX = []
                vectorY = []
                lista_click = []

#dibujar circunferencias
    if((1,0,0)==pygame.mouse.get_pressed() and listaBotones[3]!=False and cuadrante(pygame.mouse.get_pos())==8):
        Pos_Area = pygame.mouse.get_pos()
        lista_click.append(Pos_Area)
        pygame.time.delay(150)
        if(tipoCirculo == 0):
            if(len(lista_click) == 2): # circulo
                r = radio(lista_click[0],lista_click[1])
                centro = (lista_click[0][0]-200,lista_click[0][1])
                if(relleno == 0):
                    libreriaGraficaPaint.CircleMidPoint(Area_Dibujo, centro[0], centro[1], r,color)
                else:
                    libreriaGraficaPaint.CircleMidPointRellenar(Area_Dibujo, centro[0], centro[1], r,color)
                pantalla.blit(Area_Dibujo, [200,0])
                pygame.display.flip()
                lista_click = []
        if(tipoCirculo == 1): # elipse
            if(len(lista_click) == 2):
                r1 = abs(lista_click[0][0]-lista_click[1][0])
                r2 = abs(lista_click[0][1]-lista_click[1][1])
                centro = (lista_click[0][0]-200,lista_click[0][1])
                if(relleno == 0):
                    libreriaGraficaPaint.EllipseMidPoint(Area_Dibujo, centro[0], centro[1], r1, r2,color)
                else:
                    libreriaGraficaPaint.EllipseMidPointRellenar(Area_Dibujo, centro[0], centro[1], r1, r2,color)
                pantalla.blit(Area_Dibujo, [200,0])
                pygame.display.flip()
                lista_click = []
#dibujar borrar
    if((1,0,0)==pygame.mouse.get_pressed() and listaBotones[6]!=False and cuadrante(pygame.mouse.get_pos())==8):
        Pos_Area = pygame.mouse.get_pos()
        pygame.draw.rect(Area_Dibujo, (255,255,255), [Pos_Area[0] -200, Pos_Area[1],20, 20])
        pygame.display.flip()
        pantalla.blit(Area_Dibujo, [200,0])
#dibujar recorte
    if((1,0,0)==pygame.mouse.get_pressed() and listaBotones[4]!=False and cuadrante(pygame.mouse.get_pos())==8):
        Pos_Area = pygame.mouse.get_pos()
        lista_click.append(Pos_Area)
        pygame.time.delay(160)
        if(len(lista_click) == 2):
            x1 = min(lista_click[0][0] - 200,lista_click[1][0] - 200) 
            x2 = max(lista_click[0][0] - 200,lista_click[1][0] - 200)
            y1 = min (lista_click[0][1],lista_click[1][1])
            y2 = max(lista_click[0][1],lista_click[1][1])
            alto = 600
            ancho = 500
            libreriaGraficaPaint.corte(Area_Dibujo,x1,x2,y1,y2,alto,ancho,(255,255,255))
            Area_Dibujo.blit(Area_Dibujo, (0,0))
            lista_click = []
            pantalla.blit(Area_Dibujo, [200,0])        
    pygame.display.flip()

#dibujar importar
    if((1,0,0)==pygame.mouse.get_pressed() and listaBotones[5]!=False and cuadrante(pygame.mouse.get_pos())==8):
        pygame.time.delay(150)
        Pos_Area = pygame.mouse.get_pos()
        punto = (Pos_Area[0]-200,Pos_Area[1])
        Area_Dibujo.blit(goku,punto)
        pantalla.blit(Area_Dibujo, [200,0])
        
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            salir = True
pygame.quit()
