from random import randint
from os import system
from time import sleep
import csv


def encrypt(password, KEY):
    all_chars = "".join(chr(x) for x in range(33,127))
    char_to_num = {all_chars[x]: x for x in range(len(all_chars))}

    while len(KEY) < len(password):
        KEY += KEY

    encrypted_password = ""

    for i in range(len(password)):
        if i % 2 == 0:
            encrypted_password += all_chars[
                (char_to_num[password[i]] + char_to_num[KEY[i]]) % len(all_chars)
            ]
        else:
            encrypted_password += all_chars[
                (char_to_num[password[i]] - char_to_num[KEY[i]]) % len(all_chars)
            ]

    return encrypted_password


def hash(password):
    all_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    hashed_password = ""

    for i in range(0, len(password)):
        value = 0
        if i % 2 == 0:
            for j in range(i, len(password)):
                value += ord(password[j])
        else:
            for j in range(0, i+1):
                value += ord(password[j])

        hashed_password += all_chars[value % len(all_chars)]

    return hashed_password
 

def generate_salt():
    return "".join(chr(randint(33, 126)) for _ in range(10))


def get_password(password, salt):
    KEY = salt
    hashed_password = hash(encrypt(password, KEY))
    hashed_salt = hash(salt)

    return hashed_password + hashed_salt


def write_details(username, password):
    salt = generate_salt()
    password = get_password(password, salt)
    row = [username, password, salt]

    filename = "data.csv"

    with open(filename, "a") as file:
        writer = csv.writer(file)
        writer.writerow(row)


def get_details(username):
    filename = "data.csv"

    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row != []:
                if row[0] == username:
                    return [row[1], row[2]]
        return None


if __name__ == "__main__":
    while True:
        choice = input("1. Sign Up\n2. Sign In\n3. Exit\nYour choice : ")
        if choice == "1":
            system("cls")
            username = input("Username : ")
            check = get_details(username)
            if check:
                print("Username exists.")
                sleep(1.5)
                system("cls")
                continue

            password = input("Password : ")

            write_details(username, password)
            print("Sign Up successful.")
            sleep(1.5)
            system("cls")

        elif choice == "2":
            system("cls")
            username = input("Username : ")

            details = get_details(username)
            if details == None:
                print("Username not found")
                continue

            PASSWORD, SALT = details

            password = input("Password : ")

            if PASSWORD == get_password(password, SALT):
                system("cls")
                print(f"Sign in successful.\nSigned in as {username}.")
                sleep(1.5)
            else:
                system("cls")
                print("Incorrect Password")
                sleep(0.5)

        elif choice == "3":
            system("cls")
            break

        else:
            system("cls")
            print("Wrong input")
            sleep(0.5)