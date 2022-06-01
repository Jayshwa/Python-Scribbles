import threading
import time

x = 1892

"""Create a lock that is acquired (lock.acquire()) by each
thread that prevents access to other threads
untill it is released (lock.release()) after the thread
has finished running.

"""
lock = threading.Lock()


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


double_thread = threading.Thread(target=double)
halving_thread = threading.Thread(target=half)

double_thread.start()
halving_thread.start()
