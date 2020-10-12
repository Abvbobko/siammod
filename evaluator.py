import matplotlib.pyplot as plt
import numpy as np


def hist(x, bins=20):
    # weights are for frequencies on Y-axis
    weights = np.ones_like(x) / len(x)
    plt.hist(x, bins=bins, ec='black', weights=weights)
    plt.plot([0, 1], [1/bins]*2, color='red')
    plt.show()


def math_expectation(x):
    return sum(x)/len(x)


def dispersion(x):
    n = len(x)
    m = math_expectation(x)
    return sum([(xi - m)**2 for xi in x])/(n-1)


def standard_deviation(x):
    return dispersion(x)**(1/2)


def indirect_signs_check(x):
    n = len(x) if (len(x) % 2 == 0) else (len(x) - 1)
    k = 0
    for i in range(0, n-1, 2):
        if x[i]**2 + x[i+1]**2 < 1:
            k += 1

    return 2*k/n


def find_parameters(lower_limit=50000):
    a = 3
    m = 5
    R0 = 1
    offset = 9
    coef = 10
    period = generator.lehmer(a, m, R0)[1]
    iteration = 1_000
    while (period < lower_limit) and (iteration != 0):
        a = a*coef + offset
        m = m*coef + offset
        R0 = R0*coef + offset
        period = generator.lehmer(a, m, R0)[1]
        iteration -= 1

    return a, m, R0

