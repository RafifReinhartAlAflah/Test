N=int(input())
a = list(map(int, input("").split()))

j = 0
simpan = 0
eksekusi = 0
while j < N :
    if a[j] > 10 :
        simpan += a[j]%10
        a[j] = a[j] // 10
        if a[j] > 10 :
            j += 0
            eksekusi += 1
        else:
            simpan += a[j] 
            j += 1
    else : #len(a[j]) == 1
        j += 1

print(eksekusi)
