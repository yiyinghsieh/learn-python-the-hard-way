# ex17_1.py

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)
in_file = open(from_file).read()
#indata = in_file.read()
print "indata is %s" % (in_file) # %(indata)
print "the indata is %s bytes long" % len(in_file) # %len(indata)

apple = raw_input("> ")
if apple == "":
    pass
else:
    indata = apple

opennew = open(to_file, "w")
opennew.write(indata)

opennew.close()
#in_file.close()

