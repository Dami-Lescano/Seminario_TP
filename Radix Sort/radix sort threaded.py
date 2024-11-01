import random
from threading import *

def get_digit(number, n):
    return abs(number) // 10**n % 10

def flatten(xss):
    return [x for xs in xss for x in xs]


def hacer_cola_segun_digito(digito):
    lista_de_colas = [[],[],[],[],[],[],[],[],[],[]]
    for number in lista:
        n = get_digit(number, digito)
        lista_de_colas[n].append(number)
    print(f"lista de colas del digito {digito+1}: {lista_de_colas}")
    lista_de_listas_de_colas[digito] = lista_de_colas

lista = []

lista_de_listas_de_colas = []

for _ in range(10):
    lista.append(random.randint(0, 99))

print(lista)

digitos = len(str(max(lista)))

threads = []

for _ in range(digitos):
    lista_de_listas_de_colas.append([])

for digito in range(digitos):
    p = Thread(target=hacer_cola_segun_digito, args=([digito]))
    threads.append(p)
    p.start()

for t in threads:
    t.join()

print(lista_de_listas_de_colas)