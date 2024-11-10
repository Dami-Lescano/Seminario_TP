import random
import time

#--------------------------------------------------------------
#FUNCIONES EXTRAS
#--------------------------------------------------------------

def get_digit(number, n):
    return number // 10**n % 10

def flatten(xss):
    return [x for xs in xss for x in xs]

def generar_lista():
    pregenerada = ""#str(input("Cargar lista pregenerada. "))
    if pregenerada == "s":
        lista = range(0, 200)
    else:
        cantidad = 500#int(input("Ingresar cantidad de numeros. "))
        limiteMenor = 0#int(input("Ingresar el limite menor del conjunto. "))
        limiteMayor = cantidad*2#int(input("Ingresar el limite mayor del conjunto. "))
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

#--------------------------------------------------------------
# RADIX SORT
#--------------------------------------------------------------

def hacer_cola_segun_digito(lista, digito):
    global calculos
    # Creamos las colas (listas) para cada dígito del 0 al 9
    lista_de_colas = [[] for _ in range(10)]
    for number in lista:
        calculos += 1
        n = get_digit(number, digito)
        lista_de_colas[n].append(number)
    print(f"Lista de colas para el dígito {digito+1}: {lista_de_colas}")
    return flatten(lista_de_colas)

# Generamos una lista de números aleatorios para probar
lista = generar_lista()

calculos = 0

print("Lista sin ordenar:", lista)

tiempoInicio = time.time()

# Obtenemos el número máximo de dígitos entre los números
digitos = len(str(max(lista)))

# Ordenamos repetidamente por cada dígito
for digito in range(digitos):
    lista = hacer_cola_segun_digito(lista, digito)


tiempoFinal = time.time()

print(f"Lista ordenada final: {lista}")
print(f"calculos = {calculos}, digitos * cantidad")
print(f"Tiempo transcurrido: {tiempoFinal - tiempoInicio} segundos")