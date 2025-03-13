import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def solve_secant_method(fx, x0, x1, desired_relative_error):
    iteration = 1
    current_relative_error = 100

    x = sp.symbols('x')
    x_prev= x0
    x_next = x1

    try:
        f_x_prev = fx.evalf(subs={x: x0})
        f_x_next = fx.evalf(subs={x: x1})
    except Exception as e:
        print("Error evaluating fx0 at x0:", e)
        return -1

    root = x_next - ((f_x_next * (x_next - x_prev)) / (f_x_next - f_x_prev))
    x_prev = x_next
    x_next = root

    while current_relative_error > desired_relative_error:
        iteration += 1

        try:
            f_x_prev = fx.evalf(subs={x: x_prev})
            f_x_next = fx.evalf(subs={x: x_next})
        except Exception as e:
            print("Error evaluating fx", e)
            return -1

        # root
        root = x_next - ((f_x_next * (x_next-x_prev))/(f_x_next-f_x_prev))

        try:
            current_relative_error = abs((root - x_next) / root)
        except Exception as e:
            print("Error calculating relative error:", e)
            break

        print("Iteration: {}\nRelative error: {}\nRoot: {}\n".format(iteration, current_relative_error, root))

        x_prev = x_next
        x_next = root





def secant_method():
    x = sp.symbols('x')
    try:
        fx_input = input("Secant method :)\n"
                         "Please input a function in terms of x to start:\n")
        fx = sp.sympify(fx_input) # e.g. x**3 - 6*x**2 + 11*x-6.1
    except Exception as e:
        print("Error parsing function f(x):", e)
        return

    print("f(x) =", fx)

    # Create a numerical function from the sympy expression
    f_num = sp.lambdify(x, fx, 'numpy')

    # Generate x values for plotting
    x_vals = np.linspace(-5, 5, 400)
    y_vals = f_num(x_vals)

    plt.figure()
    plt.plot(x_vals, y_vals)
    plt.ylim(-5, 5)  # Set y-axis limits
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Secant Method Function Plot')
    plt.grid(True)
    plt.show()

    try:
        x0 = float(input("\n\nInput the value of X0 based on the plotted graph.\n")) #e.g. 2.5
    except ValueError:
        print("Invalid input for initial x. Please enter a numeric value.")
        return

    try:
        x1 = float(input("\n\nInput the value of X1 based on the plotted graph.\n"))  #e.g. 3.5
    except ValueError:
        print("Invalid input for initial x. Please enter a numeric value.")
        return

    try:
        desired_relative_error = float(input("\n\nInput a desired relative error in decimals (eg: 0.01 for 1%):")) # 0.01
    except ValueError:
        print("Invalid input for desired relative error. Please enter a numeric value.")
        return

    solve_secant_method(fx, x0, x1, desired_relative_error)


if __name__ == "__main__":
    try:
        secant_method()
    except Exception as e:
        print("An unexpected error occurred:", e)