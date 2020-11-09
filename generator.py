import numpy as np


def generate_thread(num_of_times, lmbd, label):
    t = list(np.random.exponential(1/lmbd, num_of_times))
    t.sort()
    thread = []
    for item in t:
        thread.append((item, label))
    return thread


def combiner(threads):
    thread = []
    for t in threads:
        thread += t
    thread.sort(key=lambda x: x[0])
    return thread


if __name__ == '__main__':
    a = np.random.exponential(1/4, 10)
    a.sort()
    print(a)

    print(combiner([[(3, 2)], [(4, 1)]]))
