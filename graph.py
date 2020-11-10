import random


class Request:
    def __init__(self, priority):
        self.type = priority

    def get_type(self):
        return self.type


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


class Queue:
    def __init__(self, size):
        self.max_size = size
        self.queue = []

    def push(self, request):
        if len(self.queue) < self.max_size:
            self.queue = [request] + self.queue
            return True

        for i in range(len(self.queue)):
            if request.get_type() < self.queue[i].get_type():
                rejected_request = self.queue[i]
                self.queue[i] = request
                return rejected_request
        return request

    def pop(self, priority):
        for i in range(len(self.queue)):
            if priority == self.queue[i].get_type():
                return self.queue.pop(i)

        return None

    def get_current_size(self):
        return len(self.queue)

    def type_of_item(self):
        if len(self.queue) > 0:
            return self.queue[0].get_type()
        return 0


class QueueingSystem:
    def __init__(self, lmbd, u1, u2, p, queue_size):
        self.lmbd = lmbd
        self.u1 = u1
        self.u2 = u2
        self.p = p
        self.queue = Queue(queue_size)
        self.service_line_1 = ServiceLine()
        self.service_line_2 = ServiceLine()
        self.processed_1 = 0
        self.processed_2 = 0
        self.rejected_1 = 0
        self.rejected_2 = 0

        self.num_of_1 = 0
        self.num_of_2 = 0

        self.states = {}
        # self.last_tact_info = None
        # self.request_number = 0

    @staticmethod
    def event(event_probability):
        n = random.uniform(0, 1)
        if n <= event_probability:
            return True
        return False

    @staticmethod
    def get_service_lines_statuses(service_lines):
        return [service_line.get_status() for service_line in service_lines]

    def tact(self, tact_event):
        # tact_event in ['l', 'u1', 'u2']
        # rejected_request_type = None
        sl_1_status, sl_2_status = self.get_service_lines_statuses([self.service_line_1, self.service_line_2])

        if tact_event == 'l':
            request = self.source()

            ##################################################
            if request.get_type() == 1:
                self.num_of_1 += 1
            elif request.get_type() == 2:
                self.num_of_2 += 1
            ##################################################

            if (request.get_type() == 1) and (sl_1_status == 0):
                self.service_line_1.give_work(request)
            elif (request.get_type() == 2) and (sl_2_status == 0):
                self.service_line_2.give_work(request)
            else:
                push_result = self.queue.push(request)
                if isinstance(push_result, Request):
                    rejected_request_type = push_result.get_type()
                    if rejected_request_type == 1:
                        self.rejected_1 += 1
                    elif rejected_request_type == 2:
                        self.rejected_2 += 1
        elif tact_event == 'u1':
            if sl_1_status == 1:
                self.processed_1 += 1
                self.service_line_1.free()
            request_from_queue = self.queue.pop(1)
            if request_from_queue:
                self.service_line_1.give_work(request_from_queue)
        elif tact_event == 'u2':
            if sl_2_status == 1:
                self.processed_2 += 1
                self.service_line_2.free()
            request_from_queue = self.queue.pop(2)
            if request_from_queue:
                self.service_line_2.give_work(request_from_queue)


        #####DEBUG###################################
        state = f'{self.queue.type_of_item()}{sl_1_status}{sl_2_status}'
        if state in self.states:
            self.states[state] += 1
        else:
            self.states[state] = 1
        ###############################################


    def request_1_processed(self):
        return self.processed_1

    def request_2_processed(self):
        return self.processed_2

    def request_1_rejected(self):
        return self.rejected_1

    def request_2_rejected(self):
        return self.rejected_2

    def source(self):
        if self.event(self.p):
            return Request(priority=1)
        return Request(priority=2)
