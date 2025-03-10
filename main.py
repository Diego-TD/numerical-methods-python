import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def input_int():
    while True:
        try:
            n = int(input("Ingrese el grado deseado (número entero): "))
            if n < 0:
                print("El grado debe ser un número entero no negativo.")
                continue
            return n
        except ValueError:
            print("Por favor, ingrese un número entero válido.")


def main():
    n = input_int()

    x = sp.symbols('x')
    fx = (x + 1) ** (-sp.Rational(1, 2))

    maclaurin_poly = 0
    for i in range(n + 1):
        derivative = sp.diff(fx, x, i)
        term = derivative.subs(x, 0) / sp.factorial(i) * x ** i
        maclaurin_poly += term

    maclaurin_poly = sp.simplify(maclaurin_poly)

    print("\nPolinomio de Maclaurin de grado", n, ":")
    sp.pprint(maclaurin_poly)

    poly_func = sp.lambdify(x, maclaurin_poly, modules=['numpy'])

    x_vals = np.linspace(-3, 2, 400)
    y_vals = poly_func(x_vals)

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'Polinomio de Maclaurin (grado {n})', color='blue')
    plt.xlim(-3, 2)
    plt.ylim(0, 7)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Polinomio de Maclaurin de $(x+1)^{-1/2}$')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()

