#implementar el algoritmo DDA, leyendo los puntos iniciales de teclado, permitiendo
#dibujar las lineas para dy=0 y/o dx=0 y permitiendo manejar el grosor de la linea

import pygame, sys


print "Digite el punto inicial:"
xa, ya = input(), input()
print "Digite el punto final:"
xb, yb = input(), input()
print "Digite Grosor:"
grosor = input()

colorfondo = 255, 255, 255
tamano = ancho, alto = 500, 500
pantalla = pygame.display.set_mode(tamano)
pantalla.fill(colorfondo)

uncolor = 0, 0, 0
dx= xb-xa
dy= yb-ya
numeropasos = abs(dy)
if abs(dx) > abs(dy):
    numeropasos = abs(dx)

incrementox = incrementoy = 0
if numeropasos <> 0:   # no dividirás por cero
    incrementox = 1.0*dx/numeropasos
    incrementoy = 1.0*dy/numeropasos
    
 # 1.0 garantiza división flotante
    

x,y = xa, ya # punto inicial

for k in range (grosor):
    pantalla.set_at((int(x), int(y)), uncolor)
    for k in range(numeropasos):
        x = x + incrementox
        y = y + incrementoy
        pantalla.set_at((int(x),int(y)), uncolor)
    x,y = xa+1, ya
    

pygame.display.flip() 

corre = 1
while corre:
    evento = pygame.event.poll()
    if evento.type == pygame.KEYDOWN:
        corre = 0
