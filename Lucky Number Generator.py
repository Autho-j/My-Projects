import random


print("\n Hello, Welcome To Lucky Number Generator")
txt = input("\n Type 'e' To Exit (or) Type 's' To Start  :  ")


while txt:

    if txt == "s":

        print("\n I'm Glad You Are Here! \n Please Select Your Options.")
        Opt = int(input(
            "\n Type '1' For One Lucky Number ( or ) Type '2' For Two Lucky Numbers  :  "))

        if Opt == 1:

            fnum = str(random.randrange(0, 9))
            print("\n Your Lucky Number is " + fnum + "\n")

        elif Opt == 2:

            fnum = str(random.randrange(0, 9))
            lnum = str(random.randrange(0, 9))

            lucky_number = fnum + lnum
            print("\n Your Lucky Number is " + lucky_number + "\n")

        break

    if txt == "e":
        break

    else:
        break
