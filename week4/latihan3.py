print('\nSoal 1 dictionaries')

# The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
    emails = []
    for domain, users in domains.items():  # Menggunakan domains.items() untuk mendapatkan pasangan kunci dan nilai dari kamus.
        for user in users:
            email = f"{user}@{domain}"  # Membuat alamat email dengan menggabungkan nama pengguna dan domain.
            emails.append(email)  # Menggunakan append untuk menambahkan alamat email ke daftar emails.
    return emails  # Mengembalikan daftar email.

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

print('\nSoal 2')

# The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.
def groups_per_user(group_dictionary):
    user_groups = {}
    # Mengiterasi melalui group_dictionary
    for group, users in group_dictionary.items():
        # Mengiterasi melalui pengguna dalam grup
        for user in users:
            # Memeriksa apakah pengguna sudah ada dalam user_groups
            if user in user_groups:
                # Jika pengguna sudah ada, tambahkan grup ke daftar grup pengguna
                user_groups[user].append(group)
            else:
                # Jika pengguna belum ada, buat entri baru dengan grup sebagai daftarnya
                user_groups[user] = [group]
    return user_groups

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

print('\nSoal 3')

# The add_prices function returns the total price of all of the groceries in the  dictionary. Fill in the blanks to complete this function.

def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for item, price in basket.items():
        # Add each price to the total calculation
        total += price
    # Limit the return value to 2 decimal places
    return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
    "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44