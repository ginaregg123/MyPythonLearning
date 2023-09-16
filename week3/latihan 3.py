print('\nSoal 1')

#What is the final value of "y" at the end of the following nested loop code? Your answer should be only one number.

for x in range(10):
    for y in range(x):
        print(y)

#should print 8

print('\n Soal 2')

#The following code is supposed to add together all numbers from x to 10. The code is returning an incorrect answer, what is the reason for this?

x=1
sum = 5 #harusnya diisi 0
while x <= 10:
    sum += x
    x +=1
print(sum)
#should print 55 --> tetapi yang kecetak 60
#kode diatas salah karena "The 'sum' variable is initialized with the wrong value" ("Variabel 'sum' diinisialisasi dengan nilai yang salah").
#Pada kode yang diberikan, inisialisasi variabel "sum" dengan nilai awal 5 adalah yang salah. Untuk menghitung jumlah semua angka dari x hingga 10, "sum" harus diinisialisasi dengan nilai 0, bukan 5.

print('\nSoal 3')
#How many numbers will this loop print? Your answer should be only one number.

for sum in range(5):
    sum += sum
    print(sum)

#jawabannya : 5

print('\nSoal 4')
#The following code causes an infinite loop. Can you figure out what is incorrect?

def test_code(num):
    x = num
    while x % 2 == 0:
        x = x / 2

#test_code(0)

#When called with 0, it triggers an infinite loop

print('\nSoal 5')
#Fill in the blanks to complete the “odd_numbers” function. This function should return a space-separated string of all odd positive numbers, up to and including the “maximum” variable that's passed into the function.
#Complete the for loop so that a function call like “odd_numbers(6)” will return the numbers “1 3 5”.

def odd_numbers(maximum):
    return_string = ""  # Initializes variable as a string

    # Complete the for loop with a range that includes all
    # odd numbers up to and including the "maximum" value.
    #for _______
    for num in range(1, maximum + 1, 2):  # Start from 1, end at maximum, increment by 2 (for odd numbers)

        # Complete the body of the loop by appending the odd number
        # followed by a space to the "return_string" variable.
        #______________________
        return_string += str(num) + " "

    # This .strip command will remove the final " " space
    # at the end of the "return_string".
    return return_string.strip()

#penjelasan:
#Loop for num in range(1, maximum + 1, 2) digunakan untuk mengiterasi melalui semua angka ganjil mulai dari 1 hingga nilai "maximum" yang diberikan. Rentang ini dimulai dari 1, berakhir pada nilai "maximum", dan increment sebesar 2 untuk memastikan hanya angka ganjil yang dimasukkan.
#Setiap angka ganjil ditambahkan ke return_string sebagai string dengan tanda spasi di belakangnya.
#Akhirnya, menggunakan .strip() untuk menghapus spasi ekstra di akhir string sebelum mengembalikannya.

print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10)) # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed.

print('\nSoal 6')
#Fill in the blanks to complete the “divisible” function. This function should count the number of values from 0 to the “max” parameter that are evenly divisible (no remainder) by the “divisor” parameter. Complete the code so that a function call like “divisible(100,10)” will return the number “10”.

def divisible(max, divisor):
    #___________ # Initialize an incremental variable
    count = 0  # Initialize an incremental variable
    #for ___________
    for x in range(max):  # Complete the for loop
        if x % divisor == 0:
            #_________
            count += 1  # Increment the appropriate variable
    return count

print(divisible(100, 10))  # Should be 10
print(divisible(10, 3))    # Should be 4
print(divisible(144, 17))  # Should be 9

#penjelasan :
#Variabel count digunakan untuk menghitung jumlah angka dari 0 hingga max yang habis dibagi (tidak memiliki sisa) oleh divisor.
#Loop for x in range(max + 1) digunakan untuk mengiterasi melalui semua angka dari 0 hingga max.
#Dalam setiap iterasi, kita memeriksa apakah x habis dibagi oleh divisor dengan menggunakan x % divisor == 0. Jika ya, kita increment count untuk menghitung angka yang memenuhi kondisi ini.
#Akhirnya, kita mengembalikan nilai count sebagai hasil perhitungan jumlah angka yang habis dibagi oleh divisor

print('\nSoal 7')
#Fill in the blanks to print the numbers from 15 to 5, counting down by fives.

#number = ____
number = 15  # Initialize the variable
#while _____
while number >= 5:  # Complete the while loop condition
    print(number, end=" ")
    #number _____
    number -= 5  # Increment the variable

# Should print 15 10 5

