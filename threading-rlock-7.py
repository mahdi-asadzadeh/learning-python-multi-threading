"""
    Race condition
    Thread safe
    Dead lock
    atomic
"""


from threading import Thread, RLock


num = 0 # shared resource

lock = RLock()


def add():
    global num
    with lock:
        subtract()
        for _ in range(100000):
            num += 1


def subtract():
    global num
    with lock:
        for _ in range(100000):
            num -= 1


def both():
    add()
    subtract()

t1 = Thread(target=both)

t1.start()

t1.join()


print('Safe result :', num, 'be must is zero.')
print('Done ...')