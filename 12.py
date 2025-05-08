# Loops in python
## for loop
# => used to iterate over a sequence (like a list or range)
# num = int(input("Enter a number: "))
# for i in range(num):
#     print(f"Count: {i}")

## while loop
# => Repeats as long as a condition is True
# count = 0
# while count < num:
#     print(f"Count: {count}")
#     count += 1

## Loop control
# => break -> exit the loop
# => continue -> skips to the next iteration

# print all even numbers from 1 to specified number
# new_num = int(input("Enter a number between 1 to 20 "))
# for i in range(1, new_num):
#     if i % 2 == 0:
#         print(i)

class Solution:
    def __init__(self, a, b, op):
        self.a = a
        self.b = b
        self.op = op

    def calculate(self):
        if self.op == "+":
            return self.a + self.b
        elif self.op == "-":
            return self.a - self.b
        elif self.op == "*":
            return self.a * self.b
        elif self.op == "/":
            if self.b == 0:
                return "Cannot divide by zero"
            return self.a / self.b
        else:
            return "Invalid operator"

if __name__ == "__main__":    
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Choose operation (+, -, *, /): ")
            result = Solution(a, b, op)
            print(f"Result: {result.calculate()}")
        except ValueError:
            print("Invalid input. Please enter numbers.")
        
        cont = input("Do you want to continue? (y/n): ")
        if cont.lower() != 'y':
            break