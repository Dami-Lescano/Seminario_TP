import random
import time

from matplotlib import pyplot as plt

#--------------------------------------------------------------
#FUNCIONES EXTRAS
#--------------------------------------------------------------




def get_digit(number, n):
    return number // 10**n % 10




def generar_lista(n, rango):
    pregenerada = ""#str(input("Cargar lista pregenerada. "))
    if pregenerada == "s":
        lista = range(0, 200)
    else:
        cantidad = n#500#int(input("Ingresar cantidad de numeros. "))
        limiteMenor = 0#int(input("Ingresar el limite menor del conjunto. "))
        limiteMayor = rango#999999#int(input("Ingresar el limite mayor del conjunto. "))
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
        for cola in lista_de_colas:
            if len(cola) > 1:
                lista_ordenada.extend(radix_sort(digito-1, cola))
            elif len(cola) == 1:
                lista_ordenada.extend(cola)
        return lista_ordenada
    


#lista = [13,3,23,11,12,0,11,44,44]

listaCalculos = []
listaTiempos = []
listaCantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
maximo = 9999

for n in listaCantidades:

    lista = generar_lista(n, maximo)

    calculos = 0

    #print("Lista sin ordenar: ", lista)

    tiempoInicio = time.time()

    digitos = len(str(max(lista)))

    lista_ordenada_final = radix_sort(digitos-1, lista)

    tiempoFinal = time.time()
    
    tiempoTotal = tiempoFinal - tiempoInicio

    listaTiempos.append(tiempoTotal)

    listaCalculos.append(calculos)

    #print(f"Lista ordenada final: {lista_ordenada_final}")
    #print(f"calculos = {calculos}, digitos * cantidad")

yi = []

for i in listaCantidades:
    current = digitos*(i)
    yi.append(current)

print("cantidades: ", listaCantidades)
print("calculos: ", listaCalculos)
print("tiempos: ", listaTiempos)
print("esperado: ", yi)

ancho_barra = 35

xi_sin_concurrencia = []
xi_con_concurrencia = []
for i in listaCantidades:
    xi_sin_concurrencia.append(i - ancho_barra/2)
    xi_con_concurrencia.append(i + ancho_barra/2)

plt.bar(xi_sin_concurrencia, listaCalculos, width=ancho_barra, color='blue', label='Sin concurrencia')
plt.bar(xi_con_concurrencia, [280, 608, 980, 1331, 1688, 2067, 2473, 2853, 3243, 3644], width=ancho_barra, color='pink', label='Con concurrencia')
plt.plot(listaCantidades, yi, color = 'red', label=f'Peor caso = n*d')#k es la base


# Etiquetas y título
plt.xlabel('Cantidad (n)')
plt.ylabel('Calculos')
plt.title(f'Radix Sort - d = {digitos}')
plt.xticks(listaCantidades)  # Configurar las etiquetas del eje x
plt.legend()  # Mostrar la leyenda

# Mostrar el gráfico
plt.show()

#-------------------------------------------------------

tiempo_concurrencia = [0.018971920013427734, 0.054999351501464844, 0.05300021171569824, 0.07000017166137695, 0.09000158309936523, 0.10600018501281738, 0.12599849700927734, 0.14021897315979004, 0.16199994087219238, 0.18200325965881348]

plt.bar(xi_sin_concurrencia, listaTiempos, width=ancho_barra, color='blue', label='Sin concurrencia')
plt.bar(xi_con_concurrencia, tiempo_concurrencia, width=ancho_barra, color='pink', label='Con concurrencia')
#plt.plot(listaCantidades, yi, color = 'red', label=f'Peor caso = n*d')#k es la base


# Etiquetas y título
plt.title(f'Radix Sort - d = {digitos}')
plt.xticks(listaCantidades)  # Configurar las etiquetas del eje x
plt.legend()  # Mostrar la leyenda

# Mostrar el gráfico
plt.xlabel('Cantidad')
plt.ylabel('Tiempo')
plt.show()