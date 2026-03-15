def list_password():
    passwords = load_passwords("password.json")
    for password in passwords:
        print (f"Service: {password['service']} | User: {password['username']}")  

print(list_password())