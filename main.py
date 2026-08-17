import random
from meals_list import evening_list
from meals_list import breakfast_list
from meals_list import snack_list
from meals_list import lunch_list

def change_meal(day_to_change):
    change_meal = random.choice(evening_list)

    while change_meal in meal_plan.values():
        change_meal = random.choice(evening_list)

    meal_plan [day_to_change]["Evening Meal"] = change_meal

    for day, meals in meal_plan.items():
        print(f"\n{day}:")

        for meal_time, meal in meals.items():
            print(f"       {meal_time}: {meal}")
    

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
meal_times = ['Breakfast', '10am Snack', 'Lunch', '3pm Snack', 'Evening Meal']
meal_options = {
    "Breakfast": breakfast_list,
    "10am Snack": snack_list,
    "Lunch" : lunch_list,
    "3pm Snack": snack_list,
    "Evening Meal": evening_list
}
random.shuffle(evening_list)

meal_plan = {}

# Populate the meal list
for day in days:
    meal_plan[day] = {}   
    for meal in meal_times:                       
            meal_plan[day][meal] = random.choice(meal_options[meal])

for day, meals in meal_plan.items():
    print(f"\n{day}:")

    for meal_time, meal in meals.items():
        print(f"       {meal_time}: {meal}")


# # Asking to change any of the meals
more_days_to_change = "no"
day_change_question = input("\nWould you like to change any of the days?").lower()
if day_change_question == "yes":
    more_days_to_change = "yes"

while more_days_to_change == "yes":
    day_to_change = input("What day would you like to change?").title() 
    if day_to_change in days:
       change_meal(day_to_change)  
       more_days_to_change = input("Would you like to change any other days?").lower() 
    else:
        print("You haven't entered a valid day!")

  
