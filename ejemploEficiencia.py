import time
from ejemploBinario import busqueda_binaria
from ejemploLineal import busqueda_lineal

# Función para medir el tiempo de ejecución
def medir_tiempo(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    fin = time.time()
    return resultado, fin - inicio

# Generar una lista grande para la prueba
import random
lista_grande = random.sample(range(1000000), 100000)

# Pruebas de tiempo de ejecución
resultado, tiempo = medir_tiempo(busqueda_lineal, lista_grande, 999999)
print(f'Búsqueda Lineal tomó {tiempo:.6f} segundos y retornó el índice {resultado}.')

lista_grande_ordenada = sorted(lista_grande)
resultado, tiempo = medir_tiempo(busqueda_binaria, lista_grande_ordenada, 999999)
print(f'Búsqueda Binaria tomó {tiempo:.6f} segundos y retornó el índice {resultado}.')
