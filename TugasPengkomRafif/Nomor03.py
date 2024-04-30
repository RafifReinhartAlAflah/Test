#program mencari suhu dalam berbagai jenis konversi
#kamus
#TC = float
#Kode = str

# input
Kode = input("Masukkan konversi(F/R/K): ")
TC = float(input("Masukkan nilai suhu celcius: "))

# proses
if   Kode == "F":
    convert = (9/5*TC) + 32
elif Kode == "R":
    convert = (4/5*TC) 
elif Kode == "K":
    convert = (TC+273) 

print(f"Konversi suhu dari derajat celcius ke {Kode} adalah {convert}")