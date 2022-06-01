import threading

"""Events are created through instantiating the
Event() class in threading.
Events() can then be listened for and reacted to.
"""
event = threading.Event()


def event_fn():
    print("Waiting for event to trigger...\n")
    event.wait()
    print("Executing event(fn) after event.wait()")


t1 = threading.Thread(target=event_fn)
t1.start()

x = input("Do you want to trigger the event? (y/n)\n")
if x == "y":
    event.set()
