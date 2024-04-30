#NIM/Nama: 16723018/Fikri Deli Al Khairi
#Tanggal: 29 Februari 2024
#Deskripsi: TP Modul 01 Problem 02
""""Tuan Kil sedang melakukan analisis tingkat kesulitan level di gamenya. Dia membuat kategori kesulitan tiap
level di gamenya sebagai berikut:"""

"""Mudah: Level berhasil diselesaikan 80% atau lebih pemain"""
"""Sedang: Level berhasil diselesaikan 30%-80% pemain"""
"""Sulit: Level berhasil diselesaikan kurang dari 30% pemain"""

"""Pada gamenya terdapat 5 level dan ingin setidaknya 2 level mudah dan 1 level sulit. Tentukan berapa banyak
level tiap kategorinya lalu tentukan apakah target 2 level mudah dan 1 level sulit tercapai."""

# Coding
mudah=0
sedang=0
sulit=0

level_1=int(input("Banyak Pemain yang memainkan level 1:"))
w_level_1=int(input("Banyak pemain yang berhasil menyelesaikan level 1:"))
if(w_level_1 >= ((level_1)*0.8)):
    mudah+=1
elif(w_level_1 < ((level_1)*0.3)):
    sulit+=1
else:
    sedang+=1

level_2=int(input("Banyak pemain yang memainkan level 2:"))
w_level_2=int(input("Banyak pemain yang berhasil menyelesaikan level 2:"))
if(w_level_2 >= ((level_2)*0.8)):
    mudah+=1
elif(w_level_2 < ((level_2)*0.3)):
    sulit+=1
else:
    sedang+=1

level_3=int(input("Banyak pemain yang memainkan level 3:"))
w_level_3=int(input("Banyak pemain yang berhasil menyelesaikan level 3:"))
if(w_level_3 >= ((level_3)*0.8)):
    mudah+=1
elif(w_level_3 < ((level_3)*0.3)):
    sulit+=1
else:
    sedang+=1

level_4=int(input("Banyak pemain yang memainkan level 4:"))
w_level_4=int(input("Banyak pemain yang berhasil menyelesaikan level 4:"))
if(w_level_4 >= ((level_4)*0.8)):
    mudah+=1
elif(w_level_4 < ((level_4)*0.3)):
    sulit+=1
else:
    sedang+=1

level_5=int(input("Banyak pemain yang memainkan level 5:"))
w_level_5=int(input("Banyak pemain yang berhasil menyelesaikan level 5:"))
if(w_level_5 >= ((level_5)*0.8)):
    mudah+=1
elif(w_level_5 < ((level_5)*0.3)):
    sulit+=1
else:
    sedang+=1

print(f"Banyak level mudah sebanyak {mudah}, level sedang sebanyak {sedang}, dan level sulit sebanyak {sulit}")

if((mudah >=2) and (sulit >=1)) and (sedang>=0):
    print(f"Target berhasil dicapai")
else:
    print(f"Target gagal dicapai")



#keterangan:
#level_(n): Banyak pemain yang memain level(n)
#w_level_(n): Banyak pemain yang berhasil menyelesaikan level(n)