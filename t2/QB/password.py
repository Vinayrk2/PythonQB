# password = input("Enter A Password : ")
password = "Vinay@999."
upper = lower = digit = special = 0
num = ''

if len(password)>=8 and len(password)<=15:
    for i in password:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        elif i.isdigit():
            digit+=1
            num += (i)
        elif i == '@' or i == '.':
            special+=1
        else:
            print("Invalid Passowrd")
            break
    
    if(upper > 0 and lower > 0 and special > 0 and digit > 0 and digit < 4 and upper+lower+special+digit == len(password)):
        sum = 0
        print(num)
        exit
        for i in num:
            sum += int(i)
        print(sum)

        # Three digit number 
        d = {0:'zero', 1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
             11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'
             ,20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred'} 

        if len(str(sum)) == 1:
            print(d[(sum)])
        elif len(str(sum)) == 2:
            print(d[(sum)//10*10], d[int(sum)%10])
        elif len(str(sum)) == 3:
            print(d[int(sum)//100*100], d[(int(sum)%100)//10*10], d[int(sum[2])])













        print("Valid Password")
    else:
        print("Invalid Password")
