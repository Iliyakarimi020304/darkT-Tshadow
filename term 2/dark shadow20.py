username = "dark shadow"
password = "020304"

input_username = input('enter your USERNAME: ')
input_password = input('enter your PASSWORD: ')

if input_username.lower() == username and input_password == password:
    print("WELCOME SIR!")
else:
    print("Password or User is incorrect pls try again!")