import sys, pygame
pygame.init()

tamano = ancho, alto = 640, 480
color = 0, 0, 0

pantalla = pygame.display.set_mode(tamano)
pantalla.fill(color)
#comienzo de dibujo del ahorcado.
# recta en y
for i in range(30):
    pantalla.set_at((80,i+100),(255,255,255) )
pygame.display.flip() 
#recta en y
for i in range(30):
    pantalla.set_at((160,i+100),(255,255,255) )
pygame.display.flip() 
#recta en x
for i in range(80):
    pantalla.set_at((80+i,100),(255,255,255) )
pygame.display.flip() 
#recta en x
for i in range(80):
    pantalla.set_at((80+i,130),(255,255,255) )
pygame.display.flip()
#recta en y
for i in range(80):
    pantalla.set_at((140,i+20),(255,255,255) )
pygame.display.flip()
#recta en x
for i in range(30):
    pantalla.set_at((140-i,20),(255,255,255) )
pygame.display.flip()
#recta en y
for i in range(30):
    pantalla.set_at((110,20+i),(255,255,255) )
pygame.display.flip()
#fin dibujo ahorcado

#comienzo dibujo de persona
# recta en y (cabeza)
for i in range(30):
    pantalla.set_at((360,i+20),(127,255,0) )
pygame.display.flip() 
#recta en y (cabeza)
for i in range(30):
    pantalla.set_at((280,i+20),(127,255,0) )
pygame.display.flip() 
#recta en x (cabeza)
for i in range(80):
    pantalla.set_at((280+i,20),(127,255,0) )
pygame.display.flip() 
#recta en x (cabeza)
for i in range(80):
    pantalla.set_at((280+i,50),(127,255,0) )
pygame.display.flip()
#recta en y ( cuello y cuerpo)
for i in range(60):
    pantalla.set_at((320,i+50),(127,255,0) )
pygame.display.flip()
#recta en x (brazos)
for i in range(80):
    pantalla.set_at((280+i,70),(127,255,0) )
pygame.display.flip() 
#recta en x (pies)
for i in range(80):
    pantalla.set_at((280+i,110),(127,255,0) )
pygame.display.flip() 
#fin dibujo Persona

#comienzo dibujar Casa
# recta en y (piso)
for i in range(60):
    pantalla.set_at((130,i+300),(255,255,0) )
pygame.display.flip() 
#recta en y (piso)
for i in range(60):
    pantalla.set_at((50,i+300),(255,255,0) )
pygame.display.flip() 
#recta en x (piso)
for i in range(80):
    pantalla.set_at((50+i,300),(255,255,0) )
pygame.display.flip() 
#recta en x (piso)
for i in range(80):
    pantalla.set_at((50+i,360),(255,255,0) )
pygame.display.flip()
# recta en y (Puerta)
for i in range(20):
    pantalla.set_at((100,i+340),(255,255,0) )
pygame.display.flip() 
#recta en y (Puerta)
for i in range(20):
    pantalla.set_at((80,i+340),(255,255,0) )
pygame.display.flip() 
#recta en x (Puerta)
for i in range(20):
    pantalla.set_at((80+i,340),(255,255,0) )
pygame.display.flip()
#recta inclinada (techo)
for i in range(40):
    pantalla.set_at((90+i,260+i),(255,255,0) )
pygame.display.flip()
#recta inclinada invertida (techo)
for i in range(40):
    pantalla.set_at((90-i,260+i),(255,255,0) )
pygame.display.flip()
#fin dibujo Casa

#Comienzo Dibujo Familia
#comienzo Padre
# recta en y (cabeza padre)
for i in range(20):
    pantalla.set_at((420,i+360),(255,0,0) )
pygame.display.flip() 
#recta en y (cabeza padre)
for i in range(20):
    pantalla.set_at((380,i+360),(255,0,0) )
pygame.display.flip() 
#recta en x (cabeza padre)
for i in range(40):
    pantalla.set_at((380+i,360),(255,0,0) )
pygame.display.flip() 
#recta en x (cabeza padre)
for i in range(40):
    pantalla.set_at((380+i,380),(255,0,0) )
