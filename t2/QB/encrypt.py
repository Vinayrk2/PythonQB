def encrypt(string,key):
    l = []
    for i in range(key):
        l.append(string[i::key])
    return "".join(l)

def decrypt(string, key):
    l = []
    for i in range(key):
        l.append(string[i::key])

string = "This is python, a programming language"
key = 4

# print(encrypt(string,key))
# print(decrypt(encrypt(string,key),key))

# l = [1,2,3,4]
# b = l[:]
# print(id(l),id(b))

st = "this is a string"
# convert abc in st to xyz letter
# translation_table = str.maketrans('abc', 'xyz')
# st = st.translate(translation_table)

trans = str.maketrans('abc','xyz')
st = st.translate(trans)
print(st)