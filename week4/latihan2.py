print('\nSoal string latihan 1')

# Use a for loop to modify elements of a list.
# Use the list.append(old,new) method.
# Use the string.endswith() and string.replace() methods to modify the elements within a list.

# This block of code changes the year on a list of dates.
# The "years" list is given with existing elements.
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# The variable "updated_years" is initialized as a list data type
# using empty square brackets []. This list will hold the new list
# with the updated years.
updated_years = []

# The for loop checks each "year" element in the list "years".
for year in years:

    # The if-statement checks if the "year" element ends with the
    # substring "2023".
    if year.endswith("2023"):

        # If True, then a temporary variable "new" will hold the
        # modified "year" element where the "2023" substring is
        # replaced with the substring "2024".
        new = year.replace("2023", "2024")

        # Then, the list "updated_years" is appended with the changed
        # element held in the temporary variable "new".
        updated_years.append(new)

    # If False, the original "year" element will be appended to the
    # the "updated_years" list unchanged.
    else:
        updated_years.append(year)

print(updated_years)
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

print('\nSoal 2')

# Use a list comprehension to return values

# This list comprehension creates a list of squared numbers (n*n). It
# accepts two integer variables through the function’s parameters.
def squares(start, end):
    # The list comprehension calculates the square of a variable integer
    # "n", where "n" ranges from the "start" to "end" variables inclusively.
    # To be inclusive in a range(), add +1 to the end of range variable.
    return [n * n for n in range(start, end + 1)]


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print('\nSoal 3')

# Use the string[index] method within a list comprehension.
# Use a list comprehension to modify elements of a list.
# Use the string.replace() method within a list comprehension.

# This block of code also changes the year on a list of dates using a
# different approach than demonstrated in Skill Group 1. By using a
# list comprehension, you can see how it is possible to refactor the
# code to a shorter, more efficient code block.

# The "years" list is given with existing elements.
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# The list comprehension below creates a new list "updated_years" to
# hold the command to replace the "2023" substring of the "year"
# element with the substring "2024". This action will be executed if
# the last 4 indices of the "year" string is equal to the substring
# "2023". If false (else), the "year" element will be included in the
# new list "updated_years" unchanged.
updated_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]


print(updated_years)
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

print('\nSoal 4')

# Use the string.split() method to separate a string into a list of individual words.
# Iterate over the new list using a for loop.
# Modify each element in the list by slicing the element’s string at a given [1:] index position and appending the substring to the end of the element.
# Convert a list back into a string.

# This function splits a given string into a list of elements. Then, it
# modifies each element by moving the first character to the end of the
# element and adds a dash between the element and the moved character.
# For example, the element "2two" will be changed to "two-2". Finally,
# the function converts the list back to a string, and returns the
# new string.
def change_string(given_string):

# Initialize "new_string" as a string data type by using empty quotes.
    new_string = ""
    # Split the "given_string" into a "new_list", with each "element"
    # holding an individual word from the string.
    new_list = given_string.split()

    # The for loop iterates over each "element" in the "new_list".
    for element in new_list:

        # Convert the list into a "new_string" by using the assignment
        # operator += to concatenate the following items:
        # + Each list "element" (starting at index position [1:]),
        # + a dash "-",
        # + append the first character of the "element" (using the index
        # [0]) to the end of the "element", and finally,
        # + a space " " to separate each "element" in the "new_string".
        new_string += element[1:] + "-"  + element[0] + " "

    # Return the list that has been converted back into a string.
    return new_string


print(change_string("1one 2two 3three 4four 5five"))
# Should print "one-1 two-2 three-3 four-4 five-5"

print('\nSoal 5')

#  Use the string.join() method to concatenate a string that provides a list name and its elements

# This function accepts a list name and a list of elements, and returns
# a string with the format: "The "list_name" list includes: element1,
# element2, element3".
def list_elements(list_name, elements):

    # This task can be completed in a single line of code. The
    # concatenation of strings, "list_name", and the list "elements" can
    # occur on the return line. In this case, the string "The " is added
    # to the "list_name", plus the string " list includes: ", then the
    # "elements" are joined using a comma to separate each element of the
    # list.
    return "The " + list_name + " list includes: " + ", ".join(elements)


print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]))
# Should print "The Printers list includes: Color Printer, Black and White Printer, 3-D Printer"

print('\nSoal 6')

# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

newfilenames = [filename.replace(".hpp", ".h") for filename in filenames]

# melakukan perulangan melalui setiap elemen (nama file) dalam list filenames.
# replace(".hpp", ".h") digunakan untuk mengganti .hpp dengan .h jika ditemukan dalam nama file.

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

print('\nSoal 7')

# Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.

def pig_latin(text):
    result = [] # Membuat list kosong result untuk menyimpan kata-kata dalam bentuk Pig Latin.
    # Separate the text into words
    words = text.split() # menggunakan metode split() untuk menghasilkan list words yang berisi kata-kata yang dipisahkan berdasarkan spasi.
    for word in words: # untuk mengiterasi melalui setiap kata dalam list words.
        # Create the Pig Latin word
        pig_word = word[1:] + word[0] + "ay"
# word[1:] digunakan untuk mengambil semua karakter dalam kata kecuali karakter pertama, kemudian karakter pertama (karakter yang telah diambil) ditambahkan ke belakang kata tersebut, dan "ay" ditambahkan di akhirnya.
# word[0] digunakan untuk mengambil karakter pertama dari kata dan memindahkannya ke belakang kata tersebut.
# Kata yang sudah diubah menjadi Pig Latin disimpan dalam list result.
# Setelah selesai mengubah semua kata, kita menggabungkan kata-kata tersebut kembali menjadi satu teks dengan menggunakan metode join()
        result.append(pig_word)
    # Join the modified words back into a phrase
    return " ".join(result)

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

print('\nSoal 8')

# The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.

def group_list(group, users):
  members = ", ".join(users) # menggunakan metode join() untuk menggabungkan elemen-elemen dalam daftar users dengan tanda koma dan spasi di antaranya.
  return f"{group}: {members}" # Menggunakan f-string (formatted string literal) untuk mengatur hasil. Di dalam f-string, kami masukkan nama group diikuti dengan titik dua dan spasi, dan kemudian kami sisipkan string members.

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

print('\nSoal 9')

# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that.

def guest_list(guests):
    for guest in guests: # Menggunakan loop for untuk mengiterasi melalui setiap tamu dalam daftar guests
        name = guest[0] # mengakses informasi masing-masing tamu dalam tupel menggunakan indeks.
        age = guest[1] # Indeks 0 adalah nama, indeks 1 adalah usia, dan indeks 2 adalah profesi tamu.
        profession = guest[2] # Ini adalah cara kami mengambil informasi nama, usia, dan profesi dari tupel.
        print("{} is {} years old and works as {}".format(name, age, profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""



