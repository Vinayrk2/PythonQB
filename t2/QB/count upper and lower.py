def countUpperLower(str):
    upper = lower = 0 

    for i in str:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1

    return [upper,lower]


str = input("Enter A String : ")
result = countUpperLower(str)
print("Upper : ",result[0],"Lower : ",result[1])