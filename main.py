from graph import QueueingSystem
from evaluator import math_expectation
import generator

if __name__ == '__main__':
    num_of_times = int(input("Enter size of one thread: ")) # ToDO: Заменить на размер одного потока
    queue_size = int(input("Enter queue size: ")) # ToDo: размер очереди с приоритетами?
    lmbd = float(input("Enter λ: "))
    u1 = float(input("Enter μ1: "))
    u2 = float(input("Enter μ2: "))
    p = float(input("Enter p: "))
    queueing_system = QueueingSystem(lmbd=lmbd, u1=u1, u2=u2, p=p, queue_size=queue_size)
    source_thread = generator.generate_thread(num_of_times=num_of_times, lmbd=lmbd, label='l')
    service_line_1_thread = generator.generate_thread(num_of_times=num_of_times, lmbd=u1, label='u1')
    service_line_2_thread = generator.generate_thread(num_of_times=num_of_times, lmbd=u2, label='u2')

    thread = generator.combiner([source_thread, service_line_1_thread, service_line_2_thread])
    for t in thread:
        queueing_system.tact(t[1])

    p_rej_1 = queueing_system.request_1_rejected()/(
                queueing_system.request_1_processed()+queueing_system.request_1_rejected()
    )

    p_rej_2 = queueing_system.request_2_rejected() / (
            queueing_system.request_2_processed() + queueing_system.request_2_rejected()
    )

    print("Pотк1: ", p_rej_1)
    print("Pотк2: ", p_rej_2)
