import string
import random
def generate_password(length,characters):
    password=""
    for r in range(length):
        password+=random.choice(characters)
    return password
def check_strength(password):
    length=len(password)
    has_appr=any(c.isupper() for c in password)
    has_lowr=any(c.islower() for c in password)
    has_digit=any(c.isdigit() for c in password)
    has_pun=any(c in string.punctuation for c in password)
    score=has_appr + has_lowr + has_digit + has_pun
    if length<8:
        return "Weak"
    elif score==4 and length>=12:
        return "Very Strong"
    elif score>=3 and length>=8:
        return "Strong"
    elif score==2:
        return "Medium"
    else:
        return "Weak"
# menu
try:
    length=int(input("Enter the length of password: "))
    if length<8:
        print("Password should be 8 characters long")
        exit()
except ValueError:
    print("Please enter a valid length")
    exit()
characters=""
upper=input("Do you want uppercase in your password: y/n ")
if upper=="y":
    characters+=string.ascii_uppercase
elif upper=="n":
    pass
else:
    print("Please enter y or n")
    exit()
lower=input("Do you want lowercase in your password: y/n ")
if lower=="y":
    characters+=string.ascii_lowercase
elif lower=="n":
    pass
else:
    print("Please enter y or n")
    exit()
numbers=input("Do you want numbers in your password: y/n ")
if numbers=="y":
    characters+=string.digits
elif numbers=="n":
    pass
else:
    print("Please enter y or n")
    exit()
symbols=input("Do you want symbols in your password: y/n ")
if symbols=="y":
    characters+=string.punctuation
elif symbols=="n":
    pass
else:
    print("Please enter y or n")
    exit()
if characters=="":
    print("Please select at least 1 or 2 character types ")
    exit()
try:
    count=int(input("How many passwords do you want: "))
    if count<=0:
        print("Please enter a number that is greater than 0")
        exit()
except ValueError:
    print("Please enter a valid count")
    exit()
for r in range(count):
    password=generate_password(length,characters)
    s=check_strength(password)
    print(f"Password: {password} | Strength: {s}")