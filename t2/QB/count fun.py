# Implementing count function

def countFun(l,sub):
    count = 0

    for i in l:
        if i == sub:
            count += 1
    return count

print(countFun("Hello Dosto",'o'))
print(countFun("Hello Dosto",'t'))