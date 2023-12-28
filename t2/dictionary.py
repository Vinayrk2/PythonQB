# Dictionary characteristics
"""
    - MUTABLE
    - INDEXING HAS NO MEANING
    - KEYS CAN'T BE DUPLICATED
    - KEYS CAN'T BE MUTABLE ITEMS
"""

# dict = {'name':"vinay",(0,1):"rahul",1:"chandu"}
# print(dict[1])
# print(dict['name'])
# print(type(dict[(0,1)])) # Str
# print(type(dict))

# dic = dict([('name',"vinay"),(0,1),"rahul","pri"])

dic = dict([("name","vinay"),("age",20),("name","rahul")])
dic["name"] = "chandu"
print(dic)

"""
    deleting key value pair : popitem
    deleting by key : pop
    clean : clear [ No error for printing it ]
    del : for deleting individual or all
"""
# dic.pop("name")
# print(dic.popitem())
# del dic["name"]
# del  dic # error for printing
# dic.clear()
# print(dic)

"""
    Iterations in dictionary
"""

#  Membership
# print("name" in dic) # True
# print("chandu" in dic) # False

# Loop
# for i in dic:
    # print(i,dic[i])
# print(len(dic))
# print(sorted(dic))
# print(min(dic))
# print(max(dic))
# print(sum(dic)) # unsupported operand type(s) for +
# print(dic.items()) # dict_items([('name','age' ), ('chandu', 20)])
# print(dic.values()) # dict_values(['vinay', 20])
# print(dic.keys()) # dict_keys(['name', 'age'])

# for i,j in dic.items():
    # print(i,j)

# dic2 = {"name":"mohamed"}
# dic.update(dic2)
# print(dic)

# setdefault
# print(dic.setdefault("nikname","unknown"))

# fromkeys
# keys = [1,2,3]
# dVal = 0

# dic1 = dict.fromkeys(keys,dVal)
# dic1 = dict.fromkeys("vin",5)

# Dictionary comprehension

# print({i:i**2 for i in range(5)})
#  {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

dic = {"a":23, "v":99,"al":100}
print({k:v**2 for k,v in dic.items()})

# zip 
# days = ['sun','mon','tue']
# temp = [34,56,78]

# print(dict(zip(days,temp)))

# print comprehension loop in loop
# print({i:{j:j*i for j in range(1,11)} for i in range(2,5)})

# Program for getting the most unique value in a dictionary

# dic  = {"camp":[5,7,9,4,0],"is":[6,7,2,3,3],"Best":[9,9,6,5,5]}

# max = 0
# key = ''
# for i in dic:
#     if len(set(dic[i])) > max:
#         max = len(set(dic[i]))
#         key = i
# print(key)

# Program to replace the string with the given dictionary value

def replace_string_with_dict_value(string, dictionary):
    """
    Replace substrings in 'string' that are keys in 'dictionary' with their corresponding values.

    :param string: The string where the replacements will be made
    :param dictionary: The dictionary with keys and their corresponding values to replace in the string
    :return: A new string with the substrings replaced by the dictionary's values
    """
    for key, value in dictionary.items():
        string = string.replace(key, str(value))
    return string

# Example usage:
# my_string = "Hello world! Have Hello Hello a great day!"
# my_dict = {"Hello": "Hi", "great": "wonderful"}
# new_string = replace_string_with_dict_value(my_string, my_dict)
# print(new_string)  # Output: Hi world! Have a wonderful day!

# def repl_str(my_string,my_dict):
#     new_str = ''
#     for i in my_string.split():
#         if i in my_dict:
#             new_str = new_str + my_dict[i]
#         else:
#             new_str = new_str + i 
#         new_str += " "
#     return new_str
        

# my_string = "Hello world! Have Hello Hello a great day!"
# my_dict = {"Hello": "Hi", "great": "wonderful"}
# new_string = repl_str(my_string, my_dict)
# print(new_string)  # Output: Hi world! Have a wonderful day!

# List of list to dictionary

# lis1 = ["camp","is","Best",8]
# lis2 = ["name","des"]

# res = []
# for i in range(0,len(lis1),2):
#     res.append({lis2[0]:lis1[i],lis2[1]:lis1[i+1]})

# print(res)



