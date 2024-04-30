#program mengetahui antarmatriks memiliki baris,kolom,dan nilai yang sama atau tidak
#kamus
# MB1, MK1, MB2, MK2 = int
# data1, data2 = list

# input
MB1 = int(input("Masukkan baris matriks 1: "))
MK1 = int(input("Masukkan kolom matriks 1: "))
MB2 = int(input("Masukkan baris matriks 2: "))
MK2 = int(input("Masukkan kolom matriks 2: "))

data1 = [[0 for j in range(MK1)] for i in range(MB1)]
data2 = [[0 for j in range(MK2)] for i in range(MB2)]
# proses
for i in range(MB1):       #Baris
    for j in range(MK1):   #Kolom
        data1[i][j] = int(input(f"Masukkan baris {i+1} dan kolom {j+1}: "))
for i in range(MB2):       #Baris
    for j in range(MK2):   #Kolom
        data2[i][j] = int(input(f"Masukkan baris {i+1} dan kolom {j+1}: "))

if MB1 == MB2 and MK1 == MK2:
    if data1 == data2:
        print("Baris, Kolom, dan Isi setiap Matriks Pertama dan Matriks Kedua sama")
    else: #data1 != data2
        print("Baris dan Kolom sama, namun Isi setiap Matriks Pertama dan Matriks Kedua tidak sama")
else:  #(MB1 != MB2 and MK1 != MK2) or (MB1 == MB2 and MK1 != MK2) or (MB1 != MB2 and MK1 == MK2)
    print("Baris, Kolom, dan Isi setiap Matriks Pertama dan Matriks Kedua tidak sama")
