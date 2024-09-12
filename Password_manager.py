
import hashlib
import getpass

password_manager = {}


def create_account():
    username = input("Enter your desired username")
    password = getpass.getpass("Enter your desired password")
    hashed_passwrod = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_passwrod
    print("Account created successfully!")


def login():
    username = input("enter your username:")
    password = getpass.getpass("enter your passwrod :")
    hashed_passwrod = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_passwrod:
        print("login successfull")
    else:
        print("invalid userneme or password.")


def main():
    while True:
        chice = input(
            "enter 1 to create an account , 2 to login , or 0 to exit:")
        if chice == "1":
            create_account()
        elif chice == "2":
            login()
        elif chice == "0":
            break
        else:
            print("invaild choice")


if __name__ == "__main__":
    main()
