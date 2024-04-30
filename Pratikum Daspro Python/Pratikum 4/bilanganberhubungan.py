n = int(input()) #banyak bilangan
x = int(input()) #bil yang dekat dengan n
Aoa = list(map(int,input("").split()))
AoS = [0 for i in range (n)]

#mencari yang sama
i = 0 
sama = 0
while i < n-1 :
    if Aoa [i] == x :
        sama += 1
        i += 1
    else :
        sama += 0
        i += 1
  
i= 0
while i < n:
    AoS[i] = Aoa[i]
    i += 1

print(AoS)
i = 0
while i < n:
    AoS[i] = abs(AoS[i] - x)
    i += 1
# print(AoS)

i = 0 
simpan = 0
while i < n-1 :
    if AoS[i] > AoS[i+1]:
        simpan = Aoa[i]
        Aoa[i] = Aoa[i+1]
        Aoa[i+1] = simpan
        i += 1
    else:
        i += 1

if sama > 0 :
    print(x)
else :
    print("TIDAK ADA")


# print(AoS)
print(Aoa[n-1])



    