canibales = [-1,-1,-1]
monjes = [1,1,1]
barco = [0,0]
llegada = [0,0,0,0,0,0]
izquierda = False
derecha = False
estadoC = ""
estadoM = ""

def mostrar(list,nombre):
	estado = ""
	for i in range(len(list)):
		if list[i] != 0:
			estado +=nombre+str(i+1)+" "
	return estado

def checkIzq(can,monj):
	cont1 = 0
	cont2 = 0
	for i in range(len(can)):
		if can[i] == -1:
			cont1 +=1
	for j in range(len(monj)):
		if monj[j] == 1:
			cont2 += 1

	if cont2 >= cont1 or (cont1 > 0 and cont2 == 0):
		return True
	return False

def checkDer(lleg):
	cont1 = 0
	cont2 = 0
	for i in range(len(lleg)):
		if i <= 2:
			if lleg[i] == -1:
				cont1 += 1
		if i >= 3:
			if lleg[i] == 1:
				cont2 += 1

	if cont2 >= cont1 or (cont1 > 0 and cont2 == 0):
		return True
	return False

def transform(barc,ind,per):
	if per == "c1" or per == "C1":
		barc[ind] = int(per[1])
	if per == "c2" or per == "C2":
		barc[ind] = int(per[1])
	if per == "c3" or per == "C3":
		barc[ind] = int(per[1])
	if per == "m1" or per == "M1":
		barc[ind] = int(per[1])+3
	if per == "m2" or per == "M2":
		barc[ind] = int(per[1])+3
	if per == "m3" or per == "M3":
		barc[ind] = int(per[1])+3
	return
	
def go(canibales,monjes,barco,izquierda,derecha,llegada):
	b1 = 0
	index1 = -1
	index2 = -1
	b2 = 0
	if barco[0] <= 3 and barco[0] > 0:
		b1 = -1
		index1 = barco[0]-1
	if barco[0] >= 4:
		b1 = 1
		index1 = barco[0]-1
	if barco[1] <= 3 and barco[0] > 0:
		b2 = -1
		index2 = barco[1]-1
	if barco[1] >= 4:
		b2 = 1
		index2 = barco[1]-1

	if izquierda:
		if b1 == 1:
			monjes[index1-3] = 0
		if b1 == -1:
			canibales[index1] = 0
		if b2 == 1:
			monjes[index2-3] = 0
		if b2 == -1:
			canibales[index2] = 0

		if index1 > -1 :
			llegada[index1] = b1
			barco[0] = 0
			b1 = 0
			index1 = -1
		if index2 > -1 :
			llegada[index2] = b2
			barco[1] = 0
			b2 = 0
			index2 = -1

	if derecha:
		if index1 > -1 :
			llegada[index1] = 0
		if index2 > -1 :
			llegada[index2] = 0

		if b1 == -1 and index1 > -1:
			canibales[index1] = -1
			barco[0] = 0
			b1 = 0
			index1 = -1
		if b1 == 1 and index1 > -1:
			monjes[index1-3] = 1
			barco[0] = 0
			b1 = 0
			index1 = -1
		if b2 == -1 and index2 > -1:
			canibales[index2] = -1
			barco[1] = 0
			b2 = 0
			index2 = -1
		if b2 == 1 and index2 > -1:
			monjes[index2-3] = 1
			barco[1] = 0
			b2 = 0
			index2 = -1

	return


def mostrarActual(list, nombre):
	s = ""
	for i in range(len(list)):
		if list[i] != 0:
			s += nombre+str(i+1)+" "

	return s

def mostrarLlegada(list):
	msj = ""
	for i in range(len(list)):
		if list[i] != 0:
			if i <= 2:
				msj += "C"+str(i+1)+" "
			if i >= 3:
				msj += "M"+str(i-2)+" "
	return msj

print "\t\t\t\t**********************"
print "\t\t\t\t* CANIBALES Y MONJES *"
print "\t\t\t\t**********************\n\n"

print "IZQUIERDA:\n"
print "CANIBALES:"
estadoC = mostrar(canibales,"C")
print estadoC
print "\nMONJES:"
estadoM = mostrar(monjes,"M")
print estadoM,'\n'

per1 = ""
per2 = ""
derecha = False
izquierda = True

while True:
	print "\n"
	opc = int(raw_input("Cuantas Personas desea llevar (1/2): "))
	print "\n"
	if izquierda and not derecha:
		print "DE IZQUIERDA A DERECHA:\n"
	if derecha and not izquierda:
		print "DE DERECHA A IZQUIERDA:\n"
	if opc == 1:
		per1 = str(raw_input("Elija la persona que desea llevar: "))
		print "\n"
		transform(barco,0,per1)

	if opc == 2:
		per1 = str(raw_input("Elija la persona que desea llevar: "))
		print "\n"
		per2 = str(raw_input("Elija la persona que desea llevar: "))
		print "\n"
		transform(barco,0,per1)
		transform(barco,1,per2)

	go(canibales,monjes,barco,izquierda,derecha,llegada)
	
	cani = mostrarActual(canibales,"C")
	mon = mostrarActual(monjes,"M")
	lleg = mostrarLlegada(llegada)
	msj = cani+mon+"                        "+lleg

	print "IZQUIERDA:                        DERECHA:"
	print msj

	if canibales[0] == 0 and canibales[1] == 0 and canibales[2] == 0 and monjes[0] == 0 and monjes[1] == 0 and monjes[2] == 0:
		print "\n\n"
		print "\t\t\t\t**********************"
		print "\t\t\t\t*    YOU  WIN!! :D   *"
		print "\t\t\t\t**********************\n\n"
		PAUSE=raw_input("PAUSE")
		break

	if derecha:
		if checkDer(llegada) == False or checkIzq(canibales,monjes) == False:
			print "\n\n"
			print "\t\t\t\t**********************"
			print "\t\t\t\t*   GAME OVER!! :'(  *"
			print "\t\t\t\t**********************\n\n"
			PAUSE=raw_input("PAUSE")
			break
		derecha = False
		izquierda = True
		continue

	if izquierda:
		if checkDer(llegada) == False or checkIzq(canibales,monjes) == False:
			print "\n\n"
			print "\t\t\t\t**********************"
			print "\t\t\t\t*   GAME OVER!! :'(  *"
			print "\t\t\t\t**********************\n\n"
			PAUSE=raw_input("PAUSE")
			break
		derecha = True
		izquierda = False
		continue



















