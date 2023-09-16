print('\nSoal 1')
# Fill in the blanks to complete the while loop so that it returns the sum of all the divisors of a number, without including the number itself.
# As a reminder, a divisor is a number that divides into another without a remainder. To do this, you will need to:
# Initialize the "divisor" and "total" variables with starting values
# Complete the while loop condition
# Increment the "divisor" variable inside the while loop
# Complete the return statement

# Fill in the blanks so that the while loop continues to run while the
# "divisor" variable is less than the "number" parameter.
# Fill in the blanks so that the while loop continues to run while the
# "divisor" variable is less than the "number" parameter.

# - def sum_divisors(number):
# Initialize the appropriate variables
# ___ = ___
# ___ = ___

  # Avoid dividing by 0 and negative numbers
  # in the while loop by exiting the function
  # if "number" is less than one
  # if number < 1:
  #  return 0

  # Complete the while loop
  # while ___:
    # if number % divisor == 0:
      # total += divisor
    # Increment the correct variable
    # ___ += 1

  # Return the correct variable
  # return ___

def sum_divisors(number):
# Initialize the appropriate variables
  divisor = 1  # Inisialisasi pembagi dengan 1
  total  = 0 # Inisialisasi total dengan 0

  # Avoid dividing by 0 and negative numbers
  # in the while loop by exiting the function
  # if "number" is less than one
  if number < 1:
    return 0

  # Complete the while loop
  while divisor < number: # Perulangan berjalan selama pembagi < "number"
    if number % divisor == 0:
      total += divisor # Jika "divisor" adalah pembagi dari "number", tambahkan ke "total"
    # Increment the correct variable
    divisor += 1 # Tambahkan "divisor" sebesar 1 setiap iterasi

  # Return the correct variable
  return total # Kembalikan "total" sebagai hasil

print(sum_divisors(0)) # Should print 0
print(sum_divisors(3)) # Should print 1 (karena 1 adalah satu-satunya pembagi dari 3)
# 1
print(sum_divisors(36)) # Should print 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should print 1+2+3+6+17+34+51
# 114

#penjelasan
#Kami menginisialisasi variabel divisor dengan 1 dan total dengan 0. divisor akan digunakan untuk mencoba semua kemungkinan pembagi, dan total akan digunakan untuk mengakumulasi jumlah pembagi yang valid.
#Terdapat pengecekan awal untuk memastikan bahwa jika number kurang dari 1, fungsi akan langsung mengembalikan 0, karena tidak ada pembagi yang valid dalam kasus tersebut.
#Perulangan while akan berjalan selama divisor kurang dari number. Ini berarti perulangan akan mencoba semua nilai pembagi yang mungkin hingga mencapai angka number.
#Dalam setiap iterasi perulangan, kita memeriksa apakah divisor adalah pembagi dari number dengan menggunakan kondisi if number % divisor == 0. Jika ya, kita menambahkannya ke total.
#Selanjutnya, kita meningkatkan nilai divisor dengan divisor += 1 untuk mencoba pembagi berikutnya.
#Setelah perulangan selesai, kita mengembalikan nilai total sebagai hasil dari fungsi.
#Terakhir, kami menguji fungsi ini dengan beberapa panggilan fungsi yang berbeda untuk melihat apakah menghitung total pembagi dengan benar sesuai dengan kriteria yang telah dijelaskan.

print('\nSoal 2')

#Find the error in the code Fix the while loop so there is an exit condition
#Hint: Try running your function with the number 0 as the input and observe the result.

#def is_power_of_two(number):
    # This while loop checks if the "number" can be divided by two
    # without leaving a remainder. How can you change the while loop to
    # avoid a Python ZeroDivisionError?

    #number = 1
   #while number % 2 == 0:
        #number = number / 2
    # If after dividing by 2 "number" equals 1, then "number" is a power
    # of 2.
    #if number == 1:
        #return True
    #return False

#penjelasan letak salah :
#Kode ini pertama-tama menginisialisasi nilai number menjadi 1. Namun, ini bukan nilai yang akan diuji sebagai pangkat dua.
#Perulangan while kemudian mencoba membagi number terus-menerus oleh 2 selama sisa hasil bagi (number % 2) adalah 0. Ini seharusnya digunakan untuk memeriksa apakah number adalah pangkat dua, tetapi ada masalah.
#Kondisi di perulangan while tidak akan pernah menjadi salah karena number selalu 1. Karena itulah, perulangan akan terus berjalan tanpa henti dan mencoba membagi 1 dengan 2, yang menyebabkan ZeroDivisionError.
def is_power_of_two(number):
        # Handle the case where number is less than or equal to 0
        if number <= 0:
            return False

        # Keep dividing the number by 2 until it's no longer even
        while number % 2 == 0:
            number = number // 2

        # Jika setelah pembagian oleh 2 "number" sama dengan 1, maka "number" adalah pangkat 2.
        if number == 1:
            return True

        return False

# Calls to the function
print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False.

#penjelasan
#Dalam kode yang diperbaiki ini, kami menangani kasus di mana number kurang dari atau sama dengan 0 dengan mengembalikan False.
#Kemudian, kami menggunakan perulangan untuk membagi number dengan 2 hingga number tidak lagi menjadi angka genap (tidak habis dibagi 2).
#Jika setelah itu number sama dengan 1, maka itu adalah pangkat dua.

print('\nSoal 3')
#Fill in the blanks to complete the function, which should output a multiplication table. The function accepts a variable “number” through its parameters. This “number” variable should be multiplied by the numbers 1 through 5, and printed in a format similar to “1x6=6” (“number” x “multiplier” = “result”). The code should also limit the “result” to not exceed 25. To satisfy these conditions, you will need to:
# Initialize the “multiplier" variable with the starting value
# Complete the while loop condition
# Add an exit point for the loop
# Increment the “multiplier" variable inside the while loop
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1  # Initialize multiplier to 1

    # Complete the while loop condition.
    while multiplier <= 5: # Perulangan berjalan selama nilai multiplier kurang dari atau sama dengan 5
        result = number * multiplier
        if result > 25:
            # Use the "break" keyword to exit the loop if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the "multiplier" variable by 1
        multiplier += 1

#penjelasan :
#Kondisi while multiplier <= 5: adalah kondisi yang mengatur kapan perulangan akan berhenti. Selama nilai multiplier kurang dari atau sama dengan 5, perulangan akan terus berjalan.
#Ini penting karena kita ingin mencetak tabel perkalian hingga 5. Dengan kata lain, kita ingin mencetak hasil perkalian dari 1 hingga 5 (1x1, 1x2, 1x3, 1x4, 1x5, dan seterusnya) sesuai dengan tabel perkalian yang umumnya dikenal.
#Jika multiplier melebihi 5 (misalnya, saat multiplier sama dengan 6), maka kondisi while menjadi salah, dan perulangan berhenti. Ini mencegah perulangan terus berjalan dan mencetak perkalian yang tidak relevan (misalnya, 6x1, 6x2, 6x3, dst.), yang tidak ada dalam tabel perkalian biasa.
#Jadi, kondisi while multiplier <= 5 adalah kunci untuk membatasi perulangan sehingga hanya mencetak perkalian hingga 5.


# Test the function with different numbers
multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

multiplication_table(5)
# Should print:
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25

multiplication_table(8)
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24