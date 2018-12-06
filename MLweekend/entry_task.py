import numpy as np
import requests
import pylab as plt

URL = 'http://165.227.157.145:8080/api/do_measurement?x={}'
FILENAME = 'results.npy'


def get_value(x):
    """ get one value from API """
    return requests.get(URL.format(x)).json()['data']['y']


def measure_point(x, measures=20, show_hist=False):
    """
    get estimation of y from multiple measurements

    :param x: x
    :param measures: number of measures
    :param show_hist: plot histogram
    :return: return mean and standard deviation of y measurements
    """
    values = []
    for _ in range(measures):
        value = get_value(x)
        if value is None:
            return None, None
        values.append(value)

    values = np.array(values)

    if show_hist:
        plt.hist(values)
        plt.title('mean: {:.2f}, std: {:.2f}'.format(values.mean(), values.std()))

    return values.mean(), values.std()


def get_insight(start=-10, stop=10, step=1.):
    """ plot approx. function in given range """
    xs = np.arange(start, stop, step)
    ys = [get_value(x) for x in xs]

    plt.plot(xs, ys, '.')


def measure(start=-5, stop=5, step=0.1, measures=20):
    """ measure function in given range and results save to file """
    results = []

    for x in np.arange(start, stop, step):
        mean, std = measure_point(x, measures)
        if mean is None:
            continue
        print(x, mean)
        results.append([x, mean, std])

    print(np.array(results))
    np.save(FILENAME, results)


def polynomial_fit(n, plot=None, round=None):
    """ load results saved in file and fit polynomial

    :param n: polynomial degree
    :param plot: x, y limits to plot
    :param round: number of decimals to round coefficients
    :return:
    """

    # load data
    results = np.load(FILENAME).T
    xs = results[0]
    ys = results[1]

    # fit polynomial
    coefficients, residuals, _, _, _ = np.polyfit(xs, ys, n, full=True)
    if round is not None:
        # round polynomial coefficients
        coefficients = np.round(coefficients, round)
    p = np.poly1d(coefficients)

    if plot is not None:
        # plot measured means and stds
        plt.errorbar(xs, ys, yerr=results[2], fmt='.r')
        # plot fitted polynomial
        xs = np.arange(xs[0], xs[-1], xs[1] - xs[0])
        plt.plot(xs, [p(x) for x in xs], '-b')
        if type(plot) != bool:
            plt.xlim(plot[0])
            plt.ylim(plot[1])

        print(p)
        print(residuals[0])

    return coefficients, residuals[0]


def find_best_n(maximal=20):
    """
    'elbow method'
    plot residuals from polynomial fit for different n
    """
    ns = range(0, maximal + 1, 2)
    residuals = []
    for n in ns:
        residuals.append(polynomial_fit(n)[1])

    plt.plot(ns, residuals)


def study_std(n=2):
    """ just try to find hidden pattern behind standard deviations """
    plt.figure()
    results = np.load(FILENAME).T
    xs = results[0]
    stds = results[2]
    coefficients = np.polyfit(xs, stds, n)
    p = np.poly1d(coefficients)

    plt.plot(xs, stds, '.r')
    xs = np.arange(xs[0], xs[-1], xs[1] - xs[0])
    plt.plot(xs, [p(x) for x in xs], '-b')

    print(p)

# how measures look like for one value? -> a normal distribution
# measure(-3, 100, show_hist=True)

# how whole function look like? -> a polynomial with even degree
# get_insight(-4, 4, 0.2)
# get_insight(-10, 10, 1)
# get_insight(-100, 100, 5)

# measurement of whole function
# measure()

# try to fit different polynomials -> n = 4 seems to be good
# polynomial_fit(4, plot=True)
# polynomial_fit(6, plot=True)

# try degrees systematically just to be sure
# find_best_n(10)

# we expect the result to be nice, so we round it little bit
polynomial_fit(4, plot=((-3, 3), (-25, 20)), round=1)

# how stds looks like? -> a quadratic relationship with x?
study_std()


plt.show()
