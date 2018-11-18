# ex5.py

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'


print "Let's talk about %s." % my_name
print "He's %d inches tell." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heave."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "He's teeth are really %s depending on the coffee." % my_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

# ===
print "\nAnother way: Formatted String!"

print "Let's talk about {}".format(my_name)
print "He's {} inches tell.".format(my_height)
print "He's {} pounds heavy.".format(my_weight)
print "Actually that's not too heave."
print "He's got {0} eyes and {1} hair.".format(my_eyes, my_hair)
print "He's teeth are really {} depending on the coffee.".format(my_teeth)

# This line is tricky, try to get it exactly right
print "If I add {0}, {1}, and {2} I get {3}.".format(
    my_age, my_height, my_weight, my_age + my_height + my_weight)
