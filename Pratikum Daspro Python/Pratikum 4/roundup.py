def terkecil_kedua(a, x):
    kecil1 = 1001
    kecil2 = 1001
    for i in a:
        if i > x:
            if i < kecil1:
                kecil2 = kecil1
                kecil1 = i
            elif i < kecil2:
                kecil2 = i
    return kecil2

N=int(input())

if N <= 0 or N>100:
    print ("Tidak valid")
else:
    a = list(map(int, input("").split()))
    x = int(input())
    hasil = terkecil_kedua(a,x)   
    if hasil == 1001:
        print(-1)
    else:
        print(hasil)
