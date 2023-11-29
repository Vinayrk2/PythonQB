# rite a python program to read three numbers (a,b,c) and check how many numbers between ‘a’ and ‘b’ are divisible by ‘c’.

a = int(input("Ebter A Number : "))
b = int(input("Ebter A Number : "))
c = int(input("Ebter A Number : "))

print("This numbers are divisible by c : 1")
for i in range(a,b+1):
    if i % c == 0:
        print(i)