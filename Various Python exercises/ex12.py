i = 1
# outer while loop
while i < 5:
    # nested for loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')
    i = i + 1