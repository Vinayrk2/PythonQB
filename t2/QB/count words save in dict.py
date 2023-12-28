string = "Dog the quick brown fox jumps over the lazy dog"
dic = {}

for i in string.split(" "):
    dic[i] = dic.get(i,0) + 1
print(sorted(dic.items(), key=lambda x:x[1],reverse=True))