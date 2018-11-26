# ex36.py

from sys import exit

def life_door():
    print "You have a job and salary."
    print "How many hours you spend on your work?"
    
    next = raw_input("> ")
    
    if next.isdigit():
        how_hours = int(next)
    else:
        print "You should learn type some number."
        life_door()
        #dead("You should learn type some number.")
    if 5 < how_hours < 9:
        print "Your life is balance, good job!."
        exit(0)
    elif how_hours < 4:
        dead("It's hard to find that kind of job.")
    else:
        dead("It's too diffical on you life.")



def finance_door():
    print "You have some money."
    print "How will you use these money?"
    print "How to make money fast?"
    
    casino_law = False

    while True:
        print "'deposit' or 'invest' or 'gamble'."
        next = raw_input("> ")
        
        if next == "deposit":
            dead("Your money will be eaten by inflation.")
        elif next == "gamble" and not casino_law:
            print "Your money will be confiscated."
        elif not casino_law and next == "invest":
            print "You earned money by your knowledge"
            print "And the gambling law was pass, how do you use them?"
            casino_law = True
        elif casino_law and next == "invest":
            dead("You will lost your invest money, because of financial crisis.") 
        elif next == "gamble" and casino_law:
            print "You earn a lot of easy money."
            life_door()
        else:
            print "I got no idea what that means."


def dead(reason):
    print reason, "Good job!"
    exit(0)


def artist_door():
    print "You must have more special idea."             
    print "You can travel a lot to rich you mind."      
    print "And you spend much time and money in the way."
    print "But you will burn out soon."
    print "Think about next step, turn 'right' or 'left'."
    next = raw_input("> ")
    if "right" in next:
        start()
    elif next == "left":
        dead("You run out of energy.")
    else:
        artist_door()


def start():
    print "Your life have two road."
    print "Both of them are interest."
    print "Which one do you choose?"
    print "'right' or 'left'?"

    next = raw_input("> ")

    if next == "right":
        finance_door()
    elif next == "left":
        artist_door()
    else:
        dead("You stumble around the road until you starve.")


start()


