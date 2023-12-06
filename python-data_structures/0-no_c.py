'''
def no_c(my_string):
    contain = []
    for char in my_string:
        if char != 'c' and char != 'C':
            contain.append(char)
    result = ''.join(contain)
    return result
'''
'''
def no_c(my_string):
    for char in my_string:
        if char == 'c' or char == 'C':
            my_string.pop
    result = no_c
    return result

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
'''


def no_c(my_string):
    result = ""
    for char in my_string:
        if char.lower() != 'c':
            result += char
    return result

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))