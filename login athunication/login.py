import os
import hashlib

# File to store user credentials
USER_DATA_FILE = 'user_data.txt'

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    """Register a new user."""
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if not username or not password:
        print("Username and password cannot be empty.")
        return

    # Check if the username already exists
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            for line in f:
                stored_username, _ = line.strip().split(':')
                if stored_username == username:
                    print("Username already exists. Please try a different username.")
                    return

    # Save the new user's credentials
    with open(USER_DATA_FILE, 'a') as f:
        f.write(f"{username}:{hash_password(password)}\n")
    print("Registration successful!")

def login():
    """Log in an existing user."""
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if not os.path.exists(USER_DATA_FILE):
        print("No users registered. Please register first.")
        return False

    with open(USER_DATA_FILE, 'r') as f:
        for line in f:
            stored_username, stored_password = line.strip().split(':')
            if stored_username == username and stored_password == hash_password(password):
                print("Login successful!")
                return True

    print("Invalid username or password.")
    return False

def secured_page():
    """Secured page that only logged-in users can access."""
    print("Welcome to the secured page!")

def main():
    while True:
        choice = input("Do you want to (R)egister, (L)ogin, or (Q)uit? ").upper()

        if choice == 'R':
            register()
        elif choice == 'L':
            if login():
                secured_page()
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose R, L, or Q.")

if __name__ == "__main__":
    main()
