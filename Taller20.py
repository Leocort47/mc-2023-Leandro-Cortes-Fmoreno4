# -*- coding: utf-8 -*-
"""ajustePolinomial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pChd78Ekc1ejVEqsMXIZl3bTS4MstJnf
"""

import numpy as np
import math
import matplotlib.pyplot as plt

# Datos de la tabla
x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([4.2, 1.4, 0, -0.4, -0.1, 1.6, 4.1])

n = len(x)

# Calcula la suma de x, y, x^2, y^2 y xy
sum_x = sum(x)
sum_y = sum(y)
sum_x2 = sum([xi**2 for xi in x])
sum_y2 = sum([yi**2 for yi in y])
sum_xy = sum([x[i]*y[i] for i in range(n)])

# Calcula la desviación estándar de los residuos (sy)
residuos = [y[i] - a - b*x[i] for i in range(n)]
sy = math.sqrt(sum([r**2 for r in residuos]) / (n-2))

#Sumatoria de Sr


# Calcula el error estándar de la estimación (s_Tyx)
styx = sy * math.sqrt(n / (n*sum_x2 - sum_x**2))

# Ajuste a un polinomio de segundo grado
coefficients = np.polyfit(x, y, 2)
a, b, c = coefficients

# Función del polinomio ajustado
f = np.poly1d(coefficients)

#Coeficiente de correlacion 
coef = np.corrcoef(x, y)[0, 1]

# Crear un rango de valores de x para graficar la función
x_range = np.linspace(x.min(), x.max(), 100)

# Graficar los datos y la función ajustada
plt.plot(x, y, 'o', label='Datos')
plt.plot(x_range, f(x_range), label='Polinomio ajustado')

# Etiquetas de los ejes y el título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajuste polinómico de segundo grado')

# Leyenda
plt.legend()

# Mostrar la gráfica
plt.show()

print(f"Polinomio ajustado: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}")
print(f"Coeficiente de correlación: r = {coef}")
print("La desviación estándar de los residuos (sy) es: {:.2f}".format(sy))
print("El error estándar de la estimación (s_Tyx) es: {:.2f}".format(styx))