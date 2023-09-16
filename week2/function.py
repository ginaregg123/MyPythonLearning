def greeting (name,departement):
# def = keyword
# function muncul setelah keyword
# disini kita membuat sebuah function dimana name,departement --> parameter
    print("Welcome " + name)
    print("You are part of " + departement)

greeting("Reggina","Data Science")
greeting("Reggina Indriani", "Data Analyst")

print('\nreturn value and none')
def greeting(name) :
    print("Welcome, " + name)

result = greeting("Annisa")
print(result) # this result is none because not return value another when initialize in variabel


print('\nWith return value')
def convert_second(second):
    hours = second // 3600
    minutes = (second - hours * 3600) // 60
    remaining_second = second - hours * 3600 - minutes * 60
    return hours, minutes, remaining_second # -- result

result = convert_second(5000)
print(result) # sedangkan ini mencetak tuple secara keseluruhan

