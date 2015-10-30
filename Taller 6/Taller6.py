import sys, pygame, time

pygame.init()

tamano = ancho, alto = 650, 500

color = 255, 255, 255
pantalla = pygame.display.set_mode(tamano)
pantalla.fill(color) 

condor0 = pygame.image.load("condorito0.jpg")
rectcondor0 = condor0.get_rect()

condor1 = pygame.image.load("condorito01.jpg")
rectcondor1 = condor1.get_rect()

condor2 = pygame.image.load("condorito02.jpg")
rectcondor2 = condor2.get_rect()

condor3 = pygame.image.load("condorito03.jpg")
rectcondor3 = condor3.get_rect()

condor4 = pygame.image.load("condorito04.jpg")
rectcondor4 = condor4.get_rect()

condor5 = pygame.image.load("condorito05.jpg")
rectcondor5 = condor5.get_rect()

condor6 = pygame.image.load("condorito06.jpg")
rectcondor6 = condor6.get_rect()

escenas = [condor0,condor1,condor2,condor3,condor4,condor5,condor6]
marco = [rectcondor0,rectcondor1,rectcondor2,rectcondor3,rectcondor4,rectcondor5,rectcondor6]

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		for i in range(len(escenas)):
			time.sleep(3)
			pantalla.fill(color) 
			pantalla.blit(escenas[i], marco[i])
			pygame.display.flip()