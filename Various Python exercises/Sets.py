# Sets: unordered, mutable, no dupe
myset = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5} # set does not allow dupes so only 1 to 5 prints.
print(myset)
print(type(myset))

for i in myset:
    print(i)
    
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