# Threads synchronization using Conditions

import threading


def printer(cond, start, stop):
    """Function which prints even/odd values depends on input values"""

    for n in range(start, stop, 2):
        with cond:
            cond.wait()
            print(n)
            cond.notify()


condition = threading.Condition()
even_thread = threading.Thread(target=printer, args=(condition, 0, 101))
odd_thread = threading.Thread(target=printer, args=(condition, 1, 101))

even_thread.start()
odd_thread.start()
with condition:
    condition.notify()
