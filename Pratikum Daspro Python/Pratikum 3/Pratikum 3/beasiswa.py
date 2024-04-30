ip = float(input())
pot = float(input()) #1.5 jt

if ip >= 3.5 :
    print(4)

elif ip < 3.5 and pot < 1.0 :
    print(1)

elif ip < 3.5 and 1.0 <= pot < 5.0 :
    if ip >= 2 :
        print(3)
    else :
        print(2)

else :
    print(0)