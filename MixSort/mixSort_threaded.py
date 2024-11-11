import random
import matplotlib.pyplot as plt
import math
import threading


current_list = []
count_operations = 0  # Operaciones en counting sort
output_operations = 0  # Operaciones al agregar a la lista ordenada
bucket_operations = 0  # Operaciones al distribuir en los cubos
lock = threading.Lock()  # Lock para proteger las operaciones compartidas

cantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
#cantidades = [100, 200]
calculos_single = []
calculos_thread = []

def generar_lista(elementos = 100, maximo = 9999):
     ret = [random.randint(0, maximo) for _ in range(elementos)]
     return ret

#-------------------------------------------------------------------------
#***COUNTING SORT***
#-------------------------------------------------------------------------
def counting_sort(arr, max_value, result, index):
    global count_operations, output_operations
    local_count_operations = 0
    local_output_operations = 0
    # Inicializar el conteo de cada número en el rango [0, max_value]
    count = [0] * (max_value + 1)
    min_value = min(arr)
    local_count_operations += max_value - min_value
    
    # Contar cada elemento en la lista original
    for num in arr:
        count[num] += 1
        #local_count_operations += 1

    # Generar la lista ordenada usando los conteos
    sorted_arr = []
    for num, freq in enumerate(count):
        if freq > 0:
            sorted_arr.extend([num] * freq)     #[3,3,3,3,3,5,5,5,5,5] -> n
            local_output_operations += freq     #[0,0,5,0,5] -> n
    
    # Guardar el resultado en la posición correspondiente
    result[index] = sorted_arr

    # Actualizar los acumuladores globales de operaciones
    with lock:
        count_operations += local_count_operations
        output_operations += local_output_operations
#-------------------------------------------------------------------------



#-------------------------------------------------------------------------
#***BUCKET SORT***
#-------------------------------------------------------------------------
def bucket_sort(arr, bucket_count = 10):
    global bucket_operations
    local_bucket_operations = 0

    # Número de cubos (buckets)
    max_value = max(arr)
    bucket_size = (max_value + 1) // bucket_count

    # Crear cubos vacíos
    buckets = [[] for _ in range(bucket_count)]
    
    # Distribuir elementos en los cubos
    for num in arr:
        index = num // bucket_size
        if index != bucket_count:
            buckets[index].append(num)
        else:
            buckets[bucket_count - 1].append(num)
        local_bucket_operations += 1  # Una operación por cada asignación a un cubo
    
    # Actualizar las operaciones de distribución globalmente
    with lock:
        bucket_operations += local_bucket_operations

    # Lista para almacenar los resultados de cada cubo ordenado
    sorted_buckets = [None] * bucket_count
    
    # Lista para almacenar los threads
    threads = []

    # Ordenar cada cubo usando counting sort y unir los resultados
    for i, bucket in enumerate(buckets):
        if bucket:
            max_value_in_bucket = max(bucket)  # Calcular el valor máximo en cada cubo
            thread = threading.Thread(target=counting_sort, args=(bucket, max_value_in_bucket, sorted_buckets, i))
            threads.append(thread)
            thread.start()
    
    # Esperar a que todos los threads terminen
    for thread in threads:
        thread.join()
    
    # Combinar los resultados de todos los cubos ordenados
    sorted_arr = []
    for bucket in sorted_buckets:
        if bucket:
            sorted_arr.extend(bucket)
    
    return sorted_arr
#-------------------------------------------------------------------------

dummy = [50]
for i in cantidades:
    current_list = generar_lista(i)
    sorted_list = bucket_sort(current_list)

    calculos_single.append(count_operations + output_operations + bucket_operations)
    count_operations = 0  # Operaciones en counting sort
    output_operations = 0  # Operaciones al agregar a la lista ordenada
    bucket_operations = 0  # Operaciones al distribuir en los cubos

"""
f = open("mixSort.txt", "w")
f.write("cantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]\n" + 
    "calculos_single = " + str(calculos_single)) + "\n" +
    "calculos_thread = " + str(calculos_thread))
f.close()
"""

f = open("MixSort/mixSort_thread.txt", "w")
f.write("cantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]\n" + 
    "calculos_single = " + str(calculos_single))
f.close()


yi = []

for i in cantidades:
    current = i+(i+10000) 
    yi.append(current)

# Configuración del ancho de las barras y posición
ancho_barra = 35  # Ancho de cada barra
#rango_cantidades = np.arange(len(cantidades))  # Posiciones para cada grupo de edad
#print(rango_cantidades)

xi_sin_concurrencia = []
xi_con_concurrencia = []
for i in cantidades:
    xi_sin_concurrencia.append(i - ancho_barra/2)
    xi_con_concurrencia.append(i + ancho_barra/2)

# Crear el gráfico de barras   (n*log(n))
plt.bar(cantidades, calculos_single, width=ancho_barra, color='blue', label='calculos realizados')
#plt.bar(xi_con_concurrencia, calculos_con_concurrencia.mean(), width=ancho_barra, color='pink', label='Con concurrencia')
plt.plot(cantidades, yi, color = 'red', label = 'peor caso posible')


# Etiquetas y título
plt.title('sort combinado')
plt.xticks(cantidades)  # Configurar las etiquetas del eje x
plt.legend()  # Mostrar la leyenda
plt.ylim(0, 20000)
# Mostrar el gráfico
plt.xlabel('Cantidad')
plt.ylabel('Calculos')
plt.show()