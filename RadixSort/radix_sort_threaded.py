import random
from threading import *
import time
from matplotlib import pyplot as plt

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




def generar_lista(n):
    pregenerada = ""#str(input("Cargar lista pregenerada. "))
    if pregenerada == "s":
        lista = range(0, 200)
    else:
        cantidad = n#500#int(input("Ingresar cantidad de numeros. "))
        limiteMenor = 0#int(input("Ingresar el limite menor del conjunto. "))
        limiteMayor = 9999999#int(input("Ingresar el limite mayor del conjunto. "))
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





#lista = [13,3,23,11,12,0,11,44,44]

listaCalculos = []
listaTiempos = []
listaCantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

for n in listaCantidades:

    lista = generar_lista(n)

    calculos = 0

    tiempoInicio = time.time()

    digitos = len(str(max(lista)))

    lista_ordenada_final = radix_sort(digitos-1, lista)

    tiempoFinal = time.time()
    
    tiempoTotal = tiempoFinal - tiempoInicio

    #print("Lista sin ordenar: ", lista)

    listaCalculos.append(calculos)

    listaTiempos.append(tiempoTotal)

    #print(f"Lista ordenada final: {lista_ordenada_final}")
    #print(f"calculos = {calculos}, digitos * cantidad")

yi = []

for i in listaCantidades:
    current = digitos*(i)
    yi.append(current)

print("cantidades: ", listaCantidades)
print("calculos: ", listaCalculos)
print("tiempos: ", listaTiempos)
print("esperado: ",yi)

ancho_barra = 35

plt.bar(listaCantidades, listaCalculos, width=ancho_barra, color='blue', label='Calculos')
#plt.bar(xi_con_concurrencia, calculos_con_concurrencia.mean(), width=ancho_barra, color='pink', label='Con concurrencia')
plt.plot(listaCantidades, yi, color = 'red', label='Peor caso = 4*(n+10)')#k es la base


# Etiquetas y título
plt.xlabel('Cantidad')
plt.ylabel('Calculos')
plt.title('Radix Sort')
plt.xticks(listaCantidades)  # Configurar las etiquetas del eje x
plt.legend()  # Mostrar la leyenda

# Mostrar el gráfico
plt.xlabel('Cantidad')
plt.ylabel('Calculos')
plt.show()

#-------------------------------------------------------