import pygame, sys, math

pygame.init()

pantalla = pygame.display.set_mode((500,500))


def imagen(pendiente,Xf,Xi,Yi):
   return pendiente*(Xf - Xi) + Yi

def Linea_Bresenham(surface, Xi, Yi, Xf, Yf, color):

   dX = (Xf - Xi)
   dY = (Yf - Yi)
   
   if (abs(dY) > abs(dX)):
      Xi, Xi = Yi, Xi
      Xf, Yf = Yf, Xf

   if (Xi > Xf):
      Xi, Xf = Xf, Xi
      Yi, Yf = Yf, Yi

   if (Yi < Yf):
      pasoY = 1

   else:
      pasoY = -1

   error = -dX / 2
   Y = Yi

   for X in range(Xi,Xf + 1):
      if (abs(dY) > abs(dX)):
         surface.set_at((Y, X), color)

      else:
         surface.set_at((X, Y), color)

      error = error + dY

      if (error > 0):
         Y = Y + pasoY
         error = error - dX



#llamado a la funcion
Linea_Bresenham(pantalla, 0, 10, 400, 100, (255, 50, 50))


pygame.display.flip() 

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()
