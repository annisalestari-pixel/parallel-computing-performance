import time
from multiprocessing import Process, Queue


def partial_sum(start, end, q):
    total = 0
    for i in range(start, end + 1):
        total += i
    q.put(total)

if __name__ == "__main__":
    n = 50_000_000
    q = Queue()

    # Bagi jadi 4 bagian (karena 4 logical processor)
    step = n // 4

    start_time = time.time()

    p1 = Process(target=partial_sum, args=(1, step, q))
    p2 = Process(target=partial_sum, args=(step+1, step*2, q))
    p3 = Process(target=partial_sum, args=(step*2+1, step*3, q))
    p4 = Process(target=partial_sum, args=(step*3+1, n, q))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    total = q.get() + q.get() + q.get() + q.get()

    end_time = time.time()
    print("=== Parallel Program (MIMD) ===")
    print("Final Total:", total)
    print("Execution Time:", end_time - start_time, "seconds")