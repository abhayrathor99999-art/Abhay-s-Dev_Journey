
import json

# =======================================================================
# PASSWORD MANAGER — OOP Version
# Day 9 Redo — Built from scratch using classes
# =======================================================================
# WHAT WE LEARNED:
# - A class bundles DATA and METHODS together
# - Data  = what the object HAS  (self.filename, self.passwords)
# - Method = what the object CAN DO (load, save, add, search, list)
# - This is ENCAPSULATION — Pillar 1 of OOP
# =======================================================================


class PasswordManager:

    # -------------------------------------------------------------------
    # __init__ — runs automatically when object is created
    # Saves starting data onto the object
    # self.filename = where passwords are saved
    # self.passwords = list of all password entries in memory
    # -------------------------------------------------------------------
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.passwords = []

    # -------------------------------------------------------------------
    # load_passwords — reads from file into self.passwords
    # Low-Level First: no shortcuts — direct json.load into self.passwords
    # pass = do nothing if file not found or JSON is broken
    # -------------------------------------------------------------------
    def load_passwords(self) -> None:
        try:
            with open(self.filename, "r") as f:
                self.passwords = json.load(f)
        except json.JSONDecodeError:
            pass
        except FileNotFoundError:
            pass

    # -------------------------------------------------------------------
    # save_passwords — writes self.passwords into file
    # Called automatically by add_password after every new entry
    # -------------------------------------------------------------------
    def save_passwords(self) -> None:
        with open(self.filename, "w") as f:
            json.dump(self.passwords, f, indent=4)

    # -------------------------------------------------------------------
    # add_password — adds a new entry to self.passwords
    # Creates a dict, appends to list, saves immediately
    # -------------------------------------------------------------------
    def add_password(self, service: str, username: str, password: str) -> None:
        new_entry = {"service": service, "username": username, "password": password}
        self.passwords.append(new_entry)
        self.save_passwords()

    # -------------------------------------------------------------------
    # search_password — finds entries by service name
    # Case insensitive — "GitHub" and "github" both match
    # Returns a list of all matching entries
    # -------------------------------------------------------------------
    def search_password(self, service: str) -> list:
        results = []
        for entry in self.passwords:
            if entry["service"].lower() == service.lower():
                results.append(entry)
        return results

    # -------------------------------------------------------------------
    # list_passwords — prints every entry one by one
    # -------------------------------------------------------------------
    def list_passwords(self) -> None:
        for entry in self.passwords:
            print(entry)

    # -------------------------------------------------------------------
    # __str__ — controls what prints when you do print(pm)
    # For USERS — friendly readable output
    # LOW-LEVEL: built manual count loop first, then earned len()
    # -------------------------------------------------------------------
    def __str__(self) -> str:
        return f"PasswordManager(file='{self.filename}', entries={len(self.passwords)})"

    # -------------------------------------------------------------------
    # __repr__ — controls what prints when you do repr(pm)
    # For DEVELOPERS — shows exact data inside the object
    # -------------------------------------------------------------------
    def __repr__(self) -> str:
        return f"PasswordManager(filename='{self.filename}', passwords={self.passwords})"

    # -------------------------------------------------------------------
    # __len__ — defines what len(pm) returns
    # LOW-LEVEL: built manual count loop first, then earned len()
    #
    # Manual version (what len() does internally):
    # count = 0
    # for entry in self.passwords:
    #     count += 1
    # return count
    #
    # Pythonic version (earned after building manually):
    # -------------------------------------------------------------------
    def __len__(self) -> int:
        return len(self.passwords)

    # -------------------------------------------------------------------
    # __eq__ — defines how == compares two PasswordManager objects
    # By default Python compares memory addresses — always False
    # __eq__ lets us compare by actual data instead
    #
    # Manual version (built first):
    # if self.filename == other.filename:
    #     if self.passwords == other.passwords:
    #         return True
    # return False
    #
    # Pythonic version (earned after building manually):
    # -------------------------------------------------------------------
    def __eq__(self, other) -> bool:
        return self.filename == other.filename and self.passwords == other.passwords


