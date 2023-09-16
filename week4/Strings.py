print('\nSoal 1')

fruit = "Pineapple"
print(fruit[:4]) #Mengakses potongan dari nol ke 4 membutuhkan empat potongan pertama karakter string, (indeks 0 hingga 3).
print(fruit[4:]) #Mengakses irisan dari 4 hingga karakter akhir ( mulai dari indeks empat dan seterusnya).
print(fruit[1:4]) #Irisan tersebut menyertakan karakter pada indeks 1, dan mengecualikan karakter pada indeks 4.

print('\nSoal 2')

#LOWER
answer = "YES"
if answer.lower() == "yes":
    print("user said yes")

# metode string Lstrip
" yes ".lstrip()
#should print 'yes '

#metode string Lstrip
" yes ".rstrip()
#should print ' yes'

#method endswith
"Forest".endswith("rest")
#Should print True -> jika true berarti string tersebut diakhir dengan kata tersebut.

print('\nFormatting String')

name ="Reggina"
number = len(name) * 3
print("Hello {} , your lucky number is {}" .format(name,number))
print("Your luck number is {number}, {name}.".format(name=name, number = len(name) * 3))

#contoh lain

#Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam".
#For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".

def student_grade(name, grade):
	return ("{} received {}% on the exam".format(name,grade))

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

#contoh lain

#kita ingin menulis harga sebelum kena pajak dan sesudah kena pajak

price = 7.5
with_tax = price * 1.09
print(price,with_tax) #--> ini belum menggunakan format string

#contoh menggunakan format string
print("Base price : ${:2f}. With Tax : ${:2f}".format(price,with_tax))  #--> di antara tanda kurung kurawal kita menulis ekspresi pemformatan( formatting expression ).
#{:2f} --> Ini berarti kita akan memformat nomor float dan harus ada dua digit setelah titik desimal.Jadi berapapun harganya, fungsi kita selalu mencetak dua desimal.

#contoh lain mengubah suhu farenheit menjadi celcius
def to_celcius(x):
    return (x-32) * 5/9

for x in range(0,101,10):
    print("{:>3} F | {:>6.2F} C".format(x, to_celcius(x)))

#menggunakan operator lebih besar dari untuk menyelaraskan tekstepat agar keluarannya selaras dengan rapi.
# {:>3} -> Dalam ekspresi pertama kami mengatakan kami ingin angka-angkanya disejajarkankanan untuk total tiga spasi.
# {:>6.2F} -> Dalam ekspresi kedua, kita ingin bilangan tersebut selalu tepat duatempat desimal dan kami ingin menyelaraskannya ke kanan pada enam spasi.