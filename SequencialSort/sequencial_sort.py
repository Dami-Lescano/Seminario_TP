import random
import time

def generar_lista():
    pregenerada = ""#str(input("Cargar lista pregenerada. "))
    if pregenerada == "s":
        lista = range(0, 100)
    else:
        cantidad = 10#int(input("Ingresar cantidad de numeros. "))
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

def sort(lista, menor, mayor):
    global calculos
    for i in range(menor, mayor+1):
        for n in lista:
            #print(i, n)
            calculos += 1
            if n == i:
                listaOrdenada.append(n)


calculos = 0

list = generar_lista()

print(f"Lista original: {list}")

listaOrdenada = []

tiempoInicio = time.time()

sort(list, min(list), max(list))

tiempoFinal = time.time()

print(f"Lista ordenada final: {listaOrdenada}")
print(f"calculos = {calculos}, rango * cantidad")
print(f"Tiempo transcurrido: {tiempoFinal - tiempoInicio} segundos")