from time import sleep, perf_counter
from threading import Thread


start = perf_counter()


def show(name):
    print(f'Starting - {name}')
    sleep(3)
    print(f'finishing - {name}')


t1 = Thread(target=show, args=('One',))
t2 = Thread(target=show, args=('Two',))


t1.start()
t2.start()


t1.join()
t2.join()


end = perf_counter()


print( end - start )
