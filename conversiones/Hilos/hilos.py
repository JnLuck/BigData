import threading
import time

def saludo(nombre):
    print("Hola como estas, soy "+nombre)
    time.sleep(2)

# Ejecutamos "saludo" de forma secuencial

saludo("Juan")
saludo("Pedro")
saludo("Ana")
saludo("Patricia")

print('Todos termianron de saludar')