string = "hello this is a python program to get dict values according to the string"
dic = {}

for i in string.split(" "):
    dic[i[0]] = dic.get(i[0],[])
    dic[i[0]].append(i)


print((sorted(dic.items(), key=lambda x:len(x[1]))))