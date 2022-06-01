import threading

"""Threads allow you to run multiple light-weight
functions at the same time.
"""


def function_one():
    beep = 0
    while beep != 20:
        beep += 1
        print(beep)


def function_two():
    boop = 100
    while boop != 200:
        boop += 10
        print(boop)


"""
Create a new thred by defining a variable.
Assign the variable to be an instance of the "Thread" class.
Target the function to be executed without calling the function.
"""
threadone = threading.Thread(target=function_one)
threadtwo = threading.Thread(target=function_two)
"""
Initiate the thread with .start()
"""
threadone.start()
threadtwo.start()

"""Wait until the thread has finished running
before running any more code.
Else other code will run at the same time,
"multi threading".
"""
threadone.join()
print("Complete")
