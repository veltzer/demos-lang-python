login = input('insert login: ')
full_name = input('insert full name: ')
password = input('insert password: ')

if login == '':
    print("Error: Login must not be empty")
else:
    print(f"login: {login}")
    print(f"full name: {full_name}")
    print(f"password: {password}")
