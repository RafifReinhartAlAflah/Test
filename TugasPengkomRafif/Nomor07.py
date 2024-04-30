#program mencari nilai terbesar dan nilai terkecil
#kamus
# X = int
# x = list

# input
print("""Pilihan 0: Nilai maximum dan minimum\nPilihan 1: Nilai maximum\nPilihan 2: Nilai minimum""")
X = int(input("Masukkan pilihan anda: "))
x = [i for i in range(1,101)]

# proses
if X == 0:
    print(f"Nilai Maximum adalah {x[99]} dan Nilai Minimum adalah {x[0]}")
elif X == 1:
    print(f"Nilai Maximum adalah {x[99]}")
elif X == 2:
    print(f"Nilai Minimum {x[0]}")