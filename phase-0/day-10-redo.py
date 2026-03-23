import json

# =======================================================================
# DAY 10 REDO — OOP Part 2
# StorageManager + PasswordManager — Full Low-Level First Build
# =======================================================================
# WHAT WE LEARNED:
# - Inheritance    → PasswordManager IS A StorageManager
# - @property      → Encapsulation — controlled access to data
# - @classmethod   → Alternative constructors — belong to the class
# - @staticmethod  → Utility functions — belong to the class logically
# - Generators     → yield one value at a time — memory efficient
# =======================================================================
# FOUR PILLARS DEMONSTRATED:
# - Encapsulation  → data bundled, controlled via @property
# - Inheritance    → PasswordManager gets load/save for free
# - Polymorphism   → same method name, different behaviour per class
# - Abstraction    → caller uses pm.filename — has no idea what runs inside
# =======================================================================


class StorageManager:
    """
    Parent class — handles all generic file storage operations.
    Any storage tool (PasswordManager, NoteManager, etc.) inherits from here.
    This is INHERITANCE — write once, all children get it for free.
    """

    # -------------------------------------------------------------------
    # __init__ — sets up filename and empty data list
    # self.filename triggers the @property setter automatically
    # -------------------------------------------------------------------
    def __init__(self, filename: str) -> None:
        self.filename = filename     # triggers setter — validates input
        self.data = []

    # -------------------------------------------------------------------
    # @property — GETTER
    # Controls HOW filename is READ from outside
    # Caller writes: pm.filename → this runs behind the scenes
    # This is ENCAPSULATION — controlled access
    # -------------------------------------------------------------------
    @property
    def filename(self) -> str:
        return self._filename        # _filename = private, don't touch directly

    # -------------------------------------------------------------------
    # @filename.setter — SETTER
    # Controls HOW filename is WRITTEN from outside
    # Caller writes: pm.filename = "x" → this runs behind the scenes
    # Validates that filename ends with .json before storing
    #
    # LOW-LEVEL INSIGHT: before @property, this was done with manual
    # get_filename() and set_filename() methods — ugly and verbose.
    # @property gives same control with clean attribute syntax.
    # -------------------------------------------------------------------
    @filename.setter
    def filename(self, value: str) -> None:
        if value.endswith(".json"):
            self._filename = value
        else:
            print(f"Error: filename must end with .json — got '{value}'")

    # -------------------------------------------------------------------
    # load — reads from file into self.data
    # Uses self._filename directly — bypasses property for internal use
    # pass = do nothing if file missing or JSON broken
    # -------------------------------------------------------------------
    def load(self) -> None:
        try:
            with open(self._filename, "r") as f:
                self.data = json.load(f)
        except json.JSONDecodeError:
            pass
        except FileNotFoundError:
            pass

    # -------------------------------------------------------------------
    # save — writes self.data into file
    # -------------------------------------------------------------------
    def save(self) -> None:
        with open(self._filename, "w") as f:
            json.dump(self.data, f, indent=4)


class PasswordManager(StorageManager):
    """
    Child class — inherits all file operations from StorageManager.
    Only adds what is UNIQUE to passwords.
    This is INHERITANCE + ENCAPSULATION working together.
    """

    # -------------------------------------------------------------------
    # @classmethod — default()
    # Alternative constructor — creates PasswordManager with default filename
    # cls = PasswordManager — called on the class, not on an object
    # LOW-LEVEL: without @classmethod this would be a floating function
    # outside the class — not encapsulated
    # -------------------------------------------------------------------
    @classmethod
    def default(cls) -> "PasswordManager":
        return cls("passwords.json")

    # -------------------------------------------------------------------
    # @classmethod — from_config()
    # Alternative constructor — creates PasswordManager from a config dict
    # -------------------------------------------------------------------
    @classmethod
    def from_config(cls, config: dict) -> "PasswordManager":
        return cls(config["filename"])

    # -------------------------------------------------------------------
    # add_password — creates new entry dict, appends, saves immediately
    # self.data inherited from StorageManager — no redefinition needed
    # -------------------------------------------------------------------
    def add_password(self, service: str, username: str, password: str) -> None:
        new_entry = {"service": service, "username": username, "password": password}
        self.data.append(new_entry)
        self.save()

    # -------------------------------------------------------------------
    # search_password — finds entries by service name, case insensitive
    # Returns list of all matches
    # -------------------------------------------------------------------
    def search_password(self, service: str) -> list:
        result = []
        for entry in self.data:
            if entry["service"].lower() == service.lower():
                result.append(entry)
        return result

    # -------------------------------------------------------------------
    # list_passwords — prints every entry one by one
    # -------------------------------------------------------------------
    def list_passwords(self) -> None:
        for entry in self.data:
            print(entry)

    # -------------------------------------------------------------------
    # @staticmethod — is_strong()
    # Utility function — checks password strength
    # No self, no cls — does not touch any object or class data
    # Called on class: PasswordManager.is_strong("abc123")
    #
    # LOW-LEVEL: built manual count loop first, then earned len()
    # Manual version:
    #   count = 0
    #   for char in password:
    #       count += 1
    #   return count >= 8
    # -------------------------------------------------------------------
    @staticmethod
    def is_strong(password: str) -> bool:
        return len(password) >= 8

    # -------------------------------------------------------------------
    # yield_passwords — generator method
    # Produces one password entry at a time — never loads all into memory
    # Memory efficient for large datasets
    #
    # LOW-LEVEL INSIGHT:
    # return → gives all data at once → high memory usage
    # yield  → pauses, gives one value, remembers position → low memory
    # -------------------------------------------------------------------
    def yield_passwords(self):
        for entry in self.data:
            yield entry


# =======================================================================
# TESTS — one section per concept
# =======================================================================

# --- Test 1: @property setter validation ---
print("=== Test 1: @property setter ===")
pm = PasswordManager("passwords.json")
pm.filename = "hacked"           # rejected — no .json
pm.filename = "new.json"         # accepted
print(pm.filename)               # new.json

# --- Test 2: @classmethod — default constructor ---
print("\n=== Test 2: @classmethod default ===")
pm1 = PasswordManager.default()
print(pm1.filename)              # passwords.json

# --- Test 3: @classmethod — from_config constructor ---
print("\n=== Test 3: @classmethod from_config ===")
pm2 = PasswordManager.from_config({"filename": "work.json"})
print(pm2.filename)              # work.json

# --- Test 4: @staticmethod — password strength ---
print("\n=== Test 4: @staticmethod is_strong ===")
print(PasswordManager.is_strong("abc"))        # False — less than 8 chars
print(PasswordManager.is_strong("abc12345"))   # True — 8 chars

# --- Test 5: add, list, search ---
print("\n=== Test 5: add, list, search ===")
pm = PasswordManager.default()
pm.load()
pm.add_password("GitHub", "abhay", "abc123")
pm.add_password("Google", "abhay", "xyz789")
pm.list_passwords()
print(pm.search_password("github"))

# --- Test 6: generator — yield_passwords ---
print("\n=== Test 6: generator yield_passwords ===")
pm3 = PasswordManager.default()
pm3.load()
for entry in pm3.yield_passwords():
    print(entry)

# --- Test 7: inheritance proof ---
print("\n=== Test 7: inheritance proof ===")
# PasswordManager has zero load/save code
# It inherited everything from StorageManager
print(type(pm3))                    # PasswordManager
print(isinstance(pm3, StorageManager))  # True — IS A StorageManager