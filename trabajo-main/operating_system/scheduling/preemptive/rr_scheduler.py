from utilities.queue import Queue

from hardware.irq import IRQ

from operating_system.pcb import *
from operating_system.scheduling.preemptive.preemptive_scheduler import PreemptiveSchedulerAlgorithm

class RRSchedulingAlgorithm(PreemptiveSchedulerAlgorithm):
    """ Implementation of Round Robin Scheduling Algorithm. """

    # TODO (5) Complete the class

    def __init__(self, kernel, quantum):
        super().__init__(kernel, quantum)

        self.__ready_queue = Queue()
        self.__currently_running = None
        self.__remaining_ticks = 0
        HARDWARE.clock.add_subscriber(self)


    def tick(self, tick_num):
        if(self.__remaining_ticks < self.quantum()):
            self.__remaining_ticks += 1

        else:
            self.__remaining_ticks = 0
            IRQ.SWAP()


    @property
    def next_process_id(self):
        self.__ready_queue.front

    
    def move_to_waiting(self, pid, pcb):
        self.__currently_running = None


    
    def move_to_ready(self, pid, pcb):
        self.__ready_queue.enqueue(pid)


    
    def move_to_running(self, pid, pcb):
        self.__currently_running = self.__ready_queue.dequeue
        self.__ready_queue.dequeue


        
 
    def __repr__(self):
        return str(self.__ready_queue)
        
