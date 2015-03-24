#print "How many passes do you want to complete?"
#passes = int(raw_input("> "))

#print "How much should be added at each pass?"
#addition = int(raw_input("> "))

runs = 5
plus =10
i = 0
numbers = []

def while_func(passes, addition):
     global i
     while i < passes:
         print "At the top i is %d" % i
         numbers.append(i)

         i = i + addition
         print "Numbers now: ", numbers
         print "At the bottom i is %d" % i

#print "How many passes do you want to complete?"
#runs = int(raw_input("> "))

#print "How much should be added at each pass?"
#plus = int(raw_input("> "))

while_func(runs, plus)

print "The numbers: "

for num in numbers:
     print num
