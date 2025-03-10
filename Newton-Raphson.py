import sympy as sp

def solve_newton_raphson(fx, initial_x, desired_relative_error):
    iteration = 1
    current_relative_error = 100

    x = sp.symbols('x')

    try:
        f_x = fx.evalf(subs={x: initial_x})
        f_x_diff = sp.diff(fx, x).evalf(subs={x: initial_x})
    except Exception as e:
        print("Error evaluating fx at initial_x:", e)
        return -1

    x_prev = initial_x - (f_x/f_x_diff)

    while current_relative_error > desired_relative_error:
        iteration += 1

        try:
            f_x = fx.evalf(subs={x: x_prev})
            f_x_diff = sp.diff(fx, x).evalf(subs={
                x: x_prev})
        except Exception as e:
            print("Error evaluating fx fx':", e)
            return -1

        x_n = x_prev - (f_x/f_x_diff)

        if x_n == 0:
            print("x n = 0")
            break



        try:
            current_relative_error = abs((x_n - x_prev) / x_n)
        except Exception as e:
            print("Error calculating relative error:", e)
            break

        print("Iteration: {}\nRelative error: {}\nRoot: {}\n".format(iteration, current_relative_error, x_n))

        x_prev = x_n






def newton_raphson():
    x = sp.symbols('x')
    try:
        fx_input = input("Newton Raphson method :)\n"
                         "Please input a function in terms of x to start:\n")
        fx = sp.sympify(fx_input)
    except Exception as e:
        print("Error parsing function f(x):", e)
        return

    print("f(x) =", fx)
    sp.plot(fx, (x, -1, 1))

    try:
        initial_x = float(input("\n\nInput the value on X based on the plotted graph.\n"))
    except ValueError:
        print("Invalid input for initial x. Please enter a numeric value.")
        return

    try:
        desired_relative_error = float(input("\n\nInput a desired relative error in decimals (eg: 0.01 for 1%):"))
    except ValueError:
        print("Invalid input for desired relative error. Please enter a numeric value.")
        return

    solve_newton_raphson(fx, initial_x, desired_relative_error)


if __name__ == "__main__":
    try:
        newton_raphson()
    except Exception as e:
        print("An unexpected error occurred:", e)