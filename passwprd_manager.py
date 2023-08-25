master_password = input("Enter Master Password: ")

def view():
    with open("password.txt", 'r') as passwords_file:
        for line_of_password in passwords_file.readlines():
            print(line_of_password)


def add():
    account_name = input("Enter Account Name: ")
    user_name = input("Enter Username: ")
    account_password = input("Enter Account Password: ")

    with open("password.txt", 'a') as passwords_file:
        passwords_file.write(f"Account Name: {account_name} |  Username: {user_name} | Account Password:{account_password} \n")

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

