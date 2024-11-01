import random

#--------------------------------------------------------------
#FUNCIONES EXTRAS
#--------------------------------------------------------------

def get_digit(number, n):
    return abs(number) // 10**n % 10

def flatten(xss):
    return [x for xs in xss for x in xs]

def agregar_a_lista(lista, numero, cantidad):
    for _ in range(cantidad):
        lista.append(numero)


#--------------------------------------------------------------



def hacer_cola_segun_digito(digito):
    lista_de_colas = [[],[],[],[],[],[],[],[],[],[]]
    for number in lista:
        n = get_digit(number, digito)
        lista_de_colas[n].append(number)
    print(f"lista de colas del digito {digito+1}: {lista_de_colas}")
    lista_de_listas_de_colas[digito] = lista_de_colas

#lista = [13,3,23,11,12,0,11,44,44]
lista = []
for _ in range(10):
    lista.append(random.randint(0, 99)) 
#lista = list(reversed(lista))
lista_de_listas_de_colas = []

print("Lista sin ordenar: ", lista)

digitos = len(str(max(lista)))



for _ in range(digitos):
    lista_de_listas_de_colas.append([])

for digito in range(digitos):
    hacer_cola_segun_digito(digito)

#print(lista_de_listas_de_colas)

#Unidades [[0], [11, 11], [12], [13, 3, 23], [44, 44], [], [], [], [], []]
#Decenas  [[3, 0], [13, 11, 12, 11], [23], [], [44, 44], [], [], [], [], []]
lista_a_ordenar = []
unidades_flat = flatten(lista_de_listas_de_colas[0])
for i in lista_de_listas_de_colas[1]:
    if len(i) == 1:
        lista_a_ordenar.append(i[0])
    elif len(i) > 1:
        #i = [3, 0]
        for u in unidades_flat:
            if i.__contains__(u):
                lista_a_ordenar.append(u)


print("Lista ordenada: ", lista_a_ordenar)