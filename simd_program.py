import numpy as np
import time

print("=== SIMD Program ===")

n = 50_000_000

# buat array dari 1 sampai n
data = np.arange(1, n + 1)

start = time.time()

total = np.sum(data)

end = time.time()

print("Final Total:", total)
print("Execution Time:", end - start, "seconds")