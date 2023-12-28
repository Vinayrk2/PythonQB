stri = input("Enter A String : ")

count = sum = 0
for i in stri:
    
    if i.isdigit():
        sum += int(i)
        count+=1
else:
    print(sum,sum/count)