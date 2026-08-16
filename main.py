import random
from meals_list import meals_list

def change_meal(day_to_change):
    change_meal = random.choice(meals_list)

    while change_meal in meal_plan.values():
        change_meal = random.choice(meals_list)

    meal_plan [day_to_change] = change_meal

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
random.shuffle(meals_list)

meal_plan = {}

for day, meal in zip(days, meals_list):
    meal_plan [day] = meal
print(meal_plan)


more_days_to_change = "no"
day_change_question = input("Would you like to change any of the days?").lower()
if day_change_question == "yes":
    more_days_to_change = "yes"

while more_days_to_change == "yes":
    day_to_change = input("What day would you like to change?").title() 
    if day_to_change in days:
       change_meal(day_to_change)  
       more_days_to_change = input("Would you like to change any other days?").lower() 
    else:
        print("You haven't entered a valid day!")

  
print(meal_plan)