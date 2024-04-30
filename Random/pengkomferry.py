1.
N = int(input("Masukkan nilai n: "))
n = [[0 for j in range(N)]for i in range(N)]

for i in range(N):
    for j in range(N):
        n[i][j] = input(f"Masukkan nama tamu pada lantai {i+1} kamar {j+1}: ")

cari = input("Masukkan nama tamu yang ingin dicari: ")

x = 0 
for i in range(N):
    for j in range(N):
        if cari == n[i][j]:
            print(f"Tamu {cari} berada di lantai {i+1} kamar {j+1}")
            x += 1
        else:
            x += 0

if x == 0: # 
    print("Tamu tidak ditemukan")

2. 
# M x N
# kapal selam mush = X
# kapal selam musuh hancur = .
# harus menghancurkan semua (X)

m = int(input("Nilai M: "))
n = int(input("Nilai N: "))
musuh = int(input("Jumlah Musuh: "))

arrmusuh = [["." for j in range (n)]for i in range (m)]

for i in range (musuh):
    y = int(input(f"Baris {i+1}: "))
    x = int(input(f"Kolom {i+1}: "))
    arrmusuh[y-1][x-1] = "X"

nembak = int(input("Jumlah Nembak: "))

for i in range(nembak):
    arah = input("Arah tembak: ")
    brs = int(input("Baris Tembak: "))
    klm = int(input("Kolom Tembak: "))
    if (arah == "horizontal"):
        for j in range(n):
            arrmusuh[brs-1][j] = "."
    if (arah == "vertikal"):
        for i in range (m):
            arrmusuh[i][klm-1] = "."


musuhsisa = 0
for i in range(m):
    for j in range(n):
        print(arrmusuh[i][j], end=" ")
        if arrmusuh[i][j] == "X":
            musuhsisa += 1
    print()

if musuhsisa > 0:
    print(f"nona deb kalah, masih ada musuh {musuhsisa}")
else:
    print(f"Nona Deb menang")

3.
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