import math


# Función general para integración de Romberg
def romberg(f, a, b, tol=1e-4, n_max=10):
    R = [[0.0] * (n_max + 1) for _ in range(n_max + 1)]
    h = b - a
    R[0][0] = (h / 2) * (f(a) + f(b))

    for i in range(1, n_max + 1):
        h /= 2
        suma = 0
        for k in range(1, 2 ** i, 2):
            suma += f(a + k * h)
        R[i][0] = 0.5 * R[i - 1][0] + suma * h

        for j in range(1, i + 1):
            R[i][j] = R[i][j - 1] + (R[i][j - 1] - R[i - 1][j - 1]) / (4 ** j - 1)

        # Condición de parada
        if abs(R[i][i] - R[i - 1][i - 1]) < tol:
            return R[i][i]

    return R[n_max][n_max]  # Regresa el mejor valor disponible si no alcanza la tolerancia


# --- Definimos las funciones del problema 4 ---

# Problema 4 a) f(x) = x^(1/3)
def f4a(x):
    return x ** (1 / 3)


# Problema 4 b) f(x) es una función por tramos
def f4b(x):
    if 0 <= x <= 0.1:
        return x ** 3 + 1
    elif 0.1 < x <= 0.2:
        return 1.001 + 0.03 * (x - 0.1) + 0.3 * (x - 0.1) ** 2 + 2 * (x - 0.1) ** 3
    elif 0.2 < x <= 0.3:
        return 1.009 + 0.15 * (x - 0.2) + 0.9 * (x - 0.2) ** 2 + 2 * (x - 0.2) ** 3
    else:
        raise ValueError("x fuera del intervalo [0, 0.3]")


# --- Ahora resolvemos los dos ejercicios ---

# Problema 4a
resultado_4a = romberg(f4a, 0, 1, tol=1e-4)
print(f"Resultado del problema 4a (integral de x^(1/3) de 0 a 1): {resultado_4a}")

# Problema 4b
resultado_4b = romberg(f4b, 0, 0.3, tol=1e-4)
print(f"Resultado del problema 4b (integral de función por tramos de 0 a 0.3): {resultado_4b}")
