def romberg(f, a, b, n):
    """
    Aproxima la integral de f(x) en [a, b] usando la integración de Romberg.

    Parámetros:
    f : función
        Función a integrar.
    a, b : float
        Extremos del intervalo de integración.
    n : int
        Número de niveles de Romberg (n > 0).

    Retorna:
    R : lista de listas
        Tabla de Romberg hasta nivel n.
    """
    R = [[0.0] * (i + 1) for i in range(n)]  # Crear una tabla triangular de ceros

    h = b - a  # Paso inicial

    # Paso 1: R[0][0] = (h/2) * (f(a) + f(b))
    R[0][0] = (h / 2) * (f(a) + f(b))

    # Paso 2: Salida (R[0][0])
    print(f"R[0][0] = {R[0][0]}")

    # Paso 3
    for i in range(1, n):
        h /= 2  # Paso 7: reducir h a la mitad

        # Paso 4: Calcular R[i][0]
        sum_f = sum(f(a + (k + 0.5) * h) for k in range(2 ** (i - 1)))
        R[i][0] = 0.5 * (R[i - 1][0] + h * sum_f)

        # Paso 5: Extrapolación
        for j in range(1, i + 1):
            R[i][j] = R[i][j - 1] + (R[i][j - 1] - R[i - 1][j - 1]) / (4 ** j - 1)

        # Paso 6: Salida del renglón i
        for j in range(i + 1):
            print(f"R[{i}][{j}] = {R[i][j]}")

    # Paso 9: PARAR
    return R


# Ejemplo de uso:
if __name__ == "__main__":
    import math


    # Definir la función a integrar
    def f(x):
        return math.sin(x)


    # Intervalo [a, b]
    a = 0
    b = math.pi

    # Niveles de Romberg
    n = 4

    # Llamar al método
    tabla_romberg = romberg(f, a, b, n)

    print("\nTabla de Romberg:")
    for fila in tabla_romberg:
        print(fila)
