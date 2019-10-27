data = {'user1': 'password1', 'Mark': '1234', 'Danny': 'qwert'}
username = input("Enter the username")
password = input("Enter the password")
if data.get(username) != password:
    print("Password or username is wrong")
elif data.get(username) == password:
    print("Everything is ok")