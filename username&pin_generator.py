# Username/PIN Generator with Strength & Uniqueness Checker
import string
import random
def generate_username(name,length):
    for i in range(length):
        if i % 2 == 0:
            name+=random.choice(string.digits)
        else:
            name+=random.choice(string.punctuation)
        # name+=random.choice(string.digits + string.punctuation)
    return name
def check_username_availability(username,existing_list):
    if username in existing_list:
        print("Username already exists!")
        return False
    else:
        existing_list.append(username)  
        print("Username available")
        return True
def generate_pin(length):
    pin=""
    for i in range(length):
        pin+=random.choice(string.digits)
    return pin
def check_pin_strength(pin):
    if len(pin) < 4:
        return "weak"
    if not any(char != pin[0] for char in pin):
        return "weak"
    steps = [int(pin[i]) - int(pin[i - 1]) for i in range(1, len(pin))]
    if all(step == 1 for step in steps) or all(step == -1 for step in steps):
        return "weak"
    return "strong"

# main menu
name=input("Enter your name: ")
try:
    name_length=int(input("Enter the length of name: "))
except ValueError:
    print("Please enter a valid number")
    exit()
username=generate_username(name,name_length)
print(username)
existing_usernames=[]
c=check_username_availability(username,existing_usernames)
try:
    p_length=int(input("Enter the length of pin: "))
except ValueError:
    print("Please enter a valid number")
    exit()
g_pin=generate_pin(p_length)
print(f"Username: {username} | Pin: {g_pin}")
print(f"Pin strength: {check_pin_strength(g_pin)}")
