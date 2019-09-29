#store 100 in cars variable
cars = 100
# store 4.0 in space_in_car variable
space_in_car = 4.0
# store 30 in drivers variable
drivers = 30
#store 90 in passangers variable
passangers = 90

#`100 - 30
# store 10 in cars_not_driven variable
cars_not_driven = cars - drivers #70
# 30 in variable cars driven
cars_driven = drivers #30
# 30 * 4.0
# 120.0 in carpool_capacity variable
carpool_capacity = cars_driven * space_in_car #120
# 90/30
# 3 in variable average_passengers_per_car
average_passengers_per_car = passangers / cars_driven #3


# "There are 100 cars available."
print("There are", cars, "cars available.")
# "There are only 30 drivers available."
print("There are only", drivers, "drivers available.")
# "There will be 10 empty cars today"
print("There will be", cars_not_driven, "empty cars today.")
#We can transport 120 people today
print("We can transport", carpool_capacity, "people today.")
# We have 90  to carpool today
print("We have", passangers, "to carpool today.")
#we need to put about 3 in each car
print("We need to put about", average_passengers_per_car, "in each car.")
