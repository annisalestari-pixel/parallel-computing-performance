import time
import random
import multiprocessing as mp

print("=== MIMD Matrix Multiplication ===")

size = 200

# Buat matrix A dan B
A = [[random.random() for _ in range(size)] for _ in range(size)]
B = [[random.random() for _ in range(size)] for _ in range(size)]

def multiply_row(i):
    row_result = []
    for j in range(size):
        total = 0
        for k in range(size):
            total += A[i][k] * B[k][j]
        row_result.append(total)
    return row_result

if __name__ == "__main__":
    start = time.time()

    with mp.Pool(4) as pool:  # karena laptop kamu 4 logical processor
        C = pool.map(multiply_row, range(size))

    end = time.time()

    print("Execution Time (MIMD Matrix):", end - start, "seconds")