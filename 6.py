# write a program to make simple calculator

# Add, Subtract, Multiplication and Division
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

def calculator(x, y, operation):
    if operation == 'add':
        return add(x, y)
    elif operation == 'subtract':
        return subtract(x, y)
    elif operation == 'multiply':
        return multiply(x, y)
    elif operation == 'divide':
        return divide(x, y)
    
if __name__ == "__main__":
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    while True:
        choice = int(input("Enter choice(1/2/3/4): "))
        if choice in (1, 2, 3, 4):
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                result = calculator(x, y, ['add', 'subtract', 'multiply', 'divide'][choice - 1])
                print("Result:", result)
                next_calculation = input("Let's do the next calculation? (yes/no): ")
                if next_calculation.lower() != 'yes' or next_calculation.lower != 'y':
                    break
            except ValueError:
                print("Invalid input. Please enter a number")
                continue
        else:
            print("Invalid choice. Please choose a valid operation.")