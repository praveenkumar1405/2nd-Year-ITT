import re
def is_valid_gmail(email):
    pattern = r'^[a-zA-Z0-9._]+@gmail\.com$'
    return re.match(pattern, email) is not None

# Input
email = input("Enter Gmail ID: ")

if is_valid_gmail(email):
    print("Valid Gmail ID")
else:
    print("Invalid Gmail ID")
