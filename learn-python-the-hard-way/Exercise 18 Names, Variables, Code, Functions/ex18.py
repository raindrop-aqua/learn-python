# this one is like your scripts with argv
def print_two(*args):
	argument1, argument2 = args
	print "argument1: %r, argument2: %r" % (argument1, argument2)

# o.k., that *args is actually pointless, we can just do this.
def print_two_again(argument1, argument2):
	print "argument1: %r, argument2: %r" % (argument1, argument2)

# this just takes one argument.
def print_one(argument1):
	print "argument1: %r" % (argument1)

# this one takes no argument.
def print_none():
	print "I got nothing."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
