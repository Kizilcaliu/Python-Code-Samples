from timeit import default_timer as timer

mylist = ['a'] * 1000000

#Bad practise when joining strings
start = timer()
mystring = ''
for i in mylist:
    mystring += i
stop = timer()
print(stop - start)

# Good practise
start = timer()
mystring = ''.join(mylist)
stop = timer()
print(stop - start)

# Formatting strings
var = 3.12567567
var2 = 6
mystring = f"The variable is {var} and {var2}"
print(mystring)
