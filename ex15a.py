# imports argv module from sys
from sys import argv

# defines arguments of argv
script, filename = argv

# creates a variable txt by opening a filename
txt = open(filename)

# prints the filename as give in teh 2nd argument on the command line.
print "Here's your file %r:" % filename
# uses read function to get the text from the file specified in the txt variable
print txt.read()