pygame.display.flip()
#recta en y ( cuello y cuerpo padre)
for i in range(60):
    pantalla.set_at((400,i+380),(255,0,0) )
pygame.display.flip()
#recta en x (brazo izq padre)
for i in range(30):
    pantalla.set_at((400-i,410-i),(255,0,0) )
pygame.display.flip() 
#recta en x (brazo der padre)
for i in range(30):
    pantalla.set_at((400+i,410-i),(255,0,0) )
pygame.display.flip() 
#recta en x (pies izquierdo padre)
for i in range(30):
    pantalla.set_at((400+i,440+i),(255,0,0) )
pygame.display.flip() 
#recta en x (pie derecho padre)
for i in range(30):
    pantalla.set_at((400-i,440+i),(255,0,0) )
pygame.display.flip() 
#fin Padre

#comienzo Hijo
# recta en y (cabeza Hijo)
for i in range(20):
    pantalla.set_at((490,i+420),(255,0,0) )
pygame.display.flip() 
#recta en y (cabeza Hijo)
for i in range(20):
    pantalla.set_at((510,i+420),(255,0,0) )
pygame.display.flip() 
#recta en x (cabeza Hijo)
for i in range(20):
    pantalla.set_at((490+i,420),(255,0,0) )
pygame.display.flip() 
#recta en x (cabeza Hijo)
for i in range(20):
    pantalla.set_at((490+i,440),(255,0,0) )
pygame.display.flip()
#recta en y ( cuello y cuerpo Hijo)
for i in range(30):
    pantalla.set_at((500,i+440),(255,0,0) )
pygame.display.flip()
#recta en x (brazo izq Hijo)
for i in range(10):
    pantalla.set_at((500-i,460-i),(255,0,0) )
pygame.display.flip() 
#recta en x (brazo der Hijo)
for i in range(10):
    pantalla.set_at((500+i,460-i),(255,0,0) )
pygame.display.flip() 
#recta en x (pies izquierdo Hijo)
for i in range(10):
    pantalla.set_at((500+i,470+i),(255,0,0) )
pygame.display.flip() 
#recta en x (pie derecho Hijo)
for i in range(10):
    pantalla.set_at((500-i,470+i),(127,0,0) )
pygame.display.flip() 
#fin Hijo

#comienzo madre
#comienzo Padre
# recta en y (cabeza madre)
for i in range(20):
    pantalla.set_at((600,i+360),(255,0,0) )
pygame.display.flip() 
#recta en y (cabeza madre)
for i in range(20):
    pantalla.set_at((560,i+360),(255,0,0) )
pygame.display.flip() 
#recta en x (cabeza madre)
for i in range(40):
    pantalla.set_at((560+i,360),(255,0,0) )
pygame.display.flip() 
#recta en x (cabeza madre)
for i in range(40):
    pantalla.set_at((560+i,380),(255,0,0) )
pygame.display.flip()
#recta en y ( cuello y cuerpo madre)
for i in range(40):
    pantalla.set_at((580,i+380),(255,0,0) )
pygame.display.flip()
#recta en x (brazo izq madre)
for i in range(30):
    pantalla.set_at((580-i,410-i),(255,0,0) )
pygame.display.flip() 
#recta en x (brazo der madre)
for i in range(30):
    pantalla.set_at((580+i,410-i),(255,0,0) )
pygame.display.flip() 
#recta en x (falda parte izquierda madre)
for i in range(30):
    pantalla.set_at((580+i,420+i),(255,0,0) )
pygame.display.flip() 
#recta en x (falda parte derecha madre)
for i in range(30):
    pantalla.set_at((580-i,420+i),(255,0,0) )
pygame.display.flip() 
#recta en x (parte baja de la falda madre)
for i in range(60):
    pantalla.set_at((550+i,450),(255,0,0) )
pygame.display.flip() 
#recta en y ( cuello y cuerpo madre)
for i in range(20):
    pantalla.set_at((570,i+450),(255,0,0) )
pygame.display.flip()
#recta en y ( cuello y cuerpo madre)
for i in range(20):
    pantalla.set_at((590,i+450),(255,0,0) )
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()


