# ex19_1.py

def dog_and_cat(cute_dog, cute_black_cat):
    print "I have %d dog!" % cute_dog
    print "I have %d cat!" % cute_black_cat
    print "There are so funny!"
    print "That play a game.\n"

print "I cant just give the function numbers directly:"
dog_and_cat(5, 6)


print "Or, we can use variables from our script:"
count_dog = 8
count_black_cat = 10
dog_and_cat(count_dog, count_black_cat)


print "We can even do math inside too:"
dog_and_cat(5 + 7, 8 + 10)


print "And we can combine the two, variables and math:"
dog_and_cat(count_dog + 100, count_black_cat + 1000)






