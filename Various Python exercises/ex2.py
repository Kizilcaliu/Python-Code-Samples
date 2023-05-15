# Print something for each odd number and something else for even numbers. From 0 to 20(inclusive).
num = 0

for i in range(0, 21):
    
    if i % 2 == 0:
        if num != 0:
            print(num, ": This number can be divided by 2")
    else:
        print(num, ": This number can not be divided by 2")
    num += 1