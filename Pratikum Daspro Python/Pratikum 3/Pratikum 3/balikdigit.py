input = int(input())
neg = input < 0

if neg :
    input = -input

ret = 0

while (input>0) :
    ret = ret * 10 + input%10
    input = input // 10

if neg :
    print(-ret)
else :
    print(ret)
# print(-ret if neg else ret)
