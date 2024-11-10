import random
import time
import concurrent.futures

def generar_lista():
    pregenerada = ""#str(input("Cargar lista pregenerada. "))
    if pregenerada == "s":
        lista = [0,1,2,3,4,5,6,7,8,9]
    else:
        cantidad = 1000#int(input("Ingresar cantidad de numeros. "))
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

def quicksort(lista):
    global calculos
    listaMenores = []
    listaMayores = []
    pivote = 0
    listaOrdenada = []
    
    if len(lista) <= 1:
        return lista
    else:
        '''lock.acquire()
        print(f"Paso {pasoNumero} {tipoPaso}")
        print(f"Lista: {lista}")
        lock.release()'''
        pivote = lista[0]
        lista.pop(0)
        for n in lista:
            #lock.acquire()
            calculos += 1
            #lock.release()
            numero = n
            if numero <= pivote:
                listaMenores.append(numero)
            else:
                listaMayores.append(numero)
        
        with concurrent.futures.ThreadPoolExecutor() as executor:

            results = list(executor.map(quicksort, [listaMenores, listaMayores]))
            #listaMenoresOrdenada = executor.submit(quicksort, listaMenores).result()
            #listaMayoresOrdenada = executor.submit(quicksort, listaMayores).result()
        
        listaOrdenada = results[0] + [pivote] + results[1]
        
        '''lock.acquire()
        print(f"Lista paso {pasoNumero} {tipoPaso}: {listaOrdenada}")
        lock.release()'''

        return listaOrdenada

lista = generar_lista()
calculos = 0
pasos = 0
quicksorts = 0

print(f"Lista original: {lista}")

tiempoInicio = time.time()

listaOrdenada = quicksort(lista)

tiempoFinal = time.time()

print(f"Lista ordenada final: {listaOrdenada}")
print(f"Cantidad de pasos: {pasos}")
print(f"Quicksorts realizados: {quicksorts}")
print(f"calculos = {calculos}")
print(f"Tiempo transcurrido: {tiempoFinal - tiempoInicio} segundos")