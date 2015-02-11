def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some maths with just some functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it anyway.
print "Here is a puzzle"

what_1 = add(age, subtract(height, multiply(weight, divide(iq, 2))))

what_2 = add(35,  subtract(74,     multiply(180,    divide(50, 2))))

what_3 = add(35,  subtract(74,     multiply(180,    25)))

what_4 = add(35,  subtract(74,     4500))

what_5 = add(35, -4426)

what_6 = -4391

print "That becomes: ", what_1, "Can you do it by hand?"

print what_2

print what_3

print what_4

print what_5

print what_6

new = 24 + 34 / 100 - 1023

print new

a = 24
b = 34
c = 100
d = 1023

new_1 = a +  b / c -d

print new_1


new_2 = add(a, b)

print new_2


def formula(a, b, c, d):
    print "%d + %d / %d - %d" % (a, b, c, d)
    return a + b / c - d

print formula(24, 34, 100, 1023)



