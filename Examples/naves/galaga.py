import random
import pygame
from pygame.locals import *
import sys

NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)


class Bloque(pygame.sprite.Sprite):

	def __init__(self, color):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([20, 15])
		self.image.fill(color)
		self.rect = self.image.get_rect()

class Jugador(Bloque):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([20, 15])
		self.image.fill(ROJO)
		self.rect = self.image.get_rect()

	def update(self):
		pos = pygame.mouse.get_pos()
		self.rect.x = pos[0] #movimento del raton <-->

class Bala(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([4, 10])
		self.image.fill(NEGRO)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y -= 3

pygame.init()

p_ancho = 700
p_alto = 400

pantalla = pygame.display.set_mode((p_ancho, p_alto))
lista_todos = pygame.sprite.Group()
lista_bloques = pygame.sprite.Group()
lista_balas = pygame.sprite.Group()

for i in range(50):
	bloque = Bloque(NEGRO)

	bloque.rect.x = random.randrange(p_ancho)
	bloque.rect.y = random.randrange(350)

	lista_bloques.add(bloque)
	lista_todos.add(bloque)

j = Jugador()
lista_todos.add(j)

fin = False
reloj = pygame.time.Clock()
puntaje = 0
j.rect.y = 370

#Sonido
slaser = pygame.mixer.Sound("")

while not fin:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			fin = True

		elif event.type == pygame.MOUSEBUTTONDOWN:
			bala = Bala()
			bala.rect.x = j.rect.x
			bala.rect.y = j.rect.y
			lista_todos.add(bala)
			lista_balas.add(bala)

	lista_todos.update()

	for bala in lista_balas:
		lista_golpes = pygame.sprite.spritecollide(bala, lista_bloques, True)

		for bloque in lista_golpes:
			lista_balas.remove(bala)
			lista_todos.remove(bala)
			puntaje += 1
			print puntaje

			if bala.rect.y < -1:
				lista_balas.remove(bala)
				lista_todos.remove(bala)

	pantalla.fill(BLANCO)
	lista_todos.draw(pantalla)
	pygame.display.flip()

	reloj.tick(60)

pygame.quit()
