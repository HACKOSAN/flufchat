import platform
import firebase_admin
from firebase_admin import credentials, db
import json
from datetime import datetime

cred = credentials.Certificate('serviceAccountKey.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://flufchat-default-rtdb.firebaseio.com/'
})

def red(text):
    return f"\033[91m{text}\033[0m"
def green(text):
    return f"\033[92m{text}\033[0m"

def add_user(username, age, email):
    # Get a database reference to the 'users' node
    users_ref = db.reference('users')

    # Get the current date
    date = datetime.now().strftime("%Y-%m-%d")

    # Prompt the user to enter a password (at least 6 characters)
    while True:
        password = input("Enter a password (at least 6 characters): ")
        if len(password) >= 6:
            break
        else:
            print("Password must be at least 6 characters long.")

    # Get information about the platform
    os_type = platform.system()
    os_version = platform.version()

    # Set the user data under the key generated from the username
    users_ref.child(username).set({
        'username': username,
        'age': age,
        'email': email,
        'date': date,
        'password': password,
        'os_type': os_type,
        'os_version': os_version
    })

# Function to check if a user exists in the database and validate the password
def check_user():
    # Get a database reference to the 'users' node
    users_ref = db.reference('users')

    # Prompt the user to enter the username and password
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")

    # Check if the user exists in the database
    user_data = users_ref.child(username).get()
    if user_data:
        # Validate the password
        if user_data.get('password') == password:
            print(green("\nLogged in successfully!"))
        else:
            print(red("\nIncorrect password."))
    else:
        print(red("\nUser not found."))

# Main function
def main():
    while True:
        print("\nOptions:")
        print("1) Sign Up")
        print("2) Log In")
        print("3) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            age = int(input("Enter your age: "))
            email = input("Enter your email: ")
            add_user(username, age, email)
            print(green("\nUser signed up successfully!"))
        elif choice == "2":
            check_user()
        elif choice == "3":
            break
        else:
            print(red("\nInvalid choice. Please try again."))


if __name__ == "__main__":
    main()

