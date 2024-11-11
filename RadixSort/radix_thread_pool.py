import random
import concurrent.futures
import time

#--------------------------------------------------------------
#FUNCIONES EXTRAS
#--------------------------------------------------------------

def get_digit(number, n):
    return number // 10**n % 10

def flatten(xss):
    return [x for xs in xss for x in xs]

def generar_lista(n):
    pregenerada = ""#str(input("Cargar lista pregenerada. "))
    if pregenerada == "s":
        lista = range(0, 200)
    else:
        cantidad = n#int(input("Ingresar cantidad de numeros. "))
        limiteMenor = 0#int(input("Ingresar el limite menor del conjunto. "))
        limiteMayor = 9999#int(input("Ingresar el limite mayor del conjunto. "))
        repetidos = "s"#str(input("Permitir repetidos. "))


        if repetidos == "s":
            lista = list()
            for _ in range(cantidad):
                lista.append(random.randint(limiteMenor, limiteMayor))
        else:
            lista = set()
            while len(lista) < cantidad:
                lista.add(random.randint(limiteMenor, limiteMayor))
    
    return list(lista)

#--------------------------------------------------------------
# RADIX SORT
#--------------------------------------------------------------

def colocar_en_colas_segmento(segmento, digito):
    global calculos
    # Crea colas para cada dígito del 0 al 9 en el segmento asignado
    colas_segmento = [[] for _ in range(10)]
    for number in segmento:
        calculos += 1
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

listaCalculos = []
listaTiempos = []
listaCantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

for c in listaCantidades:
# Generamos una lista de números aleatorios para probar
    lista = generar_lista(c)

    calculos = 0

    tiempoInicio = time.time()

    print("Lista sin ordenar:", lista)

    # Obtenemos el número máximo de dígitos entre los números
    digitos = len(str(max(lista)))

    # Ordenamos repetidamente por cada dígito
    for digito in range(digitos):
        lista = hacer_cola_segun_digito(lista, digito)

    tiempoFinal = time.time()

    tiempoTotal = tiempoFinal - tiempoInicio

    listaCalculos.append(calculos)
    listaTiempos.append(tiempoTotal)

    print(f"Lista ordenada final: {lista}")
    print(f"calculos = {calculos}, rango * cantidad")
    print(f"Tiempo transcurrido: {tiempoFinal - tiempoInicio} segundos")

print("cantidades: ", listaCantidades)
print("calculos: ", listaCalculos)
print("tiempos: ", listaTiempos)