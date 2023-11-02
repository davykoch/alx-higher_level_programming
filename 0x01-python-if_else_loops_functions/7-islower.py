#!bin/usr/python3
def islower(c):
    return 97 <= ord(c) <= 122


print(islower('a'))
print(islower('A'))
print(islower('z'))
print(islower('Z'))
