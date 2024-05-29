from ejemploLineal import busqueda_lineal
# Prueba con diferentes conjuntos de datos
lista = [10, 20, 30, 40, 50]
print(busqueda_lineal(lista, 30))  # Debería retornar 2
print(busqueda_lineal(lista, 60))  # Debería retornar -1

lista_vacia = []
print(busqueda_lineal(lista_vacia, 10))  # Debería retornar -1
