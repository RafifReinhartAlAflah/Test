# # uts = int(input("Nilai UTS = "))
# # sum = [0 for x in range (999)]
# # k = 0
# # x = 0
# # i = 0       

# # if (uts < 0 or uts > 100) :
# #     print("Data kosong, tidak ada nilai rata-rata")
# # else :
# #     j = 0
# #     while k < 999  :
# #         if (uts < 0 or uts > 100) :
# #             print("Data kosong, tidak ada nilai rata-rata !")
# #             k += 99999
# #         else :
# #             while j < 101 :
# #                 uas = int(input("Nilai UAS = "))
# #                 if (uas < 0 or uas > 100):
# #                     print("Ulangi input nilai (0..100)!")
# #                     j += 1
# #                 else :
# #                     endgrade = (uts * 0.4) + (uas * 0.6)
# #                     i += 1     
# #                     print("Nilai akhir pelajaran",i,"= ", endgrade)
# #                     sum[x]= endgrade
# #                     j += 99999
# #                     k += 1
# #                     x += 1
    
# #         if (uas >= 0 and uas <= 100) :
# #             while k < 999 :
# #                 uts = int(input("Nilai UTS = "))
# #                 if uts < 0 or uts > 100 :
# #                         k += 99999
# #                 else :
# #                     uas = int(input("Nilai UAS = "))
# #                     endgrade = (uts * 0.4) + (uas * 0.6)
# #                     i += 1     
# #                     print("Nilai akhir pelajaran",i,"= ", endgrade)
# #                     sum[x] = endgrade
# #                     k += 1
# #                     x += 1

# # k = 0
# # rata = 0
# # rata2 = 0
# # while k < 20 :
# #     rata += sum[k]
# #     k += 1

# # rata2 += rata/i
# # print("Nilai rata-rata dari",i,"pelajaran adalah =", rata2)

# i = 0
# k = 0
# while i < 3 :
#     pilihan = input()
#     if pilihan == "paralel":
#         r1 = int(input())
#         r2 = int(input())
#         r3 = int(input())
#         rt = (r1+r2+r3)/(r1*r2*r3)
 
#         if r1 < 0 and r2 < 0 and r3 < 0 :
#             print("input resistor harus (r>0)!")
#             i += 1
#         else :
#             i += 999
#     elif pilihan == "seri": 
#         r1 = int(input())
#         r2 = int(input())
#         r3 = int(input())
#         rt = r1 + r2 + r3
#         i += 9999
#     else:
#         print("Ulangi input pilihan (seri/paralel)!")
#         i += 1

# print(rt)

# p1Pembilang = float(input())
# p1Penyebut  = float(input())
# p2Pembilang = float(input())
# p2Penyebut  = float(input())

# if p1Penyebut < 0 or p2Penyebut < 0 :
#     print("Masukan tidak valid")
# else : 
#     selisihPembilang = ((p1Pembilang*p2Penyebut)-(p2Pembilang*p1Penyebut))
#     selisihPenyebut  = (p1Penyebut*p2Penyebut)

# selisih = selisihPembilang/selisihPenyebut
# if selisihPembilang > 0 : 
#     print("P1 lebih besar dari P2")
#     print(selisih)
# else :
#     print("P1 lebih besar dari P2")
#     print(selisih)

# n = int(input()) #banyak angka
# t = [int(input()) for i in range(n)]


# imin = 0
# i = 1

# while i <= n-1 :
#     if t[i] < t[imin] :
#         imin = i
#         i += 1
#     else:
#         i += 1

# print("Nilai minimum dari data adalah",t[imin],)
# print(f"Indeks terkecil dari nilai minimum adalah index ke - {imin+1}")
    
# n = int(input())
# t = [0 for i in range(n)]

# #suhu
# i = 0
# while i < n:
#     t[i] = int(input())
#     i += 1

# x = int(input())

# count = 0
# for i in range(n) :
#     if t[i] > x :
#         count += 1
#     else :
#         count += 0

# if count == 0 :
#     print("False")
# else :
#     print("True")

# n = int(input())
# t = [0 for i in range(n)]

# i = 0
# while i < n :
#     t[i] = input()
#     i += 1

# p = input()
# i = len(t)
# while i >= 1 and t[i-1] != p :
#     i -= 1

# if i >= 1 :
#     print(i)
# else :
#     print(0)