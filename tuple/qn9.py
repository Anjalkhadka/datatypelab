'''Write a Python program to convert a list to a tuple.'''
def convert(list):
    return (*list, )

list = [1, 2, 3, 4]
print(convert(list))