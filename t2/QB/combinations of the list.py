# Combinations of the list items

l = [1,2,3]
temp = l.copy()

for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l)):
            if(i != j and j != k and i != k):
                print(temp[i], temp[j], temp[k])
print(sum(set(l)))


# for i in range(len(l)):
#     for j in range(len(l)):
#         print(temp)
#         temp.insert(l[i],j)
#         # temp.pop(j+1)
#         temp.pop()
#     print(temp)