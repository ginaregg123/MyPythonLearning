name1 = 'Reggina'
name2 = 'reggina'
print(name1 == name2)
# kenapa false ? karena python case sensitive

name_rev = 'Reggina'
print(name_rev == name_rev)
# true karena perbandingan huruf sama sama case

print('\nPerbandingan lebih dari dan kurang dari pada string')
# annisa dan dina memiliki jenis baju yang berbeda
annisa = 'Dress'
dina = 'Kemeja'
print(annisa > dina)
# hasilnya false karena deret huruf b lebih awal dari huruf m

she = 'fia'
he = 'Farhan'
print(she > he)
# disini menghasilkan nilai true karena huruf non kapital ada di deret setelah z kapital

print('\nLogika operator')
number1 = 250
number2 = 200
result = number1 == (number2 + 50)
print(not result) # operator not akan mengembalikan false jika kondisi itu benar
# sebaliknya jika kondisi itu false maka operator not akan menghasilkan true
result2 = "selasa" == "selasa"
print(not result2)

print('\nBranch if else statment')

def username(name):
    if len(name) < 5: # len disini untuk menghitung jumlah karakter huruf (untuk menghitung apakah jumlah name >5
       print('name tidak valid panjang karakter name minimal lebih dari 5')
    else:
         print('username valid')
# atau bisa juga tanpa else ketika menggunakan return
# print('username valid')
username('Reggina')

def angkaGenap(x):
    if x % 2 == 0:
        return 'angka genap'
    return 'angka ganjil'

print(angkaGenap(10))

print('\nelif statement')

def password(pw):
    if len(pw) < 3:
        return 'pw tidak boleh kurang dari 3 karakter'
    elif len(pw) > 10:
        return 'pw tidak boleh lebih dari 10 karakter'
    return 'pw valid'

print(password('reggina123'))
