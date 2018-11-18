# ex22.py

from sys import argv
script, fileman = argv

def music(blue_one):
    print blue_one.read()

current = open(fileman)
music(current)

targetok = open(fileman, 'w')
print "truncating the all goodbye !"

print " Now I will writ some messages."

first = raw_input("1: ")
second = raw_input("2: ")
third = raw_input("3: ")

print "Now I want to write back to my file"

targetok.write(first)
targetok.write("\n")
targetok.write(second)
targetok.write("\n")
targetok.write(third)
targetok.write("\n")

targetok.close()

def add(a, b):
    print "adding: we leave together %d + %d" % (a , b)
    return a + b 

def since(a, b):
	print "subtract: since %d - %d" %(a, b)
	return a - b

long = add(2, 2)    
print "So we had leave together %d years." % long

years = since(2018, 2014)
print "So we had married %d years." % years














