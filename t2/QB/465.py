"""
    program to count number of strings, len>3 and first and last character must be same
"""

l = ["abc",'aba','12345','121','vsfvdvdcv']
count = 0
for i in l:
    if(len(i) == 3 and i[0] == i[-1]):
        count+=1
print(count)
    