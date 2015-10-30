import sys, pygame, time, math,figuras
import animacion
from pygame.locals import *
import py_compile
#Comando para crear ejecutables
py_compile.compile('graficador_final.py')
#--------------------------------------------------------------------------------------------------
#ANIMACION
animacion = animacion.finish
#animacion = True

#--------------------------------------------------------------------------------------------------
#PANEL GRAFICO

if animacion:
	pygame.init()
	tamano = ancho, alto = 1200, 650
	color = 255, 255, 255
	pantalla = pygame.display.set_mode(tamano)
	pygame.display.set_caption('GRAFICADOR')
	pantalla.fill(color) 

#--------------------------------------------------------------------------------------------------
#Botones Figuras
	letrero = pygame.image.load('../imagenes/color.png')
	linea = pygame.image.load('../imagenes/linea.png')
	circulo = pygame.image.load('../imagenes/circulo.png')
	elipse = pygame.image.load('../imagenes/elipse.png')
	parabola1 = pygame.image.load('../imagenes/parabola_abajo.png')
	parabola2 = pygame.image.load('../imagenes/parabola_arriba.png')
	parabola3 = pygame.image.load('../imagenes/parabola_izquierda.png')
	parabola4 = pygame.image.load('../imagenes/parabola_derecha.png')
	rectangulo = pygame.image.load('../imagenes/rectangulo.png')
	relleno = pygame.image.load('../imagenes/relleno.png')
	cortar = pygame.image.load('../imagenes/cortar.jpg')
	borrador = pygame.image.load('../imagenes/borrador.jpg')
	bres = pygame.image.load('../imagenes/br.jpg')
	dda = pygame.image.load('../imagenes/dda.png')
	logo = pygame.image.load('../imagenes/logo.png')
	bordo1 = pygame.image.load('../imagenes/bordo1.png')
	bordo2 = pygame.image.load('../imagenes/bordo2.png')

	botoneslineas = [bres,dda]
	botonesfiguras = [linea,circulo,elipse,parabola1,parabola2,parabola3,parabola4,rectangulo,cortar,borrador]

#--------------------------------------------------------------------------------------------------
#Botones presionados

	lineap = pygame.image.load('../imagenes/linea2.png')
	circulop = pygame.image.load('../imagenes/circulo2.png')
	elipsep = pygame.image.load('../imagenes/elipse2.png')
	parabola1p = pygame.image.load('../imagenes/parabola_abajo2.png')
	parabola2p = pygame.image.load('../imagenes/parabola_arriba2.png')
	parabola3p = pygame.image.load('../imagenes/parabola_izquierda2.png')
	parabola4p = pygame.image.load('../imagenes/parabola_derecha2.png')
	rectangulop = pygame.image.load('../imagenes/rectangulo2.png')
	rellenop = pygame.image.load('../imagenes/relleno2.png')
	cortarp = pygame.image.load('../imagenes/cortar2.jpg')
	borradorp = pygame.image.load('../imagenes/borrador2.jpg')
	bresp = pygame.image.load('../imagenes/br2.jpg')
	ddap = pygame.image.load('../imagenes/dda2.png')

	botoneslineaspress = [bresp,ddap]
	botonesfiguraspress = [lineap,circulop,elipsep,parabola1p,parabola2p,parabola3p,parabola4p,rectangulop,cortarp,borradorp]

	Panel_Botones = pygame.Surface((200, 650))
	Panel_Botones.fill((82,82,82))
	pantalla.blit(Panel_Botones,(0,0))
	
	Panel_Colores = pygame.Surface((1000,100))
	Panel_Colores.fill((82,82,82))
