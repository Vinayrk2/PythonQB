"""Write a Python program that prompts the user to enter numbers and stops only when the user enters “stop”. After this, 
print the minimum even, maximum even, average of even number, minimum odd, maximum odd, average of odd
 number 
from among all the numbers entered by the user."""

num = None
Even_min = Even_max = Even_sum = 0
Odd_min = Odd_max = Odd_sum = 0
count_e = count_o = 0

while(num != "stop"):
    num = input("Enter a Number or 'stop' : ")

    if(num == "stop"):
        break
    else:
        num = int(num)

        if(num % 2 == 0):

            if(num == 0):
                break

            # Even
            if(count_e == 0):
                Even_max = num 
                Even_min = num 

            elif(num>Even_max):
                Even_max = num

            elif(num<Even_min):
                Even_min = num

            Even_sum += num
            count_e += 1
        else:
            # Odd

            if(count_o == 0):
                Odd_max = num 
                Odd_min = num 

            elif(num>Odd_max):
                Odd_max = num

            elif(num<Odd_min):
                Odd_min = num

            Odd_sum += num
            count_o += 1

if(count_o != 0 and count_e != 0):
    print("Even : ",Even_max,Even_min,Even_sum/count_e," (Max, Min, Avg)")
    print("Odd : ",Odd_max,Odd_min,Odd_sum/count_o," (Max, Min, Avg)")

else:
    print("Please Enter Atleast one input each")




