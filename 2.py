from sympy import symbols, integrate

x = symbols('x')
f = x**2  # Функция для интегрирования

# Вычисляем определённый интеграл от 0 до 2
integral_definite = integrate(f, (x, 0, 2))
print(integral_definite)  # Вывод: 8/3
