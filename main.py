from graph import QueueingSystem
from evaluator import math_expectation

if __name__ == '__main__':
    num_of_tacts = int(input("Enter number of tacts: "))
    queue_size = int(input("Enter queue size: "))
    ro = float(input("Enter ρ: "))
    p1 = float(input("Enter π1: "))
    p2 = float(input("Enter π2: "))
    queueing_system = QueueingSystem(p1=p1, p2=p2, ro=ro, queue_size=queue_size)

    tact_number = 0
    true_serviced = 0
    lmbd = 0
    queue_sizes = []
    requests_in_system = []
    queue_times = []
    system_times = []
    line_1_busy = 0
    line_2_busy = 0

    num_of_rejected = 0

    for i in range(num_of_tacts):
        queueing_system.tact()
        status, request, num_of_serviced, rejected, time_in_queue, time_in_system = queueing_system.get_last_tact_log()

        print(status, num_of_serviced)

        lmbd += request
        true_serviced += num_of_serviced
        queue_sizes.append(int(status[0]))

        queue_times += time_in_queue
        system_times += time_in_system

        requests_in_system.append(int(status[0]) + int(status[1]) + int(status[2]))

        if int(status[1]) == 1:
            line_1_busy += 1
        if int(status[2]) == 1:
            line_2_busy += 1

        if rejected:
            num_of_rejected += 1

    A = true_serviced / num_of_tacts
    lmbd /= num_of_tacts
    P_rej = num_of_rejected / num_of_tacts
    Q = 1 - P_rej
    L_queue = math_expectation(queue_sizes)
    L_system = math_expectation(requests_in_system)
    W_queue = math_expectation(queue_times)
    W_system = math_expectation(system_times)

    print("A:", A)
    print("lambda:", lmbd)
    print("Q:", Q)
    print("Pотк:", P_rej)
    print("Lоч:", L_queue)
    print("Lc:", L_system)
    print("Wоч:", L_queue / A)
    print("Wс:", W_system)
    print("K_кан1:", line_1_busy / num_of_tacts)
    print("K_кан2:", line_2_busy / num_of_tacts)
