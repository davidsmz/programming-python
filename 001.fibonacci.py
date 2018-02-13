# Serie de fibonacci 1, 2, 3, 5, 8, 13, .....
# Se pide encontrar la suma de los terminos pares

n = int( input("Ingrese un numero: ") )
a = 1
b = 1
c = 0
suma = 0
#print(a, end=' ')
while b < n:
    
    print(b, end=' ')
    c = a
    a = b
    b = a + c
    if b%2 == 0:
        suma += b
print()
print("La suma de terminos pares de fibonacci es", suma)
print()


















