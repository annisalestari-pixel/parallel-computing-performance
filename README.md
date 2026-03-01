# Uji Performa Komputasi Paralel

Proyek ini dibuat sebagai bagian dari tugas mata kuliah Komputasi Paralel. 
Pengujian dilakukan langsung pada laptop pribadi untuk melihat perbedaan waktu eksekusi antara program sequential dan parallel berdasarkan konsep Flynn’s Taxonomy.

Tujuan dari program ini adalah untuk memahami bagaimana pembagian pekerjaan ke beberapa core dapat mempengaruhi performa sistem.

Arsitektur yang diimplementasikan:

- SISD (Single Instruction Single Data)
- SIMD (Single Instruction Multiple Data)
- MISD (Multiple Instruction Single Data) – simulasi
- MIMD (Multiple Instruction Multiple Data)

---

## Spesifikasi Laptop

Pengujian dilakukan pada laptop dengan spesifikasi berikut:

- Processor: Intel Core i3-1005G1
- Core Fisik: 2
- Logical Processor: 4
- Sistem Operasi: Windows

---

## Hasil Pengujian

| Arsitektur | Waktu Eksekusi (detik) |
|------------|------------------------|
| SISD | 8.02 |
| MIMD | 2.30 |
| SIMD | 0.09 |
| MISD | 2.71 |

---

## Penjelasan Singkat

### SISD
Program dijalankan secara sequential (serial), artinya perhitungan dilakukan satu per satu tanpa pembagian tugas ke core lain.

### SIMD
Menggunakan NumPy (vectorization), di mana satu instruksi diproses ke banyak data secara bersamaan. Karena menggunakan optimasi internal, waktu eksekusi menjadi jauh lebih cepat.

### MISD
Merupakan simulasi beberapa algoritma berbeda yang dijalankan pada data yang sama. Konsep ini lebih sering digunakan untuk reliability dibandingkan untuk mempercepat proses.

### MIMD
Menggunakan multiprocessing, di mana data dibagi menjadi beberapa bagian dan diproses secara paralel sesuai jumlah logical processor yang tersedia.

---

## Kesimpulan

Dari hasil pengujian dapat dilihat bahwa komputasi paralel memberikan peningkatan performa dibandingkan komputasi sequential. Namun, peningkatan tersebut tetap bergantung pada jumlah core serta overhead sistem saat membuat dan mengelola proses paralel.
