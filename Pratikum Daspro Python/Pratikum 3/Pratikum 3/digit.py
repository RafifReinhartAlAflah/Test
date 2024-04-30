arr = [0 for i in range(10)] # angka 0 sampai 9
ctr = 0

while ctr < 100 :
    angka = int(input())
    if angka < 0 :
        break # keluar dari loop
    ctr += 1  #jumlah angka yang ada
    for digit in str(angka):
        arr [int(digit)] += 1 #penambahan angka yang sama
print(ctr)

for i in range (10):
    if arr[i] > 0 :
        print(str(i) + ' : ' + str(arr[i]))


#cara sendiri

# i = 1 #inisiasi
# n = 0 #banyak inputan

# #banyak kemunculan angka
# n1 = 0
# n2 = 0
# n3 = 0
# n4 = 0
# n5 = 0
# n6 = 0
# n7 = 0
# n8 = 0
# n9 = 0
# n0 = 0

# while i <= 100 :
#     bilangan = int(input())
#     if bilangan < 0 or i == 100 :
#         i += 99999
#     elif bilangan % 10 == 0 :
#         n0 += 1
#         n += 1
#     else : #bilangan > 0 and i != 100
#         j = 1  
#         while j <= 5:
#             if bilangan % 10 == 1 :
#                 n1 += 1
#             elif bilangan % 10 == 2 :
#                 n2 += 1
#             elif bilangan % 10 == 3 :
#                 n3 += 1
#             elif bilangan % 10 == 4 :
#                 n4 += 1
#             elif bilangan % 10 == 5 :
#                 n5 += 1
#             elif bilangan % 10 == 6 :
#                 n6 += 1
#             elif bilangan % 10 == 7 :
#                 n7 += 1
#             elif bilangan % 10 == 8 :
#                 n8 += 1
#             elif bilangan % 10 == 9 :
#                 n9 += 1
#             bilangan = bilangan // 10
            
#             if bilangan == 0 :
#                 j += 9999
#             else : 
#                 j += 1
#         i += 1
#         n += 1

# print (n)
# if n0 >= 1 :
#     print ("0 : " + str(n0))
# if n1 >= 1 :
#     print ("1 : " + str(n1))
# if n2 >= 1 :
#     print ("2 : " + str(n2))
# if n3 >= 1 :
#     print ("3 : " + str(n3))
# if n4 >= 1 :
#     print ("4 : " + str(n4))
# if n5 >= 1 :
#     print ("5 : " + str(n5))
# if n6 >= 1 :
#     print ("6 : " + str(n6))
# if n7 >= 1 :
#     print ("7 : " + str(n7))
# if n8 >= 1 :
#     print ("8 : " + str(n8))
# if n9 >= 1 :
#     print ("9 : " + str(n9))
