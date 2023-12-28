# syntax : lambda para : exp

# print((lambda x: x)(10))
# a = lambda x: x**3
# l = [1,2,3,4,5]
# a = lambda x:x**2


# print(a(l[0]))

# l = [1,2,3,4,5]
# find_greater = list(map(lambda x:x>2,l))
# print(find_greater)
# OP : [3, 4, 5]

# l = [1,2,3,4,5]
# find_greater = list(filter(lambda x:x>2,l))
# print(find_greater)
# OP : [False, False, False , True, True]


# import functools

# l = [1,2,3,4,5]
# sum = functools.reduce(lambda x,y: x+y,l)
# print(sum)

# dic = {"a" : 23, "c":54, "b":2}
# print(dic.items())
# print(dict(sorted(dic.items(),key=lambda i : i[1])))
# dic = dict(((2,3),(4,5)))
# print(dic)

# t = ["vishal10", "vishal9", "vishal"]
# print(sorted(t,key=len,reverse=True))
# print(sorted(t,key=len))

# reversed

# t = ['vishal','a',90,3]
# print(list(reversed(t[0])))

# inp = eval(input())
# print(type(inp))

# print(list(sorted([1,2,3,6,4])))


# convert the given string in the list
# l = []
# string = "Hello world"
# l.extend(string)
# l = list(filter(lambda x:x != " ",l))
# print(l)


#  Find the different starting word's first letter and count the number of occurence

# string = "hello this is a demo string to find out how many starting letter to proceed"
# l = string.split(" ")
# dic = dict()

# for i in l:
#     dic[i[0]] = dic.get(i[0],0) + 1     
# print(dic)
# print({v[0]:v for k,v in enumerate(l)})


# string = "vinay"
# print(list(enumerate(list(string))))
