#1 
def check_zander_length():
    length = int(input("Enter the length of the zander in centimeters: "))

    size_limit = 42

    if length < size_limit:
        difference = size_limit - length
        print("The zander is too small.")
        print(f"Release the fish back into the lake. It is {difference} cm below the size limit.")
    else:
        print("The zander meets the size limit. You may keep the fish.")
#2 
    cabin_class = input("Enter the cabin class (LUX, A, B, or C): ").upper()

    if cabin_class == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("Above the car deck, equipped with a window.")
    elif cabin_class == "B":
        print("Windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")
#3 
def hemoglobin_level():
    sex = input("Enter biological sex (female/male): ").lower()
    hemoglobin = float(input("Enter hemoglobin value (g/l): "))

    if sex == "female":
        if hemoglobin < 117:
            print("Hemoglobin level is low.")
        elif hemoglobin <= 155:
            print("Hemoglobin level is normal.")
        else:
            print("Hemoglobin level is high.")

    elif sex == "male":
        if hemoglobin < 134:
            print("Hemoglobin level is low.")
        elif hemoglobin <= 167:
            print("Hemoglobin level is normal.")
        else:
            print("Hemoglobin level is high.")

    else:
        print("Invalid biological sex entered.")
#4 

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
#5 
def unit_price(diameter_cm, price):
    radius_m = diameter_cm / 100 / 2
    area_m2 = math.pi * radius_m ** 2
    return price / area_m2


# main program
d1 = float(input("Enter the diameter of pizza 1 (cm): "))
p1 = float(input("Enter the price of pizza 1 (USD): "))

d2 = float(input("Enter the diameter of pizza 2 (cm): "))
p2 = float(input("Enter the price of pizza 2 (USD): "))

price1 = unit_price(d1, p1)
price2 = unit_price(d2, p2)

if price1 < price2:
    print("Pizza 1 provides better value for money.")
elif price2 < price1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")
import math

# 1. 
def zander_check():
    length = int(input("Enter the length of the zander (cm): "))

    if length < 42:
        print(f"Release the fish. It is {42 - length} cm below the size limit.")
    else:
        print("The zander meets the size limit.")


# 2. 
def cabin_class():
    cabin = input("Enter cabin class (LUX, A, B, C): ").upper()

    if cabin == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin == "A":
        print("Above the car deck, equipped with a window.")
    elif cabin == "B":
        print("Windowless cabin above the car deck.")
    elif cabin == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")


# 3. 
def hemoglobin_status():
    sex = input("Enter biological sex (male/female): ").lower()
    hb = int(input("Enter hemoglobin value (g/l): "))

    if sex == "female":
        low, high = 117, 155
    elif sex == "male":
        low, high = 134, 167
    else:
        print("Invalid sex.")
        return

    if hb < low:
        print("Hemoglobin level is low.")
    elif hb > high:
        print("Hemoglobin level is high.")
    else:
        print("Hemoglobin level is normal.")


# 4. 
def leap_year():
    year = int(input("Enter a year: "))

    if year % 400 == 0:
        print("The year is a leap year.")
    elif year % 100 == 0:
        print("The year is not a leap year.")
    elif year % 4 == 0:
        print("The year is a leap year.")
    else:
        print("The year is not a leap year.")