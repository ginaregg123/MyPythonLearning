print('\nSoal 1')

file_counts = {"jpg":10, "txt":15, "pyh":5, "txt":13}
print(file_counts)

print('\nSoal 2')

#menambahkan elemen baru ke dictionary

file_counts["cfg"] = 8
print(file_counts)

print('\nSoal 3')

#mengubah elemen yang ada pada  dictionary

file_counts["cfg"] = 11
print(file_counts)

print('\nSoal 4')

#menghapus elemen yang ada pada dictionary ( menggunakan keyword del)

del file_counts["cfg"]
print(file_counts)

print('\nSoal 5')

# menggunakan dictionary dalam for

file_counts = {"jpg":10, "txt":15, "pyh":5, "txt":13}
for text,amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount,text))

print('\nSoal 6 dictionaries menggunakan perulangan for')

#Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each element in the dictionary.

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animal, body_part in cool_beasts.items():
    print("{} have {}".format(animal, body_part))

print('\nSoal 7')

# menghitung berapa kali setiap hurufmuncul dalam sepotong teks.

def count_letter(text):
    result = {} # menginisialisasi dictionaries kosong
    for letter in text: # menelusuri setiap huruf dalam string yang diberikan
        if not letter in result: # Untuk setiap huruf, kami memeriksa apakah belum ada di kamus.
            result[letter] = 0 # menginisialisasi entri dalam dictionaries dengan nilai nol.
        result[letter]+=1 # menambah jumlah huruf tersebut di dictionaries
    return result