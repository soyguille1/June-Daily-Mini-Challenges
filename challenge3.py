contar = input("Ingrese la palabra con vocales a contar: ").lower()
vocales = ["a", "e", "i", "o", "u"]
conteo = {letra: contar.count(letra) for letra in vocales}

for vocal, cantidad in conteo.items():
    print(f"La vocal '{vocal}' aparece {cantidad} veces.")
