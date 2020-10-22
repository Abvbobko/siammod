import random


class Request:
    def __init__(self):
        self.time = 0

    def tact(self):
        self.time += 1


class ServiceLine:
    def __init__(self):
        # self.free_status = 0
        self.request = None

    def give_work(self, request):
        # self.free_status = 1
        if not self.request:
            self.request = request
        else:
            raise Exception("Service line is busy!")

    def free(self):
        self.request = None
        # self.free_status = 0

    def get_status(self):
        if self.request:
            return 1
        return 0

    def tact(self):
        if self.request:
            self.request.tact()


class Queue:
    def __init__(self, size):
        self.max_size = size
        self.queue = []

    def push(self, request):
        if len(self.queue) < self.max_size:
            self.queue = [request] + self.queue
            return True
        return False

    def pop(self):
        return self.queue.pop()

    def get_current_size(self):
        return len(self.queue)

    def tact(self):
        for request in self.queue:
            request.tact()


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

    @staticmethod
    def get_service_lines_statuses(service_lines):
        return [service_line.get_status() for service_line in service_lines]

    def tact(self):
        request = self.source()
        num_of_serviced = 0
        is_rejected = False
        sl_1_status, sl_2_status = self.get_service_lines_statuses([self.service_line_1, self.service_line_2])
        # sl_1_status = self.service_line_1.get_status()
        # sl_2_status = self.service_line_2.get_status()
        self.queue.tact()
        self.service_line_1.tact()
        self.service_line_2.tact()
        if sl_1_status == 1 and self.event(1 - self.p1):
            self.service_line_1.free()
            sl_1_status = 0
            num_of_serviced += 1

        if sl_2_status == 1 and self.event(1 - self.p2):
            self.service_line_2.free()
            sl_2_status = 0
            num_of_serviced += 1

        queue_size = self.queue.get_current_size()
        if queue_size == 0:
            pass
        elif queue_size == 1:
            if sl_1_status == 0:
                self.service_line_1.give_work(self.queue.pop())
                sl_1_status = 1
            elif sl_2_status == 0:
                self.service_line_2.give_work(self.queue.pop())
                sl_2_status = 1
        elif queue_size == 2:
            if sl_1_status == 0:
                self.service_line_1.give_work(self.queue.pop())
                sl_1_status = 1
            if sl_2_status == 0:
                self.service_line_2.give_work(self.queue.pop())
                sl_2_status = 1

        if request:
            if sl_1_status == 0:
                self.service_line_1.give_work(request)
                # is_request_serviced = True
                sl_1_status = 1
            elif sl_2_status == 0:
                self.service_line_2.give_work(request)
                # is_request_serviced = True
                sl_2_status = 1
            elif not self.queue.push(request):
                is_rejected = True
                # is_request_serviced = True

        return (
            f'{self.queue.get_current_size()}{sl_1_status}{sl_2_status}',
            num_of_serviced,
            request,
            is_rejected
        )

    def source(self):
        if self.event(self.ro):
            return None
        return Request()
