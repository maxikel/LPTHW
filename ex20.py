#importing argv module from sys group
from sys import argv

# defines arguments of argv
script, input_file = argv

# create a new definition which reads the contents of a file specified
def print_all(f):
    print f.read()

# create a definition that returns to the start of the file. 
def rewind(f):
    f.seek(0)

# definition that prints a specified line in a specofied file
def print_a_line(line_count, f):
    print line_count, f.readline()

# defines the currnet file as being an open file defined at the command line
current_file = open(input_file)

print "First let's print the whole file: \n"

# carrys out the print_all function which reads the contents of the open input file.
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# carries out rewind function on input file thereby returning to the top of the file.
rewind(current_file)

print "Let's print three lines:"

# prints lines defined in current line.
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

