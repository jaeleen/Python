# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_age = int(age)
remaining_age = 90 - new_age
months_left = remaining_age * 12

weeks_left = remaining_age * 52
days_left = remaining_age * 365

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")



