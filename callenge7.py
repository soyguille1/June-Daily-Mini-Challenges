import random

piedra = ["piedra"]
papel = ["papel"]
tijera = ["tijera"]

print("Juguemos a Piedra, Papel o Tijera")
jugador = input("Elige piedra, papel o tijera: ").lower()
pepito = random.choice(piedra + papel + tijera)
if jugador == pepito:
    print(f"Empate. Ambos eligieron {pepito}")
elif (jugador == "piedra" and pepito == "tijera") or (jugador == "papel" and pepito == "piedra") or (jugador == "tijera" and pepito == "papel"):
    print(f"¡Ganaste! La computadora eligió {pepito}")
else:
    print(f"Perdiste. La computadora eligió {pepito}")
