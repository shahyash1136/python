## Day 1 - Smart Password Checker
# Features:
# - Take password input from user
# - Check minimum 8 characters
# - Check if uppercase letter exists
# - Check if digit exists
# - Check if special character exists
# - Show final strength: Weak / Medium / Strong


def passwordChecker(password):
    if len(password) < 8:
        print("Password must be minimum 8 character log")
    elif not password.isalnum():
        pass
    else:
        return  True


def passwordStrenght():
    pass

def main():
    isPasswordCorrect = False

    while not isPasswordCorrect:
        passwordInput = input("Enter Your Password: ")
        isPasswordCorrect = passwordChecker(passwordInput)

if __name__ == '__main__':
    main()




