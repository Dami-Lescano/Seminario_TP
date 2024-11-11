import random
from threading import *
import time

class NewThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        Thread.__init__(self, group, target, name, args, kwargs)

    def run(self):
        if self._target != None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return

#--------------------------------------------------------------
#FUNCIONES EXTRAS
#--------------------------------------------------------------

def place_holder(c):
    return c

def get_digit(number, n):
    return number // 10**n % 10

def generar_lista():
    pregenerada = str(input("Cargar lista pregenerada. "))
    if pregenerada == "s":
        lista = [random.randint(0,9999) for _ in range(1000)]
    else:
        cantidad = int(input("Ingresar cantidad de numeros. "))
        limite_menor = 0#int(input("Ingresar el limite menor del conjunto. "))
        limite_mayor = int(input("Ingresar el limite mayor del conjunto. "))
        repetidos = str(input("Permitir repetidos. "))


        if repetidos == "s":
            lista = list()
            for _ in range(cantidad):
                lista.append(random.randint(limite_menor, limite_mayor))
        else:
            lista = set()
            while len(lista) < cantidad:
                lista.add(random.randint(limite_menor, limite_mayor))
    
    return list(lista)

#--------------------------------------------------------------

def radix_sort(digito, lista_a_ordenar):
    lista_de_colas = [[],[],[],[],[],[],[],[],[],[]]
    lista_ordenada = []
    global calculos
    if digito == -1:
        return lista_a_ordenar
    else:
        for number in lista_a_ordenar:
            n = get_digit(number, digito)
            lista_de_colas[n].append(number)
            calculos += 1
        threads = []
        for cola in lista_de_colas:
            if len(cola) > 1:
                radix_thread = NewThread(target=radix_sort, args=([digito-1, cola]))
                threads.append(radix_thread)
                radix_thread.start()
            elif len(cola) == 1:
                radix_thread = NewThread(target=place_holder, args=([cola]))
                threads.append(radix_thread)
                radix_thread.start()
        for t in threads:
            lista_ordenada.extend(t.join())
        return lista_ordenada

lista = generar_lista()

print("Lista sin ordenar: ", lista)

calculos = 0

tiempo_inicio = time.time()

digitos = len(str(max(lista)))

lista_ordenada_final = radix_sort(digitos-1, lista)

tiempo_final = time.time()

tiempo_total = tiempo_final - tiempo_inicio

print(f"Lista ordenada final: {lista_ordenada_final}")
print(f"calculos = {calculos}, digitos * cantidad")
print(f"Tiempo transcurrido = {tiempo_total}")