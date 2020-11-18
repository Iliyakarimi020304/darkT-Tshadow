print("    BMI CALCULATOR    ")

weight = float(input("ENTER YOUR WEIGHT(KG): "))
height = float(input("ENTER YOUR HEIGHT(M): "))

BMI = weight / (height * height)
print(f"Your Body Mass Index is: {BMI:.2f}")

if BMI < 18.5:
    print("You are UNDERWEIGHT!")
elif 18.5 <= BMI and BMI <= 24.9:
    print("You are NORMAL")
elif 25 <= BMI and BMI <= 29.9:
    print("You are OVERWEIGHT!")
elif 30 <= BMI and BMI <= 34.9:
    print("You are OBESE!")
elif BMI >= 35:
    print("You are EXTREMELY OBSES!")


