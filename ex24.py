# ex24.py

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s." % five

def secret_formula(s, a):
    _beans = s * 500 + a
    _jars = _beans / 1000.0
    _crates = _jars / 100.0
    return _beans, _jars, _crates

add = 1000
started = 10000
#start_point = 10000
beans, jars, crates = secret_formula(started, add)

print 'beans: {}'.format(beans) 
print 'jars: {}'.format(jars)
print 'crates: {}'.format(crates)

print "What a starting point of: %d" % started #start_point
print "We'd have {0} beans, {1} jars, {2} crates.".format(beans, jars, crates)

started2 = started / 10.0
add2 = add / 10.0
beans2, jars2, crates2 = secret_formula(started2, add2)

print "We can also do that this way:"
print "We'd have {0} beans, {1} jars, {2} crates.".format(beans2, jars2, crates2)
