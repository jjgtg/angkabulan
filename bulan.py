#10 angka bulan
angka_bulan = [5, 8, 12, 3, 10, 7, 9, 11, 6, 4]

maks = 0

n = 0

while n < len(angka_bulan):
    if angka_bulan[n] < maks:
        maks = angka_bulan[n]
    else:
        n += 1
        continue


print("Bilangan terbesar dalam list adalah:", maks)
