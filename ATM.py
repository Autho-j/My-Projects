
# Welcome Message.
print('\n\t"Welcome to DARK Bank"')
print("\tx~~~~~~~~~x~~~~~~~~~x")

# language options.
print("\nChoose Your Language")
print("\n(1) English\n(2) Myanglish")

# User's choice input.
lang_choice = input("\nOption : ")
#cancel_operation = input("\nType (0) to Exit :")
#back_operation = input("\nType (0) to Back")

def account_en():  # Account Method English.
    print("\n(1) My Account\n(2) Security\n(3) Call Centre")
    return True


def account_mm():  # Account Method Myanglish.
    print("\n(1) Ngway Sayin\n(2) Lone Chone Yay\n(3) Aku Anyi")
    return True


def account_balance_en():  # Account Balance English.
    print("\n(1) Withdrawal Money\n(2) Transfer Money\n(3) Check Balance\n(4) Back to Menu\n")
    return True


def account_balance_mm():  # Account Balance Myanglish.
    print("\n(1) Pite San Htoke Yan\n(2) Pite San Hlwel Yan\n(3) Lat Kyan Ngway Sit Yan\n(4) Pin Ma Sar Myat Nar Pyan Thwr Yan\n")
    return True

#def exit():
    cancel_operation = input("\nType (0) to Exit : ")
    return True

# Check the condition whether your choice is option 1 or 2.
    
if lang_choice == "1":  # For option 1 - Eng language choice.
    account_en()
    account_choice = input("\nOption : ")

    # if user choose 1 in account options.
    if account_choice == "1":
        account_balance_en()
        account_balance = input("\nOption : ")

elif lang_choice == "2":  # For option 1 - Myanglish language choice.
    account_mm()
    account_choice = input("\nOption : ")

    # if user choose 1 in account options.
    if account_choice == "1":
        account_balance_mm()







