from cryptography.fernet import Fernet

#key to decrypt test 
'''
def create_key():
    created_key = Fernet.generate_key()
    with open("created_key.key", 'wb') as key_file:
        key_file.write(created_key)
'''

def load_key():
    key_file = open("created_key", "rb")
    key = key_file.read()
    key_file.close()
    return key


master_password = input("Enter Master Password: ")
key = load_key() + master_password.bytes
fer = Fernet(key)


def view():
    with open("password.txt", 'r') as passwords_file:
        for line_of_password in passwords_file.readlines():
            # print(line_of_password.rstrip())
            password_file_data = line_of_password.rstrip()
            account, username, password = password_file_data.split(" -|- ")
            print(f"Account Name: {account},  Username: {username},   Account Password:{password}")

def add():
    account_name = input("Enter Account Name: ")
    user_name = input("Enter Username: ")
    account_password = input("Enter Account Password: ")

    with open("password.txt", 'a') as passwords_file:
        passwords_file.write(f"Account: {account_name} -|-  User: {user_name} -|- Password:{account_password} \n")

while True:
    selected_mode = input(" Enter 'view' to see existing passwords or enter 'add' to add new passwords. Enter 'q' to QUIT ").upper()
    if selected_mode == "Q":
        break

    if selected_mode == "VIEW":
        view()
    elif selected_mode == "ADD":
        add()
    else:
        print("select a valid mode")

