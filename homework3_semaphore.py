# Synchronization using Semaphores

import threading


def even(esem, osem):
    """ Method which prints even values """

    for n in range(0, 101, 2):
        osem.acquire()
        print(n)
        esem.release()


def odd(esem, osem):
    """ Method which prints odd values """

    for n in range(1, 101, 2):
        esem.acquire()
        print(n)
        osem.release()


even_sem = threading.Semaphore(0)
odd_sem = threading.Semaphore(1)

even_thread = threading.Thread(target=even, args=(even_sem, odd_sem))
odd_thread = threading.Thread(target=odd, args=(even_sem, odd_sem))

even_thread.start()
odd_thread.start()
