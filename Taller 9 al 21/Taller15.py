'''Taller 15 Implementar el algoritmo del punto medio
para dibujar parabolas, para que dibuje todo tipo de
parabolas
'''

import pygame, sys

colorfondo = 255, 255, 255
tamano = ancho, alto = 1100, 600
pantalla = pygame.display.set_mode(tamano)
pantalla.fill(colorfondo)

pygame.display.flip() 

def PlotPoint(pantalla,x,y,color):
    pantalla.set_at((x,y),color)
    pantalla.set_at((x,-y),color)

def ParabolaMidPoint(pantalla, color, direccion):
    h = 500
    k = 200
    x = 0
    y = 0
    p = 1

    if direccion == "derecha":
        h = 100
        PlotPoint(pantalla,x+h,y+k,color)
        PlotPoint(pantalla,x+h,y-k,color)
        while x <= 600:
            x = x+1
            if p>0:
                y = y+1
                p = p - 2*y +1
            else:
                p = p+1
                PlotPoint(pantalla,x+h,y+k,color)
                PlotPoint(pantalla,x+h,y-k,color)
                
    if direccion == "izquierda":
        x = 600
        h = 400
        PlotPoint(pantalla,x+h,y+k,color)
        PlotPoint(pantalla,x+h,y-k,color)
        while x > 0:
            x = x-1
            if p>0:
                y = y+1
                p = p - 2*y +1
            else:
                p = p+1
                PlotPoint(pantalla,x+h,y+k,color)
                PlotPoint(pantalla,x+h,y-k,color)
                
    if direccion == "arriba":
            y = 500
            k = 50
            PlotPoint(pantalla,-x+h,-y-k,color)
            PlotPoint(pantalla,x+h,-y-k,color)
            while y > 0:
                y = y-1
                if p>0:
                    x = x+1
                    p = p - 2*x +1
                else:
                    p = p+1
                    PlotPoint(pantalla,-x+h,-y-k,color)
                    PlotPoint(pantalla,x+h,-y-k,color)
           

    if direccion == "abajo":
            k = 50 
            PlotPoint(pantalla,-x+h,-y-k,color)
            PlotPoint(pantalla,x+h,-y-k,color)
            while y <= 500:
                y = y+1
                if p>0:
                    x = x+1
                    p = p - 2*x +1
                else:
                    p = p+1
                    PlotPoint(pantalla,-x+h,-y-k,color)
                    PlotPoint(pantalla,x+h,-y-k,color)
                
        
def main():
    print "Ingrese direccion de la parabola: "
    direccion = raw_input()
    ParabolaMidPoint(pantalla,(0,0,0),direccion)
    pygame.display.flip() 

    while True:
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
             sys.exit()

if __name__ == "__main__":
    main()