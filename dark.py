
# Welcome Message.
print('\n\t"Welcome to DARK Bank"')
print("\tx~~~~~~~~~x~~~~~~~~~x")

print("\nCreate new account\n")
userID = input("Username : ")
userPD = input("Password : ")

print("\nYou've just created new DARK Bank account and this account will link to your Bank Statement. \nYou can login to your account\n")

print("\nLogin to your account\n")
userName = input("Username : ")
userPassword = input("Password : ")

while True:  # check the account condidtion whether username and password is correct.

    # if username and password is correct.
    if userName == userID and userPassword == userPD:
        print("\ndark\n")
        break

    elif userName != userID and userPassword == userID:  # if username is incorrect.
        print("\nUsername or password is incorrect.")
        print("\nLogin to your account\n")
        userName = input("Username : ")
        userPassword = input("Password : ")

    elif userName == userID and userPassword != userID:  # if password is incorrect.
        print("\nUsername or password is incorrect.\nPlease try again")
        print("\nLogin to your account\n")
        userName = input("Username : ")
        userPassword = input("Password : ")

    # if username and password is incorrect.
    elif userName != userID and userPassword != userID:
        print("\nUsername or password is incorrect.\nPlease try again")
        print("\nLogin to your account\n")
        userName = input("Username : ")
        userPassword = input("Password : ")

    else:
        # this else will loop till while statement is true.
        print("\nUsername or password is incorrect.\nPlease try again")
        print("\nLogin to your account\n")
        userName = input("Username : ")
        userPassword = input("Password : ")
