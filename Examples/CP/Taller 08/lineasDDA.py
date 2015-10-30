import pygame, sys, math

pygame.init()

pantalla = pygame.display.set_mode((500,500))


def imagen(pendiente,Xf,Xi,Yi):
   return pendiente*(Xf - Xi) + Yi

def Linea_DDA(surface, Xi, Yi, Xf, Yf, color):
   
   dX = Xf- Xi
   dY = Yf - Yi

   numeroPasos = abs(dY)

   if abs(dX) > abs(dY):
      numeroPasos = abs(dX)

   incrementoX = incrementoY = 0

   if numeroPasos <> 0:
      incrementoX = 1.0*dX/numeroPasos
      incrementoY = 1.0*dY/numeroPasos

   X, Y = Xi, Yi

   pantalla.set_at((int(X), int(Y)), (26,255,89))

   for k in range (numeroPasos):
      X = X + incrementoX
      Y = Y + incrementoY
      pantalla.set_at((int(X), int(Y)), (26,255,89))


#llamado a la funcion


Linea_DDA(pantalla, 0, 100, 480, 54, (50,255,50))

pygame.display.flip() 

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()

