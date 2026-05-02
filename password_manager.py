
master_pwd = input("Enter master password: ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, pwd = data.split(":")
            print(f"Name: {name}, Password: {pwd}")

def add():
    name = input("Enter the account name: ")
    pwd = input("Enter the password: ")
    
    
    with open("passwords.txt", "a") as f:
        f.write(f"{name}:{pwd}\n")
        
        
while True:
    mode = input("Would you like to add a new password or view the existing ones? (add / view) press 'q' to quit: ").lower()
    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode. Please try again.")
        