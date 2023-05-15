# Tuple : ordered, immutable, allows duplicate elements.
# Working with large data, a tuple can be more efficient as it is immutable. So less chances of messing up.
mytuple = ('Max')
print(type(mytuple)) # If you dont put a comma after the first element type becomes a str.

mytuple = ('Max',)
print(type(mytuple)) # This is the correct way to create a tuple with only one element.

# Slicing a tuple example.
mytuple = (0, 1, 2, 3, 4, 5)
i1, *i2, i3 = mytuple

print(i1)
print(i3)
print(i2)

# A tuple covers less space than a list
import sys
mylist = [0, 1, 2, 'hello', True]
mytuple = (0, 1, 2, 'hello', True)

print(sys.getsizeof(mylist), 'bytes')
print(sys.getsizeof(mytuple), 'bytes')

# A tuple is quicker
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 'hello', True]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 'hello', True)", number=1000000))











