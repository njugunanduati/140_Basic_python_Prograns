# Core Python Data Structures
# 1) => lists -> Ordered, mutable (can change), allows duplicates
# fruits = ['apple', 'banana', 'orange']
# fruits.append('mango')
# fruits.append('water melon')
# fruits.append('banana')
# print(fruits)
# print(fruits[0])
# fruits.remove('banana')
# print(fruits)
# fruits.pop()
# print(fruits)
# for fruit in fruits:
#     print(f"{fruit} is a fruit")
# 2) => tuples -> Ordered, immutable(can't change), allows duplicates
# coordinates = (10.5, 20.3)
# print(coordinates[1])
# 3) => sets -> Unordered,no duplicates, greate for checking membership.
# items = {"pen", "pencil", "pen"}
# items.add("eraser")
# print(items)
# 4) => Dictionaries -> Key - Value pairs, fast lookup
# user = {"name": "James", "email": "njugunanduati@gmail.com", "is_coder": True}
# user["state"] = "Washington"
# user["city"] = "Renton"
# for key, value in user.items():
#     print(f"{key}: {value}")


class Solution:
    def __init__(self):
        self.movies = []
        self.users = {}
        self.unique = set()
    
    def add_movie(self, movie):
        self.movies.append(movie)
    
    def add_user(self, name, age):
        self.users["name"] = name
        self.users["age"] = age
    
    def add_unique_chars_from_name(self, name):
        for char in name:
            self.unique.add(char)
    
    def display_all(self):
        print("\n Movies Watched: ")
        for movie in self.movies:
            print(f"- {movie}")
        
        print("\n User Info: ")
        for k, v in self.users.items():
            print(f"{k.capitalize()}: {v}")
        
        print("\n Unique letters in Name: ")
        print(", ".join(sorted(self.unique)))
    

if __name__ == "__main__":
    solution = Solution()

    num = int(input("How many movies have you watched this week?  "))
    for _ in range(num):
        movie = input("Enter movie name: ")
        solution.add_movie(movie)
    
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    solution.add_user(name, age)
    solution.add_unique_chars_from_name(name)
    
    solution.display_all()