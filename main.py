import random
from meals_list import meals_list

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
random.shuffle(meals_list)

for day, meal in zip(days, meals_list):
    print(f"{day}: {meal}" )

