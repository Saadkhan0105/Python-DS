'''
Multithreading in Python allows you to run multiple threads (smaller units of a process) concurrently within a single process. This is particularly useful for I/O-bound tasks, such as web scraping, file handling, or network operations, where threads can operate independently without waiting for each other to complete.

Q. When to use Multithreading?
- When tasks are I/O-bound and can be performed concurrently.
- When you want to improve the responsiveness of applications, such as GUI applications.
- I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
- Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.
'''

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")
        
def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")
        

##create 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)

t=time.time()
## start the thread
t1.start()
t2.start()

### Wait for the threads to complete
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)
