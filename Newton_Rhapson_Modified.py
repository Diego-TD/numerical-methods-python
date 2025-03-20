# x = sp.Symbol('x')
# fx = sp.sympify(input("Function:"))
# print(fx)
# print(sp.factor(fx))
# # x**3 - 5*x**2 + 7*x - 3


import sympy as sp

def solve_newton_raphson_modifed(fx, initial_x, desired_relative_error):
    iteration = 1
    current_relative_error = 100

    x = sp.symbols('x')

    try:
        f_x_eval = fx.evalf(subs={x: initial_x})
        f_x_diff = sp.diff(fx, x)
        f_x_diff_eval = f_x_diff.evalf(subs={x: initial_x})
        f_x_second_diff = sp.diff(f_x_diff, x)
        f_x_second_diff_eval = f_x_second_diff.evalf(subs={x: initial_x})

        if f_x_eval == 0 or f_x_diff_eval == 0 or f_x_second_diff_eval == 0:
            print("Evaluation at fx or f'x or f''x equals 0")
            return -1

        x_prev = initial_x - ((f_x_eval * f_x_diff_eval )/( f_x_diff_eval ** 2 - f_x_eval * f_x_second_diff_eval))
        print("iteration: {}\nroot: {}\n".format(iteration,x_prev))

    except Exception as e:
        print("Error in first iteration", e)
        return -1


    while current_relative_error > desired_relative_error:
        iteration += 1

        try:
            f_x_eval = fx.evalf(subs={x: x_prev})
            f_x_diff_eval = f_x_diff.evalf(subs={x: x_prev})
            f_x_second_diff_eval = f_x_second_diff.evalf(subs={x: x_prev})

        except Exception as e:
            print("Error in evaluating in previous x value", e)
            return -1

        x_n = x_prev - ((f_x_eval * f_x_diff_eval) / (f_x_diff_eval ** 2 - f_x_eval * f_x_second_diff_eval))

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



def newton_raphson_modified():
    x = sp.symbols('x')
    try:
        fx_input = input("Newton Raphson method modified:)\n"
                         "Please input a function in terms of x to start:\n")
        fx = sp.sympify(fx_input)
    except Exception as e:
        print("Error parsing function f(x):", e)
        return

    print("f(x) =", fx)
    print(sp.factor(fx))
    sp.plot(fx, (x, -10, 10))

    try:
        initial_x = float(input("\n\nInput the value on X.\n"))
    except ValueError:
        print("Invalid input for initial x. Please enter a numeric value.")
        return

    try:
        desired_relative_error = float(input("\n\nInput a desired relative error in decimals (eg: 0.01 for 1%):"))
    except ValueError:
        print("Invalid input for desired relative error. Please enter a numeric value.")
        return

    solve_newton_raphson_modifed(fx, initial_x, desired_relative_error)


if __name__ == "__main__":
    try:
        newton_raphson_modified()
    except Exception as e:
        print("An unexpected error occurred:", e)