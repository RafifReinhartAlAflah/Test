# n > x (< 1000)
# n < y (< 1000) and (n % 3 == 0 or n % 4 == 0)

x = int(input())
y = int(input())
Arr1 = [x for i in range(y-x+1)]
# print(Arr1)
i = 0

if y-x < 0 :
    print("Tidak Ada")
else:
    while i < (len(Arr1)-1):
        x += 1
        Arr1[i+1] = x 
        # print(Arr1[i])
        i += 1
    # print(Arr1)
    ada = 0
    j = 0
    while j < (len(Arr1)) :
        if Arr1[j] % 3 == 0 or Arr1[j] % 4 == 0 :
            ada += 1
            j += 1
        else :
            ada += 0
            j += 1
    
    if ada > 0 :
        print(ada)
    else :
        print("Tidak Ada")
