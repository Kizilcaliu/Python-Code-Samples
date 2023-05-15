for i in range(1,200):
    if i > 1:
        for x in range(2, i):
            if i % x == 0:
                break
        else:
            print(i)
    else:
        continue
        
        
        