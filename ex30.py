# ex30.py

people = 30 
cars = 40
buses = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That too many buses."
elif buses < cars:
    print "Maybe we shoult take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

if cars > people and buses > people:
    print "We just take the buses."
elif cars < people and buses < people:
    print "We shout take buses in line / in the queue."
else:
	print "We can fly."

if cars > people and buses > people:
    print "We just take the buses."
elif cars < people or buses < people:
    print "We shout take buses in line / in the queue."
else:
	print "We can fly."



