# Loop through prime numbers from 1 to 200 and print them only

for i in range(1, 200):
    for x in range (2, i):
        if i % x == 0:
            break
        else:
            print(i)
    