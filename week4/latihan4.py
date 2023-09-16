print('\nSoal 1')

#  Consider the following scenario about using Python dictionaries:
# Tessa and Rick are hosting a party. Together, they sent out invitations, and collected the responses in a dictionary, with names of their friends and the number of guests each friend will be bringing.
# Complete the function so that the “check_guests” function retrieves the number of guests (value) the specified friend “guest” (key) is bringing. This function should:
# 1. accept a dictionary “guest_list” and a key “guest” variable passed through the function parameters;
# 2. print the values associated with the key variable.

def check_guests(guests, guest):
  return guests.get(guest) # Return the value for the given key

# menggunakan metode .get() dari kamus untuk mengambil nilai yang terkait dengan key guest. Metode ini lebih kuat karena mengatasi kasus di mana keys mungkin tidak ada dalam kamus. Jika keys tidak ada, .get() secara default mengembalikan None

guest_list = { "Adam":3, "Camila":3, "David":5, "Jamal":3, "Charley":2, "Titus":1, "Raj":6, "Noemi":1, "Sakira":3, "Chidi":5}


print(check_guests(guest_list, "Adam")) # Should print 3
print(check_guests(guest_list, "Sakira")) # Should print 3
print(check_guests(guest_list, "Charley")) # Should print 2

print('\nSoal 2')

# Complete the function so that input like "This is a sentence." will return a dictionary that holds the count of each letter that occurs in the string: {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}. This function should:
# accept a string “text” variable through the function’s parameters;
# iterate over each character the input string to count the frequency of each letter found, (only letters should be counted, do not count blank spaces, numbers, or punctuation; keep in mind that Python is case sensitive);
# populate the new dictionary with the letters as keys, ensuring each key is unique, and assign the value for each key with the count of that letter;
# return the new dictionary.

def count_letters(text):
    # Initialize a new dictionary.
    dictionary = {}
    # Complete the for loop to iterate through each "text" character and
    # use a string method to ensure all letters are lowercase.
    for char in text.lower(): # mengiterasi melalui karakter teks dalam huruf kecil.
        # Complete the if-statement using a string method to check if the
        # character is a letter.
        if char.isalpha(): # memastikan bahwa karakter adalah huruf.
            # Complete the if-statement using a logical operator to check if
            # the letter is not already in the dictionary.
            if char not in dictionary: # memeriksa apakah huruf belum ada dalam dictionaries sebelumnya.
                # Use a dictionary operation to add the letter as a key
                # and set the initial count value to zero.
                dictionary[char] = 0 # Menambahkan huruf ke dalam dictionaries sebagai kunci jika belum ada, dan menginisialisasi hitungan (value) dengan 0.
            # Use a dictionary operation to increment the letter count value
            # for the existing key.
            dictionary[char] += 1 # menambahkan 1 ke hitungan huruf jika huruf tersebut sudah ada dalam dictionaries.
            # Increment the letter counter.
    return dictionary

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

print('\nSoal 3')

# Fill in the blanks to complete the “car_listing” function. This function accepts a “car_prices” dictionary. It should iterate through the keys (car models) and values (car prices) in that dictionary. For each item pair, the function should format a string so that a dictionary entry like ““Kia Soul“:19000” will print "A Kia Soul costs 19000 dollars". Each new string should appear on its own line.

def car_listing(car_prices):
    result = "" # digunakan untuk mengumpulkan hasil akhir berupa daftar mobil dan harganya dalam bentuk string yang diformat.
    # Complete the for loop to iterate through the key and value items
    # in the dictionary.
    for car, price in car_prices.items(): # untuk mengiterasi melalui item-item dalam kamus car_prices menggunakan metode .items(). Setiap iterasi dari loop ini akan mengambil pasangan kunci (model mobil) dan nilai (harga mobil).
        result += "A {} costs {} dollars\n".format(car, price) # Use a string method to format the required string.
    return result

print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo": 55000, "Ford Fiesta": 13000, "Toyota Prius": 24000}))

print('\nSoal 4')

# Fill in the blank to complete the “squares” function. This function should use a list comprehension to create a list of squared numbers (using either the expression n*n or n**2). The function receives two variables and should return the list of squares that occur between the “start” and “end” variables inclusively (meaning the range should include both the “start” and “end” values). Complete the list comprehension in this function so that input like “squares(2, 3)” will produce the output “[4, 9]”.

def squares(start, end):
    return [n * n for n in range(start, end + 1)] # Create the required list comprehension.


print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print('\nSoal 5')

# Consider the following scenario about using Python lists:
# Employees at a company shared the distance they drive to work (in miles) through an online survey. These distances were automatically added by Python to a list called “distances” in the order that each employee submitted their distance. Management wants the list to be sorted in the order of the longest distance to the shortest distance.
# Complete the function to sort the “distances” list. This function should:
# sort the given “distances” list, passed through the function’s parameters; ;
# reverse the sort order so that it goes from the longest to the shortest distance;
# return the modified “distances” list.

def sort_distance(distances):
    distances.sort()  # Sort the list in ascending order
    distances.reverse()  # Reverse the order of the list to make it descending
    return distances

