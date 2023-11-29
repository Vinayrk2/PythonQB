num = int(input("Enter a Product : "))

for i in range (100000,1000000):
    temp = 1
    for digit in str(i):
        temp *= int(digit)
    if(temp==num):
        print(i)