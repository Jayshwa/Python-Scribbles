import threading
import time
import os


"""daemon threads will constantly run,
meaning they can be used to constantly read
files even as they are edited.
"""
path = os.path.join(os.path.dirname(__file__), "text.txt")
text = ""


def readfile():
    global path, text
    while True:
        with open(path, "r") as f:
            f.seek(0)
            text = f.read()
        time.sleep(3)


def printloop():
    while True:
        print(text)
        time.sleep(1)


t1 = threading.Thread(target=readfile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()
