import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
cantidades = [10, 50, 100, 500, 1000] # de 100 a 1000 con paso 100
calculos_sin_concurrencia = [27, 259, 685, 5085, 11344]
calculos_con_concurrencia = [28, 245, 641, 4654, 10670]

# Configuración del ancho de las barras y posición
ancho_barra = 0.35  # Ancho de cada barra
rango_cantidades = np.arange(len(cantidades))  # Posiciones para cada grupo de edad

# Crear el gráfico de barras
plt.bar(rango_cantidades - ancho_barra/2, calculos_sin_concurrencia, width=ancho_barra, color='blue', label='Sin concurrencia')
plt.bar(rango_cantidades + ancho_barra/2, calculos_con_concurrencia, width=ancho_barra, color='pink', label='Con concurrencia')

# Etiquetas y título
plt.xlabel('Cantidad')
plt.ylabel('Calculos')
plt.title('Quick Sort')
plt.xticks(rango_cantidades, cantidades)  # Configurar las etiquetas del eje x
plt.legend()  # Mostrar la leyenda

# Mostrar el gráfico
plt.show()

#-------------------------------------------------------
