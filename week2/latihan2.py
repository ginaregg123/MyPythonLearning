print('\nSoal 1')
#Hint : if a function returns multiple values, don't forget to store these values in multiple variables

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller,bigger = order_numbers(100, 99)
print(smaller, bigger)

print('\nSoal 2')
def print_seconds(hours, minutes, seconds):
    print(hours*3600+minutes*60+seconds)

print_seconds(1,2,3)
#output will print to the screen

print('\nSoal 3')
#This function converts miles to kilometers (km)

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

# Do not indent any of the following lines of code as they are
# meant to be located outside of the function above

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the my_trip_km conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result of
#    my_trip_km.
round_trip_km = my_trip_km * 2

# 5) Fill in the blank to print the result of the round_trip_km calculation
print("The round-trip in kilometers is " + str(round_trip_km))