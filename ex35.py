# ex35.py

from sys import exit

def gold_room():
    print "This room is full of gold.  How much do you take?"

    next = raw_input("> ")
    # if "0" in next or "1" in next:
    if next.isdigit():
        how_much = int(next)
    else:
        # dead("Man, learn to type a number.")
        print "Man, learn to type a number"
        # Recursion.
        gold_room()

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"

    bear_moved = False

    while True:
        print "'take honey' or 'taunt bear' or 'open door'"
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif not bear_moved and next == "taunt bear":
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif bear_moved and next == "taunt bear":
            dead("The bear gets pissed off and chews you leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat you head?"
    print "'flee' or 'head'"

    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("That was tastly!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)


def start():
    print "You are in a dark room."
    print "There is a door to you right and left."
    print "Which one do you take?"
    print "'left' or 'right'"

    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room untial you starve.")


start()









