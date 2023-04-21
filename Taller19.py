# -*- coding: utf-8 -*-
"""Error en la Regresión Lineal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jHvLS03QUMOLr1Ogrh4mKtlVxKF4i-gA
"""

import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Datos de entrada
x = [1, 2, 3, 4, 5, 6, 7]
y = [0.2, 0.5, 1.8, 3.4, 5.7, 9.0, 13.8]

n = len(x)

# Calcula la suma de x, y, x^2, y^2 y xy
sum_x = sum(x)
sum_y = sum(y)
sum_x2 = sum([xi**2 for xi in x])
sum_y2 = sum([yi**2 for yi in y])
sum_xy = sum([x[i]*y[i] for i in range(n)])

# Calcula los coeficientes de la regresión
b = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
a = (sum_y - b*sum_x) / n

# Calcula la desviación estándar de los residuos (sy)
residuos = [y[i] - a - b*x[i] for i in range(n)]
sy = math.sqrt(sum([r**2 for r in residuos]) / (n-2))

# Calcula el error estándar de la estimación (s_Tyx)
styx = sy * math.sqrt(n / (n*sum_x2 - sum_x**2))

# Calcula el coeficiente de correlación (r)
r = (n*sum_xy - sum_x*sum_y) / math.sqrt((n*sum_x2 - sum_x**2)*(n*sum_y2 - sum_y**2))

# Imprime los resultados
print("La ecuación de la recta de regresión es: y = {:.2f} + {:.2f}x".format(a, b))
print("La desviación estándar de los residuos (sy) es: {:.2f}".format(sy))
print("El error estándar de la estimación (s_Tyx) es: {:.2f}".format(styx))
print("El coeficiente de correlación (r) es: {:.2f}".format(r))

plt.scatter(x,y)
plt.plot(x,y,'g', alpha=0.8)
plt.grid()
plt.show()