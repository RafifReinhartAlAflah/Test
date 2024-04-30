# 1. kuis

# x = int(input("kuis1 :"))
# y = int(input("kuis2 :"))
# z = int(input("kuis3 :"))

# Nilai = (x + y + z)/3

# if Nilai >= 80:
#     print("Lulus memuaskan")
# elif Nilai >= 70:
#     print("Lulus")
# else: #<70
#     print("Tidak lulus")

# # 2.empat bilangan
# # persyaratan
# alfa = int(input("setiap digit naik/turun :"))
# beta = "dua digit pertama - dua digit terakhir = 30"
# gamma= "alfa dan beta"
# delta= "tidak alfa dan beta"

# angka = int(input("masukkan nilai :"))

# satuan = angka % 10 
# puluhan= ((angka%100)-satuan)/10
# ratusan= ((angka%1000)-satuan)/100
# ribuan= ((angka%10000)-satuan)/1000
# duadigitterakhir = angka%100
# duadigitawal = (angka-(angka%100))/100

# if(satuan>puluhan>ratusan>ribuan) or (satuan<puluhan<ratusan<ribuan):
#  if(((satuan>puluhan>ratusan>ribuan) or (satuan<puluhan<ratusan<ribuan)) and ((duadigitterakhir-duadigitawal)>=30) or ((duadigitawal-duadigitterakhir)>=30)):
#     print("gama")
#  else:
#    print("alfa")
# elif((duadigitterakhir-duadigitawal)>=30) or ((duadigitawal-duadigitterakhir)>=30):
#   print("beta")
# else:
#   print("delta")

# a = x-x%1000
# x -= a
# b = x-x%100
# x -= b
# c = x-x%10
# x -= c
# d = x-c

# a /= 1000
# b /= 100
# c /= 10

# if bool(Nilai.sort()):
#     print("bilangan alfa")
# elif bool(Nilai()):
#     print("bilangan beta")
# elif Nilai():
#     print("bilangan gamma")
# else: #selain g
#     print("bilangan delta")

# # 3. pengiriman

# Metode = input("Masukkan metode pengiriman =")
# Barang = int(input("Masukkan banyak barang ="))
# Berat  = int(input("Masukkan berat barang ="))
# biaya_awal = 15000
# # berat >10 kg, maka tambah 2000/kg
# # reguler >4 = diskon 10%
# # kilat >=2 dan 9000/kg
# # kilat   >4 = diskon 15%

# if (Metode == "reguler"):
#     if (Berat>10 and Barang>4 ):
#      print((biaya_awal+Berat*5000+(Berat-10)*2000)-((biaya_awal+Berat*5000+(Berat-10)*2000)*0.1))
#     elif (Berat>10 and Barang<=4):
#      print(biaya_awal+Berat*5000+(Berat-10)*2000)
#     elif(Berat<=10 and Barang>4 ):
#      print((biaya_awal+Berat*5000)-((biaya_awal+Berat*5000)*0.1))
#     elif(Berat<=10 and Barang<=4 ):
#      print(biaya_awal+Berat*5000)

# elif (Metode == "kilat" and Barang >= 2):
#     if (Berat>10 and Barang>4 ):
#      print((biaya_awal+Berat*9000+(Berat-10)*2000)-((biaya_awal+Berat*9000+(Berat-10)*2000)*0.15))
#     elif (Berat>10 and Barang<=4):
#      print(biaya_awal+Berat*9000+(Berat-10)*2000)
#     elif(Berat<=10 and Barang>4 ):
#      print((biaya_awal+Berat*9000)-((biaya_awal+Berat*9000)*0.15))
#     elif(Berat<=10 and Barang<=4 ):
#      print(biaya_awal+Berat*9000)

# elif (Metode == "kilat" and Barang < 2):
#   print("Tidak bisa mengirim dengan metode kilat")
  
4.
# r1 = float(input("masukkan r1 = "))
# r2 = float(input("masukkan r2 = "))
# r3 = float(input("masukkan r3 = "))

# rtot = (r1+r2+r3)*0.1

# if(rtot and r1>0 and r2>0 and r3>0):
#     print(rtot,"ohm")
# else:
#     print("tidak dapat menghitung hambatan")

6.
# x = int(input("masukkan berat kardus 1 = "))
# y = int(input("masukkan berat kardus 2 = "))
# z = int(input("masukkan berat kardus 3 = "))
# xtot = int(input("masukkan berat X = "))
# <= X "kg"
# angkat>1 and <= X "kg"
# >X :
#  X*banyak_orang

# if ( x<=xtot and y<=xtot and z<=xtot):
#  if((xtot-x)<=xtot and (xtot-y)<=xtot and (xtot-z)<=xtot):
  
# 7.
# N = int(input("anak ayam: "))
# print("anak ayam turunlah",N)

# while N>1:
#     N -= 1
#     print("mati satu tinggallah",N)

# if N == 1:
#     print("Mati satu tinggal induknya")

# 8.
# x2 = int(input("masukkan x2: "))
# x1 = int(input("masukkan x1: "))
# fungsi2 = x2**3+x2+1
# fungsi1 = x1**3+x1+1


# integral = fungsi2-fungsi1

# print(integral)

8.

# n1 = int(input("Masukkan nilai latihan ke-1: "))
# n2 = int(input("Masukkan nilai latihan ke-2: "))
# count = 3

# while (n1 + n2)/2 < 70:
#     if n1 < n2:
#         n1 = n2
#     n2 = int(input(f"Masukkan nilai latihan ke-{count}: "))
#     count += 1
# print(f"Adik Tuan Kil berhasil mencapai target dengan nilai rata-rata {(n1 +n2)/2:.2f}.")

