# Threads synchronization using Timer

from threading import Timer
import time


def printer(start, stop):
    """ Function which prints even/odd values depends on input values """

    for n in range(start, stop, 2):
        print(n)
        time.sleep(1)


t1 = Timer(1, printer, args=[0, 101])
t2 = Timer(2, printer, args=[1, 101])

t1.start()
t2.start()
