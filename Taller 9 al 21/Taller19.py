'''
Hacer un programa que permita, rellenar triangulos 
y rectangulos
'''
import pygame, sys,math

colorfondo = 255, 255, 255
tamano = ancho, alto = 900, 600
pantalla = pygame.display.set_mode(tamano)
pantalla.fill(colorfondo)

pygame.display.flip()


def Linea_Punto_Medio (pantalla, Xi, Yi, Xf, Yf, color):
    puntos = list()
    dx = (Xf - Xi)
    dy = (Yf - Yi)
    if dy < 0:
            dy = -dy
            stepy = -1
    else:
            stepy = 1
    if dx < 0:
            dx = -dx
            stepx = -1
    else:
            stepx = 1
    x = Xi
    y = Yi
    pantalla.set_at((x,y),color)
    puntos.append([x,y])
    if dx > dy:
            p = 2*dy - dx
            incE = 2*dy
            incNE = 2*(dy-dx)
            while x != Xf:
                    x = x + stepx
                    if p <= 0:
                            p = p + incE
                    else:
                            y = y + stepy
                            p = p + incNE
                    pantalla.set_at((x,y),color)
                    puntos.append([x,y])

    else:
            p = 2*dx - dy
            incE = 2*dx
            incNE = 2*(dx-dy)
            while  y != Yf:
                    y = y + stepy
                    if p < 0:
                            p = p + incE
                    else:
                            x = x + stepx
                            p = p + incNE
                    pantalla.set_at((x,y),color)
                    puntos.append([x,y])
    return puntos

def Linea_Grosor(pantalla, Xa,Ya,Xb,Yb,color,grosor):
    for i in range(grosor):
        x = Linea_Punto_Medio(pantalla,Xa,Ya,Xb,Yb,color)
        Ya -=1
        Yb -=1
    return x

def rectangulo(pantalla,x,y,largo,ancho,color):
    x1 = x
    y1 = y
    x2 = x1+largo
    y2 = y1
    x3 = x
    y3 = y1+ancho
    x4 = x+largo
    y4 = y + ancho
    Linea_Grosor (pantalla, x1, y1, x2, y2, color,2)
    Linea_Grosor (pantalla, x1, y1, x3, y3, color,2)
    Linea_Grosor (pantalla, x3, y3, x4, y4, color,2)
    Linea_Grosor (pantalla, x2, y2, x4, y4, color,2)
    i = 0
    while i <= ancho:
        Linea_Grosor(pantalla, x1,y1+i,x2,y2+i,color,2)
        i+=1
            

def triangulo(pantalla,vertices,color):
    x=Linea_Grosor (pantalla, vertices[0][0], vertices[0][1], vertices[1][0], vertices[1][1],color,2)
    y=Linea_Grosor (pantalla, vertices[1][0], vertices[1][1], vertices[2][0], vertices[2][1],color,2)
    z=Linea_Grosor (pantalla, vertices[2][0], vertices[2][1], vertices[0][0], vertices[0][1],color,2)

    for i in range(len(x)):
        Linea_Grosor(pantalla, vertices[2][0], vertices[2][1],x[i][0],x[i][1],color,2)





def main():
    #Rectangulo:
    '''print "Ingrese coordenadas: "
    x = input()
    y = input()
    print "Ingrese largo: "
    largo = input()
    print "Ingrese ancho: "
    ancho = input()
    rectangulo(pantalla,x,y,largo,ancho,(0,0,0))
    pygame.display.flip()'''

    #Triangulo
    '''print "Ingrese las 3 coordenadas del triangulo:"
    print "coordenada 1:"
    x1 = input()
    y1 = input()
    print "coordenada 2:"
    x2 = input()
    y2 = input()
    print "coordenada 3:"
    x3 = input()
    y3 = input()'''

    vertices = [[500,200],[300,50],[100,200]]
    triangulo(pantalla,vertices,(218,165,032))
    rectangulo(pantalla,150,220,300,200,(222,184,135))  


    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    main()
