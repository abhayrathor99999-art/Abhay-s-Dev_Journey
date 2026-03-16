# import os

# # Where am I right now?
# print(os.getcwd())

# # List all files in current folder
# print(os.listdir())

# # Does a file or folder exist?
# print(os.path.exists("passwords.json"))
# print(os.path.exists("missing_file.txt"))

# import os

# # Create a folder
# os.makedirs("test_folder", exist_ok=True)
# print("Folder created")

# # Check if it exists
# print(os.path.exists("test_folder"))

# # Is it a folder or a file?
# print(os.path.isdir("test_folder"))
# print(os.path.isfile("test_folder"))

# # Join paths properly
# path = os.path.join("test_folder", "notes.txt")
# print(path)


# import os 

# print(os.getcwd())
# os.makedirs("my_data", exist_ok=True)
# print(os.path.isdir("my_data"))
# path = os.path.join("my_data","passwords.json")
# print(path)


# from datetime import datetime

# now = datetime.now()

# print(now.strftime("%d-%m-%Y"))
# print(now.strftime("%d %B %Y"))
# print(now.strftime("%H:%M:%S"))

from datetime import datetime

def get_current_date():
    now = datetime.now()
    return now.strftime("%d-%m-%Y")

print(get_current_date())



# 1. load_passwords()
import json
def load_passwords(filename):
    try:
        with open(filename, "r") as f:
            content = json.load(f)
            return content
    except json.JSONDecodeError:
            return []
    except FileNotFoundError:
            return []

# 2. save_passwords(passwords)
def save_passwords(passwords):
    with open("passwords.json", "w") as f:
        json.dump(passwords, f, indent=4)
    return "saved"

# 3. add_password(service, username, password)
def add_password(service, username, password):
    passwords = load_passwords("passwords.json") 
    new_entry = {"service": service, "username": username, "password": password, "date"    : get_current_date()}
    passwords.append(new_entry) 
    save_passwords(passwords) 
    print("Saved.")
        
# 4. list_passwords()
def list_password():
    passwords = load_passwords("passwords.json")
    for password in passwords:
        print((f"Service: {password['service']} | User: {password['username']}") )

# 5. search_password(service)
def search_password(service):
    passwords = load_passwords("passwords.json")
    found = False
    for password in passwords:
        if password['service'] == service:
            print(f"Found: {password['service']} | {password['username']}")
            found = True
    if not found:
        print("Not found")



add_password("gmail", "abhay@gmail.com", "pass123")
add_password("github", "abhayrathor", "ghpass456")
add_password("netflix", "abhay@gmail.com", "nfpass789")
list_password()
search_password("gmail")
search_password("twitter")