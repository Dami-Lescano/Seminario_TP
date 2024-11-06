import random
import concurrent.futures

#--------------------------------------------------------------
#FUNCIONES EXTRAS
#--------------------------------------------------------------

def get_digit(number, n):
    return abs(number) // 10**n % 10

def flatten(xss):
    return [x for xs in xss for x in xs]


#--------------------------------------------------------------
# RADIX SORT
#--------------------------------------------------------------

def colocar_en_colas_segmento(segmento, digito):
    # Crea colas para cada dígito del 0 al 9 en el segmento asignado
    colas_segmento = [[] for _ in range(10)]
    for number in segmento:
        n = get_digit(number, digito)
        colas_segmento[n].append(number)
    return colas_segmento

def hacer_cola_segun_digito(lista, digito):
    # Dividimos la lista en segmentos para procesar en paralelo
    num_threads = 4  # Puedes ajustar este valor según la CPU
    tamaño_segmento = len(lista) // num_threads
    segmentos = [lista[i * tamaño_segmento: (i + 1) * tamaño_segmento] for i in range(num_threads)]

    # Usamos un pool de threads para procesar cada segmento en paralelo
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Procesamos cada segmento en paralelo
        colas_por_segmento = list(executor.map(lambda seg: colocar_en_colas_segmento(seg, digito), segmentos))
    
    # Combina las colas de cada segmento en colas finales para el dígito
    lista_de_colas = [[] for _ in range(10)]
    for colas_segmento in colas_por_segmento:
        for i in range(10):
            lista_de_colas[i].extend(colas_segmento[i])   
    
    print(f"Lista de colas para el dígito {digito + 1}: {lista_de_colas}")
    return flatten(lista_de_colas)

# Generamos una lista de números aleatorios para probar
lista = [random.randint(0, 9999) for _ in range(100)]

print("Lista sin ordenar:", lista)

# Obtenemos el número máximo de dígitos entre los números
digitos = len(str(max(lista)))

# Ordenamos repetidamente por cada dígito
for digito in range(digitos):
    lista = hacer_cola_segun_digito(lista, digito)

print("Lista ordenada:", lista)
