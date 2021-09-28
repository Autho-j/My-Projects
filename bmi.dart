import 'dart:io';

void main() {
  //user input data
  print("Height (cm) :");
  double? height = double.parse(stdin.readLineSync()!);
  print("Weight (lbs) :");
  double? weight = double.parse(stdin.readLineSync()!);

  //converting stage
  double height_m = height / 100;
  double height_m2 = height_m * height_m;
  double weight_kg = weight / 2.205;

  //bmi formula
  double bmi = weight_kg / height_m2;

  //check the condition
  if (bmi <= 18.5) {
    print("BMI result is $bmi and you are UNDER_WEIGHT.");
  } else if (bmi >= 18.5 && bmi <= 24.9) {
    print("BMI result is $bmi and you are NORMAL.");
  } else if (bmi >= 25.0 && bmi <= 29.9) {
    print("BMI result is $bmi and you are OVER_WEIGHT.");
  } else if (bmi >= 30.0) {
    print("BMI result is $bmi and you are OBESE!");
  }
}