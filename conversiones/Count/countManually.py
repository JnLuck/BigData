import threading
import time

# Función para contar del 1 al 10 con un retraso de un segundo entre cada número
def contar(nombre):
    for i in range(1, 11):
        print(f"{nombre}: {i}")
        time.sleep(1)

# Creamos seis hilos, cada uno para contar del 1 al 10
hilo1 = threading.Thread(target=contar, args=('Hilo 1',))
hilo2 = threading.Thread(target=contar, args=('Hilo 2',))
hilo3 = threading.Thread(target=contar, args=('Hilo 3',))
hilo4 = threading.Thread(target=contar, args=('Hilo 4',))
hilo5 = threading.Thread(target=contar, args=('Hilo 5',))
hilo6 = threading.Thread(target=contar, args=('Hilo 6',))

# Iniciamos los hilos para que comiencen su ejecución
hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()
hilo5.start()
hilo6.start()

# Esperamos a que cada hilo termine su ejecución antes de continuar
hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()
hilo5.join()
hilo6.join()

# Imprimimos un mensaje para indicar que todos los hilos han terminado de contar
print('Todos los hilos han terminado de contar')
