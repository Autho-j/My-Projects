
# Operator Message

# Main Menu Method
def menu_main():
    print("\n1. My Account")
    print("2. Data Package")
    print("3. Voice Package")
    print("4. Special Offers")
    print("0. Exit")
    return True

# Opt-1 My Account Method


def my_account():
    print("\nYour Account Number Is : 0000253\n")
    return True

# Opt-2 Data Package Method


def data_package():
    print("\n1. 1GB = 99Ks")
    print("2. 2GB = 199Ks")
    print("3. 5GB = 499Ks")
    return True

# Opt-3 Voice Package Method


def voice_package():
    print("\n1. 100Min = 99Ks")
    print("2. 200Min = 199Ks")
    print("3. 500Min = 499Ks")
    return True

# Opt-4 Special Offers Method


def special_offers():
    print("\n1. 5GB = 99Ks for 3 Days")
    print("2. 500Min = 99Ks for 3 Days")
    return True


# main menu options
menu_main()
userInput = input("\nPlease select number or Type (e) to EXIT : ")

while userInput != "e":

    if userInput == "1":  # account option stage
        my_account()
        userInput_back = input(
            "\nTpye (0) To Return Main Menu or Type (e) to EXIT : ")

        if userInput_back == "0":
            menu_main()
            userInput = input("\nPlease select number or Type (e) to EXIT : ")

        elif userInput_back == "e":
            break

    elif userInput == "2":  # data package option stage
        data_package()
        userInput = input("\nPlease select number or Type (e) to EXIT : ")

        if userInput == "1":  # 1GB option stage
            print("\n1GB = 99Ks for 30 Days")
            userInput = input(
                "\nType (1) to buy or Type (0) to back to Data Packages :")
            if userInput == "1":
                print("\nCongratulations!")
            elif userInput == "0":
                menu_main()
                userInput = input(
                    "\nPlease select number or Type (e) to EXIT : ")
                if userInput == "e":
                    break

        elif userInput == "2":  # 2GB option stage
            print("\n2GB = 199Ks for 30 Days")
            userInput = input(
                "\nType (1) to buy or Type (0) to back to Data Packages :")
            if userInput == "1":
                print("\nCongratulations!")
            elif userInput == "0":
                menu_main()
                userInput = input(
                    "\nPlease select number or Type (e) to EXIT : ")
                if userInput == "e":
                    break

        elif userInput == "3":  # 5GB option stage
            print("\n5GB = 499Ks for 30 Days")
            userInput = input(
                "\nType (1) to buy or Type (0) to back to Data Packages :")
            if userInput == "1":
                print("\nCongratulations!")
            elif userInput == "0":
                menu_main()
                userInput = input(
                    "\nPlease select number or Type (e) to EXIT : ")
                if userInput == "e":
                    break

        elif userInput == "e":  # ending the data option stage
            break

    elif userInput == "3":  # voice package option stage
        voice_package()
        userInput = input("\nPlease select number or Type (e) to EXIT : ")

        if userInput == "1":  # 100Min option stage
            print("\n100Min = 99Ks for 30 Days")
            userInput = input(
                "\nType (1) to buy or Type (0) to back to Data Packages :")
            if userInput == "1":
                print("\nCongratulations!")
            elif userInput == "0":
                menu_main()
                userInput = input(
                    "\nPlease select number or Type (e) to EXIT : ")
                if userInput == "e":
                    break

        if userInput == "2":  # 200Minoption stage
            print("\n200 = 199Ks for 30 Days")
            userInput = input(
                "\nType (1) to buy or Type (0) to back to Data Packages :")
            if userInput == "1":
                print("\nCongratulations!")
            elif userInput == "0":
                menu_main()
                userInput = input(
                    "\nPlease select number or Type (e) to EXIT : ")
                if userInput == "e":
                    break

        if userInput == "3":  # 500Min option stage
            print("\n500 = 499Ks for 30 Days")
            userInput = input(
                "\nType (1) to buy or Type (0) to back to Data Packages :")
            if userInput == "1":
                print("\nCongratulations!")
            elif userInput == "0":
                menu_main()
                userInput = input(
                    "\nPlease select number or Type (e) to EXIT : ")
                if userInput == "e":
                    break

        elif userInput == "e":  # ending the data option stage
            break

    elif userInput == "4":  # special offfer option stage
        special_offers()
        userInput = input("\nPlease select number or Type (e) to EXIT : ")

        if userInput == "1":  # 5GB option stage
            print("\n5GB = 99Ks for 3 Days")
            userInput = input(
                "\nType (1) to buy or Type (0) to back to Data Packages :")
            if userInput == "1":
                print("\nCongratulations!")
            elif userInput == "0":
                menu_main()
                userInput = input(
                    "\nPlease select number or Type (e) to EXIT : ")
                if userInput == "e":
                    break

        elif userInput == "2":  # 500Min option stage
            print("\n500Min = 99Ks for 3 Days")
            userInput = input(
                "\nType (1) to buy or Type (0) to back to Data Packages :")
            if userInput == "1":
                print("\nCongratulations!")
            elif userInput == "0":
                menu_main()
                userInput = input(
                    "\nPlease select number or Type (e) to EXIT : ")
                if userInput == "e":
                    break

        elif userInput == "e":  # ending the data option stage
            break

    elif userInput == "e":  # ending the process
        break

    break
