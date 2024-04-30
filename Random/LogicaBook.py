# 1.
# g = float(input("masukkan nilai gravitasi ="))
# h = float(input("masukkan tinggi ="))

# v = (2*g*h)**(1/2)

# print (v)

# 2.
# x = "TV"
# y = "AC"
# z = "Kulkas"

# xp = 100
# yp = 200
# zp = 300

# Xp = 3
# Yp = 8
# Zp = 5

# Xtot = (Xp*xp*30)/1000
# print(Xtot,"Kwh")
# Ytot = (Yp*yp*30)/1000
# print(Ytot,"Kwh")
# Ztot = (Zp*zp*30)/1000
# print(Ztot,"Kwh")

# Tot = int(Xtot + Ytot + Ztot)*1500
# print("Tagihan listrik satu bulan",Tot,"Rupiah")

3.
# benar +2
# salah -1
# # kosong 0

# x = int(input("masukkan nilai x ="))
# y = int(input("masukkan nilai y ="))
# jawaban = int(input("masukkan jawaban kamu ="))

# nilai = x + y

# if (nilai==jawaban and jawaban>0):
#     print("Kamu benar dapat 2")
# elif (nilai!=jawaban and jawaban>0):
#     print("kamu salah dapat -1")
# elif (jawaban==0):
#     print("jawaban kosong dapat 0")

# x = int(input())

# 4.
# a = int(input("masukkan nilai a ="))
# b = int(input("masukkan nilai b ="))
# c = int(input("masukkan nilai c ="))

# pyth = (a**2) + (b**2) 

# if (pyth < (c**2)):
#     print("lancip")
# elif (pyth == (c**2)):
#     print("siku-siku")
# else: #(pyth == c*2)
#     print("tumpul")

5.
# # ada 7 kelompok (1)
# kelompok = int(input("masukkan nilai = "))

# if kelompok in range(1,101,6):
#  print("kelompok1")
# elif kelompok in range(2,101,6):
#  print("kelompok2")
# elif kelompok in range(3,101,6):
#  print("kelompok3")
# elif kelompok in range(4,101,6):
#  print("kelompok4")
# elif kelompok in range(5,101,6):
#  print("kelompok5")
# elif kelompok in range(6,101,6):
#  print("kelompok6")
# else:
#  print("tidak masuk kelompok")

# 6.
# a = int(input("masukkan nomor absen ="))

# if (a<=6 and 1<=a<=100):
#     print("anda dikelompok",a)
# elif(a>6 and a%6==0 and 1<=a<=100):
#     print("anda dikelompok 6")
# elif(a>6 and a%6>0 and 1<=a<=100):
#     print("anda di kelompok",a%6)
# else:
#     print("error")

6.
# y2 = int(input("nilai y2 ="))
# y1 = int(input("nilai y1 ="))
# x2 = int(input("nilai x2 ="))
# x1 = int(input("nilai x1 ="))
# m = (y2-y1)/(x2-x1)

# if (m>0):
#     print("gradien naik")
# elif(m<0):
#     print("gradien turun")
# else:
#     print("gradien sejajar sumbu x")

##materi

# for i in range(10):
#     print("rafif")

# for i in range(1,9):
#     print("kelompok",i) #i ditambah angka

# for i in range(1,10, 2):
#     print("kelompok ganjil",i)

# i=1 

# while(i<12):
#     print(i)
#     i += 2  #interval

# for i in range(4): #for luar (berurutan)
#     for j in range(5): #for dalam (ngulang sama)
#         print("A", end="")  #end menghubungkan for dalam dengan for luar
#     else:
#         print("")

# i=1
# while(i<6):
#     j=1
#     while(j<7):
#         print("A", end="")
#         j +=1
#     else:
#         print("")
#         i += 1

7. 
# N = int(input("masukkan interval= "))
# i = 0
# countA = 0

# while i < N:
#    if countA%2 != 0 and countA % 3 == 0: #and (harus keduanya terpenuhi)
#       print(countA, end=" ")
#    countA += 1
#    i += 1

# ATAU

# a = int(input("masukkan bilangan pertama= "))
# b = int(input("masukkan bilangan kedua= "))

# for i in range (a,b+1):
#     if (i%2 != 0 and i %3 == 0):
#         print(i, end=" ")

8.
a = int(input("masukkan bilangan pertama= "))
b = int(input("masukkan bilangan kedua= "))

for i in range(a,b+1):
    print(i**2, end=" ")
    

# ATAU
N = int(input("masukkan interval = "))
i = 0
while i < N+1:
    print(i**2, end=" ")
    i += 1

print()

x = int(input("Masukkan nilai interval= "))
i = 0

while i < x+1:
 if i%2==0 or i%5== 0:
  print("Duar")
 elif i%3==0:
  print("Bom")
 else: 
  print("Tidak berkata apapun")
 i += 1

A = [1,2,3,4,5,6]

print(f"Banyaknya elemen pada array A adalah {len(A)}")

for i in A:
    print(i, end=" ")

print (A[0:6])

# 9. 
# a = int(input("Masukkan nilai dimensi dari vektor: "))
# print ("Vektor pertama")
# vec1 = [0 for i in range(a)]

# for i in range(a):
#     vec1[i]= float(input("Masukkan komponen vektor ke-"+ str(i+1)+": "))

# print ("Vektor kedua")
# vec2 = [0 for i in range(a)]

# for i in range(a):
#     vec2[i]= float(input("Masukkan komponen vektor ke-"+ str(i+1)+": "))

# print("jumlah kedua vektor adalah")
# jumlah = [0 for i in range (a)]
# for i in range (a):
#     jumlah[i] = vec1[i] + vec2[i]
#     print(jumlah[i])

10.
# a = int(input("Masukkan harga barang: "))
# d = int(input("Duit pembeli:"))

# b = a-d
# print (f"kembalian uang pembeli {b}")

# N = int(input("Masukkan banyak barang: "))
# brg = [0 for i in range(N)]

# for i in range(N):
#     brg[i] = int(input("Masukkan harga barang ke-"+ str(i+1) +": "))

# for i in range (N):
#     a = sum(brg)
# print("Harga barangnya adalah", sum(brg))

# a = int(input("Masukkan uang yang dibayarkan: "))

# kembali = a - sum(brg)
# if kembali < 0:
#     print("Uang anda kurang sebesar", kembali)
# elif kembali > 0:
#     print("Kembaliannya adalah",kembali)
# else: 
#     print("Uang anda pas, tidak ada kembalian")

11.
# n = int(input("Masukkan banyak nilai mahasiswa:")) 

# x = [0 for i in range(n)] # len() hanya untuk variabel, int tidak bisa menggunakan len()

# for i in range (n):
#     x[i] = int(input("Masukkan nilai mahasiswa ke-"+ str(i+1)+": "))

# for i in range (n):
#     jumlah = sum(x)
# print(f"nilai rata-rata mahasiswa {jumlah/len(x)}")

12.
# n = int(input("Masukkan banyak nilai mahasiswa:")) 

# nilai = [0 for i in range(n)]

# for i in range (n):
#     nilai[i] = int(input("Masukkan nilai mahasiswa ke-"+ str(i+1) + ": "))

# minimum = nilai[0]

# for i in range (n) :
#     if nilai[i] < minimum:
#         minimum = nilai[i]
# print ("Nilai terkecil adalah", minimum)

# maximum = nilai[0]
# for i in range(n) :
#     if nilai[i] > maximum:
#         maximum = nilai[i]
# print ("Nilai terbesar adalah",maximum)
