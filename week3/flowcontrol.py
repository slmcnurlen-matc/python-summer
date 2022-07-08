#!/usr/bin/env python3
"""
Sam McNurlen
This script is a short text-based game made using Python.
"""

print("""You enter a dark room with three doors.
Do you go through door 1, 2 or 3?""")


door = input("-> ")

# == Door Number 1 Logic =====================
if door == "1":
    print("\nThere's a giant creature here eating a cheese cake.")
    print("What do you do?\n")

    print("1. Take the cake.")
    print("2. Scream at the creature.")

    # == Monster Logic ==========================
    monster = input("-> ")

    if monster == "1":
        print("\nThe creature tears your face off. Good job!")
    elif monster == "2":
        print("\nThe creature tears your legs off. Good job!")
    else:
        print(f"\nWell, doing {monster} is probably better.")
        print("The creature disappears into the dark.")

# == Door Number 2 Logic =====================
elif door == "2":
    print("\nYou stare into the endless abyss at Cthulhu's retina. \n")

    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    # == Insanity Logic ======================
    insanity = input("-> ")

    if insanity == "1" or insanity == "2":
        print("\nYour body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("\nThe insanity rots your eyes into a pool of muck.")
        print("Good job!")

# == Door Number 3 Logic =====================
elif door == "3":
    print("\nYou have entered some kind of laboratory. A scientist is working on something nearby. \n")

    print("1. Ask him about the washing machine he's screwing a transistor onto.")
    print("2. Ask him about the 9-foot tall corpse stitched together on his table.")

    # == Mad Scientist Logic =================
    lab = input("-> ")

    if lab == "1":
        print("\nHe shoves you inside and teleports you to Mars, where you instantly freeze to death.")
        print("Good job!")
    elif lab == "2":
        print("\nHe straps you down and transfers your brain into the corpse.")
        print("Congratulations! You are now an affront against nature.")
    else:
        print(f"\nYeah, doing {lab} is probably better.")
        print("The scientist is undone by his own hubris.")

else:
    print("You did not select a door??? Good Call :)")