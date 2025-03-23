""" solution 1 """

login = input("insert login: ")
full_name = input("insert full name: ")
password = input("insert password: ")

if login == "":
    print("Error: Login must not be empty")
else:
    print("login: ", login)
    print("full name: ", full_name)
    print("password: ", password)
