# Lists: ordered, mutable, allows duplicate elements

mylist = ['banana', 'cherry', 'apple']

print(mylist)

# This creates empty list
mylist2 = list()
print(mylist2)

# List allows different data types. Int, bool, string etc..

# List allows same elements. 
mylist = ['apple', 'apple']

# You can use index on a list
item = mylist[0] 

# You can iterate within the loop with for in loop. Note that you can call 'i' on below example anything. 
for i in mylist:
    print(i)
    
# You can check if an item is in a list.
if 'banana' in mylist:
    print('Yes it is in my list.')
else:
    print('No, it isnt in my list.')
    
    
# See how many element in a list using len    
print(len(mylist))

# Append new item to a list
mylist.append('lemon')
print(mylist)

mylist.insert(1, 'blueberry')
print(mylist)

# 'pop' removes last item, 'remove' removes a specific element, 'clear' removes all, 'reverse' reverses all elements
# 'sort' sorts list

mylist = ['apple'] * 5
print(mylist)

# Slicing
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = mylist[1:5] # Start index 1 and stop index 5. If you dont specify a start index it starts from beginning. And equally if you dont specify an end index then it goes all the way to the end
a = mylist[: : -1] # In this example no start nor end index, and there is a step of -1 which mean go in reverse order.
print(a)

# If you want to make a copy of an original list you must use 'copy' method
list_org = ['apple', 'banana', 'cherry']

list_copy = list_org.copy()
list_copy.append('lemon')

print(list_org)
print(list_copy)

# You can use an expression like i*i or anything else in a 'for in' loop like below
mylist = [1,2,3,4,5,6,7,8,9]
b = [ i*i for i in mylist]

print(mylist)
print(b)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

i = evens.intersection(primes)
print(i)