#penjelasan:
# Kita inisialisasi variabel number dengan nilai awal 15.
# Dalam loop while, kita memeriksa apakah nilai number lebih besar atau sama dengan 5. Jika ya, maka loop akan berlanjut. Jika tidak, loop akan berhenti.
# Dalam setiap iterasi, kita mencetak nilai number dengan menggunakan print(number, end=" "). Penggunaan end=" " digunakan untuk memastikan angka-angka yang dicetak dipisahkan dengan spasi.
# Kemudian, kita mengurangkan nilai number sebesar 5 dengan pernyataan number -= 5, sehingga nilai number berkurang sebanyak 5 setiap kali iterasi. Ini memungkinkan kita untuk menghitung mundur dari 15 ke 5 dengan selang waktu 5.

print('\nSoal 8')

#Find and correct the error in the for loop below. The loop should check each number from 1 to 5 and identify if the number is odd or even.

#for number in range(5):
for number in range(1,6): #Kami ingin membuat deret angka yang dimulai dari 1 hingga 5, yang berarti inklusif untuk 1 (1 akan disertakan) dan eksklusif untuk 6 (6 tidak akan disertakan).Dengan menggunakan range(1, 6), kita mencakup semua angka dari 1 hingga 5.
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


# Should print:
# odd
# even
# odd
# even
# odd

#penjelasan :
#Kita menggunakan loop for untuk mengiterasi melalui angka-angka dari 1 hingga 5 (inklusif).
#Di dalam loop, kita memeriksa setiap angka dengan menggunakan operasi modulo (number % 2). Jika sisa pembagian oleh 2 adalah 0, maka angka tersebut adalah angka genap, dan kita mencetak "even." Jika sisa pembagian bukan 0, maka angka tersebut adalah angka ganjil, dan kita mencetak "odd."
#Hasil cetakan akan sesuai dengan identifikasi angka sebagai ganjil atau genap, sesuai yang diharapkan.

print('\nSoal 9')

#Fill in the blanks to complete the function “even_numbers(n)”. This function should count how many even numbers exist in a sequence from 0 to the given “n”number, where 0 counts as an even number.  For example, even_numbers(25) should return 13, and even_numbers(6) should return 4.

def even_numbers(n):
    count = 0
    current_number = 0
    #while ______
    while current_number <= n:  # Complete the while loop condition
        if current_number % 2 == 0:
            #_______
            count += 1  # Increment the appropriate variable
            #________
        current_number += 1  # Increment the appropriate variable
    return count


print(even_numbers(25))  # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000))  # Should print 501
print(even_numbers(0))  # Should print 1

#Penjelasan:

#Kami menggunakan loop while untuk mengiterasi melalui semua angka dari 0 hingga n.
#Dalam setiap iterasi, kami memeriksa apakah current_number adalah angka genap dengan menggunakan current_number % 2 == 0. Jika ya, maka kami increment count untuk menghitung jumlah angka genap.
#Kami juga increment current_number setiap kali iterasi untuk memeriksa setiap angka dalam rentang dari 0 hingga n.
#Akhirnya, kami mengembalikan nilai count sebagai hasil perhitungan jumlah angka genap dalam rentang dari 0 hingga n.

print('\nSoal 10')

#Fill in the blanks to complete the “multiplication_table” function. This function should print a multiplication table, where each number is the result of multiplying the first number of its row by the number at the top of its column. Complete the range sequences in the nested loops so that “multiplication_table(1, 3)” will print:
# 1 2 3
# 2 4 6
# 3 6 9 .

def multiplication_table(start, stop):
    # Complete the outer loop range
    #for x in range _____
    for x in range(start, stop + 1):  # Complete the outer loop range
         # Complete the inner loop range
         #for y in range _____
        for y in range(start, stop + 1):  # Complete the inner loop range
            # Prints the value of "x" multiplied by "y"
            # and inserts a space after each value
            print(str(x * y), end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()

multiplication_table(1, 3)
# Should print the multiplication table shown above

#penjelasan :
#Kami menggunakan dua loop for bersarang untuk membuat tabel perkalian.
#Loop pertama (for x in range(start, stop + 1)) mengontrol baris tabel, mulai dari start hingga stop.
#Loop kedua (for y in range(start, stop + 1)) mengontrol kolom tabel, juga mulai dari start hingga stop.
#Di dalam loop kedua, kami mencetak hasil perkalian x dan y (x * y) dan memasukkan spasi setelah setiap nilai.
#Setelah mencetak semua nilai dalam baris, kami menggunakan print() kosong untuk memasukkan pemisah baris (line break) sehingga hasil cetakan terlihat seperti tabel perkalian yang diharapkan.