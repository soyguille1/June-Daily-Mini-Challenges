entrada = input("Ingrese los números separados por espacios: ")
numeros = [int(numero) for numero in entrada.split()]
numeros.sort()
print("Lista ordenada en orden ascendente:")
print(numeros)