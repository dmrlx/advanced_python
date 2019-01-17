# Synchronization using Semaphores

import multiprocessing


def even(esem, osem):
    """Method which prints even values"""

    for n in range(0, 101, 2):
        osem.acquire()
        print(n)
        esem.release()


def odd(esem, osem):
    """Method which prints odd values"""

    for n in range(1, 101, 2):
        esem.acquire()
        print(n)
        osem.release()


even_sem = multiprocessing.Semaphore(0)
odd_sem = multiprocessing.Semaphore(1)

even_thread = multiprocessing.Process(target=even, args=(even_sem, odd_sem))
odd_thread = multiprocessing.Process(target=odd, args=(even_sem, odd_sem))

even_thread.start()
odd_thread.start()
