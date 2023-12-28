# string = "hello world"
# print(string.capitalize())
# print(string.count("l"))
# print(string.endswith("lo"))
# print(string.find("l",4))
# print(string.index("l"))
# print(string.isalnum())
# print(string.isalpha())

string = "   hello world   "
# print(string.strip())
count = 0
char = "o"
for i in string:
    if(i == char):
        count += 1
print(count) 

array = [-1, 2, -3, 5, -6, 7, -9, 11]

# This line sorts the array in two steps:
# 1. It places all non-negative numbers before negative numbers.
# 2. Within each group (non-negative and negative), it sorts the numbers by their absolute value.
sorted_array = sorted(array, key=lambda x: (x < 0, abs(x)))

print(sorted_array)  # Output: [2, 5, 7, 11, -1, -3, -6, -9]
string = "Hello World! Hello Hello"
print(string.count("Hello",12,25))
