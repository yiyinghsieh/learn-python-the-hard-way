# ex16.py

from sys import argv
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that , hit RETURN."

raw_input("?")

print "Open the file..."
# target = open(filename, 'r')  # Readable only.
target = open(filename, 'w')  # Write only.
# target = open(filename, 'a')    # Could append.

print "Truncating the file.  Goodbye!"
# target.truncate()  # No need with 'w'.

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally we close it."
target.close()
