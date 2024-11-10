import random
import time
from threading import*

class NewThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        Thread.__init__(self, group, target, name, args, kwargs)

    def run(self):
        if self._target != None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def generar_lista(n):
    pregenerada = ""#str(input("Cargar lista pregenerada. "))
    if pregenerada == "s":
        lista = [0,1,2,3,4,5,6,7,8,9]
    else:
        cantidad = n#int(input("Ingresar cantidad de numeros. "))
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

def quicksort(lista, pasoNumero, tipoPaso):
    global pasos
    global quicksorts
    global calculos
    listaMenores = []
    listaMayores = []
    pivote = 0
    listaOrdenada = []
    
    if len(lista) <= 1:
        return lista
    else:
        '''lock.acquire()
        print(f"Paso {pasoNumero} {tipoPaso}")
        print(f"Lista: {lista}")
        lock.release()'''
        pivote = lista[0]
        lista.pop(0)
        for n in lista:
            #lock.acquire()
            calculos += 1
            #lock.release()
            numero = n
            if numero <= pivote:
                listaMenores.append(numero)
            else:
                listaMayores.append(numero)
        
        listaMenoresAOrdenar = NewThread(target=quicksort, args=([listaMenores, pasoNumero+1, "Menores"]))
        listaMayoresAOrdenar = NewThread(target=quicksort, args=([listaMayores, pasoNumero+1, "Mayores"]))
        
        listaMenoresAOrdenar.start()
        listaMayoresAOrdenar.start()
        
        listaMenoresOrdenada = listaMenoresAOrdenar.join()
        listaMayoresOrdenada = listaMayoresAOrdenar.join()
        
        listaOrdenada = listaMenoresOrdenada + [pivote] + listaMayoresOrdenada
        
        '''lock.acquire()
        print(f"Lista paso {pasoNumero} {tipoPaso}: {listaOrdenada}")
        lock.release()'''

        if pasoNumero > pasos:
            pasos = pasoNumero

        quicksorts += 1

        return listaOrdenada

lock = Lock()

listaCalculos = []
listaTiempos = []
listaCantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

for n in listaCantidades:

    listaAOrdenar = generar_lista(n)
    calculos = 0
    pasos = 0
    quicksorts = 0

    tiempoInicio = time.time()

    listaOrdenada = quicksort(listaAOrdenar, 0, "inicial")

    tiempoFinal = time.time()

    listaCalculos.append(calculos)

    tiempoTotal = tiempoFinal - tiempoInicio

    listaTiempos.append(tiempoTotal)

    print(f"Lista ordenada final: {listaOrdenada}")
    print(f"Cantidad de pasos: {pasos}")
    print(f"Quicksorts realizados: {quicksorts}")
    print(f"calculos = {calculos}")
    print(f"Tiempo transcurrido: {tiempoFinal - tiempoInicio} segundos")

for n in range(10):
    print(f"Cantidad: {listaCantidades[n]}, Calculos: {listaCalculos[n]}, Tiempo {listaTiempos[n]}")

print("cantidades: ", listaCantidades)
print("calculos: ", listaCalculos)
print("tiempos: ", listaTiempos)

'''
cantidades:  [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
----------------------------------------------------------------
calculos:
[637, 1624, 2732, 3460, 4366, 6942, 6705, 8709, 9158, 10426]
[567, 1498, 2543, 3486, 4725, 6441, 7061, 8589, 10169, 10589]
[786, 1534, 2543, 3502, 4568, 5782, 7233, 8215, 9805, 10768]
[542, 1495, 2888, 3636, 4978, 5541, 7106, 8646, 10100, 13051]
[621, 1435, 2549, 3472, 4641, 5978, 7455, 7879, 9543, 11255]
[613, 1510, 2428, 3944, 5369, 5651, 6636, 8729, 9753, 11502]
[593, 1560, 2710, 3691, 4486, 5582, 8062, 7901, 9264, 11038]
[851, 1575, 2540, 3573, 5211, 5695, 7045, 7616, 10132, 11365]
[614, 1780, 2660, 3848, 5036, 6193, 6749, 8355, 10018, 10908]
[776, 1618, 2645, 3714, 5085, 5714, 6797, 8707, 9466, 11655]
----------------------------------------------------------------
'''