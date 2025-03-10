import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os

def false_position():
    print("hola")

    # Define function
    x = sp.symbols('x')
    fx_expr = 5*x**3 - 5* x**2 + 6*x -2
    f = sp.lambdify(x, fx_expr, 'numpy')

    # Compute the actual root using a numerical solver (for the root in our bracket)
    actual_root = sp.nsolve(fx_expr, 0)  # initial guess 0
    actual_root = float(actual_root)

    # plot function here to see how it looks
    sp.plot(fx_expr, (x, -3, 3), title="f(x) vs x", xlabel="x", ylabel="f(x)")

    # define relative error
    current_relative_e = 100
    desired_relative_e = 0.01

    # define xl and xu
    xl = -2.5
    xu = 2.5
    xr_old = None
    iteration = 0

    # Create folder and list to store frames for the animation
    temp_dir = "temp_frames"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    frame_files = []

    # Store iteration data in a list (iteration, xl, f(xl), xu, f(xu), xr, f(xr), f(xl)*f(xr), error)
    iter_data = []

    while current_relative_e > desired_relative_e:
        iteration += 1
        f_xl = f(xl)
        f_xu = f(xu)

        # Calculate xr using the false position formula:
        xr = xu - f_xu * (xl - xu) / (f_xl - f_xu)
        f_xr = f(xr)

        # Calculate relative error if this is not the first iteration
        if xr_old is not None:
            current_relative_e = abs((xr - xr_old) / xr) * 100

        # Save iteration data
        iter_data.append((iteration, xl, f_xl, xu, f_xu, xr, f_xr, f_xl * f_xr, current_relative_e))

        # Plot and save the frame for the current iteration
        x_vals = np.linspace(-3, 3, 400)
        y_vals = f(x_vals)
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, 'b-', label='f(x)')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(x=xl, color='green', linestyle='--', label='xl')
        plt.axvline(x=xu, color='red', linestyle='--', label='xu')
        # Plot a line connecting the points (xl, f(xl)) and (xu, f(xu))
        plt.plot([xl, xu], [f(xl), f(xu)], 'm--', label='Interval line')
        # Plot the actual root for comparison
        plt.axvline(x=actual_root, color='purple', linestyle='-.', label='actual root')
        plt.plot(xr, f_xr, 'ko', markersize=8, label='xr')
        plt.text(xl, f(xl), f' xl={xl:.3f}', color='green', verticalalignment='bottom')
        plt.text(xu, f(xu), f' xu={xu:.3f}', color='red', verticalalignment='bottom')
        plt.text(xr, f_xr, f' xr={xr:.3f}', color='black', verticalalignment='top')
        plt.title(f'Iteration {iteration}\nRelative Error: {current_relative_e:.4f}%')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend(loc='upper left')
        plt.xlim(-3, 3)
        plt.ylim(min(y_vals) - 1, max(y_vals) + 1)
        plt.grid(True)
        frame_path = os.path.join(temp_dir, f"frame_{iteration:02d}.png")
        plt.savefig(frame_path)
        plt.close()
        frame_files.append(frame_path)

        # Update the interval based on the sign of f(xl)*f(xr)
        if f_xl * f_xr < 0:
            xu = xr
        elif f_xl * f_xr > 0:
            xl = xr
        else:  # f(xr) is zero, found exact root
            current_relative_e = 0

        xr_old = xr

    # Print the iteration table
    header = ("Iteration", "xl", "f(xl)", "xu", "f(xu)", "xr", "f(xr)", "f(xl)*f(xr)", "Error (%)")
    print("{:>9s} | {:>8s} | {:>8s} | {:>8s} | {:>8s} | {:>8s} | {:>8s} | {:>14s} | {:>10s}".format(*header))

    for data in iter_data:
        print("{:9d} | {:8.4f} | {:8.4f} | {:8.4f} | {:8.4f} | {:8.4f} | {:8.4f} | {:14.4f} | {:10.4f}".format(*data))

    print("\nApproximate root:", xr)

    # Create animation GIF from frames
    images = []
    for file in frame_files:
        images.append(imageio.imread(file))
    gif_path = "false_position_animation.gif"
    imageio.mimsave(gif_path, images, duration=0.5)
    print("Animation saved as", gif_path)

    # Clean up temporary frame files
    for file in frame_files:
        os.remove(file)
    os.rmdir(temp_dir)



if __name__ == "__main__":
    false_position()