def encrypt(plain,key):
    enc = ""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in plain:
        if letter in alpha:
            enc += alpha[(alpha.find(letter) + key)%len(alpha)]
        else:
            enc += letter
    return enc

plain = input("Enter The Message: ").upper()
key = int(input("Key? "))

print(encrypt(plain,key))