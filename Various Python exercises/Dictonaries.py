# Dictionary: key-value pairs, unordered, mutable
mydict = {'name' : 'Max', 'age': 28, 'city' : 'New York'}
print(mydict)

value = mydict["age"] # Looking up a value of a dictionary
print(value)

for value in mydict:
    print(value)
    
print('\n')

for key in mydict:
    print(key)