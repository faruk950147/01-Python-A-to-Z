import getpass

password = getpass.getpass("Enter your password: ")
print("Password entered successfully.")
if password == "950147":
    print("Access granted.")
else:
    print("Access denied.")


# user_name = getpass.getuser()
# print("User name:", user_name)
# pass_word = "admin"
# user = input("Enter your user name: ")
# password = getpass.getpass("Enter your password: ")
# if user == user_name and password == pass_word:
#     print("Access granted.")
# else:
#     print("Access denied.")