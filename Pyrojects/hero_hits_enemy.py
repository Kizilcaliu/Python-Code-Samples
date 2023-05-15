import random

elife = 4 + random.randint(1, 3)
hdmg = 1 + random.randint(1, 4)

while True:
    input("Press enter to start")
    print(" ")  # this line for style purpose
    print("Your enemy has", elife, "life.")
    print("You hit for", hdmg, "damage.")
    elife = elife - hdmg

    if elife <= 0:
        print("Your enemy is dead")
        break
    print("Enemy has", elife, "life left.")
    print(" ")  # this line for style purpose
