import numpy as np
import sympy as sp

def solve_fixed_point(initial_x, desired_relative_error, gx):
    iteration = 1
    current_relative_error = 100

    try:
        g_x_prev = gx(initial_x)
    except Exception as e:
        print("Error evaluating gx at initial_x:", e)
        return -1

    g_x = 0
    safe_counter = 0
    safe_error_start = current_relative_error
    user_input_continue_or_not = 0

    while current_relative_error > desired_relative_error:
        iteration += 1
        safe_counter += 1

        try:
            g_x = gx(g_x_prev)
        except Exception as e:
            print("Error evaluating gx during iteration:", e)
            break

        if g_x == 0:
            print("g(x) evaluated to zero, stopping iteration to avoid division by zero.")
            break

        try:
            current_relative_error = abs((g_x - g_x_prev) / g_x)
        except Exception as e:
            print("Error calculating relative error:", e)
            break

        print("Iteration: {}\nRelative error: {}\nRoot: {}\n".format(iteration, current_relative_error, g_x))

        g_x_prev = g_x

        if safe_counter >= 10:
            # If error did not decrease (or even increased) relative to the start of the window,
            # or if it's become invalid (nan), then prompt the user.
            if current_relative_error >= safe_error_start or np.isnan(current_relative_error):
                calculating_input = input(
                    "\n\nAfter {} iterations, with the provided x=g(x) function, the relative error doesn't seem to be reducing. "
                    "Would you like to change either the initial x value or the x=g(x) function?\n"
                    "0: exit\n"
                    "1: Continue\n"
                    "2: Change Xo\n"
                    "3: Change x=g(x)\n".format(iteration))
                if calculating_input not in ["0", "1", "2", "3"]:
                    print("Invalid choice, continuing with iterations.")
                elif calculating_input == "0":
                    return 0
                elif calculating_input == "1":
                    pass
                elif calculating_input == "2":
                    return 2
                elif calculating_input == "3":
                    return 3

            safe_counter = 0
            safe_error_start = current_relative_error

    if user_input_continue_or_not == 0:
        print("\n\nRoot found: {} with {} relative error after {} iterations".format(g_x, current_relative_error, iteration))
    return user_input_continue_or_not


def fixed_point():
    x = sp.symbols('x')
    try:
        fx_input = input("Welcome to my lab, today we are going to do some delicious fixed point experiments :)\n"
                         "Please input a function in terms of x to start:\n")
        fx = sp.sympify(fx_input)
    except Exception as e:
        print("Error parsing function f(x):", e)
        return

    print("f(x) =", fx)
    # Plot over a more focused range to better visualize the function.
    sp.plot(fx, (x, -1, 1))

    try:
        initial_x = float(input("\n\nNow input the value on X based on the plotted graph.\n"
                                  "Tip: You want to input a value near the point the graph looks like touching the X axis:"))
    except ValueError:
        print("Invalid input for initial x. Please enter a numeric value.")
        return

    try:
        desired_relative_error = float(input("\n\nNow input a desired relative error in decimals (eg: 0.01 for 1%):"))
    except ValueError:
        print("Invalid input for desired relative error. Please enter a numeric value.")
        return

    try:
        gx_input = input("\n\nNow input the x = g(x) function derived from f(x):")
        gx_expr = sp.sympify(gx_input)
    except Exception as e:
        print("Error parsing function g(x):", e)
        return

    #Convert the symbolic expression gx_expr into a callable function
    try:
        gx_func = sp.lambdify(x, gx_expr, modules=['numpy'])
    except Exception as e:
        print("Error converting g(x) to a callable function:", e)
        return

    print("Calculating..")
    output = solve_fixed_point(initial_x, desired_relative_error, gx_func)

    flag = True
    while flag:
        if output == 0:
            print("Good bye my friend")
            flag = False
        elif output == 2:
            print("Changing initial x (Xo)")
            sp.plot(fx, (x, -1, 1))
            try:
                new_initial_x = float(input("\n\nNow input the new value on X based on the plotted graph.\n"
                                            "Tip: You want to input a value near the point the graph looks like touching the X axis:"))
            except ValueError:
                print("Invalid input for new initial x. Exiting.")
                return
            output = solve_fixed_point(new_initial_x, desired_relative_error, gx_func)
        elif output == 3:
            print("Changing x = g(x)\n")
            new_gx_input = input("Input the new x = g(x) function derived from f(x) for {}:\n".format(gx_expr))
            try:
                new_gx_expr = sp.sympify(new_gx_input)
                gx_func = sp.lambdify(x, new_gx_expr, modules=['numpy'])
            except Exception as e:
                print("Error parsing or converting new g(x):", e)
                return
            output = solve_fixed_point(initial_x, desired_relative_error, gx_func)
        else:
            flag = False

if __name__ == "__main__":
    try:
        fixed_point()
    except Exception as e:
        print("An unexpected error occurred:", e)
