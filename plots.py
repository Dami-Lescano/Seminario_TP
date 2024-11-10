import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

def flatten(xss):
    return [x for xs in xss for x in xs]

# Datos de ejemplo
cantidades = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000] # de 100 a 1000 con paso 100
calculos_sin_concurrencia = pd.DataFrame([[805, 1585, 2780, 3764, 4357, 5846, 7439, 9179, 9714, 10781],
[662, 1439, 2546, 3687, 5605, 6051, 6919, 8230, 10129, 10664],
[646, 1459, 2293, 4096, 4799, 6470, 7344, 8593, 9150, 11264],
[686, 1551, 2771, 3610, 5095, 5815, 7081, 8850, 9341, 10679],
[683, 1448, 3074, 3776, 5041, 6263, 6874, 8707, 9650, 11673],
[671, 1447, 2601, 3745, 4678, 5913, 7182, 8599, 11517, 11066],
[586, 1445, 2508, 3509, 4754, 6231, 6796, 8631, 10604, 11896],
[605, 1740, 2492, 3491, 4518, 5491, 7162, 9141, 9679, 11571],
[667, 1640, 2381, 3357, 4707, 6381, 6853, 8139, 9704, 11033],
[711, 1491, 2681, 3807, 4805, 5946, 6662, 8393, 8780, 11103]])
calculos_con_concurrencia = pd.DataFrame([[637, 1624, 2732, 3460, 4366, 6942, 6705, 8709, 9158, 10426],
[567, 1498, 2543, 3486, 4725, 6441, 7061, 8589, 10169, 10589],
[786, 1534, 2543, 3502, 4568, 5782, 7233, 8215, 9805, 10768],
[542, 1495, 2888, 3636, 4978, 5541, 7106, 8646, 10100, 13051],
[621, 1435, 2549, 3472, 4641, 5978, 7455, 7879, 9543, 11255],
[613, 1510, 2428, 3944, 5369, 5651, 6636, 8729, 9753, 11502],
[593, 1560, 2710, 3691, 4486, 5582, 8062, 7901, 9264, 11038],
[851, 1575, 2540, 3573, 5211, 5695, 7045, 7616, 10132, 11365],
[614, 1780, 2660, 3848, 5036, 6193, 6749, 8355, 10018, 10908],
[776, 1618, 2645, 3714, 5085, 5714, 6797, 8707, 9466, 11655]])

media = calculos_sin_concurrencia.mean()[9]

print(media)

yi = []

for i in cantidades:
    current = i*math.log(i, 10)
    yi.append(current)

#d = {'Cantidad':pd.Series([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])}





# Configuración del ancho de las barras y posición
ancho_barra = 35  # Ancho de cada barra
rango_cantidades = np.arange(len(cantidades))  # Posiciones para cada grupo de edad
#print(rango_cantidades)

xi_sin_concurrencia = []
xi_con_concurrencia = []
for i in cantidades:
    xi_sin_concurrencia.append(i - ancho_barra/2)
    xi_con_concurrencia.append(i + ancho_barra/2)

# Crear el gráfico de barras   (n*log(n))
plt.bar(xi_sin_concurrencia, calculos_sin_concurrencia.mean(), width=ancho_barra, color='blue', label='Sin concurrencia')
plt.bar(xi_con_concurrencia, calculos_con_concurrencia.mean(), width=ancho_barra, color='pink', label='Con concurrencia')
plt.plot(cantidades, yi, color = 'red')


# Etiquetas y título
plt.xlabel('Cantidad')
plt.ylabel('Calculos')
plt.title('Quick Sort')
plt.xticks(cantidades)  # Configurar las etiquetas del eje x
plt.legend()  # Mostrar la leyenda

# Mostrar el gráfico
plt.xlabel('Cantidad')
plt.ylabel('Calculos')
plt.show()

#-------------------------------------------------------
