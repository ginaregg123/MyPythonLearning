print('==== deret angka 1-5 ====')

for x in range(5):
    print(x)

print('==== menghitung deret angka ====')

number = [23,45,67,89,34] #mendefinisikan daftar nilai
#inisialisasi 2 variabel:sum,length
sum = 0
length = 0
#Dalam perulangan for, kami mengulangi setiap nilai dalam daftar,menambahkan nilai saat ini ke jumlah nilai
#kemudian menambahkan 1 ke panjangnya,yang menghitung berapa banyak elemen yang ada dalam daftar
for x in number:
    sum+= x
    length+= 1

print('Total sum: ' + str(sum) + ' - Average: ' + str(sum/length))

sum = 0
length = 0

print('==== Example ====')
for x in range(10):
    sum += x
    length += 1

print('this sum is: ', str(sum), ' - average is: ', str(sum/length))

print('\n==== Memunculkan data di dalam deret list ====')

orangIndonesia= ['Annisa', 'Dinda', 'Reggina']

for x in orangIndonesia:
    print('hallo ', str(x))

print('\n==== about fungsi range ====')

# range(start, stop, step)
print('\nRange start, stop, step')

print('\nContoh 1')
for x in range(2, 10, 2):
    print(x)

print('\nContoh 2')
for x in range(2, 10+1, 2):
    print('\n', str(x))

print('\nContoh 3')
for x in range(10, 0, -1):
    print('\n', str(x))

print('\nContoh 4')
for x in range(2, -2, -1):
    print('\n', str(x))

print('\Contoh 5')
for number in range(1,6+1,2):
    print(number*3)

# Pada iterasi pertama, number adalah 1 (nilai awal dalam rentang), dan 1 * 3 dicetak, menghasilkan output 3.
# Pada iterasi kedua, number adalah 3 (ditambahkan 2 dari iterasi sebelumnya), dan 3 * 3 dicetak, menghasilkan output 9.
# Pada iterasi ketiga, number adalah 5 (ditambahkan 2 dari iterasi sebelumnya), dan 5 * 3 dicetak, menghasilkan output 15.

# range(start, stop)
print('\nRange start,stop')

print('\nContoh 1')
for number in range(2,7+1):
    print(number*3)

#Pertama, variabel number diatur ke nilai 2 (nilai awal dalam rentang).
#Pada iterasi pertama, nilai number adalah 2, maka 2 * 3 dicetak, dan outputnya adalah 6.
#Selanjutnya, nilai number akan bertambah 1 menjadi 3, dan 3 * 3 dicetak, menghasilkan output 9.
#Proses ini berlanjut hingga mencapai nilai 7. Pada iterasi terakhir, nilai number adalah 7, sehingga 7 * 3 dicetak, menghasilkan output 21.

print('\n==== nested loop ====')

for left in range(7):
    for right in range(left, 7):
        print('[ ' + str(left) + ' | ' + str(right) + ' ]', end=" ")
    print()

print('\n==== example another neted loop====')
club = ['Liverpool', 'MU', 'PSG', 'Barcelona', 'Real madrid', 'Arsenal']

for team_a in club:
    for team_b in club:
        if (team_a != team_b):
            print(team_a, " vs ", team_b)

print('\nFor loops in iterable string')

def helloName(name):
    for x in name:
        print('hello ', x)

helloName("reggina")


