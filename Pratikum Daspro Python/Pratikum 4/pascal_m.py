N=int(input())
M=int(input())

def segitiga_pascal(N, M):
    pascal = [[M]]
    for i in range(1,N):
        baris_inisial = pascal[-1]
        baris_baru = [M]
        for j in range(1, i):
            baris_baru.append(baris_inisial[j-1] + baris_inisial[j])
        baris_baru.append(M)
        pascal.append(baris_baru)
    return pascal
pascal_triangle = segitiga_pascal(N, M)
for row in pascal_triangle:
    print(" ".join(map(str, row)))