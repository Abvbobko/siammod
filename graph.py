import random


class Request:
    def __init__(self):
        self.time = 0

    def tact(self):
        self.time += 1

    def get_time(self):
        return self.time


class ServiceLine:
    def __init__(self):
        self.request = None

    def give_work(self, request):
        if not self.request:
            self.request = request
        else:
            raise Exception("Service line is busy!")

    def free(self):
        request = self.request
        self.request = None
        return request

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
        self.last_tact_info = None

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
        self.last_tact_info = {
            'status': 0,
            'request': 0,
            'num_of_serviced': 0,
            'is_rejected': False,
            'time_in_queue': [],
            'time_in_system': []
        }

        request = self.source()
        sl_1_status, sl_2_status = self.get_service_lines_statuses([self.service_line_1, self.service_line_2])
        self.queue.tact()
        self.service_line_1.tact()
        self.service_line_2.tact()

        # run service lines
        if sl_1_status == 1 and self.event(1 - self.p1):
            self.last_tact_info['time_in_system'].append(self.service_line_1.free().get_time())
            sl_1_status = 0
            self.last_tact_info['num_of_serviced'] += 1

        if sl_2_status == 1 and self.event(1 - self.p2):
            self.last_tact_info['time_in_system'].append(self.service_line_2.free().get_time())
            sl_2_status = 0
            self.last_tact_info['num_of_serviced'] += 1

        # run queue shift
        queue_size = self.queue.get_current_size()
        if queue_size == 1:
            if sl_1_status == 0:
                request_from_queue = self.queue.pop()
                self.last_tact_info['time_in_queue'].append(request_from_queue.get_time())
                self.service_line_1.give_work(request_from_queue)
                sl_1_status = 1
            elif sl_2_status == 0:
                request_from_queue = self.queue.pop()
                self.last_tact_info['time_in_queue'].append(request_from_queue.get_time())
                self.service_line_2.give_work(request_from_queue)
                sl_2_status = 1
        elif queue_size == 2:
            if sl_1_status == 0:
                request_from_queue = self.queue.pop()
                self.last_tact_info['time_in_queue'].append(request_from_queue.get_time())
                self.service_line_1.give_work(request_from_queue)
                sl_1_status = 1
            if sl_2_status == 0:
                request_from_queue = self.queue.pop()
                self.last_tact_info['time_in_queue'].append(request_from_queue.get_time())
                self.service_line_2.give_work(request_from_queue)
                sl_2_status = 1

        # process request
        if request:
            self.last_tact_info['request'] = 1
            if sl_1_status == 0:
                self.service_line_1.give_work(request)
                sl_1_status = 1
            elif sl_2_status == 0:
                self.service_line_2.give_work(request)
                sl_2_status = 1
            elif not self.queue.push(request):
                self.last_tact_info['is_rejected'] = True
        else:
            self.last_tact_info['request'] = 0

        self.last_tact_info['status'] = f'{self.queue.get_current_size()}{sl_1_status}{sl_2_status}'
        return self.last_tact_info['status']

    def get_last_tact_log(self):
        return (
            self.last_tact_info['status'],
            self.last_tact_info['request'],
            self.last_tact_info['num_of_serviced'],
            self.last_tact_info['is_rejected'],
            self.last_tact_info['time_in_queue'],
            self.last_tact_info['time_in_system']
        )

    def source(self):
        if self.event(self.ro):
            return None
        return Request()
