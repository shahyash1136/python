name = input("Enter your full name: ")
result = len(name)
result = name.find("Y")
result = name.rfind("S") # rfind finds the value in reverse
name = name.capitalize()
name = name.upper()
name = name.lower()
result = name.isdigit()
result = name.isalpha()
phone_num = input("Enter your phone #: ")
result = phone_num.count("-")
phone_num = phone_num.replace("-","")
print(phone_num)

# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("username is no more than 12 characters")
elif not username.isalpha():
    print("username must not contain digits")
elif not username.find(" ") == -1:
    print("username must not contain spaces")
else:
    print(f"Your username is: {username}")