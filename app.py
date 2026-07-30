from flask import Flask
import random
from meals_list import meals_list

app = Flask(__name__)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

@app.route("/")

def home():
    print("Page loaded")
    shuffled_meals = meals_list.copy()
    random.shuffle(shuffled_meals)

    plan = ""

    for day, meal in zip(days, shuffled_meals):
        plan += f"{day}: {meal}<br>"

    return plan

if __name__ == "__main__":
    app.run(debug=True)


