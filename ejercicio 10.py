import math

# Función a integrar
def f10(x):
    return math.sqrt(1 + math.cos(x)**2)

# Tabla de Romberg completa
def romberg_table(f, a, b, n_max=10):
    R = [[0.0] * (n_max + 1) for _ in range(n_max + 1)]
    h = b - a
    R[0][0] = (h / 2) * (f(a) + f(b))

    for i in range(1, n_max + 1):
        h /= 2
        suma = 0
        for k in range(1, 2 ** i, 2):
            suma += f(a + k * h)
        R[i][0] = 0.5 * R[i-1][0] + suma * h

        for j in range(1, i + 1):
            R[i][j] = R[i][j-1] + (R[i][j-1] - R[i-1][j-1]) / (4 ** j - 1)

    return R

# Aplicación del ejercicio 10
a = 0
b = 48
n_max = 10

R = romberg_table(f10, a, b, n_max)

# Mostrar valores clave que pide el problema
def mostrar_valores():
    print("Inciso a)")
    print(f"R[1][1] = {R[0][0]}")
    print(f"R[2][1] = {R[1][0]}")
    print(f"R[3][1] = {R[2][0]}")
    print(f"R[4][1] = {R[3][0]}")
    print(f"R[5][1] = {R[4][0]}")
    print()

    print("Inciso b)")
    print(f"R[2][2] = {R[1][1]}")
    print(f"R[3][3] = {R[2][2]}")
    print(f"R[4][4] = {R[3][3]}")
    print(f"R[5][5] = {R[4][4]}")
    print()

    print("Inciso c)")
    print(f"R[6][1] = {R[5][0]}")
    print(f"R[6][2] = {R[5][1]}")
    print(f"R[6][3] = {R[5][2]}")
    print(f"R[6][4] = {R[5][3]}")
    print(f"R[6][5] = {R[5][4]}")
    print(f"R[6][6] = {R[5][5]}")
    print()

    print("Inciso d)")
    print(f"R[7][7] = {R[6][6]}")
    print(f"R[8][8] = {R[7][7]}")
    print(f"R[9][9] = {R[8][8]}")
    print(f"R[10][10] = {R[9][9]}")
    print()

    print("Predicción final (R[10][10]):")
    print(f"{R[9][9]}")

mostrar_valores()
