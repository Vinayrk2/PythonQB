# string = "HellO WorlD"

# print(string.swapcase())

string = "HellO WorlD 43"

res = ''
for i in string:
    res += (i.upper() if i.islower() else i.lower())
print(res) 
 