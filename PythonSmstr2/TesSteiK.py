b = float(input()) #budget
n = float(input()) #normal/vip
p = float(input()) #banyak orang yg ikut

normal = 0
vip = 0

if b < 25 :
    print("TIDAK")
else :
    print("YA")

if n == 0 :
    if 1<=p<=4 :
        normal = 25 - 25 * 0.1
    elif 5<=p<=10 :
        normal = 25 - 25 * 0.15
    elif 11<=p<=20 :
        normal = 25 - 25 * 0.15
    elif 21<=p<=30 :
        normal = 25 - 25 * 0.15
    else :
        normal = 25 - 25 * 0.3

elif n == 1 :
    if 1<=p<=4 :
        vip = 100 - 100 * 0.1
    elif 5<=p<=10 :
        vip = 100 - 100 * 0.15
    elif 11<=p<=20 :
        vip = 100 - 100 * 0.15
    elif 21<=p<=30 :
        vip = 100 - 100 * 0.15
    else :
        vip = 100 - 100 * 0.3

if n == 0 :
    total = normal * p
    print(f"{b-total:.2f}")
elif n == 1 :
    total = vip * p
    print(f"{b-total:.2f}")

    