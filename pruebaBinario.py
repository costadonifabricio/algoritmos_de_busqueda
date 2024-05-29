from ejemploBinario import busqueda_binaria

# Prueba con diferentes conjuntos de datos
lista_ordenada = [1, 3, 5, 7, 9, 11, 13]
print(busqueda_binaria(lista_ordenada, 7))  # Debería retornar 3
print(busqueda_binaria(lista_ordenada, 2))  # Debería retornar -1

lista_ordenada_vacia = []
print(busqueda_binaria(lista_ordenada_vacia, 5))  # Debería retornar -1