#--------------------------------------------------------------------------------------------------
	#Definimos colores
	
	GrisOscuro = (127,127,127)
	GrisState = (47,79,79)
	Negro = (0,0,0)
	Blanco = (255,255,255)
	Verde = (0,255,0)
	Azul = (0,0,255)
	Rojo = (255,0,0)
	Amarillo = (255,255,0)
	Naranja = (255,165,0)
	Rosado = (255,192,203)
	Salmon = (250,128,114)
	RojoOscuro = (139,0,0)
	Oro = (255,215,0)
	VerdeOscuro = (0,100,0)
	Oliva = (128,128,0)
	Agua = (0,255,255)
	AguaMarina = (127,255,212)
	Turquesa = (64,224,208)
	Violeta = (238,130,238)
	Fucsia = (255,0,255)
	VioletaOscuro = (148,0,211)
	Purpura = (128,0,128)
	Indigo = (75,0,130)
	AzulOscuro = (0,0,139)
	Teal = (0,128,128)
	Chocolate = (210,105,30)
	Siena = (160,82,45)
	Spring = (0,255,127)
	Steel = (176,196,222)
	RNaranja = (255,69,0)
	AVerde = (154,205,50)
	Crimson = (220,20,60)

	barracolores = [GrisOscuro,GrisState,Negro,Blanco,Verde,Azul,\
					Rojo,Amarillo,Naranja,Rosado,Salmon,RojoOscuro,\
					Oro,VerdeOscuro,Oliva,Agua,AguaMarina,Turquesa,\
					Violeta,Fucsia,VioletaOscuro,Purpura,Indigo,AzulOscuro,\
					Teal,Chocolate,Siena,Spring,Steel,RNaranja,AVerde,Crimson
				   ]

	ColorActual = barracolores[2]
	ColorFigura = barracolores[2]
	Area_Dibujo = pygame.Surface((1000, 550))
	Area_Dibujo.fill(barracolores[3])
	pygame.draw.rect(Panel_Colores,ColorActual,[110,0,90,80])

	tipolinea = 0 #0--> Bresenhan 1--> punto medio
	botonlinea = False
	botoncirculo = False
	botonelipse = False
	botoneparabola_abajo = False
	botoneparabola_arriba = False
	botoneparabola_izquierda = False
	botoneparabola_derecha = False
	botonrectangulo =False
	botoncortar = False
	botonborrar = False
	flagboton = 0
	rellenof = 0
	click = 0

	ListaClick = []
	ListaBotones = [botonlinea,botoncirculo,botonelipse,botoneparabola_abajo,botoneparabola_arriba,botoneparabola_izquierda,\
					botoneparabola_derecha,botonrectangulo,botoncortar,botonborrar
					]

	def radio(cord1,cord2):
	    x = abs(cord1[0] - cord2[0])
	    y = abs(cord1[1] - cord2[1])
	    d = 1.0 * math.sqrt((x * x)+(y * y))
	    return int(d)

	def CuadranteColores(evento):
		if (evento[0]>=400 and evento[0]<=450 and evento[1]>=0 and evento[1]<=50):
			return 0;
		if (evento[0]>=450 and evento[0]<=500 and evento[1]>=0 and evento[1]<=50):
			return 1;
		if (evento[0]>=500 and evento[0]<=550 and evento[1]>=0 and evento[1]<=50):
			return 2;
		if (evento[0]>=550 and evento[0]<=600 and evento[1]>=0 and evento[1]<=50):
			return 3;
		if (evento[0]>=600 and evento[0]<=650 and evento[1]>=0 and evento[1]<=50):
			return 4;
		if (evento[0]>=650 and evento[0]<=700 and evento[1]>=0 and evento[1]<=50):
			return 5;
		if (evento[0]>=700 and evento[0]<=750 and evento[1]>=0 and evento[1]<=50):
			return 6;
		if (evento[0]>=750 and evento[0]<=800 and evento[1]>=0 and evento[1]<=50):
			return 7;
		if (evento[0]>=800 and evento[0]<=850 and evento[1]>=0 and evento[1]<=50):
			return 8;
		if (evento[0]>=850 and evento[0]<=900 and evento[1]>=0 and evento[1]<=50):
			return 9;
		if (evento[0]>=900 and evento[0]<=950 and evento[1]>=0 and evento[1]<=50):
			return 10;
		if (evento[0]>=950 and evento[0]<=1000 and evento[1]>=0 and evento[1]<=50):
			return 11;
		if (evento[0]>=1000 and evento[0]<=1050 and evento[1]>=0 and evento[1]<=50):
			return 12;
		if (evento[0]>=1050 and evento[0]<=1100 and evento[1]>=0 and evento[1]<=50):
			return 13;
		if (evento[0]>=1100 and evento[0]<=1150 and evento[1]>=0 and evento[1]<=50):
			return 14;
		if (evento[0]>=1150 and evento[0]<=1200 and evento[1]>=0 and evento[1]<=50):
			return 15;
		if (evento[0]>=400 and evento[0]<=450 and evento[1]>=50 and evento[1]<=100):
			return 16;
		if (evento[0]>=450 and evento[0]<=500 and evento[1]>=50 and evento[1]<=100):
			return 17;
		if (evento[0]>=500 and evento[0]<=550 and evento[1]>=50 and evento[1]<=100):
			return 18;
		if (evento[0]>=550 and evento[0]<=600 and evento[1]>=50 and evento[1]<=100):
			return 19;
		if (evento[0]>=600 and evento[0]<=650 and evento[1]>=50 and evento[1]<=100):
			return 20;
		if (evento[0]>=650 and evento[0]<=700 and evento[1]>=50 and evento[1]<=100):
			return 21;
		if (evento[0]>=700 and evento[0]<=750 and evento[1]>=50 and evento[1]<=100):
			return 22;
		if (evento[0]>=750 and evento[0]<=800 and evento[1]>=50 and evento[1]<=100):
			return 23;
		if (evento[0]>=800 and evento[0]<=850 and evento[1]>=50 and evento[1]<=100):
			return 24;
		if (evento[0]>=850 and evento[0]<=900 and evento[1]>=50 and evento[1]<=100):
			return 25;
		if (evento[0]>=900 and evento[0]<=950 and evento[1]>=50 and evento[1]<=100):
			return 26;
		if (evento[0]>=950 and evento[0]<=1000 and evento[1]>=50 and evento[1]<=100):
			return 27;
		if (evento[0]>=1000 and evento[0]<=1050 and evento[1]>=50 and evento[1]<=100):
			return 28;
		if (evento[0]>=1050 and evento[0]<=1100 and evento[1]>=50 and evento[1]<=100):
			return 29;
		if (evento[0]>=1100 and evento[0]<=1150 and evento[1]>=50 and evento[1]<=100):
			return 30;
		if (evento[0]>=1150 and evento[0]<=1200 and evento[1]>=50 and evento[1]<=100):
			return 31;

	def CuadranteBotones(evento):
		if (evento[0]>=10 and evento[0]<=60 and evento[1]>=200 and evento[1]<=250):
			return 0;
		if (evento[0]>=60 and evento[0]<=130 and evento[1]>=260 and evento[1]<=330):
			return 1;
		if (evento[0]>=50 and evento[0]<=140 and evento[1]>=340 and evento[1]<=390):
			return 2;
		if (evento[0]>=30 and evento[0]<=80 and evento[1]>=400 and evento[1]<=450):
			return 3;
		if (evento[0]>=120 and evento[0]<=170 and evento[1]>=400 and evento[1]<=450):
			return 4;
		if (evento[0]>=30 and evento[0]<=82 and evento[1]>=460 and evento[1]<=510):
			return 5;
		if (evento[0]>=120 and evento[0]<=170 and evento[1]>=460 and evento[1]<=510):
			return 6;
		if (evento[0]>=50 and evento[0]<=164 and evento[1]>=520 and evento[1]<=570):
			return 7;
		if (evento[0]>=30 and evento[0]<=87 and evento[1]>=590 and evento[1]<=642):
			return 8;
		if (evento[0]>=120 and evento[0]<=170 and evento[1]>=590 and evento[1]<=638):
			return 9;
		if (evento[0]>=230 and evento[0]<=280 and evento[1]>=20 and evento[1]<=70):
			return 10;
		if (evento[0]>=200 and evento[0]<=1200 and evento[1]>=100 and evento[1]<=650):
			return 11;
	
	def CuadranteBotones_Linea(evento):
		if(evento[0]>=70 and evento[0]<=120 and evento[1]>=200 and evento[1]<=250):
			return 0;
		if(evento[0]>=130 and evento[0]<=180 and evento[1]>=200 and evento[1]<=250):
			return 1;

	def PanelColores(pantalla):
		pygame.draw.rect(Panel_Colores,(82,82,82),[190,0,10,80])
		pygame.draw.rect(Panel_Colores,barracolores[0],[200,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[1],[250,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[2],[300,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[3],[350,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[4],[400,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[5],[450,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[6],[500,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[7],[550,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[8],[600,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[9],[650,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[10],[700,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[11],[750,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[12],[800,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[13],[850,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[14],[900,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[15],[950,0,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[16],[200,50,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[17],[250,50,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[18],[300,50,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[19],[350,50,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[20],[400,50,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[21],[450,50,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[22],[500,50,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[23],[550,50,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[24],[600,50,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[25],[650,50,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[26],[700,50,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[27],[750,50,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[28],[800,50,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[29],[850,50,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[30],[900,50,50,50])
		pygame.draw.rect(Panel_Colores,barracolores[31],[950,50,50,50])
		Panel_Colores.blit(bordo2,(0,0))
		pantalla.blit(Panel_Colores,(200,0))
		pantalla.blit(letrero,(310,85))
		pantalla.blit(borrador,(230,20))

	def PanelBotones(pantalla):
		pantalla.blit(logo,(0,0))
		#linea
		pantalla.blit(linea,(10,200))
		pantalla.blit(bres,(70,200))
		pantalla.blit(dda,(130,200))
		#circulo
		pantalla.blit(circulo,(60,260))
		#elipse
		pantalla.blit(elipse,(50,340))
		#parabolas
		pantalla.blit(parabola1,(30,400))
		pantalla.blit(parabola2,(120,400))
		pantalla.blit(parabola3,(30,460))
		pantalla.blit(parabola4,(120,460))
		#rectangulos
		pantalla.blit(rectangulo,(50,520))
		if rellenof == 0:
			pantalla.blit(relleno,(30,590))
		#cortar 
		pantalla.blit(cortar,(120,590))

	def SeleccionActualRelleno(pos):
		if pos == 0:
			posimag = (10,200)
		if pos == 1:
			posimag = (60,260)
		if pos == 2:
			posimag = (50,340)
		if pos == 3:
			posimag = (30,400)
		if pos == 4:
			posimag = (120,400)
		if pos == 5:
			posimag = (30,460)
		if pos == 6:
			posimag = (120,460)
		if pos == 7:
			posimag = (50,520)
		if pos == 8:
			posimag = (30,590)
			Panel_Botones.blit(rellenop,posimag)
		if pos == 9:
			posimag = (120,590)
			Panel_Botones.blit(cortarp,posimag)
		if pos == 10:
			posimag = (230,20)
			pantalla.blit(botonesfiguraspress[pos-1],posimag)
		if pos < 8:
			Panel_Botones.blit(botonesfiguraspress[pos],posimag)
		pantalla.blit(Panel_Botones,(0,0))
		pygame.display.flip()

	def SeleccionActual(pos):
		if pos == 0:
			posimag = (10,200)
		if pos == 1:
			posimag = (60,260)
		if pos == 2:
			posimag = (50,340)
		if pos == 3:
			posimag = (30,400)
		if pos == 4:
			posimag = (120,400)
		if pos == 5:
			posimag = (30,460)
		if pos == 6:
			posimag = (120,460)
		if pos == 7:
			posimag = (50,520)
		if pos == 8:
			posimag = (30,590)
			Panel_Botones.blit(relleno,posimag)
		if pos == 9:
			posimag = (120,590)
			Panel_Botones.blit(cortar,posimag)
		if pos == 10:
			posimag = (230,20)
			pantalla.blit(botonesfiguras[pos-1],posimag)
		if pos < 8:
			Panel_Botones.blit(botonesfiguras[pos],posimag)
		pantalla.blit(Panel_Botones,(0,0))
		pygame.display.flip()

	def SeleccionActual_Linea(pos):
		if pos == 0:
			posimag = (70,200)
		if pos == 1:
			posimag = (130,200)
		Panel_Botones.blit(botoneslineas[pos],posimag)
		pantalla.blit(Panel_Botones,(0,0))
		pygame.display.flip()

	def SeleccionActual_LineaRelleno(pos):
		if pos == 0:
			posimag = (70,200)
		if pos == 1:
			posimag = (130,200)
		Panel_Botones.blit(botoneslineaspress[pos],posimag)
		pantalla.blit(Panel_Botones,(0,0))
		pygame.display.flip()

	def ColorActual(pos=2):
		ColorActual = barracolores[pos]
		pygame.draw.rect(Panel_Colores,ColorActual,[100,0,90,80])
		pygame.draw.rect(Panel_Colores,(82,82,82),[190,0,10,80])
		pantalla.blit(Panel_Colores,(200,0))
		pantalla.blit(letrero,(310,85))
		if ListaBotones[9]:
			pantalla.blit(borradorp,(230,20))
		else:
			pantalla.blit(borrador,(230,20))
		pygame.display.flip()
		return ColorActual
	
	#-------------------------------------------------------------------------------------
	#Recorte
	def Cortar(pantalla,color,ListaClick):
		ancho = 1000
		alto = 550
		posx = ListaClick[0][0]-200
		posx2 = ListaClick[1][0]-200
		posy = ListaClick[0][1]-100
		posy2 = ListaClick[1][1]-100
		pygame.draw.rect(pantalla,color,[0,0,ancho,posy])#arriba
		pygame.draw.rect(pantalla,color,[0,0,posx,alto])#izquierda
		pygame.draw.rect(pantalla,color,[0,posy2,ancho,(alto-posy2)])#abajo
		pygame.draw.rect(pantalla,color,[posx2,0,(ancho-posx2),alto])#derecha

	PanelBotones(Panel_Botones)
	PanelColores(pantalla)
	pantalla.blit(Panel_Botones,(0,0))
	Area_Dibujo.blit(bordo1,(0,0))
	pantalla.blit(Area_Dibujo,(200,100))
	pygame.display.flip()
	Salir = True
	Dibujar = True
	band = True

	while Salir:
		if pygame.mouse.get_pressed() == (0,1,0) and CuadranteBotones(pygame.mouse.get_pos()) == 11:
			Dibujar = False
			fuente = pygame.font.Font(None, 40)
			texto1 = fuente.render("Acabas de desactivar el area de dibujo,", 0, (192,192,192))
			texto2 = fuente.render("Esto quiere decir que deseas cerrar la aplicacion,", 0, (192,192,192))
			texto3 = fuente.render("Ya puedes dar click en cerrar, ", 0, (192,192,192))
			texto4 = fuente.render("Gracias por utilizar nuestra aplicacion :D", 0, (192,192,192))
			Area_Dibujo.blit(texto1,(200,200))
			Area_Dibujo.blit(texto2,(200,240))
			Area_Dibujo.blit(texto3,(200,280))
			Area_Dibujo.blit(texto4,(200,320))
			Area_Dibujo.blit(bordo1,(0,0))
			pantalla.blit(Area_Dibujo,[200,100])
			pygame.display.flip()
		if pygame.mouse.get_pressed() == (1,0,1) and CuadranteBotones(pygame.mouse.get_pos()) == 11:
			Dibujar = True
			Area_Dibujo.fill(ColorFigura) 
			Area_Dibujo.blit(bordo1,(0,0))
			pantalla.blit(Area_Dibujo,[200,100])
			pygame.display.flip()
		if not Dibujar:
			event = pygame.event.poll()
			if event.type == pygame.QUIT:
				Salir = False
		#--------------------------------------------------------------------------------------------------
	    #Seleccion de botones
		if Dibujar:
			pygame.event.wait()
			mouse = pygame.mouse.get_pressed()
			PanelBotones(Panel_Botones)
			#Activo boton linea
			if((1,0,0) == mouse and CuadranteBotones(pygame.mouse.get_pos()) == 0):
				for i in range(len(ListaBotones)):
					ListaBotones[i] =False
				if flagboton <= 1:
					ListaBotones[0] = True
					SeleccionActualRelleno(0)
					flagboton += 1
				if flagboton > 1:
					ListaBotones[0] = False
					SeleccionActual(0)
					pantalla.blit(Panel_Botones,(0,0))
					pantalla.blit(Panel_Colores,(200,0))
					pantalla.blit(letrero,(310,85))
					pygame.display.flip()
					SeleccionActual(10)
					flagboton = 0
			#Activo boton linea Bressenham
			if((1,0,0) == mouse and CuadranteBotones_Linea(pygame.mouse.get_pos()) == 0):
				for i in range(len(ListaBotones)):
					ListaBotones[i] = False
				if flagboton <= 1:
					ListaBotones[0] = True
					tipolinea = 0
					SeleccionActualRelleno(0)
					SeleccionActual_LineaRelleno(0)
					flagboton += 1
				if flagboton > 1:
					ListaBotones[0] = False
					SeleccionActual_Linea(0)
					pantalla.blit(Panel_Botones,(0,0))
					pantalla.blit(Panel_Colores,(200,0))
					pantalla.blit(letrero,(310,85))
					pygame.display.flip()
					SeleccionActual(10)
					flagboton = 0
			#Activo boton DDA
			if((1,0,0) == mouse and CuadranteBotones_Linea(pygame.mouse.get_pos()) == 1):
				for i in range(len(ListaBotones)):
					ListaBotones[i] = False
				if flagboton <= 1:
					ListaBotones[0] = True
					tipolinea = 1
					SeleccionActualRelleno(0)
					SeleccionActual_LineaRelleno(1)
					flagboton += 1
				if flagboton > 1:
					ListaBotones[0] = False
					SeleccionActual_Linea(1)
					pantalla.blit(Panel_Botones,(0,0))
					pantalla.blit(Panel_Colores,(200,0))
					pantalla.blit(letrero,(310,85))
					pygame.display.flip()
					SeleccionActual(10)
					flagboton = 0
			#Activo boton circunferencia
			if((1,0,0) == mouse and CuadranteBotones(pygame.mouse.get_pos()) == 1):
				for i in range(len(ListaBotones)):
					ListaBotones[i] = False
				if flagboton <= 1:
					ListaBotones[1] = True
					SeleccionActualRelleno(1)
					flagboton += 1
				if flagboton > 1:
					ListaBotones[1] = False
					SeleccionActual(1)
					pantalla.blit(Panel_Botones,(0,0))
					pantalla.blit(Panel_Colores,(200,0))
					pantalla.blit(letrero,(310,85))
					pygame.display.flip()
					SeleccionActual(10)
					flagboton = 0
			#Activo boton elipses
			if((1,0,0) == mouse and CuadranteBotones(pygame.mouse.get_pos()) == 2):
				for i in range(len(ListaBotones)):
					ListaBotones[i] = False
				if flagboton <= 1:
					ListaBotones[2] = True
					SeleccionActualRelleno(2)
					flagboton += 1
				if flagboton > 1:
					ListaBotones[1] = False
					SeleccionActual(2)
					pantalla.blit(Panel_Botones,(0,0))
					pantalla.blit(Panel_Colores,(200,0))
					pantalla.blit(letrero,(310,85))
					pygame.display.flip()
					SeleccionActual(10)
					flagboton = 0
			#Activo boton parabola hacia abajo
			if((1,0,0) == mouse and CuadranteBotones(pygame.mouse.get_pos()) == 3):
				for i in range(len(ListaBotones)):
					ListaBotones[i] = False
				if flagboton <= 1:
					ListaBotones[3] = True
					SeleccionActualRelleno(3)
					flagboton += 1
				if flagboton > 1:
					ListaBotones[3] = False
					SeleccionActual(3)
					pantalla.blit(Panel_Botones,(0,0))
					pantalla.blit(Panel_Colores,(200,0))
					pantalla.blit(letrero,(310,85))
					pygame.display.flip()
					SeleccionActual(10)
					flagboton = 0
			#Activo boton parabola hacia arriba
			if((1,0,0) == mouse and CuadranteBotones(pygame.mouse.get_pos()) == 4):
				for i in range(len(ListaBotones)):
					ListaBotones[i] = False
				if flagboton <= 1:
					ListaBotones[4] = True
					SeleccionActualRelleno(4)
					flagboton += 1
				if flagboton > 1:
					ListaBotones[4] = False
					SeleccionActual(4)
					pantalla.blit(Panel_Botones,(0,0))
					pantalla.blit(Panel_Colores,(200,0))
					pantalla.blit(letrero,(310,85))
					pygame.display.flip()
					SeleccionActual(10)
					flagboton = 0
			#Activo boton parabola hacia izquierda
			if((1,0,0) == mouse and CuadranteBotones(pygame.mouse.get_pos()) == 5):
				for i in range(len(ListaBotones)):
					ListaBotones[i] = False
				if flagboton <= 1:
					ListaBotones[5] = True
					SeleccionActualRelleno(5)
					flagboton += 1
				if flagboton > 1:
					ListaBotones[5] = False
					SeleccionActual(5)
					pantalla.blit(Panel_Botones,(0,0))
					pantalla.blit(Panel_Colores,(200,0))
					pantalla.blit(letrero,(310,85))
					pygame.display.flip()
					SeleccionActual(10)
					flagboton = 0
			#Activo boton parabola hacia derecha
			if((1,0,0) == mouse and CuadranteBotones(pygame.mouse.get_pos()) == 6):
				for i in range(len(ListaBotones)):
					ListaBotones[i] = False
				if flagboton <= 1:
					ListaBotones[6] = True
					SeleccionActualRelleno(6)
					flagboton += 1
				if flagboton > 1:
					ListaBotones[6] = False
					SeleccionActual(6)
					pantalla.blit(Panel_Botones,(0,0))
					pantalla.blit(Panel_Colores,(200,0))
					pantalla.blit(letrero,(310,85))
					pygame.display.flip()
					SeleccionActual(10)
					flagboton = 0
			#Activo boton rectangulo
			if((1,0,0) == mouse and CuadranteBotones(pygame.mouse.get_pos()) == 7):
				for i in range(len(ListaBotones)):
					ListaBotones[i] = False
				if flagboton <= 1:
					ListaBotones[7] = True
					SeleccionActualRelleno(7)
					flagboton += 1
				if flagboton > 1:
					ListaBotones[7] = False
					SeleccionActual(7)
					pantalla.blit(Panel_Botones,(0,0))
					pantalla.blit(Panel_Colores,(200,0))
					pantalla.blit(letrero,(310,85))
					pygame.display.flip()
					SeleccionActual(10)
					flagboton = 0
			#Activo boton relleno
			if((1,0,0) == mouse and CuadranteBotones(pygame.mouse.get_pos()) == 8):
				if flagboton <= 1:
					rellenof = 1
					SeleccionActualRelleno(8)
					flagboton += 1
				if flagboton > 1:
					rellenof = 0
					SeleccionActual(8)
					pantalla.blit(Panel_Botones,(0,0))
					pantalla.blit(Panel_Colores,(200,0))
					pantalla.blit(letrero,(310,85))
					pygame.display.flip()
					SeleccionActual(10)
					flagboton = 0
			#Activo boton cortar
			if((1,0,0) == mouse and CuadranteBotones(pygame.mouse.get_pos()) == 9):
				for i in range(len(ListaBotones)):
					ListaBotones[i] = False
				if flagboton <= 1:
					ListaBotones[8] = True
					SeleccionActualRelleno(9)
					flagboton += 1
				if flagboton > 1:
					ListaBotones[8] = False
					SeleccionActual(9)
					pantalla.blit(Panel_Botones,(0,0))
					pantalla.blit(Panel_Colores,(200,0))
					pantalla.blit(letrero,(310,85))
					pygame.display.flip()
					SeleccionActual(10)
					flagboton = 0
			#Activo boton borrar
			if((1,0,0) == mouse and CuadranteBotones(pygame.mouse.get_pos()) == 10):
				for i in range(len(ListaBotones)):
					ListaBotones[i] = False
				if flagboton <= 1:
					ListaBotones[9] = True
					SeleccionActualRelleno(10)
					flagboton += 1
				if flagboton > 1:
					ListaBotones[9] = False
					pantalla.blit(Panel_Botones,(0,0))
					pantalla.blit(Panel_Colores,(200,0))
					pantalla.blit(letrero,(310,85))
					pygame.display.flip()
					SeleccionActual(10)
					flagboton = 0
			#Activo boton color
			if((1,0,0) == mouse and CuadranteColores(pygame.mouse.get_pos()) <= 31):
				if CuadranteColores(pygame.mouse.get_pos()) == 0:
					ColorFigura = ColorActual(0)
				if CuadranteColores(pygame.mouse.get_pos()) == 1:
					ColorFigura = ColorActual(1)
				if CuadranteColores(pygame.mouse.get_pos()) == 2:
					ColorFigura = ColorActual(2)
				if CuadranteColores(pygame.mouse.get_pos()) == 3:
					ColorFigura = ColorActual(3)
				if CuadranteColores(pygame.mouse.get_pos()) == 4:
					ColorFigura = ColorActual(4)
				if CuadranteColores(pygame.mouse.get_pos()) == 5:
					ColorFigura = ColorActual(5)
				if CuadranteColores(pygame.mouse.get_pos()) == 6:
					ColorFigura = ColorActual(6)
				if CuadranteColores(pygame.mouse.get_pos()) == 7:
					ColorFigura = ColorActual(7)
				if CuadranteColores(pygame.mouse.get_pos()) == 8:
					ColorFigura = ColorActual(8)
				if CuadranteColores(pygame.mouse.get_pos()) == 9:
					ColorFigura = ColorActual(9)
				if CuadranteColores(pygame.mouse.get_pos()) == 10:
					ColorFigura = ColorActual(10)
				if CuadranteColores(pygame.mouse.get_pos()) == 11:
					ColorFigura = ColorActual(11)
				if CuadranteColores(pygame.mouse.get_pos()) == 12:
					ColorFigura = ColorActual(12)
				if CuadranteColores(pygame.mouse.get_pos()) == 13:
					ColorFigura = ColorActual(13)
				if CuadranteColores(pygame.mouse.get_pos()) == 14:
					ColorFigura = ColorActual(14)
				if CuadranteColores(pygame.mouse.get_pos()) == 15:
					ColorFigura = ColorActual(15)
				if CuadranteColores(pygame.mouse.get_pos()) == 16:
					ColorFigura = ColorActual(16)
				if CuadranteColores(pygame.mouse.get_pos()) == 17:
					ColorFigura = ColorActual(17)
				if CuadranteColores(pygame.mouse.get_pos()) == 18:
					ColorFigura = ColorActual(18)
				if CuadranteColores(pygame.mouse.get_pos()) == 19:
					ColorFigura = ColorActual(19)
				if CuadranteColores(pygame.mouse.get_pos()) == 20:
					ColorFigura = ColorActual(20)
				if CuadranteColores(pygame.mouse.get_pos()) == 21:
					ColorFigura = ColorActual(21)
				if CuadranteColores(pygame.mouse.get_pos()) == 22:
					ColorFigura = ColorActual(22)
				if CuadranteColores(pygame.mouse.get_pos()) == 23:
					ColorFigura = ColorActual(23)
				if CuadranteColores(pygame.mouse.get_pos()) == 24:
					ColorFigura = ColorActual(24)
				if CuadranteColores(pygame.mouse.get_pos()) == 25:
					ColorFigura = ColorActual(25)
				if CuadranteColores(pygame.mouse.get_pos()) == 26:
					ColorFigura = ColorActual(26)
				if CuadranteColores(pygame.mouse.get_pos()) == 27:
					ColorFigura = ColorActual(27)
				if CuadranteColores(pygame.mouse.get_pos()) == 28:
					ColorFigura = ColorActual(28)
				if CuadranteColores(pygame.mouse.get_pos()) == 29:
					ColorFigura = ColorActual(29)
				if CuadranteColores(pygame.mouse.get_pos()) == 30:
					ColorFigura = ColorActual(30)
				if CuadranteColores(pygame.mouse.get_pos()) == 31:
					ColorFigura = ColorActual(31)

	#--------------------------------------------------------------------------------------------------
		    #Dibujar figuras
		    #Dibujar linea
			if (1,0,0) == mouse and ListaBotones[0] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 0: 
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				click = 1
			
			if (0,0,1) == mouse and ListaBotones[0] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 1:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				if len(ListaClick) == 2:
					x1 = ListaClick[0][0] - 200
					y1 = ListaClick[0][1] - 100
					x2 = ListaClick[1][0] - 200
					y2 = ListaClick[1][1] - 100
					if tipolinea == 0:
						figuras.Linea_Bresenham(Area_Dibujo, x1, y1, x2, y2, ColorFigura)
					if tipolinea == 1:
						figuras.lineaDDA(Area_Dibujo,x1, y1, x2, y2,ColorFigura)
					Area_Dibujo.blit(bordo1,(0,0))
					pantalla.blit(Area_Dibujo,[200,100])
					pygame.display.flip()
					ListaClick = []
					click = 0

			#Dibujar circunferencia
			if (1,0,0) == mouse and ListaBotones[1] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 0:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				click = 1
			
			if (0,0,1) == mouse and ListaBotones[1] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 1:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				if len(ListaClick) == 2:
					r = radio(ListaClick[0],ListaClick[1])
					centrox = ListaClick[0][0] - 200
					centroy = ListaClick[0][1] - 100
					if rellenof == 0:
						figuras.CircleMidPoint(Area_Dibujo, centrox, centroy, r, ColorFigura)
					else:
						figuras.CirculoRelleno(Area_Dibujo, centrox, centroy, r,ColorFigura)
					Area_Dibujo.blit(bordo1,(0,0))
					pantalla.blit(Area_Dibujo,[200,100])
					pygame.display.flip()
					ListaClick = []
					click = 0

			#Dibujar elipses
			if (1,0,0) == mouse and ListaBotones[2] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 0:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				click = 1
				
			if (0,0,1) == mouse and ListaBotones[2] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 1:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				if len(ListaClick) == 2:
					centrox = ListaClick[0][0] - 200
					centroy = ListaClick[0][1] - 100
					ry = abs(ListaClick[0][1]-ListaClick[1][1])
					rx = abs(ListaClick[0][0]-ListaClick[1][0])
					if rellenof == 0:
						figuras. ElipseMidPoint(Area_Dibujo,centrox,centroy,rx,ry,ColorFigura)
					else:
						figuras.EllipseMidPointRellenar(Area_Dibujo,centrox,centroy,rx,ry,ColorFigura)
					Area_Dibujo.blit(bordo1,(0,0))
					pantalla.blit(Area_Dibujo,[200,100])
					pygame.display.flip()
					ListaClick = []
					click = 0

			#Dibujar parabola abajo
			if (1,0,0) == mouse and ListaBotones[3] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 0:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				click = 1
				
			if (0,0,1) == mouse and ListaBotones[3] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 1:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				if len(ListaClick) == 2:
					centro = [ListaClick[0][0]-200,ListaClick[0][1]-100]
					longitud = abs(ListaClick[0][1]-ListaClick[1][1])
					figuras.ParabolaMidPoint(Area_Dibujo, ColorFigura, "abajo",centro,longitud)
					Area_Dibujo.blit(bordo1,(0,0))
					pantalla.blit(Area_Dibujo,[200,100])
					pygame.display.flip()
					ListaClick = []
					click = 0

			#Dibujar parabola arriba
			if (1,0,0) == mouse and ListaBotones[4] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 0:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				click = 1

			if (0,0,1) == mouse and ListaBotones[4] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 1:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				if len(ListaClick) == 2:
					centro = [ListaClick[0][0]-200,ListaClick[0][1]-100]
					longitud = abs(ListaClick[0][1]-ListaClick[1][1])
					figuras.ParabolaMidPoint(Area_Dibujo, ColorFigura, "arriba",centro,longitud)
					Area_Dibujo.blit(bordo1,(0,0))
					pantalla.blit(Area_Dibujo,[200,100])
					pygame.display.flip()
					ListaClick = []
					click = 0

			#Dibujar parabola izquierda
			if (1,0,0) == mouse and ListaBotones[5] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 0:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				click = 1

			if (0,0,1) == mouse and ListaBotones[5] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 1:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				if len(ListaClick) == 2:
					centro = [ListaClick[0][0]-200,ListaClick[0][1]-100]
					longitud = abs(ListaClick[0][0]-ListaClick[1][0])
					figuras.ParabolaMidPoint(Area_Dibujo, ColorFigura, "izquierda",centro,longitud)
					Area_Dibujo.blit(bordo1,(0,0))
					pantalla.blit(Area_Dibujo,[200,100])
					pygame.display.flip()
					ListaClick = []
					click = 0

			#Dibujar parabola derecha
			if (1,0,0) == mouse and ListaBotones[6] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 0:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				click = 1
			
			if (0,0,1) == mouse and ListaBotones[6] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 1:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				if len(ListaClick) == 2:
					centro = [ListaClick[0][0]-200,ListaClick[0][1]-100]
					longitud = abs(ListaClick[0][0]-ListaClick[1][0])
					figuras.ParabolaMidPoint(Area_Dibujo, ColorFigura, "derecha",centro,longitud)
					Area_Dibujo.blit(bordo1,(0,0))
					pantalla.blit(Area_Dibujo,[200,100])
					pygame.display.flip()
					ListaClick = []
					click = 0

			#Dibujar rectangulo
			if (1,0,0) == mouse and ListaBotones[7] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 0:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				click = 1
			
			if (0,0,1) == mouse and ListaBotones[7] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 1:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				if len(ListaClick) == 2:
					x1 = ListaClick[0][0]-200
					y1 = ListaClick[0][1]-100
					x2 = ListaClick[1][0]-200
					y2 = ListaClick[1][1]-100
					if rellenof == 0:
						figuras.Rectangulo(Area_Dibujo,x1,y1,x2,y2,ColorFigura)
					else:
						figuras.RectanguloRelleno(Area_Dibujo,x1,y1,x2,y2,ColorFigura)
					Area_Dibujo.blit(bordo1,(0,0))
					pantalla.blit(Area_Dibujo,[200,100])
					pygame.display.flip()
					ListaClick = []
					click = 0

			#Hacer recorte
			if (1,0,0) == mouse and ListaBotones[8] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 0:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				click = 1
				
			if (0,0,1) == mouse and ListaBotones[8] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 1:
				Pos_Area = pygame.mouse.get_pos()
				ListaClick.append(Pos_Area)
				if len(ListaClick) == 2:
					Cortar(Area_Dibujo,barracolores[3],ListaClick)
					Area_Dibujo.blit(bordo1,(0,0))
					pantalla.blit(Area_Dibujo,[200,100])
					pygame.display.flip()
					ListaClick = []
					click = 0	

			#Borrar
			if (1,0,0) == mouse and ListaBotones[9] and CuadranteBotones(pygame.mouse.get_pos()) == 11 and click == 0:
				Pos_Area = pygame.mouse.get_pos()
				pygame.draw.rect(Area_Dibujo,ColorFigura,[Pos_Area[0]-200,Pos_Area[1]-100, 50,50])
				Area_Dibujo.blit(bordo1,(0,0))
				pantalla.blit(Area_Dibujo,[200,100])
				pygame.display.flip()
				click = 0

	pygame.quit()