import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')
f_expr = 5*x**3 - 5*x**2 + 6*x - 2
f = sp.lambdify(x, f_expr, 'numpy')

def find_bracket(func, x_min, x_max, num_points=1000):
    x_vals = np.linspace(x_min, x_max, num_points)
    for i in range(len(x_vals) - 1):
        if func(x_vals[i]) * func(x_vals[i + 1]) < 0:
            return x_vals[i], x_vals[i + 1]
    return None, None

def bisection(func, xl, xu, error_tol):
    iter_count = 0
    xr_old = None
    xr = (xl + xu) / 2.0
    relative_error = np.inf
    iterations = []
    print("Inicio evaluación del método de bisección.")
    while relative_error > error_tol:
        iter_count += 1
        xr_old = xr
        xr = (xl + xu) / 2.0
        iterations.append((iter_count, xl, xu, xr, func(xr)))
        if np.isclose(func(xr), 0, atol=1e-12):
            relative_error = 0
            break
        if func(xl) * func(xr) < 0:
            xu = xr
        else:
            xl = xr
        if xr != 0:
            relative_error = abs((xr - xr_old) / xr)
        print(f"Iteración {iter_count}: xl = {xl}, xu = {xu}, xr = {xr}, f(xr) = {func(xr)}, error_rel = {relative_error}")
    print("Fin evaluación del método de bisección.")
    return xr, iter_count, iterations

if __name__ == "__main__":
    error_input = float(input("Ingrese el error relativo aceptable (ej. 0.001 para 0.1%): "))
    x_min = float(input("Ingrese el límite inferior del rango a evaluar en x (ej. -10): "))
    x_max = float(input("Ingrese el límite superior del rango a evaluar en x (ej. 10): "))
    xl, xu = find_bracket(f, x_min, x_max)
    if xl is None or xu is None:
        print("No se encontró un intervalo con cambio de signo en el rango dado.")
    else:
        print(f"Intervalo encontrado: xl = {xl}, xu = {xu}")
        raiz, total_iter, iter_details = bisection(f, xl, xu, error_input)
        print(f"La raíz encontrada es: {raiz} en {total_iter} iteraciones.")
        x_plot = np.linspace(x_min, x_max, 400)
        y_plot = f(x_plot)
        plt.figure(figsize=(8, 6))
        plt.plot(x_plot, y_plot, label="f(x)")
        plt.axhline(0, color="black", linewidth=0.5)
        plt.plot(raiz, f(raiz), "ro", label="Raíz encontrada")
        plt.title("Método de Bisección")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.show()
