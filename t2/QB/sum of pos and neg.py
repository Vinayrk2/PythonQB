l = [23,-43,5,-24,54,-32,4,3,-34]

pos_num = list(filter(lambda x:x>0,l))
neg_num = list(filter(lambda x:x<0,l))
print(sum(pos_num))
print(sum(neg_num))