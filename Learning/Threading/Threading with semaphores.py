import threading
import time

x = 1892

"""Create a limit on how many threads can access the resource
at a single time.
"""
semaphore = threading.BoundedSemaphore(value=5)


def access(thread):
    print(f"{thread} is trying to access")
    semaphore.acquire()
    print(f"{thread} was granted access")
    time.sleep(5)
    print(f"{thread} is now releasing")
    semaphore.release()


for thread in range(1, 11):
    """
    (args=) is how paramaters are passed into the
    (target=) function.
    """
    t = threading.Thread(
        target=access,
        args=(thread,)
    )
    t.start()
    time.sleep(1)
