# Author: Ryan Wigglesworth

# This class exists as an abstraction for launching workqueue
# Workers through a python interpreter
import os

class Worker:
    ''' simple class to provide an abstraction over launching workers '''
        
    def add_worker(self, machine_name, port):
        os.system(f'work_queue_worker {machine_name} {port}')