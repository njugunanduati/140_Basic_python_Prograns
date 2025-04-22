# Write a program to check if a number is positive, 
# negative or zero


def check_number(n):
    if n < 0:
        return f'{n} is a negative number'
    elif n > 0:
        return f'{n} is a positive number'
    else:
        return f'{n} is zero'

if __name__ == "__main__":
    n = -3
    print(check_number(n))
    n = 3
    print(check_number(n))