import firebase_admin
from firebase_admin import credentials, db
import json
from datetime import datetime



cred = credentials.Certificate('serviceAccountKey.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://flufchat-default-rtdb.firebaseio.com/'
})


def add_user(name, age, email):
    users_ref = db.reference('users')

    date = datetime.now().strftime("%Y-%m-%d")

    users_ref.child(name).set({
        'name': name,
        'age': age,
        'email': email,
        'date': date
    })

def red(text):
    return f"\033[91m{text}\033[0m"

def green(text):
    return f"\033[92m{text}\033[0m"

def check_user(name):
    users_ref = db.reference('users')

    if users_ref.child(name).get():
        print(green("\nLogged in successfully!\n"))
    else:
        print(red("\nUser not found.\n"))

def main():
    while True:
        print("Options:")
        print("1) Sign Up")
        print("2) Log In")
        print("3) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            email = input("Enter your email: ")
            add_user(name, age, email)
            print("User signed up successfully!")
        elif choice == "2":
            name = input("Enter your name: ")
            check_user(name)
            break
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()