print(sort_distance([2,4,0,15,8,9]))
# Should print [15, 9, 8, 4, 2, 0]

print('\nSoal 6')

# Fill in the blank to complete the “highlight_word” function. This function should change the given “word” to its upper-case version in a given “sentence”. Complete the string method needed in this function so that a function call like "highlight_word("Have a nice day", "nice")" will return the output "Have a NICE day".

def highlight_word(sentence, word):
    # Complete the return statement using a string method.
    return sentence.replace(word, word.upper())

print(highlight_word("Have a nice day", "nice"))
# Should print: "Have a NICE day"
print(highlight_word("Shhh, don't be so loud!", "loud"))
# Should print: "Shhh, don't be so LOUD!"
print(highlight_word("Automating with Python is fun", "fun"))
# Should print: "Automating with Python is FUN"

# Metode replace digunakan untuk mencari setiap kemunculan dari word yang ditentukan dan menggantikannya dengan word.upper()

print('\nSoal 7')

# The format of the input variable “address_string” is: numeric house number, followed by the street name which may contain numbers and could be several words long (e.g., "123 Main Street", "1001 1st Ave", or "55 North Center Drive").
# Complete the string methods needed in this function so that input like "123 Main Street" will produce the output "House number 123 on a street named Main Street". This function should:
# accept a string through the parameters of the function
# separate the address string into new strings: house_number and street_name
# return the variables in the string format: "House number X on a street named Y".

def format_address(address_string):
    house_number = ""
    street_name = ""

    # Separate the house number from the street name.
    address_parts = address_string.split() # metode split() digunakan untuk memecah alamat menjadi potongan-potongan kata (seperti nomor rumah dan nama jalan) berdasarkan spasi.

    for address_part in address_parts:
        # Complete the if-statement with a string method.
        if address_part.isdigit(): # Jika suatu potongan adalah digit (gunakan metode isdigit()), maka itu adalah nomor rumah; jika tidak, itu adalah bagian dari nama jalan.
            house_number = address_part
        else:
            street_name += address_part + " "

    # Remove the extra space at the end of the last "street_name".
    street_name = street_name.strip() # metode strip() untuk menghilangkan spasi ekstra di akhir nama jalan.

    # Use a string method to return the required formatted string.
    return "House number {} on a street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "House number 1001 on a street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "House number 55 on a street named North Center Drive"

print('\nSoal 8')
#  Fill in the blank to complete the “even_numbers” function. This function should use a list comprehension to create a list of even numbers using a conditional if statement with the modulo operator to test for numbers evenly divisible by 2. The function receives two variables and should return the list of even numbers that occur between the “first” and “last” variables

def even_numbers(first, last):
  return [ n for n in range (first,last) if n % 2 == 0]


print(even_numbers(4, 14)) # Should print [4, 6, 8, 10, 12]
print(even_numbers(0, 9))  # Should print [0, 2, 4, 6, 8]
print(even_numbers(2, 7))  # Should print [2, 4, 6]

print('\nSoal 9')

# Fill in the blanks to complete the “countries” function. This function accepts a dictionary containing a list of continents (keys) and several countries from each continent (values).&nbsp; For each continent, format a string to print the names of the countries only. The values for each key should appear on their own line.

def countries(countries_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items
    # in the dictionary.
    for continent, countries_list in countries_dict.items(): # perulangan for digunakan untuk mengakses setiap elemen dalam kamus countries_dict. Elemen-elemen ini berisi daftar negara yang terkait dengan benua tertentu.
        # Use a string method to format the required string.
        result += str(countries_list) + "\n" # menggunakan str(countries_list) untuk mengonversi daftar negara menjadi string, dan "\n" digunakan untuk menambahkan baris baru antara setiap benua.
    return result

print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))

print('\nSoal 10')

#Consider the following scenario about using Python dictionaries:
# A teacher is using a dictionary to store student grades. The grades are stored as a point value out of 100. Currently, the teacher has a dictionary setup for Term 1 grades and wants to duplicate it for Term 2. The student name keys in the dictionary should stay the same, but the grade values should be reset to 0.
# Complete the “setup_gradebook” function so that input like “{"James": 93, "Felicity": 98, "Barakaa": 80}” will produce a resulting dictionary that contains “{"James": 0, "Felicity": 0, "Barakaa": 0}”. This function should:
# accept a dictionary “old_gradebook” variable through the function’s parameters
# make a copy of the “old_gradebook” dictionary
# iterate over each key and value pair in the new dictionary
# replace the value for each key with the number 0
# return the new dictionary.

def setup_gradebook(old_gradebook):
    # Use a dictionary method to create a new copy of the "old_gradebook".
    new_gradebook = old_gradebook.copy() # menggunakan metode copy() untuk membuat salinan baru dari old_gradebook
    # Complete the for loop to iterate over the new gradebook.
    for student in new_gradebook:
        # Use a dictionary operation to reset the grade values to 0.
        new_gradebook[student] = 0 # mengatur ulang nilai-nilai grade ke 0 dalam loop for menggunakan operasi penugasan new_gradebook[student] = 0.
    return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}

