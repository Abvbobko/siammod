from graph import QueueingSystem

if __name__ == '__main__':
    queue_size = int(input("Enter queue size: "))
    ro = float(input("Enter ρ: "))
    p1 = float(input("Enter π1: "))
    p2 = float(input("Enter π2: "))
    queueing_system = QueueingSystem(p1=p1, p2=p2, ro=ro, queue_size=queue_size)
    for i in range(100):
        print(queueing_system.tact())


#
# ERROR есть статусы 100, а таких быть не должно
# Причина: не очищается очередь нигда (не удаляется из нее элемент)
#
#