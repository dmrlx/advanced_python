# Threads synchronization using Events

import threading


def even():
    """ Method which prints even values """

    for n in range(0, 101, 2):
        odd_printed.wait()
        print(n)
        odd_printed.clear()
        even_printed.set()


def odd():
    """ Method which prints odd values """

    for n in range(1, 101, 2):
        even_printed.wait()
        print(n)
        even_printed.clear()
        odd_printed.set()


even_printed = threading.Event()
odd_printed = threading.Event()

even_thread = threading.Thread(target=even)
odd_thread = threading.Thread(target=odd)

even_thread.start()
odd_thread.start()

odd_printed.set()
