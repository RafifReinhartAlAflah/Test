#1.) persegi

# #persegi 1
# xawal1 = int(input())
# yawal1 = int(input())
# xakhir1 = int(input())
# yakhir1 = int(input())

# #persegi 2
# xawal2 = int(input()) 
# yawal2 = int(input())
# xakhir2 = int(input())
# yakhir2 = int(input())

# s1 = (abs(xawal1-xakhir1) * abs(yawal1-yakhir1))
# s2 = (abs(xawal2-xakhir2) * abs(yawal2-yakhir2))

# if xawal1 == xakhir1 :
#     print("Masukkan ulang koordinat")
# elif yawal1 == yakhir1 :
#     print("Masukkan ulang koordinat")
# elif xawal2 == xakhir2 :
#     print("Masukkan ulang koordinat")
# elif yawal2 == yakhir2 :
#     print("Masukkan ulang koordinat")
# else : # x /= y
#     if s1 > s2 :
#         print("SegiEmpat pertama lebih luas daripada SegiEmpat kedua")

#     elif s1 < s2 :
#         print("SegiEmpat kedua lebih luas daripada SegiEmpat pertama")

#     else: # s1 = s2
#         print("Luas SegiEmpat sama")

#2.) uang

# n = int(input ("baki: "))
# harga = [int(input(f"harga-{i}: ")) for i in range (1,n+1)]
# jumlah = [int(input(f"jumlah-{i}: ")) for i in range (1,n+1)]
# baki = [i for i in range (1,n+1)]

# simpan = 0
# for i in range (len(jumlah)):
#     simpan += jumlah[i]

# total = simpan

# while total > 0 :
#     print(f"baki: {baki}")
#     print(f"harga: {harga}")
#     print(f"jumlah: {jumlah}")
#     print(total)
#     beli = int(input("beli : "))
#     idx = beli - 1
#     if jumlah[idx] > 0 :
#         print(f"Barang terbeli dengan harga {harga[idx]}\n")
#         jumlah[idx] -= 1
#         total -= 1
#     else :
#         print("Barang Sold Out\n")

# print ("Semua barang Sold Out")







# nomor = int(input("Masukkan nomor baki : "))
# AoB = [1 for i in range (40)]

# for i in range (1,41) :
#     AoB[i-1] = int(i)

# if AoB[nomor] :
#     AoB[nomor-1] = 0

# print (AoB)


