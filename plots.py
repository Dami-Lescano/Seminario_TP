import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
edades = [10, 12, 14, 16, 18, 20]
pesos_hombres = [32, 37, 48, 52, 65, 72]
pesos_mujeres = [30, 35, 45, 50, 60, 68]





# Configuración del ancho de las barras y posición
ancho_barra = 0.35  # Ancho de cada barra
rango_edades = np.arange(len(edades))  # Posiciones para cada grupo de edad

# Crear el gráfico de barras
plt.bar(rango_edades - ancho_barra/2, pesos_hombres, width=ancho_barra, color='blue', label='Hombres')
plt.bar(rango_edades + ancho_barra/2, pesos_mujeres, width=ancho_barra, color='pink', label='Mujeres')

# Etiquetas y título
plt.xlabel('Edad')
plt.ylabel('Peso (kg)')
plt.title('Relación entre Edad y Peso por Género')
plt.xticks(rango_edades, edades)  # Configurar las etiquetas del eje x
plt.legend()  # Mostrar la leyenda

# Mostrar el gráfico
plt.show()