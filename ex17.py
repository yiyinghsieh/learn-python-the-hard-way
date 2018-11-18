# ex17.py

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Coyping from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()
print "in_file: {}".format(in_file)
print "indata: {}".format(indata)

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
inputdata = raw_input("> ")
if inputdata == "":
	pass
else:
	indata = inputdata

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

