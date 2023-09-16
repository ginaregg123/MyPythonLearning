# Using the format() method

print('\nSoal 1')
# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""

# Jika placeholder menunjukkan angka, maka digantikan oleh variabel yang sesuai dengan urutan tersebut (dimulai dari nol).
# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""

print('\nSoal 2')
#Use a for loop to iterate through each letter of a string.
#Add a character to the front of a string.
#Add a character to the end of a string.
#Use the .lower() string method to convert the case (uppercase/lowercase) of the letters within a string variable. This method is often used to eliminate cases as a factor when comparing two strings. For example, all lowercase “cat” is not equal to “Cat” because “Cat” contains an uppercase letter. To be able to compare the two strings to see if they are the same word, you can use the .lower() string method to remove capitalization as a factor in the string comparison.

# This function accepts a given string and checks each character of
# the string to see if it is a letter or not. If the character is a
# letter, that letter is added to the end of the string variable
# "forwards" and to the beginning of the string variable "backwards".
def mirrored_string(my_string):

    # Two variables are initialized as string data types using empty
    # quotes. The variable "forwards" will hold the "my_string"
    # minus any character that is not a letter. The "backwards"
    # variable will hold the same letters as "forwards", but in
    # in reverse order.
    forwards = ""
    backwards = ""

    # The for loop iterates through each character of the "my_string"
    for character in my_string:

         # The if-statement checks if the character is not a space.
         if character.isalpha():
             # If True, the body of the loop adds the character to the
             # to the end of "forwards" and to the front of
             # "backwards".
             forwards += character
             backwards = character + backwards

          # If False (meaning the character is not a letter), no action
          # is needed. This coding approach results prevents any
          # non-alphabetical characters from being written to the
          # "forwards" and "backwards" variables. The for loop will
          # restart until all characters in "my_string" have been
          # processed.

    # The final if-statement compares the "forwards" and "backwards"
    # strings to see if the letters are the same both forwards and
    # backwards. Since Python is case sensitive, the two strings will
    # need to be converted to use the same case for this comparison.
    if forwards.lower() == backwards.lower():
        return True
    return False

print(mirrored_string("12 Noon"))  # Should be True
print(mirrored_string("Was it a car or cat I saw"))  # Should be False
print(mirrored_string("'eve, Madam Eve"))  # Should be True

print('\nSoal 3')
#Use the format() method, with {} placeholders for variable data, to create a new string.
#Use a formatting expression, like {:.2f}, to format a float variable and configure the number of decimal places to display for the float.

# This function converts measurement equivalents. Output is formatted
# as, "x ounces equals y pounds", with y limited to 2 decimal places.
def convert_weight(ounces):
    # Conversion formula: 1 pound = 16 ounces
    pounds = ounces / 16

    # The result is composed using the .format() method. There are two
    # placeholders in the string: the first is for the "ounces"
    # variable and the second is for the "pounds" variable. The second
    # placeholder formats the float result of the conversion
    # calculation to be limited to 2 decimal places.
    result = "{} ounces equals {:.2f} pounds".format(ounces, pounds)
    return result


print(convert_weight(12))  # Should be: 12 ounces equals 0.75 pounds
print(convert_weight(50.5))  # Should be: 50.5 ounces equals 3.16 pounds
print(convert_weight(16))  # Should be: 16 ounces equals 1.00 pounds

print('\nSoal 4')

#Within the format() parameters, select characters at specific index [ ] positions from a variable string.
#Use the format() method, with {} placeholders for variable data, to create a new string.

# This function generates a username using the first 3 letters of a
# user’s last name plus their birth year.
def username(last_name, birth_year):
    # The .format() method will use the first 3 letters at index
    # positions [0,1,2] of the "last_name" variable for the first
    # {} placeholder. The second {} placeholder concatenates the user’s
    #  "birth_year" to that string to form a new string username.
    return ("{}{}".format(last_name[0:3], birth_year))


print(username("Ivanov", "1985"))
# Should display "Iva1985"
print(username("Rodríguez", "2000"))
# Should display "Rod2000"
print(username("Deng", "1991"))
# Should display "Den1991"

print('\nSoal 5')

# Use the .replace() method to replace part of a string.
# Use the len() function to get the number of index positions in a string.
# Slice a string at a specific index position.

# This function checks a given schedule entry for an old date and, if
# found, the function replaces it with a new date.
def replace_date(schedule, old_date, new_date):
    # Check if the given "old_date" appears at the end of the given
    # string variable "schedule".
    if schedule.endswith(old_date):
        # If True, the body of the if-block will run. The variable "n" is
        # used to hold the slicing index position. The len() function
        # is used to measure the length of the string "new_date".
        p = len(old_date)

        # The "new_schedule" string holds the updated string with the
        # old date replaced by the new date. The schedule[:-p] part of
        # the code trims the "old_date" substring from "schedule"
        # starting at the final index position (or right-side) counting
        # towards the left the same number of index positions as
        # calculated from len(old_date). Then, the code schedule[-p:]
        # starts the indexing position at the slot where the first
        # character of the "old_date" used to be positioned. The
        # .replace(old_date, new_date) code inserts the "new_date" into
        # the position where the "old_date" used to exist.
        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)

        # Returns the schedule with the new date.
        return new_schedule

    # If the schedule does not end with the old date, then return the
    # original sentence without any modifications.
    return schedule


print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024"))
# Should display "Last year’s annual report will be released in March 2024"
print(replace_date("In April, the CEO will hold a conference", "April", "May"))
# Should display "In April, the CEO will hold a conference"
print(replace_date("The convention is scheduled for October", "October", "June"))
# Should display "The convention is scheduled for June"

print('\nSoal 6')


def sales_prices(item_and_price):
    # Initialize variables "item" and "price" as strings
    item = ""
    price = ""
    # Create a variable "item_or_price" to hold the result of the split.
    item_or_price = item_and_price.split()

    # For each element "x" in the split variable "item_or_price"
    for x in item_or_price:

        # Check if the element is a number
        if x.isalpha():

            # If true, assign the element to the "item" string variable and add a space
            # for any item names containing multiple words, like "Winter fleece jacket".
            item += x + " "

        # Else, if x is a number (if x.isalpha() is false):
        else:
            # Assign the element to the "price" string variable.
            price = x

    # Strip the extra space to the right of the last "item" word
    item = item.strip()

    # Return the item name and price formatted in a sentence
    return "{} are on sale for ${}".format(item,price)


# Call to the function
print(sales_prices("Winter fleece jackets 49.99"))
# Should print "Winter fleece jackets are on sale for $49.99"
