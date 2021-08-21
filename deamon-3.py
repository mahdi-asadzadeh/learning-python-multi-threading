from time import sleep, perf_counter
from threading import Thread
import sys


start = perf_counter()


def show(name):
    print(f'Starting - {name}')
    sleep(3)
    print(f'finishing - {name}')


t1 = Thread(target=show, args=('One',), daemon=True)
t2 = Thread(target=show, args=('Two',), daemon=True)


t1.start()
t2.start()


end = perf_counter()


print( end - start )
sys.exit()