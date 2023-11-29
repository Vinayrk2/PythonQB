# Required Arguments : We ust asign values to all it's parameter. In a specified order.

def func(a,b):
    # Doc string
    """ This function prints firstArg - secondArg """

    print(a-b)
    return 

func(10,5)
func(5,10)
print(func.__doc__)

# default Arguments : We can assign values to the arguments, but only from the last.

def func(a,b=5):
    # Doc string
    """ This function prints firstArg - secondArg """

    print(a-b)
    return 

func(10)
func(5)
print(func.__doc__)


# Keyword argument : We can assign values to the arguments, in in formal order. 

def func(a=0,b=0):
    # Doc string
    """ This function prints firstArg - secondArg """

    print(a-b)
    return 

func(b=10,a=50)
func(a=5)
print(func.__doc__)

# Arbitrary Arguments : when we don't know in advance how many args to pass. We use *refer in parameter.

def func(a,*values):
    # Doc string
    """ This function prints firstArg - secondArg  thiz is arbitrary """
    sum = a

    for i in values:
        sum += i
    return sum

print(func(10,50))
print(func(10,20,4))
print(func.__doc__)

# **args

def func(**values):
    # Doc string
    """ This function prints firstArg - secondArg """

    for i in values:
        print(i)

    for (key,value) in values.items():
        print(f"{key} -> {value}")

arg = {"india":"hindi","USA":"English","Pakistan":"Urdu"}
print(type(arg))

print(func(india="hindi",USA="English",Pakistan="Urdu"))
print(func(a=10,b=20,c=4))
print(func.__doc__)
