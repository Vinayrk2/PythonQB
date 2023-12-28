stri = input("Enter A String")

print(" ".join([i for i in stri.split(" ") if len(i)%2 == 0]))