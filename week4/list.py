print('\n Soal 1')

# Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word from a passed sentence. For example, get_word("This is a lesson about lists", 4) should return "lesson", which is the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1.

def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()  # Using the "split" string method from the preceding lesson
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return words[n - 1]  # Adjust the index to be 0-based
    return ""

print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing
print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing

print('\nSoal 2 append method')

#metode append yaitu menambahkan elemen baru di akhir daftar.

fruits = ["Melon", "Banana", "Apple"]
fruits.append("Kiwi")
print(fruits)

print('\nSoal 3 Insert method')

# metode insert yaitu menyisipkan elemen baru di list(daftar)

fruits.insert(3,"Orange")
print(fruits)

print('\nSoal 4 Insert method')

# mencoba metode insert diluar jangkauan list

fruits.insert(10, "Strawberry")
print(fruits)

print('\nSoal 5 remove method')

# metode remove yaitu menghapus elemen tertentu dari list

fruits.remove("Banana")
print(fruits)

print('\nSoal 6 pop method')

# metode pop yaitu menghapus elemen tertentu berdasarkan index

fruits.pop(3)
'Kiwi'
print(fruits)

print('\nSoal 7 mengubah elemen di list')

# metode ini mengubah elemen tertentu ke list
# mengubah elemen dalam daftar dengan menggunakan pengindeksan untuk menimpa nilai yang disimpan pada indeks yang ditentukan. Misalnya, Anda dapat memasukkan list[0] = "Data lama" untuk menimpa elemen pertama dalam daftar dengan string baru "Data lama".

fruits[2] = ("Melon")
print(fruits)

print('\nSoal 8 Tuple')

# Let's use tuples to store information about a file: its name, its type and its size in bytes. Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.

def file_size(file_info):
	name, type, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

print('\nSoal 9 iterating over a list')

# menjalankan suatu operasi pada setiap elemen dalam daftar tersebut, satu per satu, dan melakukan beberapa tindakan atau operasi pada setiap elemen.
# menggunakan perulangan for untuk melakukan iterasi pada setiap elemen dalam daftar

animals = ["Monkey", "Dolphin", "Lion" ,"Zebra"]
chars = 0
for animals in animals:
    chars +=len(animals)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

# Dalam contoh ini, perulangan akan mengakses setiap item dalam animals, dan item akan mengambil nilai setiap elemen secara bergantian.

print ('\nSoal 10 another example')

#  know the index of an element while going through the list
# You could use a range function and then use indexing to access the elements at the index that range just returned or you could just use the enumerate function.
# menggunakan fungsi enumerate yang secara otomatis memberikan Anda indeks dan elemen dalam satu langkah.
# fungsi enumerate digunakan untuk melakukan iterasi melalui daftar sambil melacak indeksnya, sehingga Anda tidak perlu membuat indeks secara manual.

winners = ['Ashley', 'Dylan', 'Reese']

for index, person in enumerate(winners):
    print("{}. {}".format(index + 1, person))

print ('\nSoal 11 another example')

def full_emails(people):
    result = []
    for email,name in people:
        result.append("{} <{}>".format(name,email))
    return result

print(full_emails([("alex@example.com", "Alex Diego"),("Reggina@gmail.com" , "Reggina Indriani")]))

print('\nSoal 12 using the enumerate function')

#Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is in an even position or an odd position.

def skip_elements(elements):
    result = []  # Inisialisasi sebuah list kosong bernama "result".
    for index, character in enumerate(elements):
        if index % 2 == 0:  # Cek apakah indeks adalah bilangan genap.
            result.append(character)  # Jika indeks adalah bilangan genap, tambahkan karakter ke dalam list "result".
    return result  # Mengembalikan list "result" yang berisi karakter-karakter pada indeks-indeks genap.


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# result = []: Ini adalah inisialisasi sebuah list kosong dengan nama "result" yang akan digunakan untuk menyimpan elemen-elemen pada indeks genap.
# for index, character in enumerate(elements):: Ini adalah loop for yang menggunakan fungsi enumerate untuk mengambil indeks dan karakter dari setiap elemen dalam daftar elements.
# result.append(character): Jika indeks adalah bilangan genap, karakter (character) pada indeks tersebut akan ditambahkan ke dalam list "result".
# return result: Fungsi ini mengembalikan list "result" yang berisi karakter-karakter pada indeks-indeks genap.

print('\nSoal 13 list comprehension')

multiples = [] # inisialisasi list kosong bernama multiples yang akan digunakan untuk menyimpan hasil perkalian.
for x in range(1,11):
    multiples.append(x*7)

print(multiples)

print('\nSoal 14 another example')

languages = ["python", "Java", "C", "Ruby", "Perl"]
lengths = [len(language) for language in languages]
print(languages)

print('\nSoal 15 another example')

z = [x for x in range(0,101) if x % 3 == 0]
print (z)

print('/nSoal 16 another example')

#The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using list comprehension. Hint: remember that list and range counters start at 0 and end at the limit minus 1.

def odd_numbers(n):
	return [x for x in range(0,n+1) if x % 2 == 1]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

print('/nSoal 17 Simple List Comprehension')

### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines
# of code into one line:
print([x*2 for x in range(1,11)])



### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,11):
   my_list.append(x*2)
print(my_list)


# Click Run to compare the two results.

print('/nSoal 18 List Comprehension with Conditional Statement')

### List Comprehension with Conditional Statement
print("List comprehension result:")

# The following list comprehension compacts multiple lines
# of code into one line:
print([ x for x in range(1,101) if x % 10 == 0 ])

### Long form for loop with nested if-statement
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,101):
  if x % 10 == 0:
    my_list.append(x)
print(my_list)

# Click Run to observe the two results.
