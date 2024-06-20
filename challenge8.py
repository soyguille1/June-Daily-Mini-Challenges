import secrets
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud = int(input("Ingresa la longitud de la contraseña (entre 8 y 16): "))
if 8 <= longitud <= 16:
    nueva_contrasena = generar_contrasena(longitud)
    print(f"Contraseña generada: {nueva_contrasena}")
else:
    print("La longitud debe estar entre 8 y 16 caracteres.")
