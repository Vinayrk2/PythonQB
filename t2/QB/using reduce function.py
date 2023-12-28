from functools import reduce

l = eval(input("Ener A List :"))
ans = reduce(lambda x,y:x*y,l)
print(ans)