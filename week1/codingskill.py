# Skill 1
# Use the print() function to output a string

print('\nSyntax for printing a string of text')

print("I love Python!")


# Syntax for printing numeric values
print(360)
print(32*45)


# Syntax for printing the value of a variable
value = 8*6
print(value)

# Skill 2
# - Use arithmetic operators, with a focus on exponent

print('\nMultiplication, division, addition, and subtraction')

print(3 * 8 / 2 + 5 - 1)
print((6-2)/(5 *(1 + 4))+ 3)
print(6*2-5/((1 + 4))+ 3**2)

# Exponents
print(4 ** 6)  # Syntax means 4 to the power of 6
print(4 ** 2)  # To square a number
print(4 ** 3)  # To cube a number
print(4 ** 0.5)  # To find the square root of a number

# To calculate how many different possible combinations can be
# formed using a set of "x" characters with each character in "x"
# having "y" number of possible values, you will need to use an
# exponent for the calculation:
x = 4
y = 26
print(y ** x)

# Skill 3
# Use variables with assignment and arithmetic operators

print('\nAssignment of values to the variables')

years = 10
weeks_in_a_year = 52
# This variable is assigned an arithmetic calculation:
weeks_in_a_decade = years * weeks_in_a_year
# Prints the calculation stored in the "weeks_in_a_decade" variable:
print(weeks_in_a_decade)
