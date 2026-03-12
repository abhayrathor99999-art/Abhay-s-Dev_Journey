print("Function 1 — clean_input------------------------------------------------------")

def clean_input(name):
    return name.strip().lower()

result = clean_input("   Abhay  ")
print (result)

print("Function 2 — is_valid_email---------------------------------------------------")

def is_valid_email(email_id):
    return ("@" in email_id and  "." in email_id)

result = is_valid_email("abhayrathor55@gmail.com")
print(result)

print("Function 3 — count_words------------------------------------------------------")

def count_words(sentence):
    split_s = sentence.split(" ")
    return len(split_s)

result = count_words("Hello my name is Abhay")
print(result)

print("Function 4 — initials---------------------------------------------------------")

def initials(full_name):
    words = full_name.split(" ")
    result = []
    for word in words:
        result.append(word[0].upper())
    return ".".join(result)

print(initials("abhay singh rathor"))
print(initials("rahul kumar"))
print(initials("a b c d"))