import matplotlib.pyplot as plt
import numpy as np

def plot_equation(equation_func, filename='plot.png'):
    x_vals = np.linspace(-10, 10, 400)
    y_vals = equation_func(x_vals)
    plt.plot(x_vals, y_vals)
    plt.axhline(0, color='black')
    plt.title('Graph')
    plt.grid(True)
    plt.savefig(filename)
    plt.close()
