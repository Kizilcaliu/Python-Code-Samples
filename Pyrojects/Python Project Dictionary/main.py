# Dictionary data set.
dictionary = {
    "this": ("zamir","bu, su"),
    "is": ("fiil", "olmak"),
    "a": ("belirtec", "bir"),
    "book": ("isim", "kitap"),
    "pen": ("isim", "kalem")
}

# When we wrap all the code in a while loop, we can get an infinite.
while True:
    # Asks user to enter a sentence
    sentence = input("Bir cumle giriniz: (Cikmak icin entera basiniz!)")
    # Break condition. If user presses enter without any input that breaks the program.
    if sentence == "":
        break
    # Checks for special characters stated inside single/double quotes using a for loop.
    for signCharacter in ".!?,":
        # Any characters found inside quotes are replaced by an empty string which means deleted.
        sentence = sentence.replace(signCharacter, '')
    # Sentence that the user enters converted into lower case first, then split into individual words. Then stored in a variable called words
    words = set(sentence.lower().split())
    # Iterate through words and check if variable wordsMaxLength (which is set to 1) lesser than word iterator. If yes assign the iterators letter count into wordsMaxLength.
    wordsMaxLength = 1
    for word in words:
        if wordsMaxLength < len(word):
            wordsMaxLength = len(word)
    # Iterate through words and store each into variable calle word. Then get that word from the dictionary dict and store into wordMeaning variable.
    for word in words:
        wordMeaning = dictionary.get(word, "Anlami bulunamadi")
        # Print both the word and its meaning.
        # Print word and leave space after printing the word. Space left equals to the difference of the word and wordsMaxLength. 
        print(f'{word:<{wordsMaxLength}} : ({wordMeaning[0]:^8}) {wordMeaning[1]}')
        
    print()

print('Kullanici cikisi.')