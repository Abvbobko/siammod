from graph import QueueingSystem
from evaluator import math_expectation
import generator as gen

import matplotlib.pyplot as plt

if __name__ == '__main__':
    num_of_times = 1000000  # int(input("Enter size of one thread: "))
    queue_size = int(input("Enter queue size: "))  # 1
    lmbd = float(input("Enter λ: "))  # 4
    u1 = float(input("Enter μ1: "))  # 2
    u2 = float(input("Enter μ2: "))  # 2
    p = float(input("Enter p: "))  # 0.6

    queueing_system = QueueingSystem(lmbd=lmbd, u1=u1, u2=u2, p=p, queue_size=queue_size)
    source_thread = gen.create_time_thread(num_of_times, lmbd=lmbd, label='l')
    service_line_1_thread = gen.create_time_thread(num_of_times, lmbd=u1, label='u1')
    service_line_2_thread = gen.create_time_thread(num_of_times, lmbd=u2, label='u2')

    thread = gen.combiner([source_thread, service_line_1_thread, service_line_2_thread])

    for t in thread:
        # print(t[1])
        queueing_system.tact(t[1])

    num_of_1 = queueing_system.request_1_processed() + queueing_system.request_1_rejected()
    if num_of_1 != 0:
        p_rej_1 = queueing_system.request_1_rejected() / num_of_1
        print("Pотк1: ", p_rej_1)
    else:
        print("Requests 1 were not generated.")

    num_of_2 = queueing_system.request_2_processed() + queueing_system.request_2_rejected()
    if num_of_2 != 0:
        p_rej_2 = queueing_system.request_2_rejected() / num_of_2
        print("Pотк2: ", p_rej_2)
    else:
        print("Requests 2 were not generated.")

    # for k in queueing_system.states:
    #     print(f'{k}: {queueing_system.states[k]/len(thread)}')

