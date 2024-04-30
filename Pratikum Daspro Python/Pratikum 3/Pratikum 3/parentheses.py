stack = []
input = input()

for i in input :
    if i == '(' or i == '[' or i == '{' :
        stack.append(i) #menambah string '(' or '[' or '{' ke dalam array ke-i
        continue #mirip i += 1, tapi 'continue' untuk penambahan string += 1
    
    if len(stack) == 0 :
        stack.append('d') #kenapa 'd' nya ngaruh ?
        break #keluar loop
    
    if i == ')' and stack[-1] == '(' :
        stack.pop() #mengeluarkan string yang sepasang '() or {} or []' dari array 
    elif i == ']' and stack[-1] == '[' :
        stack.pop() #mengeluarkan string yang sepasang '() or {} or []' dari array 
    elif i == '}' and stack[-1] == '{' :
        stack.pop() #mengeluarkan string yang sepasang '() or {} or []' dari array 
    else : 
        break
    
if len(stack) == 0 :
    print('valid')
else:
    print('tidak valid')