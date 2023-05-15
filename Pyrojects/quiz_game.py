print("Welcome to my computer quiz!")

prompt = input('So, you want to play, kitten? ')
if prompt.lower() != "yes":
    quit()
else:
    print("OK, Let's play!")

score = 0

answer = input('What\'s the color of the night? ')
if answer.lower() != "sanguine":
    print("Incorrect!")
else:
    print("You got it!")
    score += 1

answer = input('What color is the sky? ')
if answer.lower() != "blue":
    print("Incorrect!")
else:
    print("You got it!")
    score += 1

answer = input('Do kids like chocolate? ')
if answer.lower() != "yes":
    print("Incorrect!")
else:
    print("You got it!")
    score += 1

print("You got " + str(score) + " correct answers!")





