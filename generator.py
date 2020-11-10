import numpy as np


def generate_thread(num_of_times, lmbd):
    return list(np.random.exponential(1/lmbd, num_of_times))


def thread_to_timeline(thread):
    result_thread = thread
    if len(thread) > 1:
        result_thread = [thread[0]]
        for i in range(1, len(thread)):
            result_thread.append(thread[i] + result_thread[i-1])
    return result_thread


def add_label(thread, label):
    result_thread = []
    for t in thread:
        result_thread.append((t, label))
    return result_thread


def combiner(threads):
    thread = []
    for t in threads:
        thread += t
    thread.sort(key=lambda x: x[0])
    return thread


def create_time_thread(thread_size, lmbd, label):
    return add_label(
        thread_to_timeline(
            generate_thread(num_of_times=thread_size, lmbd=lmbd)
        ),
        label=label
    )


if __name__ == '__main__':
    a = np.random.exponential(1/4, 10)
    a.sort()
    print(a)

    print(combiner([[(3, 2)], [(4, 1)]]))
