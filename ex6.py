# defines variable x as a string containing a number
x = "There are %d types of people." % 10
# defines variable as text
binary = "binary"
do_not = "don't"
# defines variable as a string containing two previous strings
y = "Those who know %s and those who %s." % (binary, do_not)

# prints variables x and y
print x
print y

# prints text containing the x variable string
print "I said: %r." % x
print "I also said: '%s'." % y

# defines a variable with a condition
hilarious = False
# defines a variable which will print the result of a defined variable.
joke_evaulation = "Isn't that joke so funny?! %r"

# prints 1 variable and gives the varibale condition for this variable.
print joke_evaulation % hilarious

# defines two variables
w = "This is the left side of..."
e = "a string with a right side."

# prints the result of adding the two variables together.
print w + e
