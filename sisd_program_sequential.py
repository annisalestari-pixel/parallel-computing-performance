import time

print("=== Sequential Program (SISD) ===")

n = 50_000_000   # jumlah angka yang akan dijumlahkan
total = 0        # variabel untuk menyimpan hasil

start = time.time()   # mulai hitung waktu

for i in range(1, n + 1):
    total += i

end = time.time()     # selesai hitung waktu

print("Final Total:", total)
print("Execution Time:", end - start, "seconds")