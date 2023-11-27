print("BODY MASS INDEX CALCULATOR")
# 1st input: enter height in meters 
height = input("What is your height? ")
# 2nd input: enter weight in kilograms 
weight = input("What is your weight? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
weight_in_int = int(weight)
height_in_float = float(height)
Bmi = weight_in_int / (height_in_float **2)
print(round(Bmi))



