1.
# x = int(input("masukkan bilangan= ")) #12345

# digit1 = (x//10000)     #1
# digit2 = (x//1000)%10   #2
# digit3 = (x//100)%10    #3
# digit4 = (x//10)%10     #4
# digit5 = (x//1)%10      #5
 
# result = digit1*digit2*digit3*digit4*digit5
# print (result)

2. 
# before = int(input("Harga sebelum diskon ="))
# diskon = int(input("Besar diskon(dalam persen)= "))

# diskon /= 100
# after = before- (before*diskon)
# print(f"Harga setelah diskon {after}")

3.

# NIM = int(input("Masukkan 3 angka terakhir NIM anda: "))


#     #MAT
# if NIM % 2 == 0:
#     x = 1
# elif NIM % 2 == 1:
#     x = 2
#     #FIS
# if   NIM % 3 == 0:
#     y = 7
# elif NIM % 3 == 1:
#     y = 8
# elif NIM % 3 == 2:
#     y = 9
#     #KIM
# if   NIM % 4 == 0:
#     z = 9
# elif NIM % 4 == 1:
#     z = 10
# elif NIM % 4 == 2:
#     z = 11
# elif NIM % 4 == 3:
#     z = 12

# print("Anda berada di kelas:")
# print(f"kelas {x} - Matematika")
# print(f"kelas {y} - Fisika")
# print(f"kelas {z} - Kimia")

## Materi
# for i in range(2,5):
#     print(i**2, end=" ")

# for i in range (9,-2,-1):
#     print(i, end=" ")

# for i in range(1,7):
#     for j in range (1, i+1):
#         print(j, end=" ")
#     print() #buat baris baru setelah looping j selesai

4.
# N = int(input("Masukkan nilai N= ")) #60

# faktor = 1
# while faktor < N+1:
#  if N%faktor == 0:
#    print(faktor)
#  faktor += 1

# ATAU

# # for i in range (N,0,-1):
# #     if N%i == 0 :
# #         print(i)

5.
# n9 = int(input("Masukkan bilangan: "))

# digit1 = n9//100
# digit2 = (n9//10)%10
# digit3 = n9%10

# result = digit1+digit2+digit3

# print(f"Jumlah semua digitnya adalah {result}")

# ATAU

# n9 = int(input("Masukkan bilangan: ")) #576
# jumlahkan = 0

# while n9>0:
#     jumlahkan += n9%10   #6-15-
#     n9 = n9//10

# print(f"jumlah semua digitnya adalah {jumlahkan}.")

6.
# N = int(input("Masukkan nilai N: "))

# hasil = N**(1/2)

# print(f"{hasil:.3f}")

7.
# A = int(input("Masukkan nilai A: "))
# B = int(input("Masukkan nilai B: "))

# # n=3

# # for i in range(A,B+1):
# #    if i%n != 0 and i%2 == 1:
# #       print(i)

# for i in range (A,B+1):
#  if i != 0 and i != 1:
#     n=2
#     is_prima= True
#     while (n<i) and (is_prima):
#       if i % n == 0:
#          is_prima = False
#       n += 1
#     if is_prima:
#       print(i)

8.
# N = int(input("Masukkan N: "))
# n = [0 for i in range(N)]

# for i in range(N):
#     n[i] = int(input(f"Masukkan angka dari kiri ke kanan ke-{i+1} : "))
#     # print([i])
# print("Angka dari kanan ke kiri")
# for i in range(N-1,-1,-1):
#     print(n[i])

9. 
# N = int(input("Banyaknya barang: "))
# n = [0 for i in range(N)]

# print("Masukkan harga barang:")
# for i in range (N):
#     n[i] = int(input())
#     print(n)

# D = int(input("Masukkan harga diskon: "))

# print("Harga barang sesudah diskon:")
# for i in range(N):
#     print (str(n[i] - n[i]*D/100))

10.

# a = float(input("Masukkan a: "))
# b = float(input("Masukkan b: "))
# c = float(input("Masukkan c: "))

# operasi_tambah = ((-b) + ((b**2) - (4*a*c))**1/2)/2*a
# operasi_kurang = ((-b) - ((b**2) - (4*a*c))**1/2)/2*a

# if operasi_kurang and operasi_tambah < 0:
#     print("akar-akar dari persamaan kuadrat tidak ada")
# elif operasi_tambah == operasi_kurang:
#     print(f"akar-akar dari persamaan kuadrat ada 1,yakni {operasi_tambah}")
# else:
#     print(f"akar-akar dari persamaan kuadrat ada 2,yakni {operasi_tambah} dan {operasi_kurang}")

11.
# print("Masukkan beras merk A!")
# hargaA = int(input("Harga: "))
# satuanA = int(input("Satuan: "))
# print("Masukkan beras merk B!")
# hargaB = int(input("Harga: "))
# satuanB = int(input("Satuan: "))
# print("Masukkan beras merk C!")
# hargaC = int(input("Harga: "))
# satuanC = int(input("Satuan: "))

# totalA = hargaA/satuanA
# print(totalA)
# totalB = hargaB/satuanB
# print(totalB)
# totalC = hargaC/satuanC
# print(totalC)

# if totalA < totalB and totalC:
#     print("Beras termurah adalah beras merk A")
# elif totalB < totalA and totalC:
#     print("Beras termurah adalah beras merk B")
# else: #C murah
#     print("Beras termurah adalah beras merk C")

