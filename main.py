import random
from meals_list import meals_list

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
random.shuffle(meals_list)

meal_plan = {}

for day, meal in zip(days, meals_list):
    meal_plan [day] = meal
print(meal_plan)

change_wednesday = random.choice(meals_list)

while change_wednesday in meal_plan.values():
    change_wednesday = random.choice(meals_list)

meal_plan ['Wednesday'] = change_wednesday
