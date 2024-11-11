import random
import time

#--------------------------------------------------------------
#FUNCIONES EXTRAS
#--------------------------------------------------------------

def get_digit(number, digit):
    return number // 10**digit % 10

def generar_lista():
    pregenerada = str(input("Cargar lista pregenerada. "))
    if pregenerada == "s":
        lista = [random.randint(0,99) for _ in range(10)]
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
    global digitos
    if digito == digitos:
        return lista_a_ordenar
    else:
        for number in lista_a_ordenar:
            n = get_digit(number, digito)
            lista_de_colas[n].append(number)
            calculos += 1
        print(f"Buckets: {lista_de_colas}")
        for cola in lista_de_colas:
            lista_ordenada.extend(cola)
        lista_ordenada = radix_sort(digito+1,lista_ordenada)
        return lista_ordenada

lista = generar_lista()

calculos = 0

print("Lista sin ordenar: ", lista)

tiempo_inicio = time.time()

digitos = len(str(max(lista)))

lista_ordenada_final = radix_sort(0, lista)

tiempo_final = time.time()

tiempo_total = tiempo_final - tiempo_inicio

print(f"Lista ordenada final: {lista_ordenada_final}")
print(f"calculos = {calculos}")
print(f"Tiempo transcurrido = {tiempo_total}")