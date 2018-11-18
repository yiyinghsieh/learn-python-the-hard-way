# ex18_1.py

def cute_dog(name):
    print "dog name: %r" % name

def cute_dog_cat(dog, cat):
    print "dog name: %r, cat name: %r" % (dog, cat)

def cute_none():
    print "Nothing is here."

cute_dog("Biru")
cute_dog_cat("Biru", "Beefnoodle")
cute_none()
