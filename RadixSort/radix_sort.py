import random

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

lista = [13,3,23,11,12,0,11,44,44]#list(range(0,20))#[29, 66, 20, 0, 97, 26, 7, 5, 53, 6, 99, 99]
#lista = list(reversed(lista))
lista_de_listas_de_colas = []

""" for _ in range(10):
    lista.append(random.randint(0, 99)) """

print(lista)

digitos = len(str(max(lista)))

for _ in range(digitos):
    lista_de_listas_de_colas.append([])

for digito in range(digitos):
    hacer_cola_segun_digito(digito)

print(lista_de_listas_de_colas)
'''
lista_numeros_ordenados = []

for lc in lista_de_listas_de_colas:
    for c in lc:
        for n in c:
            veces_que_aparece = 1
            es_el_menor = True
            if not(lista_numeros_ordenados.__contains__(n)):

                for lc2 in reversed(lista_de_listas_de_colas):
                    for c2 in lc2:
                        for n2 in c2:
                            if not(lista_numeros_ordenados.__contains__(n2)):
                                if n == n2:
                                    veces_que_aparece += 1
                                elif n > n2:
                                    es_el_menor = False
                if es_el_menor:
                    lista_numeros_ordenados.append(n)
                    for _ in range(int(veces_que_aparece/(digitos))):
                        lista_ordenada.append(n)
'''
'''lista_ordenada = lista
for d in range(digitos):
    lista_ordenada = sorted(lista_ordenada, key=lambda n : get_digit(n, d))
    print(lista_ordenada)'''

lista_ordenada = lista.copy()
""" for d in range(digitos):
    lista_aux2 = list()
    for n in range(10):#reversed(range(10)):
        for number in lista_ordenada:
            if(get_digit(number, d) == n):
               lista_aux2.append(number)
    lista_ordenada = lista_aux2.copy()
    print(f"lista ordenada por digito {d+1}: {lista_ordenada}") """

lista_ordenada = list()

'''for i in reversed(range(len(lista_de_listas_de_colas))):
    lc = lista_de_listas_de_colas[i]
    for c in lc:
        for n in c:
            veces_que_aparece = c.count(n)
            if len(c) > 1 and veces_que_aparece != len(c) and i == 0:
                pass
            else:
                for _ in range(veces_que_aparece):
                    lista_ordenada.append(n)'''

def agregar_a_lista(lista, numero, cantidad):
    for _ in range(cantidad):
        lista.append(numero)

'''for c in lista_de_listas_de_colas[digitos-1]:
    for n in c:
        aux = digitos - 1
        veces_que_aparece = c.count(n)
        es_el_menor = True
        if len(c) > 1 and veces_que_aparece != len(c) and digitos != 1:
            c2 = lista_de_listas_de_colas[aux][get_digit(n, digitos)]
            if(len(c2) == 1):
                agregar_a_lista(lista_ordenada, n, veces_que_aparece)
            else:
                
                es_el_menor = min(c2) == n
                if es_el_menor:
                    agregar_a_lista(lista_ordenada, n, veces_que_aparece)
                
            """ if(not es_el_menor):
            for _ in range(veces_que_aparece):
                print(n)
                lista_ordenada.append(n) """
        else:
            agregar_a_lista(lista_ordenada, n, veces_que_aparece)'''

""" lista_aux = list()

for c in lista_de_listas_de_colas[1]:
    for n in c:
        lista_aux.append(n)
    print(lista_aux)

lista_aux2 = list() """

""" for c in lista_de_listas_de_colas[0]:
    while len(lista_aux) > len(lista_aux2):
        for n in c:
            for i in lista_aux:
                if n == i:
                    lista_aux2.append(n)
                    print(lista_aux2)
                    


print(lista_ordenada) """