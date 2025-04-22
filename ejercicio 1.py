import math
from scipy.integrate import quad

# A
def f_a(x):
    return x**2 * math.log(x)

a = 1
b = 4
#b = 1.5
resultado, error = quad(f_a, a, b)
print(f"A) Resultado: {resultado}, Error estimado: {error}")

# B
def f_b(x):
    return x**2 * math.exp(-x)

a = 0

b = 1
resultado, error = quad(f_b, a, b)
print(f"B) Resultado: {resultado}, Error estimado: {error}")

# C
def f_c(x):
    return 2 / (x**2 - 4)

a = 0

b = 0.35
resultado, error = quad(f_c, a, b)
print(f"C) Resultado: {resultado}, Error estimado: {error}")

# D
def f_d(x):
    return x**2 * math.sin(x)

a = 0

b = math.pi / 4
resultado, error = quad(f_d, a, b)
print(f"D) Resultado: {resultado}, Error estimado: {error}")

# E
def f_e(x):
    return math.exp(3*x) * math.sin(2*x)

a = 0

b = math.pi / 4
resultado, error = quad(f_e, a, b)
print(f"E) Resultado: {resultado}, Error estimado: {error}")

# F
def f_f(x):
    return (2 * x) / (x**2 - 4)

a = 1

b = 1.6
resultado, error = quad(f_f, a, b)
print(f"F) Resultado: {resultado}, Error estimado: {error}")

# G
def f_g(x):
    return x / math.sqrt(x**2 - 4)

a = 3

b = 3.5
resultado, error = quad(f_g, a, b)
print(f"G) Resultado: {resultado}, Error estimado: {error}")

# H
def f_h(x):
    return (math.cos(x))**2

a = 0

b = math.pi / 4
resultado, error = quad(f_h, a, b)
print(f"H) Resultado: {resultado}, Error estimado: {error}")
