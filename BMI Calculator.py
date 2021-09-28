height = float(input("Height in cm : "))
weight = float(input("Weight in Lbs : "))

height_in_m = height / 100
height_m2 = height_in_m ** 2
weight_m2 = weight / 2.205

bmi_result = "{:.2f}".format(weight_m2 / height_m2)

final_bmi = weight_m2 / height_m2

if final_bmi <= 18.5:

    print("Your BMI result is " + str(bmi_result) +
          "\n You are UNDER-WEIGHT" + "\n You need to GAIN more WEIGHT!!")

elif final_bmi >= 18.5 and final_bmi <= 24.9:

    print("Your BMI result is " + str(bmi_result) +
          "\n You are NORMAL" + "\n You need to maintain your WEIGHT!!")

elif final_bmi >= 25.0 and final_bmi <= 29.9:

    print("Your BMI result is " + str(bmi_result) +
          "\n You are OVER-WEIGHT" + "\n You need to lose WEIGHT!!")

elif final_bmi >= 30.0:
    print("Your BMI result is " + str(bmi_result) +
          "\n You are OBESE" + "\n You HAVE TO LOSE more WEIGHT!!")
