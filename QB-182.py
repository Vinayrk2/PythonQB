# Write a python program to print all numbers between 1 and 100 (including 1 and 100) that are both,
# Disarium and Harshad  numbers

# disarium = 172 = 1^1 + 7^2 + 2^3 = 172

for i in range(1,101):
    sum = 0
    div = 1
    temp = i
    rem = 0
    length = len(str(i))
    harshad = 0
    while(i!=0):
        rem = i%10
        sum = sum + (rem**length)
        length -= 1
        i //= 10
        harshad += rem

    if(temp % harshad == 0 and temp == sum):
        print("Harshad Number and disaster number both : ",temp)
