import matplotlib.pyplot as plt
import random

cantidades = []

for i in range(10):
    cantidades.append(i*3)

calculos_radix = []
calculos_counting = []
calculos_mix = []
calculos_bubble = []


def generar_lista(n, k):
    ret = [random.randint(0, k) for _ in range(n)]
    return ret


def c_radix(n, d, b):
    return d * (n + b)

def c_mix(n, k):
    return n+k

def c_bubble(n):
    return n*n

for i in cantidades:
    current_radix = c_radix(i, 4, 10)
    calculos_radix.append(current_radix)
    #current_counting = c_counting(i, 10000)
    #calculos_counting.append(current_counting)
    current_mix = c_mix(i, 10000)
    calculos_mix.append(current_mix)
    current_bubble = c_bubble(i)
    calculos_bubble.append(current_bubble)

plt.plot(cantidades, calculos_radix, color = 'red', label = 'radix sort')
#plt.plot(cantidades, calculos_counting, color = 'green', label = 'counting sort')
plt.plot(cantidades, calculos_bubble, color = 'blue', label = 'bubble sort')

plt.title('Comparación de complejidades con ordenando pocos elementos')
plt.xticks(cantidades)  # Configurar las etiquetas del eje x
plt.legend()  # Mostrar la leyenda

# Mostrar el gráfico
plt.xlabel('Cantidad')
plt.ylabel('Calculos')
plt.show()
