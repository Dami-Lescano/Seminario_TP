import random
import time

def generar_lista():
    pregenerada = ""#str(input("Cargar lista pregenerada. "))
    if pregenerada == "s":
        lista = [0,1,2,3,4,5,6,7,8,9]
    else:
        cantidad = 10000#int(input("Ingresar cantidad de numeros. "))
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
    
    print(f"Paso {pasoNumero} {tipoPaso}")
    print(f"Lista: {lista}")
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
        print(f"Lista paso {pasoNumero}: {listaOrdenada}")
        return listaOrdenada

calculos = 0

list = generar_lista()

print(f"Lista original: {list}")

tiempoInicio = time.time()

listaOrdenada = quicksort(list, 0, "inicial")

tiempoFinal = time.time()

print(f"Lista ordenada final: {listaOrdenada}")
print(f"calculos = {calculos}")
print(f"Tiempo transcurrido: {tiempoFinal - tiempoInicio} segundos")