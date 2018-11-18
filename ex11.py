# ex11.py

print "How old are you?",
age = raw_input()
print "How tall are you?",
# height = raw_input()
height = int(raw_input())
print "Your height plus 1 is {}".format(height + 1)
print "How much do you weigh?",
weight = raw_input()
print "So, you are %r old, %r tall and %r heavy." % (
	age, height, weight)

