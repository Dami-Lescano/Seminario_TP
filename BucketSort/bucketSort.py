import random

acumulador = 0
current_list = []

cantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
calculos_single = []


def generar_lista(elementos = 100, maximo = 9999):
     ret = [random.randint(0, maximo) for _ in range(elementos)]
     return ret

def bucket_sort(arr, bucket_count = 10):
    # Número de cubos (buckets)
    max_value = max(arr)
    bucket_size = (max_value + 1) // bucket_count
    
    #bucket ---> {[0, 500],[500, 1000]...]

    # Crear cubos vacíos
    buckets = [[] for _ in range(bucket_count)]
    
    # Distribuir elementos en los cubos
    for num in arr:
        index = num // bucket_size
        if index != bucket_count:
            buckets[index].append(num)
        else:
            buckets[bucket_count - 1].append(num)
    
    # Ordenar cada cubo y unir los resultados
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr

for i in cantidades:
    current_list = generar_lista(i)
    bucket_sort(current_list)
    calculos_single.append(acumulador)
    acumulador = 0

"""
f = open("bucketSort.txt", "w")
f.write("cantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]\n" + 
    "calculos_single = " + str(calculos_single))
f.close()
"""

data = generar_lista()
sorted_data = bucket_sort()

print("Lista original:", data)
print("Lista ordenada:", sorted_data)