import random
import math
calculos = 0

def quicksort(lista, pasoNumero = 0, tipoPaso = 0):
    global calculos
    listaMenores = []
    listaMayores = []
    pivote = 0
    listaOrdenada = []
    tamañoLista = len(lista)
    
    '''print(f"Paso {pasoNumero} {tipoPaso}")
    print(f"Lista: {lista}")'''
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
        #print(f"Lista paso {pasoNumero}: {listaOrdenada}")
        return listaOrdenada
    
data = [random.randint(0, 100) for _ in range(10000)]
sorted = quicksort(data, 0, 0)

print("calculos en 100 elementos: " + str(calculos))

esperado = 10000* math.log(10000, 10)
print("calculos esperados: " + str(esperado))