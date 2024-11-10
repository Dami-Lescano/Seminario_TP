import random
import matplotlib.pyplot as plt
import math

acumulador = 0
current_list = []

cantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
calculos_single = []
calculos_thread = []

def generar_lista(elementos = 100, maximo = 9999):
     ret = [random.randint(0, maximo) for _ in range(elementos)]
     return ret

#-------------------------------------------------------------------------
#***COUNTING SORT***
#-------------------------------------------------------------------------
def counting_sort(arr, max_value, min_value = 0):
    global acumulador
    # Inicializar el conteo de cada número en el rango [0, max_value]
    count = [0] * (max_value + 1)

    #count ---> [0, 0, 0, ...]
    
    # Contar cada elemento en la lista original
    for num in arr:
        count[num] += 1
        acumulador += 1
    
    # Generar la lista ordenada usando los conteos
    sorted_arr = []
    for num, freq in enumerate(count):
        sorted_arr.extend([num] * freq)
        #acumulador += max(freq, 1)
    
    return sorted_arr
#-------------------------------------------------------------------------



#-------------------------------------------------------------------------
#***BUCKET SORT***
#-------------------------------------------------------------------------
def bucket_sort(arr, bucket_count = 10):
    global acumulador
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
        acumulador += 1
    # Ordenar cada cubo y unir los resultados
    # Ordenar cada cubo usando counting sort y unir los resultados
    sorted_arr = []
    for bucket in buckets:
        if bucket:
            max_value_in_bucket = max(bucket)  # Calcular el valor máximo en cada cubo
            #min_value_in_bucket = min(bucket)
            sorted_bucket = counting_sort(bucket, max_value_in_bucket)
            sorted_arr.extend(sorted_bucket)
    
    return sorted_arr
#-------------------------------------------------------------------------

dummy = [50]
for i in cantidades:
    current_list = generar_lista(i)
    sorted_list = bucket_sort(current_list)
    calculos_single.append(acumulador)
    print("data: " + str(current_list))
    print("sorted: " + str(sorted_list))
    acumulador = 0

"""
f = open("mixSort.txt", "w")
f.write("cantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]\n" + 
    "calculos_single = " + str(calculos_single)) + "\n" +
    "calculos_thread = " + str(calculos_thread))
f.close()
"""

f = open("MixSort/mixSort.txt", "w")
f.write("cantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]\n" + 
    "calculos_single = " + str(calculos_single))
f.close()


yi = []

for i in cantidades:
    current = i*math.log(i, 10)
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
plt.bar(xi_sin_concurrencia, calculos_single, width=ancho_barra, color='blue', label='Sin concurrencia')
#plt.bar(xi_con_concurrencia, calculos_con_concurrencia.mean(), width=ancho_barra, color='pink', label='Con concurrencia')
plt.plot(cantidades, yi, color = 'red')


# Etiquetas y título
plt.xlabel('Cantidad')
plt.ylabel('Calculos')
plt.title('Quick Sort')
plt.xticks(cantidades)  # Configurar las etiquetas del eje x
plt.legend()  # Mostrar la leyenda

# Mostrar el gráfico
plt.xlabel('Cantidad')
plt.ylabel('Calculos')
plt.show()