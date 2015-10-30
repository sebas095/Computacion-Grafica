


def esVocal(palabra):
    for i in range(0, len(palabra)):
        if palabra[i]== 'a':
           return True 
        elif  palabra[i]== 'e':
           return True
        elif  palabra[i]== 'i':
           return True
        elif  palabra[i]== 'o':
           return True
        elif  palabra[i]== 'u':
           return True
       
    else: return False

    
f = open('texto.txt','r')
lista = f.readlines()
contador = 0

for i in range(0, len(lista[0])):
 if esVocal(lista[0][i]):
     contador = contador + 1


f.close()

print contador
