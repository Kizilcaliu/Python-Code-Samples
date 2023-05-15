name = 'Jesaa29Roy'
size = len(name)
i = -1
name = name.lower()

# iterate loop till the last character
while i < size - 1:
    i = i + 1
    # skip while loop body if current character is not alphabet
    if not name[i].isalpha():
        print(end = " ")
        continue
    # print current character
    else:
        name = name.title()
        print(name[i], end=' ')