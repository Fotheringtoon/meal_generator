import random
from meals_list import meals_list

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
random.shuffle(meals_list)

mealPlan = {}

for day, meal in zip(days, meals_list):
    mealPlan [day] = meal
print(mealPlan)

change_wednesday = random.choice(meals_list)

while change_wednesday == mealPlan['Wednesday']:
    change_wednesday = random.choice(meals_list)

mealPlan ['Wednesday'] = change_wednesday
