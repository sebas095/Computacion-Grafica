def leer():
    contador = 0
    archi1 = open('Archivo1Taller4.txt','r')
    archi2 = open('Archivo2Taller4.txt','r')
    
    palabra = archi1.readline()
    texto = archi2.readlines()
    for li in texto:
        aux = li.split(' ')
        for i in aux:
            if i == palabra:
                contador += 1            
    archi1.close
    archi2.close
    print contador
leer()
