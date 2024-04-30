# romawi = input()
# n = 0
# ToC = [0 for i in range(len(romawi))]

# #masukin data
# for i in range (len(romawi)) :
#     if romawi[i] == "I" :
#             ToC[i] = 1
        
#     elif romawi[i] == "V" :
#             ToC[i] = 5
            
#     elif romawi[i] == "X" :
#             ToC[i] = 10
            
#     elif romawi[i] == "L" :
#             ToC[i] = 50
            
#     elif romawi[i] == "C" :
#             ToC[i] = 100
            
#     elif romawi[i] == "D" :
#             ToC[i] = 500
            
#     elif romawi[i] == "M" :
#             ToC[i] = 1000


# if len(romawi)%2 == 0 :
#        for i in range (0,len(romawi), 2) :
#                if  ToC[i] < ToC[i+1] :
#                        n += ToC[i+1]-ToC[i]
#                else :
#                        n += ToC[i+1]+ToC[i]

# else :
#         n += ToC[0]  
#         for i in range (1,len(romawi),2) :
#                 if ToC[i] < ToC[i+1] :
#                        n += ToC[i+1]-ToC[i]
#                 else :  
#                        n += ToC[i+1]+ToC[i]
# print (n)

#cara lain

hash = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
}

s = input()
ret = 0

for i in range (len(s)) :
    c = s[i]
    if ((i + 1) < len(s) and hash[s[i+1]] > hash[c]) :
        ret -= hash[c]
    else:
        ret += hash[c]

print(ret)