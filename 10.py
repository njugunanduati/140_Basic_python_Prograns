# Write a python program that asks the user 
# the name, age and location

class User:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
    
    def age_in_months(self):
        return self.age * 12


if __name__ == "__main__":
    name = input("What is your name? ")
    age = int(input("How old are you? ")) # Cast to int
    location = input("where do you live? ")
    user = User(name, age, location)

    print(f"Hello {user.name}, you're {user.age} years old and you live in {user.location}.")
    print(f"You are approximately {user.age_in_months()} months old")