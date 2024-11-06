import random

#--------------------------------------------------------------
#FUNCIONES EXTRAS
#--------------------------------------------------------------

def get_digit(number, n):
    return abs(number) // 10**n % 10

def flatten(xss):
    return [x for xs in xss for x in xs]


#--------------------------------------------------------------
# RADIX SORT
#--------------------------------------------------------------

def hacer_cola_segun_digito(lista, digito):
    # Creamos las colas (listas) para cada dígito del 0 al 9
    lista_de_colas = [[] for _ in range(10)]
    for number in lista:
        n = get_digit(number, digito)
        lista_de_colas[n].append(number)
    print(f"Lista de colas para el dígito {digito+1}: {lista_de_colas}")
    return flatten(lista_de_colas)

# Generamos una lista de números aleatorios para probar
lista = [random.randint(0, 999) for _ in range(10)]

print("Lista sin ordenar:", lista)

# Obtenemos el número máximo de dígitos entre los números
digitos = len(str(max(lista)))

# Ordenamos repetidamente por cada dígito
for digito in range(digitos):
    lista = hacer_cola_segun_digito(lista, digito)

print("Lista ordenada:", lista)