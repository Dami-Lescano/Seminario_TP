import random
import time

from matplotlib import pyplot as plt

def generar_lista(n):
    pregenerada = ""#str(input("Cargar lista pregenerada. "))
    if pregenerada == "s":
        lista = range(0, 100)
    else:
        cantidad = n#int(input("Ingresar cantidad de numeros. "))
        limiteMenor = 0#int(input("Ingresar el limite menor del conjunto. "))
        limiteMayor = 999#int(input("Ingresar el limite mayor del conjunto. "))
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






def sort(lista, menor, mayor):
    global calculos
    for i in range(menor, mayor+1):
        for n in lista:
            #print(i, n)
            calculos += 1
            if n == i:
                listaOrdenada.append(n)






listaCalculos = []
listaTiempos = []
listaCantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

for n in listaCantidades:
    calculos = 0

    listaOrdenada = list()

    listaAOrdenar = generar_lista(n)

    print(f"Lista original: {listaAOrdenar}")

    sort(listaAOrdenar, min(listaAOrdenar), max(listaAOrdenar))

    listaCalculos.append(calculos)

    print(f"Lista ordenada final: {listaOrdenada}")
    print(f"calculos = {calculos}")

print("cantidades: ", listaCantidades)
print("calculos: ", listaCalculos)

yi = []

for i in listaCantidades:
    current = i*999
    yi.append(current)

print("cantidades: ", listaCantidades)
print("calculos: ", listaCalculos)
print("esperado: ", yi)

ancho_barra = 35

plt.bar(listaCantidades, listaCalculos, width=ancho_barra, color='blue', label='Calculos')
#plt.bar(xi_con_concurrencia, calculos_con_concurrencia.mean(), width=ancho_barra, color='pink', label='Con concurrencia')
plt.plot(listaCantidades, yi, color = 'red', label = 'Formula: n*r')

#plt.axis([0, 1200, 0, 1200000])

# Etiquetas y título
plt.xlabel('Cantidad')
plt.ylabel('Calculos')
plt.title('Sort - r=999 ')
plt.xticks(listaCantidades)  # Configurar las etiquetas del eje x
plt.legend()  # Mostrar la leyenda

# Mostrar el gráfico
plt.xlabel('Cantidad (n)')
plt.ylabel('Calculos')
plt.ticklabel_format(style='plain')
plt.show()

#-------------------------------------------------------