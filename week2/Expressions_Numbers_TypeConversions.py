# contoh soal

print('\nSoal 1')
base = 6
height = 3
area = (base * height)/2

print('The area of the triangle is : ' + str(area))

print('\nSoal 2')
'''
In this scenario, we have a directory with 5 files in it. Each file has a different size: 2048, 4357, 97658, 125, and 8.
Fill in the blanks to calculate the average file size by having Python add all the values for you, and then set the files variable to the number of files.
Finally, output a message saying "The average size is: " followed by the resulting number. Remember to use the str() function to convert the number into a string.
'''
file_sizes = [2048, 4357, 97658, 125, 8]  # List of file sizes
total_size = sum(file_sizes)  # Sum of all file sizes
files = len(file_sizes)  # Number of files
# Kita menggunakan len(file_sizes) untuk menghitung jumlah file dalam daftar dan
# menyimpan hasilnya dalam variabel files. Ini adalah jumlah file dalam direktori.
average_size = total_size / files  # Calculate the average size

# Output the result
print("The average size is: " + str(average_size))

# why variabel average converg to str ?
# because impossible when add the text
# the text is "The average size is:"
# this is explicit conversion

