
def Fibonacci(n):
    a,b=0,1
    print a
    print b
    while a<n:
        Primos(a)
        a,b=b,a+b
    print "fin"

def Primos(a):
    contador=0
    for i in range(1,a+1):
        if(a%i)==0:
           contador=contador+1
    if contador==2:
        print a