# =======================================================================
# TESTS — one for each method and dunder
# =======================================================================

# --- Test 1: Basic creation and __str__ ---
print("=== Test 1: Create object ===")
pm = PasswordManager("passwords.json")
print(pm)                        # uses __str__

# --- Test 2: load and add ---
print("\n=== Test 2: Load and Add ===")
pm.load_passwords()
pm.add_password("GitHub", "abhay", "abc123")
pm.add_password("Google", "abhay", "xyz789")
pm.list_passwords()

# --- Test 3: __str__ and __repr__ after adding ---
print("\n=== Test 3: str and repr ===")
print(pm)                        # uses __str__
print(repr(pm))                  # uses __repr__

# --- Test 4: __len__ ---
print("\n=== Test 4: len(pm) ===")
print(len(pm))                   # uses __len__ — should print 2

# --- Test 5: search ---
print("\n=== Test 5: Search ===")
results = pm.search_password("github")   # lowercase — tests case insensitive
print(results)

# --- Test 6: __eq__ — same data ---
print("\n=== Test 6: Equality — same data ===")
pm1 = PasswordManager("passwords.json")
pm2 = PasswordManager("passwords.json")
print(pm1 == pm2)                # True — both empty, same filename

# --- Test 7: __eq__ — different data ---
print("\n=== Test 7: Equality — different data ===")
pm1.add_password("GitHub", "abhay", "abc123")
print(pm1 == pm2)                # False — pm1 has entry, pm2 is empty






































































































































































# import json

# class PasswordManager:
#     def __init__(self, filename: str) -> None:
#         self.filename = filename
#         self.passwords = []

#     def load_passwords(self) -> None:
#         try:
#             with open(self.filename, "r") as f:
#                 self.passwords = json.load(f)
#         except json.JSONDecodeError:
#             pass
#         except FileNotFoundError:
#             pass

#     def save_passwords(self) -> None:
#         with open(self.filename, 'w') as f:
#             json.dump(self.passwords, f, indent=4)

#     def add_password(self, service: str, username: str, password: str) -> None:
#         new_entry = {"service": service, "username": username, "password": password}
#         self.passwords.append(new_entry)
#         self.save_passwords()

#     def search_password(self, service: str) -> list:
#         results = []
#         for entry in self.passwords:
#             if entry["service"].lower() == service.lower():
#                 results.append(entry)
#         return results

#     def list_passwords(self) -> None:
#         for entry in self.passwords:
#             print(entry)
        
#     def __str__(self) -> str:
#         return f"PasswordManager(file='{self.filename}', entries={len(self.passwords)})"

#     def __repr__(self) -> str:
#         return f"PasswordManager(filename='{self.filename}', passwords={self.passwords})"

#     def __len__(self) -> int:
#         # count = 0
#         # for entry in self.passwords:
#         #     count += 1
#         # return count 
#         return len(self.passwords)

#     # def __eq__(self, other) -> bool:
#     #     if self.filename == other.filename:
#     #         if self.passwords == other.passwords:
#     #             return True
#     #     return False

#     def __eq__(self,other) -> bool:
#         return self.filename == other.filename and self.passwords == other.passwords

# # pm = PasswordManager("passwords.json")
# # pm.load_passwords()
# # pm.add_password("GitHub", "abhay", "abc123")
# # pm.list_passwords()
# # print(pm)
# # print(repr(pm))
# # pm.load_passwords()
# # pm.add_password("GitHub", "abhay", "abc123")
# # print(len(pm))

# # pm1 = PasswordManager("passwords.json")
# # pm2 = PasswordManager("passwords.json")
# # print(pm1 == pm2)

# pm1 = PasswordManager("passwords.json")
# pm2 = PasswordManager("passwords.json")
# pm1.add_password("GitHub", "abhay", "abc123")
# print(pm1 == pm2)