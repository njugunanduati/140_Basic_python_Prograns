# Write a program to check is a number is a prime number
# NB: A prime number is a number that cannot be evenly divided
# by any other number except for 1 and itself.
# For example, 2, 3, 5, 7, 11 and 13 are prime numbers because 
# they cannot be divided by any other positive integer except for 
# 1 and their own value.
import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Enter a number to check if it's prime: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
