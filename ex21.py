# ex21.py

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


print "Let's do some math with just functions!"

age = add(30, 5) 
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, Iq: %d" % (age, height, weight, iq)


# A pizzle for the extra credit, type it in anyway.
print "Here is a pizzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That's become:", what, "Can you do it by hand?"





