import time

print("=== MISD Program (Simulation) ===")

n = 50_000_000

def sum_formula(n):
    return n * (n + 1) // 2

def sum_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

start = time.time()

result1 = sum_formula(n)
result2 = sum_loop(n)

end = time.time()

print("Result 1 (Formula):", result1)
print("Result 2 (Loop):", result2)
print("Execution Time:", end - start, "seconds")
