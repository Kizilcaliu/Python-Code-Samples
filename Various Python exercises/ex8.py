name = 'Jesaa29Roy'
size = len(name)
i = 0

# iterate loop till the last character
while i < size:
    # break loop if current character is number
    # if name[i] == '2': # Use this statement if you want to break loop at character 2 for the same result as below. 
    # be careful 2 is a string here.
    if name[i].isdecimal():
        break;
    # print current character
    print(name[i], end='--')
    i = i + 1