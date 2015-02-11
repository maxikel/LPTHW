from sys import argv

script, filename = argv

txt = open(filename)

print "Here is the contents of the file"
print txt.read()
