# ex13.py

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# line 13 to line 24 extra exercise
print "(1) {}, (2) {}, (3) {}".format(first, second, third)

raw_input("So we call (1):")
raw_input("So we call (2):")
raw_input("So we call (3):")

ex13 = raw_input("The script is called:")
bowen = raw_input("Your first variable is:")
ivy = raw_input("Your seond variable is:")
we = raw_input("Your third variable is:")
print "So this is called %s module, the first is %s, then is %s, the last is %s." %(
	ex13, bowen, ivy, we)
