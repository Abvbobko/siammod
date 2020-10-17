import random


class ServiceLine:
    def __init__(self):
        self.free_status = 0

    def give_work(self):
        self.free_status = 1

    def free(self):
        self.free_status = 0

    def get_status(self):
        return self.free_status


class Queue:
    def __init__(self, size):
        self.max_size = size
        self.queue = []

    def push(self):
        if len(self.queue) < self.max_size:
            self.queue = [1] + self.queue
            return True
        return False

    def pop(self):
        self.queue.pop()

    def has_free_cell(self):
        if len(self.queue) == self.max_size:
            return False
        return True

    def get_current_size(self):
        return len(self.queue)


class QueueingSystem:
    def __init__(self, ro, p1, p2, queue_size):
        self.ro = ro
        self.p1 = p1
        self.p2 = p2
        self.queue = Queue(queue_size)
        self.service_line_1 = ServiceLine()
        self.service_line_2 = ServiceLine()

    @staticmethod
    def event(event_probability):
        n = random.uniform(0, 1)
        if n <= event_probability:
            return True
        return False

    def tact(self):
        request = self.source()
        is_request_serviced = False
        sl_1_status = self.service_line_1.get_status()
        sl_2_status = self.service_line_1.get_status()
        if sl_1_status == 1 and self.event(1 - self.p1):
            self.service_line_1.free()
            sl_1_status = 0

        if sl_2_status == 1 and self.event(1 - self.p2):
            self.service_line_2.free()
            sl_2_status = 0

        queue_size = self.queue.get_current_size()
        if queue_size == 0:
            pass
        elif queue_size == 1:
            if sl_1_status == 0:
                self.service_line_1.give_work()
                sl_1_status = 1
                self.queue.pop()
            elif sl_2_status == 0:
                self.service_line_2.give_work()
                sl_2_status = 1
                self.queue.pop()
        elif queue_size == 2:
            if sl_1_status == 0:
                self.service_line_1.give_work()
                sl_1_status = 1
                self.queue.pop()
            if sl_2_status == 0:
                self.service_line_2.give_work()
                sl_2_status = 1
                self.queue.pop()

        if request == 1:
            if sl_1_status == 0:
                self.service_line_1.give_work()
                is_request_serviced = True
                sl_1_status = 1
            elif sl_2_status == 0:
                self.service_line_2.give_work()
                is_request_serviced = True
                sl_2_status = 1
            elif self.queue.push():
                is_request_serviced = True

        return (
            f'{self.queue.get_current_size()}{sl_1_status}{sl_2_status}',
            is_request_serviced,
            request
        )

    def source(self):
        if self.event(self.ro):
            return 0
        return 1
