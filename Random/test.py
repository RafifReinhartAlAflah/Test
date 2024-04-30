# x = int(input("Masukkan banyak: "))
# X = [0 for i in range(x)]
# for i in range (x):   #len(panjang) hanya bisa untuk string
#     X[i] = int(input("Masukkan angka: "))     #untuk menjumlahkan jadikan lagi integer
# print(X)

1.
# baris = 4
# kolom = j

# N = int(input("Masukkan nilai banyak mahasiswa (n) : "))

# if N%2 == 0:
#     data = [[0 for j in range (N)]for i in range(4)] #baris
#     for i in range(4):
#         for j in range(N):
#             data[i][j] = int(input(f"Masukkan nilai pratikum {i+1} mahasiswa {j+1}: "))

# else:
#     data = [0 for i in range (4)] #baris
#     print("Masukkan nilai pratikum:")
#     for i in range(4):
#         baris = input()
#         data[i] = baris.split(" ")
# print(data)

# target = int(input("Masukkan target(x) : "))

# x = 0
# for j in range(N):
#     sum = 0 
#     for i in range(4):
#         sum += int(data[i][j])  # data[baris][kolom]
#         if sum/4 > target:
#             # print("lebih dari target")
#             # print(sum/4)
#             x += 1
#         else:
#             # print("tidak > target")
#             # print(sum)
#             x += 0

# print(f"Terdapat {x} mahasiswa yang mendapatkan rata-rata nilai pratikum di atas {target}")

2.
# i-x = index ke-i dikurang berapa kali dimundurkan
# enkripsi = dari kata logis -> tidak logis
# dekripsi = dari kata tidak logis -> logis

# tipe    = input("Masukkan tipe pesan: ")
# pesan   = input("Masukkan pesan: ")
# X       = int(input("Masukkan nilai x: "))

# huruf = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# i = 0
# if tipe == "enkripsi":
#     for i in range(len(pesan)):
#         j = 0
#         while j < 26:
#             if pesan[i] == huruf[j]:
#                 print(huruf[j-X],end = "")
#                 j += 1000
#             elif pesan[i] == " ":
#                 print(" ", end = "")
#                 j += 1000
#             else:
#                 j += 1
#         i += 1

# elif tipe == "dekripsi":
#     for i in range(len(pesan)):
#         j = 0
#         while j < 26:
#             if pesan[i] == huruf[j]:
#                 j += X
#                 if j >=26:
#                     sisa = j - 26
#                     print(huruf[sisa],end = "")
#                     j += 1000
#                 elif j:
#                     print(huruf[j], end ="")
#                     j += 1000
                
            
#             elif pesan[i] == " ":
#                 print(" ", end = "")
#                 j += 1000
#             else:
#                 j += 1
#         i += 1

3.
# matrix 2n x 2n
# N = int(input("Masukkan nilai n: "))

# if N  > 2:
#     print("Masukkan elemen matrix")
#     data = [0 for i in range(N)]
#     for i in range(N):
#         matrix = input()
#         matrix = matrix.split(" ")
#         data[i] = matrix
#     print(data)
#     for i in range(N):
#         j = 0
#         while j < N:
#             print(f"{data[i][j]} {data[i][j]}", end = " ")
#             j += 1
#         print()

# else:
#     data = [[0 for j in range(N)]for i in range(N)]
#     for i in range(N):
#         for j in range(N):
#             data[i][j] = int(input(f"Masukkan Elemen baris {i+1} kolom {j+1}: "))
#     print(data)
#     for i in range(N):
#         j = 0
#         while j < N:
#             print(f"{data[i][j]} {data[i][j]}", end = " ")
#             j += 1
#         print()

4.
bilangan = input("Masukkan sebuah bilangan: ") #678
x = len(bilangan)
i = 0

while i < x:
    hasil = int(bilangan[0])
    for i in range(1,len(bilangan)):
        hasil = hasil*int(bilangan[i])
    bilangan = hasil
    i += 1
    print(bilangan)




   



