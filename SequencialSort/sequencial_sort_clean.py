import random
import time

def generar_lista():
    pregenerada = str(input("Cargar lista pregenerada. "))
    if pregenerada == "s":
        lista = [random.randint(0,9999) for _ in range(1000)]
    else:
        cantidad = int(input("Ingresar cantidad de numeros. "))
        limiteMenor = 0#int(input("Ingresar el limite menor del conjunto. "))
        limiteMayor = int(input("Ingresar el limite mayor del conjunto. "))
        repetidos = str(input("Permitir repetidos. "))


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
                lista_ordenada.append(n)

calculos = 0

lista_ordenada = list()

lista_a_ordenar = generar_lista()

print(f"Lista original: {lista_a_ordenar}")

tiempo_inicio = time.time()

sort(lista_a_ordenar, min(lista_a_ordenar), max(lista_a_ordenar))

tiempo_final = time.time()

tiempo_total = tiempo_final - tiempo_inicio

print(f"Lista ordenada final: {lista_ordenada}")
print(f"calculos = {calculos}")
print(f"Tiempo transcurrido = {tiempo_total}")