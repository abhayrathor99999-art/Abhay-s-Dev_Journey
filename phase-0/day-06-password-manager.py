# CLI Password Manager — Version 1
# Data saved to passwords.json
# Functions needed:


from datetime import datetime
def get_current_date():
    now = datetime.now()
    return now.strftime("%d-%m-%Y")

print(get_current_date())


# 1. load_passwords()
import json
def load_passwords(filename: str) -> list:
    try:
        with open(filename, "r") as f:
            content = json.load(f)
            return content
    except json.JSONDecodeError:
            return []
    except FileNotFoundError:
            return []

# 2. save_passwords(passwords)
def save_passwords(passwords: list) -> str:
    with open("passwords.json", "w") as f:
        json.dump(passwords, f, indent=4)
    return "saved"

# 3. add_password(service, username, password)
def add_password(service: str, username: str, password: str) -> None:
    passwords = load_passwords("passwords.json") 
    new_entry = {"service": service, "username": username, "password": password}
    passwords.append(new_entry) 
    save_passwords(passwords) 
    print("Saved.")
        
# 4. list_passwords()
def list_password() -> None:
    passwords = load_passwords("passwords.json")
    for password in passwords:
        print((f"Service: {password['service']} | User: {password['username']}") )

# 5. search_password(service)
def search_password(service: str) -> dict | None:
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
# list_password()
search_password("gmail")
# search_password("twitter")
search_password("ygfcdygc")










































































# # 1. load_passwords()
# import json
# def load_passwords(filename):
#     try:
#         with open(filename, "r") as f:
#             content = json.load(f)
#             return content
#     except json.JSONDecodeError:
#             return []
#     except FileNotFoundError:
#             return []

# # 2. save_passwords(passwords)
# def save_passwords(passwords):
#     with open("passwords.json", "w") as f:
#         json.dump(passwords, f, indent=4)
#     return "saved"

# # 3. add_password(service, username, password)
# def add_password(service, username, password):
#     passwords = load_passwords("passwords.json") 
#     new_entry = {"service": service, "username": username, "password": password, "date"    : get_current_date()}
#     passwords.append(new_entry) 
#     save_passwords(passwords) 
#     print("Saved.")
        
# # 4. list_passwords()
# def list_password():
#     passwords = load_passwords("passwords.json")
#     for password in passwords:
#         print((f"Service: {password['service']} | User: {password['username']}") )

# # 5. search_password(service)
# def search_password(service):
#     passwords = load_passwords("passwords.json")
#     found = False
#     for password in passwords:
#         if password['service'] == service:
#             print(f"Found: {password['service']} | {password['username']}")
#             found = True
#     if not found:
#         print("Not found")

# # 6. get_current_date():
# from datetime import datetime

# def get_current_date():
#     now = datetime.now()
#     return now.strftime("%d-%m-%Y")

# print(get_current_date())



# add_password("gmail", "abhay@gmail.com", "pass123")
# add_password("github", "abhayrathor", "ghpass456")
# add_password("netflix", "abhay@gmail.com", "nfpass789")
# list_password()
# search_password("gmail")
# search_password("twitter")