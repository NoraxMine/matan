import numpy as np
import matplotlib.pyplot as plt

# Размер сетки и шаг
d = 1
N_x, N_y = 5, 5  # Количество точек по осям

# Создание сетки точек
x = np.arange(0, N_x * d, d)
y = np.arange(0, N_y * d, d)
X, Y = np.meshgrid(x, y)

# Визуализация точек
plt.scatter(X, Y, marker='o', color='red')
plt.grid(True)
plt.title("Квадратно-гнездовое расположение точек")
 
plt.show()