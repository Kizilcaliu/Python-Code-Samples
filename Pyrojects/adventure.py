experience = 0

name = input("Whoa, you dare disturbing my meditation! Who you might be? Quick, tell me your name before I turn you "
             "into a frog..")
print("Ah, so you are called", name.capitalize() + ", not that I care. But as it happened, I might need a small favour to ask.")
favour = input("Tell me if you are interested. Make it quick, yes or no?").lower()
if favour == "yes":
    print("I should think so too..")
    favour = input("Go and stand near that altar, over there. And whisper the words \"Abra Cadabra\" once you "
                   "are there ")
    abra = "Abra Cadabra"
    if favour == abra.lower(): 
        print("Watch out! *Before the master arcanist finished his warning, you see a puff of smoke before yourself*")
        print("Although a scary experiment, master's study proves to be positive. Maybe, not so much fun for you but you gained some experience from this event.")
        experience += 50
elif favour == "no":
    print("Quick! Get off my sight, I thought I could see a spark in you. How terribly wrong observation of mine..")
else:
    print("Go then, and come back when you make your mind up!")
    
    

