#program mencari sisi miring phytagoras
#kamus
#a,b,c = int

# input
a = int(input("Masukkan nilai alas: "))
b = int(input("Masukkan nilai tinggi: "))

# proses
c = ((a**2) + b**2)**(1/2)

print(f"Sisi miring dari segitiga siku-siku adalah {c}")