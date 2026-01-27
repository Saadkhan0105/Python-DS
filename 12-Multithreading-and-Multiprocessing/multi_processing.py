'''
Multiprocessing in Python allows you to run multiple processes concurrently, each with its own Python interpreter and memory space. This is particularly useful for CPU-bound tasks, such as data processing, mathematical computations, or any task that requires significant CPU resources.
Q. When to use Multiprocessing?
- When tasks are CPU-bound and require parallel execution to improve performance.
- When you want to bypass the Global Interpreter Lock (GIL) in Python, which can limit the performance of multithreaded applications.
- CPU-bound tasks: Tasks that require significant CPU resources and spend more time performing computations.
- Parallel execution: When you want to fully utilize multiple CPU cores for better performance.
'''

import multiprocessing

import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i * i * i}")

if __name__=="__main__":

    ## create 2 processes
    p1=multiprocessing.Process(target=square_numbers)
    p2=multiprocessing.Process(target=cube_numbers)
    t=time.time()

    ## start the process
    p1.start()
    p2.start()

    ## Wait for the process to complete
    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)