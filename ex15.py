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

txt.close()

# prompts user to supply the filename again.
print "Type the filename again:"
file_again = raw_input("> ")

# defines variable which contains the result of the open function of the previously supplied filename
txt_again = open(file_again)

# uses read function to then print the contents of the previously give file.
print txt_again.read()

txt_again.close()

