# Print following pattern using nested while loops
'''
* 
* * 
* * * 
* * * *
'''
i = 1
# outer while loop
# 4 rows in pattern
while i < 10:
    print(i, end = " ")
    j = 0
    # nested while loop
    while j < i:
        print(j, end=" ")
        #print('*', end='  ')
        j += 1
    # end of nested while loop
    # new line after each row
    print('')
    i += 1