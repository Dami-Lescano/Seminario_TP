import random
import time

def generar_lista(n):
    pregenerada = "s"#str(input("Cargar lista pregenerada. "))
    if pregenerada == "s":
        lista = range(0, 200)
    else:
        cantidad = n#int(input("Ingresar cantidad de numeros. "))
        limiteMenor = -cantidad#int(input("Ingresar el limite menor del conjunto. "))
        limiteMayor = cantidad#int(input("Ingresar el limite mayor del conjunto. "))
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



def quicksort(lista, pasoNumero, tipoPaso):
    global calculos
    listaMenores = []
    listaMayores = []
    pivote = 0
    listaOrdenada = []
    tamañoLista = len(lista)
    
    '''print(f"Paso {pasoNumero} {tipoPaso}")
    print(f"Lista: {lista}")'''
    if tamañoLista <= 1:
        return lista
    else:
        
        pivote = lista.pop(0)#random.randint(0, tamañoLista-1))
        for n in lista:
            calculos += 1
            numero = n
            if numero <= pivote:
                listaMenores.append(numero)
            else:
                listaMayores.append(numero)
        listaMenoresOrdenados = quicksort(listaMenores, pasoNumero+1, "Menores")
        listaMayoresOrdenados = quicksort(listaMayores, pasoNumero+1, "Mayores")
        listaOrdenada = listaMenoresOrdenados + [pivote] + listaMayoresOrdenados
        #print(f"Lista paso {pasoNumero}: {listaOrdenada}")
        return listaOrdenada

listaCalculos = []
listaTiempos = []
listaCantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

for n in listaCantidades:
    calculos = 0

    listaAOrdenar = generar_lista(n)

    print(f"Lista original: {listaAOrdenar}")

    tiempoInicio = time.time()

    listaOrdenada = quicksort(listaAOrdenar, 0, "inicial")

    tiempoFinal = time.time()

    listaCalculos.append(calculos)

    tiempoTotal = tiempoFinal - tiempoInicio

    listaTiempos.append(tiempoTotal)

    print(f"Lista ordenada final: {listaOrdenada}")
    print(f"calculos = {calculos}")
    print(f"Tiempo transcurrido: {tiempoTotal} segundos")

for n in range(10):
    print(f"Cantidad: {listaCantidades[n]}, Calculos: {listaCalculos[n]}, Tiempo {listaTiempos[n]}")

print("cantidades: ", listaCantidades)
print("calculos: ", listaCalculos)
print("tiempos: ", listaTiempos)

'''
cantidades:  [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
----------------------------------------------------------------
calculos:
[805, 1585, 2780, 3764, 4357, 5846, 7439, 9179, 9714, 10781]
[662, 1439, 2546, 3687, 5605, 6051, 6919, 8230, 10129, 10664]
[646, 1459, 2293, 4096, 4799, 6470, 7344, 8593, 9150, 11264]
[686, 1551, 2771, 3610, 5095, 5815, 7081, 8850, 9341, 10679]
[683, 1448, 3074, 3776, 5041, 6263, 6874, 8707, 9650, 11673]
[671, 1447, 2601, 3745, 4678, 5913, 7182, 8599, 11517, 11066]
[586, 1445, 2508, 3509, 4754, 6231, 6796, 8631, 10604, 11896]
[605, 1740, 2492, 3491, 4518, 5491, 7162, 9141, 9679, 11571]
[667, 1640, 2381, 3357, 4707, 6381, 6853, 8139, 9704, 11033]
[711, 1491, 2681, 3807, 4805, 5946, 6662, 8393, 8780, 11103]
----------------------------------------------------------------
'''