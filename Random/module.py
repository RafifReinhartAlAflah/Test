# print("Hello , World!", end="") # (1)
# print(" My name is", end="") # (2)
# print(" Rafif") # (3)
# print("I'm","freshman")
# print("Ready to"+" study")

# variable = "Rafif"
# print(f"Call me {variable}")

# S = input("I want to learn coding") # 1
# print("What do u wanna learn ?" + S) # 2
# N = int(input("Addition :")) # 3
# print("5 +",N, "= " + str(N + 5)) # 4

# print("Input value of N: ", end="")
# N = int(input())
# if (N > 0):
#   print(str(N) + " is positive number")  
# else: # N <= 0
#   print(str(N) + " is negative number")

# if (N > 0):
#   print(str(N) + " is positive number")  
# elif (N < 0):
#   print(str(N) + " is negative number")
# else: # N == 0
#   print(str(N) + " is zero")

# if (N >= 0):
#  if (N > 0):
#   print(str(N) + " is positive number")
#  else: # N == 0
#   print(str(N) + " is zero")
# else: # N < 0
#  print(str(N) + " is negative number")

# a = int(input("nilai a :"))
# b = int(input("nilai b :"))
# i = a
# while (i <= b):
#  print(i)
#  i += 1

# a = int(input("nilai a :"))
# b = int(input("nilai b :"))
# for i in range(a, b+1):
#  print(i)

# n = int(input("berapa baris?"))
# for i in range(n):
#  for j in range(n):
#   print("rafif",end="") # Executed n * n times (2*2=4 kali "rafif")
#  print()                # Executed n times (beda paragraf)

# n = int(input("masukkan untuk nilai pangkat"))
# N = 10 ** n 
# print(int(N))

# n = int(input("berapa baris?"))
# for i in range(1, n + 1):
#  for j in range(1, i+ 1):
#   print(j,end=" ")      # Executed n * n times (2*2=4 kali "rafif")
#  print()                # Executed n times (beda paragraf)

# x= ["x" for x in range(10)]
# print(x)

# arr = [0 for i in range(5)]

# arr [0] = int (input("Input value index 0: "))
# arr [1] = int(input("Input value index 1: "))
# arr [2] = int(input("Input value index 2: "))
# arr [3] = int(input("Input value index 3: "))
# arr [4] = int(input("Input value index 4: "))
  
# for i in range(5):
#  arr[i] = int(input("Input value index " + str(i+1) + ": "))

# def persegi(x):
#     x2 = x*x
#     return x2

# x = int(input("masukkan nilai = "))
# x2 = persegi(x)
# print(x2)

# def nilai(a, b):  # assume b >= 0
#     c = 1
#     for i in range(b):
#      c *= a
#     return c

# a = int(input("masukkan nilai = "))
# b = int(input("masukkan nilai = "))
# c = nilai(a,b)
# print(c)

# def tulisMenu (makanan , minuman , tambahan):
#  if makanan == 1:
#   makanan = ("Burger")
#  elif makanan == 2:
#   makanan = ("Fried Chicken")
#  elif makanan == 3:
#   makanan = ("Instant Noodle")
#  if minuman == 1:
#   minuman = ("Avocado Juice")
#  elif minuman == 2:
#   minuman = ("Thai Tea")
#  elif minuman == 3:
#   minuman = ("Milk Tea")
#  if tambahan == 1:
#   tambahan = ("Fried Fries")
#  elif tambahan == 2:
#   tambahan = ("Kerupuk")
#  elif tambahan == 3:
#   tambahan = ("Doughnut")
#  hasil = f"Pilihan anda adalah {makanan}, {minuman}, dan {tambahan}"
#  return hasil


# print ("""Menu:\n1.Burger\n2.Fried Chicken\n3.Instant Noodle""")
# makanan = int(input("mau makan apa?="))
# print ("""Menu:\n1.Avocado Juice\n2.Thai Tea\n3.Milk Tea""")
# minuman = int(input("mau minum apa?="))
# print ("""Menu:\n1.Fried Fries\n2.Kerupuk\n3.Doughnut""")
# tambahan = int(input("mau tambahan apa?="))

# hasil = tulisMenu (makanan , minuman , tambahan)
# print(hasil,end=" ")

# MATRIX 
# n = int(input("n= "))
# m = int(input("m= "))

# A = [[0 for j in range(m)] for i in range(n)]

# for i in range(n):
#     for j in range(m):
#         A[i][j] = int(input("input element row " + str(i + 1) + " column " + str(j + 1) + ":" ))

# for i in range(n):
#     for j in range(m):
#         print(f"[{A[i][j]}]", end=" ")
#     print("")   # ini untuk membuat baris baru 


# n = int(input("n= "))
# m = int(input("m= "))
# l = int(input("l ="))

# A = [[0 for j in range(m)] for i in range(n)]  #kode lebih ringkas
# B = [[0 for j in range(l)] for i in range(m)]
# C = [[0 for j in range(l)] for i in range(n)]

# for i in range(n):
#  for j in range(m):
#   A[i][j] = int(input("input element A row " + str(i + 1) + " column " + str(j + 1) + ": "))

# for i in range(m):
#  for j in range(l):
#    B[i][j] = int(input("input element B row " + str(i + 1) + " column " + str(j + 1) + ": "))

# for i in range(n):
#  for j in range(l):
#    C[i][j] = 0
#    for k in range(m):
#     C[i][j] += A[i][k] * B[k][j]
#    print(C[i][j], end=" ")
#  print("")
