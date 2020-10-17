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
    line_1_busy = 0
    line_2_busy = 0
    d = {
        "000": 0,
        "001": 0,
        "010": 0,
        "011": 0,
        "111": 0,
        "211": 0,
    }

    for i in range(num_of_tacts):
        status, is_serviced, is_new_request = queueing_system.tact()
        print(status, is_serviced)
        requests_in_system.append(int(status[0]) + int(status[1]) + int(status[2]))
        d[status] += 1
        if int(status[1]) == 1:
            line_1_busy += 1
        if int(status[2]) == 1:
            line_2_busy += 1
        queue_sizes.append(int(status[0]))
        if is_serviced:
            true_serviced += 1
        lmbd += is_new_request

    A = true_serviced/num_of_tacts
    print("A:", A)
    lmbd = lmbd/num_of_tacts
    print("lambda:", lmbd)
    Q = A/lmbd
    print("Q:", Q)
    print("Pотк:", 1-Q)
    L_queue = math_expectation(queue_sizes)
    print("Lоч:", L_queue)
    L_s = math_expectation(requests_in_system)
    print("Lc:", L_s)
    print("Wоч:", L_queue/A)
    print("Wс:", L_s / A)
    print("K_кан1:", line_1_busy / num_of_tacts)
    print("K_кан2:", line_2_busy / num_of_tacts)

    for k in d:
        print(k, d[k]/num_of_tacts)
