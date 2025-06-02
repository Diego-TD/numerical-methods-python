import numpy as np
import matplotlib.pyplot as plt

def find_max_index(arr):
    max_value = abs(arr[0])
    max_index = 0

    for i in range(1, len(arr)):
        if abs(arr[i]) > max_value:
            max_value = abs(arr[i])
            max_index = i

    return max_index


def gauss_elimination_with_partial_pivoting(matrix):
    np.set_printoptions(suppress=True)
    print("Original Matrix:\n", matrix)

    # forward elimination ---------------------
    k = 0  # counter that helps to start from a lower row when switching columns
    # Iterate the matrix in diagonal
    # i = column, j = row
    for i in range(matrix.shape[1] - 1):
        for j in range(matrix.shape[0] - 1):
            j = j + k

            if j >= matrix.shape[0] - 1:
                continue

            if matrix[i, j] == 0:
                max_index = find_max_index(matrix[:, i])

                row_to_swap = matrix[i, :].copy()
                row_max_value = matrix[max_index, :].copy()

                matrix[i, :] = row_max_value
                matrix[max_index, :] = row_to_swap
                print("Pivot:\n", matrix)

            b = matrix[j + 1, i].copy()
            a = matrix[i, i].copy()
            factor = b / a
            row = matrix[i,].copy()
            array = factor * row
            temp = matrix[j + 1,].copy() - array

            matrix[j + 1, :] = temp
            print("step {},{} :\n{}".format(i, j, matrix))

        # to start the next iteration 1 row down
        k = k + 1

    # back substitution
    n = matrix.shape[0]
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        sum_ax = 0
        for j in range(i + 1, n):
            sum_ax += matrix[i, j] * x[j]

        x[i] = (matrix[i, -1] - sum_ax) / matrix[i, i]
    print("Roots:", x)
    return x


def multi_linear_regression():
    # Datos filas: x1, x2, x3, x4, y
    data = np.array([
        [25,4,7,3,28],
        [27,5,7,6,28],
        [28,4,7,4,30],
        [14,3,8,4,23],
        [21,4,6,6,20],
        [13,3,8,2,23],
        [30,3,5,6,25],
        [16,2,4,3,19],
        [22,5,6,5,23],
        [14,3,6,2,21]
    ], dtype=float)
    x1 = data[:, 0]
    x2 = data[:, 1]
    x3 = data[:, 2]
    x4 = data[:, 3]
    y  = data[:, 4]
    n = len(y)

    # Sumas simples
    Sx1 = x1.sum()
    Sx2 = x2.sum()
    Sx3 = x3.sum()
    Sx4 = x4.sum()
    Sy = y.sum()

    # Sumas de cuadrados
    Sx1x1 = (x1 ** 2).sum()
    Sx2x2 = (x2 ** 2).sum()
    Sx3x3 = (x3 ** 2).sum()
    Sx4x4 = (x4 ** 2).sum()

    # Productos cruzados x_i * x_j
    Sx1x2 = (x1 * x2).sum()
    Sx1x3 = (x1 * x3).sum()
    Sx1x4 = (x1 * x4).sum()
    Sx2x3 = (x2 * x3).sum()
    Sx2x4 = (x2 * x4).sum()
    Sx3x4 = (x3 * x4).sum()

    # Cálculo de sumas de productos xi * y
    Sx1y = (x1 * y).sum()
    Sx2y = (x2 * y).sum()
    Sx3y = (x3 * y).sum()
    Sx4y = (x4 * y).sum()

    # Sistema de ecuaciones
    M = np.array([
        [n, Sx1, Sx2, Sx3, Sx4, Sy],
        [Sx1, Sx1x1, Sx1x2, Sx1x3, Sx1x4, Sx1y],
        [Sx2, Sx1x2, Sx2x2, Sx2x3, Sx2x4, Sx2y],
        [Sx3, Sx1x3, Sx2x3, Sx3x3, Sx3x4, Sx3y],
        [Sx4, Sx1x4, Sx2x4, Sx3x4, Sx4x4, Sx4y]
    ], dtype=float)

    # Resolver con gauss
    beta = gauss_elimination_with_partial_pivoting(M)

    # Imprimir coeficientes
    print("Coeficientes estimados (Gauss):")
    print(f"  β₀ = {beta[0]:.6f} (intercepto)")
    print(f"  β₁ = {beta[1]:.6f} (coeficiente para x1)")
    print(f"  β₂ = {beta[2]:.6f} (coeficiente para x2)")
    print(f"  β₃ = {beta[3]:.6f} (coeficiente para x3)")
    print(f"  β₄ = {beta[4]:.6f} (coeficiente para x4)")

    # Construir ecuación de predicción como string
    equation = (
        f"y = {beta[0]:.3f} "
        f"{beta[1]:+.3f}*x1 "
        f"{beta[2]:+.3f}*x2 "
        f"{beta[3]:+.3f}*x3 "
        f"{beta[4]:+.3f}*x4"
    )
    print(f"\nEcuación de predicción:\n  {equation}")

    # Calcular predicciones y R²
    y_hat = (beta[0]
             + beta[1] * x1
             + beta[2] * x2
             + beta[3] * x3
             + beta[4] * x4)
    resid = y - y_hat
    SS_res = (resid ** 2).sum()
    SS_tot = ((y - y.mean()) ** 2).sum()
    R2 = 1 - SS_res / SS_tot
    print(f"\nR² del modelo = {R2:.4f}")

    # Grafica valores reales vs predicciones
    plt.figure(figsize=(6, 5))
    plt.scatter(range(n), y, color='blue', label='Y real')
    plt.plot(range(n), y_hat, color='red', linestyle='--', label='Ŷ predicción')
    plt.xlabel("Índice de muestra")
    plt.ylabel("Valor de Y")
    plt.title("Valores reales y predicciones de Y")
    plt.legend()
    plt.grid(True)
    plt.show()

    while True:
        print("\nElige una opción:")
        print("1) Predecir y con nuevos valores de x1, x2, x3, x4")
        print("2) Salir")
        choice = input("Opción (1 o 2): ").strip()

        if choice == "1":
            try:
                x1_val = float(input("Ingresa las LOC esperadas (en miles) (x1): ").replace(",", "."))
                x2_val = float(input("Ingresa el número Programadores (x2): ").replace(",", "."))
                x3_val = float(input("Ingresa la Complejidad del 1-10 (x3): ").replace(",", "."))
                x4_val = float(input("Ingresa la experiencia en años (x4): ").replace(",", "."))
            except ValueError:
                print("Error: Debes ingresar números válidos.")
                continue

            # Calcular y_hat
            y_hat = (beta[0]
                     + beta[1] * x1_val
                     + beta[2] * x2_val
                     + beta[3] * x3_val
                     + beta[4] * x4_val)
            print(f"\n=> Predicción:  Tiempo en semanas (ŷ) = {y_hat:.4f}")

        elif choice == "2":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Ingresa 1 o 2.")


if __name__ == '__main__':
    multi_linear_regression()