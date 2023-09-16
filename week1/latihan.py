print('\nSoal 1')

#Mercury has a diameter of approximately 1,516 miles. Earth has a diameter of approximately 3,959 miles.
#Use Python to calculate how much larger Earth’s diameter is than Mercury's (in miles). Note: Your result should be in the format of a number, not a sentence.

# Diameter Merkurius dalam mil
diameter_merkurius = 1516

# Diameter Bumi dalam mil
diameter_bumi = 3959

# Menghitung perbandingan diameter Bumi dengan Merkurius dan mengkonversinya ke integer
perbandingan_diameter = diameter_bumi - diameter_merkurius

# Menampilkan hasil
print (perbandingan_diameter)

#should print 2443

print('\nSoal 2')

#Fill in the blank to calculate how many sectors a given 16 GB (gigabyte) hard disk drive has.
#The given hard drive is divided into sectors of 512 bytes each. How many sectors should this drive have?
# Your result should be in the format of just a number, not a sentence. Note: To calculate the disk size, multiply by multiples of 1024.
# In the code below, the "disk_size" of 16 GB is expressed as multiplying 16 by 1024 three times to get from bytes, to kilobytes, to megabytes, and finally to gigabytes.

disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size / sector_size


print(sector_amount)
# Should print 33554432.0

print('\nSoal 3')

#Keeping in mind there are 86400 seconds per day, write a program that calculates how many seconds there are in a week, if a week is 7 days.
#Print the result to the screen. Note: Your result should be in the format of just a number, not a sentence.

# Enter code here:
second_per_day = 86400
day_per_week = 7
second_in_a_week = second_per_day * day_per_week

print(second_in_a_week)
# Should print 604800

print('\nSoal 4')
#Assuming there are 60 minutes in an hour, write a program that calculates the number of minutes in a 24 hour day.
#Print the result on the screen. Note: Your result should be in the format of just a number, not a sentence.

# Enter code here:
minutes_per_hour = 60
hour_per_day = 24
minute_per_day = minutes_per_hour * hour_per_day

print(minute_per_day)
# Should print 1440

print('\nSoal 5')
#Use Python to calculate how many number-based passcodes can be formed with 10 numerals (0 through 9).  For a 1 numeral passcode, there would be 10 possibilities.  For a 2 numeral passcode, each numeral is independent of the other, so there would be 10 times 10 possibilities.
#Using this information, print the amount of possible passwords that can be formed with 8 numerals. Note: Your result should be in the format of just a number, not a sentence.

# Enter code here:
possibilities_per_digit = 10
passcode_length = 8
total_possibilities = possibilities_per_digit ** passcode_length

print(total_possibilities)
# Should print 100000000

print('\nSoal 6')
#Consider this scenario about using Python to make calculations:
#On a college campus, there are 30 computers in each of the 20 computer labs that are spread across campus.
#The computers have a life cycle where they are replaced every 5 years, with an equal number (one-fifth) of the computers replaced each year.

total_computers = 30 * 20  # Total number of computers in all labs
replacement_cycle = 5  # The replacement cycle in years
computers_per_year = total_computers / replacement_cycle  # Number of computers replaced each year
print(computers_per_year)
# Should print 120.0

print('\nSoal 7')
#Complete the code so that the string "I'am& writing Python code!" will print to the screen.
#Remember that syntax precision is important in programming languages. A missing capital letter, spelling error, or punctuation mark can produce errors.

# Replace the blanks with the correct code and syntax:
print("I am writing Python code!")

# Should print: I am writing Python code!