# 9.
# b1 = int(input("Masukkan bilangan pertama:"))
# b2 = int(input("Masukkan bilangan kedua:"))
# b3 = int(input("Masukkan bilangan ketiga:"))
# b4 = int(input("Masukkan bilangan keempat:"))
# ken = b4/b1 - 1
# suku = 0
# n = 0
# if b2 / b1 == b3 / b2:
#     while suku <= ken:
#         suku = b1*(b2/b1)**(n)
#         n+=1
#     if b4 == suku:
#         print(b4,f"suku ke-{n-1}")
#     elif b4 > suku:
#         print(b4,"bukan merupakan suku dari barisan geo")
# else:
#     print("bukan barisan geo")

10.
# harga = int(input("Masukkan harga minuman: "))

# j = harga
# k = 0
# j = 0
# while j < harga:
 
#  while j < harga:
#     j = j + 7**k  # 1-8-57-400
#     k += 1

# j = j + 7**k  #65-109
# k += 1

# if j == harga:
#     print("pembelian dapat dilakukan")

# else:
#     print("tidak dapat dilakukan")

# 7**k 
# k >= 0

# 11.
# A = int(input("Masukkan nilai A: ")) #1
# T = int(input("Masukkan nilai T: ")) #10

# simpan_hasil = 1
# i = 0

# while A < T:
#   A += i #1-2-4-7-11

#   i +=1

# print(f"Penambahan dilakukan sebanyak {i-1} kali dengan nilai A terakhir adalah {A-i+1}")

12.
# n = int(input("Masukkan n: "))

# y = 1
# a = 0
# b = 0
# z = 2
# for i in range (0, n+1):
#  if i % 2 == 0:
#     for j in range (1,n):
#         print(y+a, end="")
#         a += 2
#  else:
#      for j in range (1,n):
#         print(z+b, end="")
#         b += 2
#  i += 1
    
13.

# jam   = int(input("Masukkan pukul jam: "))
# menit = int(input("Masukkan pukul menit: "))
# kecepatan = int(input("Masukkan kecepatan motor: "))

# # s = 15 km dari rumah
# # A = 11:00 (40 menit/sekali dan 60 menit waktu tempuh)
# # B = 11:30 (50 menit/sekali dan 50 menit waktu tempuh)
# # C = 12:00 (60 menit/sekali dan 40 menit waktu tempuh)


# t = (15*60)/kecepatan
# waktu = jam,menit t 

# while jam < 24 :
#    if menit < 60 :
#        menit + t


# for i in range (1100,2400,40):
#     print(f"{i}")
# for j in range (1130,2400,50):
#     print(f"{i}")
# for k in range (1100,2400,40):
#     print(f"{i}")

14.
# N = int(input("Masukkan nilai n: "))
# n = [[0 for j in range(N)]for i in range(N)]

# for i in range(N):
#     for j in range(N):
#         n[i][j] = input(f"Masukkan nama tamu pada lantai {i+1} kamar {j+1}: ")

# cari = input("Masukkan nama tamu yang ingin dicari: ")

# x = 0 
# for i in range(N):
#     for j in range(N):
#         if cari == n[i][j]:
#             print(f"Tamu {cari} berada di lantai {i+1} kamar {j+1}")
#             x += 1
#         else:
#             x += 0

# if x == 0: # 
#     print("Tamu tidak ditemukan")

15. 
# M x N
# kapal selam mush = X
# kapal selam musuh hancur = .
# harus menghancurkan semua (X)

# m = int(input("Nilai M: "))
# n = int(input("Nilai N: "))
# musuh = int(input("Jumlah Musuh: "))

# arrmusuh = [["." for j in range (n)]for i in range (m)]

# for i in range (musuh):
#     y = int(input(f"Baris {i+1}: "))
#     x = int(input(f"Kolom {i+1}: "))
#     arrmusuh[y-1][x-1] = "X"

# nembak = int(input("Jumlah Nembak: "))

# for i in range(nembak):
#     arah = input("Arah tembak: ")
#     brs = int(input("Baris Tembak: "))
#     klm = int(input("Kolom Tembak: "))
#     if (arah == "horizontal"):
#         for j in range(n):
#             arrmusuh[brs-1][j] = "."
#     if (arah == "vertikal"):
#         for i in range (m):
#             arrmusuh[i][klm-1] = "."


# musuhsisa = 0
# for i in range(m):
#     for j in range(n):
#         print(arrmusuh[i][j], end=" ")
#         if arrmusuh[i][j] == "X":
#             musuhsisa += 1
#     print()

# if musuhsisa > 0:
#     print(f"nona deb kalah, masih ada musuh {musuhsisa}")
# else:
#     print(f"Nona Deb menang")

16.
print("Masukkan nilai persamaan")

a = int(input("Nilai a: "))
b = int(input("Nilai b: "))
c = int(input("Nilai c: "))
print("Masukkan nilai batas dan partisi")
BB = int(input("Batas bawah: "))
BA = int(input("Batas atas: "))
JP = int(input("Jumlah partisi: "))

x = BB
jumlah = 0
def riman(jumlah,a,b,c,BB,BA,JP,x):
    lebar = int((BA-BB)/JP)
    while x < BA:
        fungsi = ((a*(x**2)) + (b*x) + c)*lebar
        # print(fungsi)
        jumlah += fungsi
        # print(jumlah)
        x += lebar
    return jumlah

jumlah = riman(jumlah,a,b,c,BB,BA,JP,x)

print(f"Nilai Rieman kiri yang diperoleh adalah {jumlah}")