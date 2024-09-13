# Python Password Manager

This is a simple password management application built using Python, designed for secure user authentication. It allows users to create accounts and log in using hashed passwords for enhanced security. This project demonstrates fundamental principles of cybersecurity, such as password hashing and input validation.

## Features
- **Account Creation:** Users can create accounts with unique usernames and passwords.
- **Secure Password Handling:** Passwords are hashed using the SHA-256 algorithm before being stored.
- **User Login:** Users can securely log in using their username and password.
- **Input Validation:** Includes checks for username uniqueness and minimum password length.

## How It Works
1. **Account Creation:**
   - Users provide a username and password.
   - Passwords are hashed using `hashlib.sha256` before being stored to ensure security.
   
2. **Login:**
   - Users provide their username and password.
   - The password is hashed and compared with the stored hash to verify user identity.

3. **Password Security:**
   - The `getpass` module ensures that passwords are not visible on the screen when entered.
   - SHA-256 hashing provides a cryptographic way of protecting passwords.

## Requirements
- Python 3.x

## Usage
1. Clone the repository or download the `password_manager.py` file.
2. Run the script using Python:
   ```bash
   python password_manager.py

Example
Create an Account:

hamzah

Enter your desired username: user1
Enter your desired password: ********
Account created successfully!

Login:

hamzah

Enter your username: user1
Enter your password: ********
Login successful!
