# Suma de los numeros multiplos de 3 y 5 menores a 1000

suma = 0
for i in range(2, 1000):
    if i%3 == 0 or i%5 ==0:
        suma+=i

print("La suma de numeros a mil miltiplos de 3 y 5 es ", suma)