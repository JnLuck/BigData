import threading
import time

# Función para contar del 1 al 100 con un retraso de 1 segundo entre cada número
def contar_numeros(nombre):
    for i in range(1, 11):
        print(f"{nombre}: {i}")
        time.sleep(1)
    return nombre  # Devolvemos el nombre del hilo al finalizar el conteo

# Función para iniciar y ejecutar 5 hilos de conteo
def contar_en_paralelo():

    hilos = []  # Lista para almacenar los hilos
    
    # Creamos y comenzamos 5 hilos
    for i in range(1, 6):
        nombre_hilo = f"Hilo{i}"
        hilo = threading.Thread(target=contar_numeros, args=(nombre_hilo,))
        hilo.start()
        hilos.append(hilo)  # Agregamos el hilo a la lista

    # Esperamos a que todos los hilos terminen su ejecución
    for hilo in hilos:
        hilo.join()

    # Obtenemos los nombres de los hilos que terminaron primero
    ganador = None
    for hilo in hilos:
        if hilo.is_alive():
            ganador = hilo.name
            break

# Llamamos a la función para contar en paralelo
contar_en_paralelo()
