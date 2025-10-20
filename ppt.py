# ppt.py
import random

opciones = {"1": "Piedra", "2": "Papel", "3": "Tijera"}

def pedir_opcion():
    while True:
        v = input("Elige 1 (Piedra), 2 (Papel), 3 (Tijera): ").strip()
        if v in opciones:
            return v
        print("Entrada inválida. Ingresa 1, 2 o 3.")

def jugar():
    usuario = pedir_opcion()
    pc = random.choice(list(opciones.keys()))
    print("Tú:", opciones[usuario], "- PC:", opciones[pc])
    if usuario == pc:
        print("Empate.")
    elif (usuario == "1" and pc == "3") or (usuario == "2" and pc == "1") or (usuario == "3" and pc == "2"):
        print("¡Ganaste!")
    else:
        print("Perdiste.")

if __name__ == "__main__":
    while True:
        jugar()
        if input("Jugar otra vez? (s/n): ").lower() != "s":
            break
