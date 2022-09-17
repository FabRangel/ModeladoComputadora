#realizar el programa para imprimir cada uno de los siguientes patrones
n=input('Ingresa n: ')
n=int(n)

#Triángulo decadente
for i in range(n,-1,-1):
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")
print("\n")


#Triángulo izquierdo
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")
print("\n")

#Triángulo derecho
k = 2*n - 2
for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
print("\n")

#Cuadrado
k=n
for i in range(0,n):
    for j in range(0,n):
        print("* ", end="")
    print("\r")
print("\n")

