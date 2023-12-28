l = [5,5,2,5,8]
# l.remove(5)
# print(l)
for i,val in enumerate(l):
    temp = l.copy()
    temp.pop(i)

    if(sum(temp[0::2]) == sum(temp[1::2])):
        print("Index to be removed :",i)
        print("The List is balanced : ",temp)
        
    