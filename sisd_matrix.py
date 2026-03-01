import time
import random

print("=== SISD Matrix Multiplication ===")

size = 200  # ukuran matrix (jangan terlalu besar dulu)

# Buat matrix A dan B
A = [[random.random() for _ in range(size)] for _ in range(size)]
B = [[random.random() for _ in range(size)] for _ in range(size)]

# Buat matrix hasil
C = [[0 for _ in range(size)] for _ in range(size)]

start = time.time()

for i in range(size):
    for j in range(size):
        for k in range(size):
            C[i][j] += A[i][k] * B[k][j]

end = time.time()

print("Execution Time (SISD Matrix):", end - start, "seconds")