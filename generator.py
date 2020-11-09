import numpy as np


def generate_thread(num_of_times, lmbd):
    t = np.random.exponential(1/lmbd, num_of_times)
    t.sort()
    return t





if __name__ == '__main__':
    a = np.random.exponential(1/4, 10)
    a.sort()
    print(a)
