# Balanced String in python,.
string1 = "LJUNC"
string2 = "LCUNJ"

if len(string1) == len(string2):
    for i in string1:
        if i in string2:
            continue
        else:
            print("Not Balanced")
            break
    else:
        print("Balanced")
else:
    print("Not Balanced")