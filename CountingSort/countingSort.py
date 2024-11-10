import random

# Generar lista de 100 números aleatorios menores a 1000
data = [random.randint(0, 999) for _ in range(100)]

# Función para el counting sort
def counting_sort(arr, max_value):
    # Inicializar el conteo de cada número en el rango [0, max_value]
    count = [0] * (max_value + 1)
    
    # Contar cada elemento en la lista original
    for num in arr:
        count[num] += 1
    
    # Generar la lista ordenada usando los conteos
    sorted_arr = []
    for num, freq in enumerate(count):
        sorted_arr.extend([num] * freq)
    
    return sorted_arr

# Usar counting sort para ordenar la lista generada
sorted_data = counting_sort(data, 999)

"""
f = open("countingSort.txt", "w")
f.write("cantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]\n" + 
    "calculos_single = " + str(calculos_single))
f.close()
"""

print("Lista original:", data)
print("Lista ordenada:", sorted_data)
