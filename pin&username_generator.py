import string
import random
def generate_username(name,length):
    for i in range(length):
        if i % 2 == 0:
            name+=random.choice(string.digits)
        else:
            name+=random.choice(string.punctuation)
    return name
def check_username_availability(username,existing_list):
    if username in existing_list:
        print("Username is not available")
        return False
    else:
        existing_list.append(username)
        print("Username is available")
        return True
def generate_pin(length):
    pin=""
    for i in range(length):
        pin+=random.choice(string.digits)
    return pin
def check_pin_strength(pin):
    if len(pin)<4:
        return "Weak"
    if not any(char !=pin[0] for char in pin):
        return "Weak"
    steps=[int(pin[i]) - int(pin[i - 1]) for i in range(1, len(pin))]
    if all(step==1 for step in steps) or all(step==-1 for step in steps):
        return "Weak"
    return "Strong"
name=input("Enter your name: ")
length=int(input("How many digits or symbols you want in username: "))
username=generate_username(name,length)
print(username)
existing_usernames=[]
c=check_username_availability(username,existing_usernames)
print(existing_usernames)
pin_length=int(input("Enter the length of pin: "))
g_pin=generate_pin(pin_length)
print(f"Username: {username} | Pin: {g_pin}")
s=check_pin_strength(g_pin)
print(f"Strength: {s}")
