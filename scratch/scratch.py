import matplotlib.pyplot as plt
import numpy as np

def setup_basic(title = None, xlabel = None, ylabel = None):
    """
    Sets up the basic 1x1 graph
    :return:
    """
    fig, ax = plt.subplots(1, 1)
    if title:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    return fig, ax

def line_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(np.asarray(data1), np.asarray(data2), **param_dict)
    return out

# plt.subplots(number graphs rows, number graphs cols)
fig, ax = setup_basic(title = 'Simple Plot', xlabel = 'X Label', ylabel = 'Y Label')
x = np.linspace(0, 2, 100)
line_plotter(ax, x, x, {'label':'linear'})
line_plotter(ax, x, x**2, {'label':'quadratic'})
line_plotter(ax, x, x**3, {'label':'cubic'})

ax.legend()