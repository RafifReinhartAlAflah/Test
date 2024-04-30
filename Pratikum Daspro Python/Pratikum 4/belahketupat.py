def benar (n):
    if n <= 0 or n % 2 == 0:
        return False
    else:
       return True 
def belahketupat (n):
    for i in range (N):
        if i < N // 2: 
            print(" " * ((N // 2) - i), end="")
            print("*" * (2 * i + 1))
        else:
            print(" " * ((N // 2) - (N - i - 1)), end="")
            print("*" * (2 * (N - i - 1) + 1))  

N = int(input())
if benar (N):
    belahketupat(N)
else:
    print("Masukan tidak valid")