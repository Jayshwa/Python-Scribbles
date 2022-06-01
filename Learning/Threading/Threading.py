import threading
import time

x = 1892

"""Create a lock that is acquired (lock.acquire()) by each
thread that prevents access to other threads
untill it is released (lock.release()) after the thread
has finished running.

"""
lock = threading.Lock()

"""Create a limit on how many threads can access the resource
at a single time.
"""
semaphore = threading.BoundedSemaphore(value=5)


def double():
    global x, lock
    """Lock the variable so other threads cannot access
    """
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached the maximum")
    """Release the lock when the function has completed
    """
    lock.release()


def half():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the minimum")
    lock.release()


def access(thread):
    print(f"{thread} is trying to access")
    semaphore.acquire()
    print(f"{thread} was granted access")
    time.sleep(5)
    print(f"{thread} is now releasing")
    semaphore.release()


double_thread = threading.Thread(target=double)
halving_thread = threading.Thread(target=half)

double_thread.start()
halving_thread.start()
