# 1) Data Type
## Common built-in type
####
# => int -> whole numbers (10)
# => float -> decimal numbers (10.5)
# => str -> text("Hello")
# => bool -> True/False
# => list -> ordered, mutable: [1, 2, 3]
# => tuple -> ordered, immutable: (1, 2, 3)
# => dict -> key-value pairs: {"name": "James"}
# => set -> unique items: {1, 2, 3}
#  
# 2) Conditionals (if, else, elif)
# 3) Typecasting (converting between types)

from datetime import date

class User:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob
    
    def get_age(self):
        current_year = date.today().year
        return current_year - self.yob
    
    def check_age_bracket(self):
        age = self.get_age()
        if age < 18:
            return "Minor"
        elif age < 60:
            return "Adult"
        else:
            return "Senior"


if __name__ == "__main__":
    name = input("What is your name? ")

    try:
        yob = int(input("What year were you born? "))
        current_year = date.today().year
        if yob < 1900 or yob > current_year:
            raise ValueError("Invalid year of birth.")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        user = User(name, yob)
        print(f"\nHello {user.name}, your age is {user.get_age()}")
        print(f"You are a {user.check_age_bracket()}")





