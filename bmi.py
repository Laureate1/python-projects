# BMI stands for Body Mass Index.
# It's basically a number that tells you whether 
# your weight is healthy for your height. Doctors and health 
# professionals use it as a quick way to check if someone is 
# underweight, healthy, overweight or obese.
# The formula to calculate BMI is:
# BMI = weight (kg) / (height (m))^2 
   
print("Welcome to the BMI(Body Mass Index) Calculator, let's get started.")
name = input("What is your name? ")
print(f"Hello {name}, Let's calculate your BMI.")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres (e.g 1.75): "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {round(bmi, 2)}")
if bmi < 18.5:
    print("You are underweight.")
    print("Tip: Consider eating more nutritious meals and consult a doctor 🥗")
elif 18.5 <= bmi < 24.9:
    print("You are normal weight.")     
    print("Tip: Maintain your current diet and exercise routine 🏃‍♂️")
elif 25 <= bmi < 29.9:
    print("You are overweight.")            
    print("Tip: Consider a balanced diet and regular exercise 🏋️‍♂️")
else:    
    print("You are obese.")
    print("Tip: Consult a doctor and consider a comprehensive weight management plan 🩺")

print(f"\nThank you for using the BMI Calculator {name}, Stay healthy always") 
