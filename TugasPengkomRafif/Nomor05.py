#program mencari kelipatan dalam suatu interval
#kamus
# X,a,b = int

# input
X = int(input("Masukkan nilai kelipatan: "))
a = int(input("Masukkan nilai awal: "))
b = int(input("Masukkan nilai akhir: "))


# proses
for i in range(a,b): #urutan dimulai dari a hingga b-1 
    if a < b :
        if i%X == 0: #jika angka dari range(a,b) modulo X == 0, maka ia termasuk kelipatan X
            print(i)
    else: #a >b 
        print("Nilai a harus lebih kecil dari b") 
    
