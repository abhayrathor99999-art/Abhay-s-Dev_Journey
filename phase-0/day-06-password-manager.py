# CLI Password Manager — Version 1
# Data saved to passwords.json
# Functions needed:

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
    new_entry = {"service": service, "username": username, "password": password}
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