12.
# status = input("Status(menikah/lajang): ")
# paham  = input("Mengerti investasi(tidak/iya): ")
# buat   = input("Investasi buat apa(menikah?masa depan): ")
# waktu  = input("Jangka waktu investasi(<5 tahun/ >5 tahun): ")
# nilai  = input("Nilai investasi -15%, bagaimana(jual/tambah): ")

# x = 0

# if status == "lajang":
#     x += 1
# elif paham == "iya":
#     x += 1
# elif buat == "masa depan":
#     x += 1
# elif waktu == ">5 tahun":
#     x += 1
# elif nilai == "tambah":
#     x += 1

# print("Jenis investasi yang cocok adalah")
# if 0<=x<=2:
#     print("Deposito")
# if 0<=x<=3:
#     print("RD Pendapatan Tetap,Obligasi")
# if 0<=x<=5:
#     print("RD Pasar Uang,Emas,USD")
# if 2<=x<=4:
#     print("Properti tanah")
# if 2<=x<=5:
#     print("RD Saham, RD Campuran, P2P Lending")
# if 3<=x<=5:
#     print("Saham")

13.
# angka = int(input("Masukkan bilangan: "))

# jawaban = str(angka) + " merupakan"

# if (angka >= 1 and angka <= 9):
#     jawaban += " satuan "
# elif (angka >= 10 and angka <= 99):
#     jawaban += " puluhan "
# elif (angka >= 100 and angka <= 999):
#     jawaban += " ratusan "

# if (angka%2 == 0 or angka%3 == 0 or angka%5 == 0 or angka%7 == 0):
#     jawaban += "yang habis dibagi"
#     prev = False
#     if (angka%2 == 0):
#         if (prev and (angka%3 != 0 and angka%5 != 0 or angka%7 != 0)):
#             jawaban += " dan"
#         elif(prev):
#             jawaban += ","
#         jawaban += " dua"
#         prev = True
#     if (angka%3 == 0):
#         if (prev and (angka%5 != 0 and angka%7 != 0)):
#             jawaban += " dan"
#         elif(prev):
#             jawaban += ","
#         jawaban += " tiga"
#         prev = True
#     if (angka%5 == 0):
#         if (prev and (angka%7 != 0)):
#             jawaban += ", dan"
#         elif(prev):
#             jawaban += ","
#         jawaban += " lima"
#         prev = True
#     if (angka%7 == 0):
#         if(prev):
#             jawaban += " dan"
#         jawaban += " tujuh"
           
# else:
#     jawaban += "yang tidak habis dibagi oleh dua, tiga, lima, dan tujuh"

# print(jawaban)

14.
# N = int(input("Masukkan N: "))
# n = [0 for i in range(N)]
# print("Masukkan angka dari kiri ke kanan:")

# for i in range (N): # mulai dari 0 hingga 3
#     n[i] = int(input())

# print("Masukkan angka dari kanan ke kiri:")

# for i in range(N-1,-1,-1):  #mulai dari 3 hingga 0
#     print(n[i])

15.
# N = int(input("Banyaknya barang: "))
# n = [0 for i in range(N)] #inisiasi array baru yang akan disimpan
# x = [0 for i in range(N)] #inisiasi array kedua yang akan disimpan

# print("Masukkan harga barang")

# for i in range(N):
#     n[i] = int(input())

# diskon = int(input("Masukkan diskon: "))
# print("Barang sesudah diskon: ")

# setelahDiskon = diskon/100

# for i in range(N):
#     print(str([i]-(n[i]*setelahDiskon)))

16.
# N = int(input("Masukkan jumlah pokemon Tuan Wang: "))
# n = [0 for i in range(N)] #inisiasi array1
# menang = 0  #inisiasi kita menang
# kalah  = 0  #inisiasi kita kalah(lawan dapat poin)
# for i in range(N):
#     n[i] = int(input(f"Masukkan combat power pokemon Tuan Wang ke-{i+1}: "))

# nilaiMusuh = int(input("Masukkan combat power pokemon musuh: "))

# for i in range(N):
#     if nilaiMusuh<n[i]:
#         menang += 1
#     elif nilaiMusuh>=n[i]:
#         kalah  += 1

# if menang == kalah:
#     print("Tuang Wang tidak dapat mengalahkan pokemon musuh")

# elif menang > kalah:
#     print("Tuang Wang dapat mengalahkan pokemon musuh")

17.
# N = int(input("Masukkan banyaknya stik Tuan Wang: "))
# n = [0 for i in range (N)] #inisiasi
# print("Masukkan panjang stik: ")

# for i in range(N):
#     n[i] = int(input())

# print("Daftar segitiga yang dapat dibuat")

# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1,N):
#             a = n[i]
#             b = n[j]
#             c = n[k]
      
#             if ((a+b > c) and (a+c > b) and (b+c > a)):
#                 print(str(a)+" "+str(b)+" "+str(c))

18.
# rantai = input("Masukkan rantai DNA: ")
# pola   = input("Masukkan pola yang dicari: ")

# muncul = False

# panjang_rantai    = len(rantai)
# panjang_pola      = len(pola)
# panjang_pencarian = panjang_rantai-panjang_pola

# for i in range(panjang_pencarian+1):
#     pola_sesuai = True
#     j = 0
#     while (j<panjang_pola) and (pola_sesuai):
#         if (rantai[i+j] != pola[j]):
#             pola_sesuai = False
#         j += 1
#     if pola_sesuai:
#         muncul = True

# if (muncul) :
#     print("Pola muncul pada rantai DNA ")
# else:
#     print("Pola tidak muncul pada rantai DNA")
