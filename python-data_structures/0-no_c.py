def no_c(my_string):
    contain = []
    for char in my_string:
        if char != 'c' and char != 'C':
            contain.append(char)
    result = ''.join(contain)
    return result

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))