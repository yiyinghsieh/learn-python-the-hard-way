# ex21_1.py

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b


print "That do some math use function."

apple = add(2, 5)
orange = subtract(8, 3)
straberry = multiply(4, 2)
vegetable = divide(6, 3)


print "I have %d apple %d orange %d straberry %d vegetable." % (apple, orange, straberry, vegetable)


what = add(apple, subtract(orange, multiply(straberry, divide(vegetable, 2))))
print "That becomes: ", what, "can you do it by hand?"
print "That becomes: %d can you do it by hand?" % what


# c = 1
# d = 2
# print "c: 1 d: 2 c + d = %d" % (c + d)

