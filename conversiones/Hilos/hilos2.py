import threading
import time

def saludo(nombre):
    print("Hola como estas, soy "+nombre)
    time.sleep(2)

# Creamos cuatro hilos, cada uno para saludar a una persona diferente
hilo1 = threading.Thread(target=saludo, args=('Juan',))
hilo2 = threading.Thread(target=saludo, args=('Pedro',))
hilo3 = threading.Thread(target=saludo, args=('Ana',))
hilo4 = threading.Thread(target=saludo, args=('Patricia',))

# Iniciamos los hilos para que comiencen su ejecución
hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()

# Esperamos a que cada hilo termine su ejecución antes de continuar
hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()

# Imprimimos un mensaje para indicar que todos los hilos han terminado de saludar
print('Todos terminaron de saludar')