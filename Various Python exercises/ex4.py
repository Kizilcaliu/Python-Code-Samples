count = 0
# run loop till count is less than 5
while count <= 15:
    if count == 0 or count == 5 or count == 10 or count == 15:
        count += 1
        print('Oooop')
        continue
    else:
        print(count)
        count += 1
    