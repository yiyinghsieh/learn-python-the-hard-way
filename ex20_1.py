# ex20_1.py

from sys import argv

script, my_file = argv

def print_allof(p):
	print p.read()

def rewind(p):
	p.seek(0)

def print_a_line(line_count, p):
	print line_count, p.readline()

new_file = open(my_file)

print "First let's print the whole file:\n"

print_allof(new_file)

print "Now let's rewind, kind of like a tape."

rewind(new_file)

print "Let print three lines:"

current_line = 1
print_a_line(current_line, new_file)

current_line = current_line + 1
print_a_line(current_line, new_file)

current_line = current_line + 1
print_a_line(current_line, new_file)


