# number of cars
cars = 100
# number of seats per car
space_in_a_car = 4
# nubmer of drivers
drivers = 30
# number of passengers
passengers = 90
#number of cars not driven is total cars minus the available drivers
cars_not_driven = cars - drivers
#number of cars driven is equal to the number of available drivers
cars_driven = drivers
#carpool capacity is the number of cars that can be driven multiplied by the space available in the cars
carpool_capacity = cars_driven * space_in_a_car
# the average number of passengers in the cars is the number of the passengers divided by the number of the number of cars that can be driven.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
