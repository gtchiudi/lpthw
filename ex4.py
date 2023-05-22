# declare cars and initialize to 100
cars = 100
# declare space and initialize to 4.0. Floating point
space_in_a_car = 4.0
# declare drivers initialize to 30
drivers = 30
# declare passengers and initialize to 90
passengers = 90
# declare cars_not_driven and initialize to cars - drivers
cars_not_driven = cars - drivers

#declare cars_driven and initialize to same value as drivers
cars_driven = drivers

#declare carpool_capacity as amount of cars driven multiplied by space in a car
carpool_capacity = cars_driven * space_in_a_car

# declare avg_pass_per_car and initialize to passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven

print("there are", cars, "cars available.")
print("there are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
