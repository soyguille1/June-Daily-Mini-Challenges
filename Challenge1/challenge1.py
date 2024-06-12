user_word = input("Ingrese su palabra a invertir ")
def inversion (palabra):
    return palabra [::-1]

palabra_invertida = inversion(user_word)
print(f"La palabra invertida es: {palabra_invertida}")

