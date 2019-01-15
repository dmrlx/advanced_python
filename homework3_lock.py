# Synchronization using Lock object

import threading
import time

thread_lock = threading.Lock()
sleep_time = .05


def even():
    """Function which prints even values only"""

    n = 0
    while n <= 100:
        with thread_lock:
            if not n % 2:
                print(n)
        n += 1
        time.sleep(sleep_time)


def odd():
    """Function which prints odd values only"""

    n = 0
    while n <= 100:
        with thread_lock:
            if n % 2:
                print(n)
        n += 1
        time.sleep(sleep_time)


even_thread = threading.Thread(target=even)
odd_thread = threading.Thread(target=odd)

even_thread.start()
odd_thread.start()
