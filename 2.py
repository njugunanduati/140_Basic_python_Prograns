# Write a program to check if a number is odd or even

def check_odd_even(n):
    result = ''
    if n % 2 == 0:
        result = f'{n} is an even number'
    else:
        result =  f'{n} is an odd number'
    return result

if __name__ == "__main__":
    n = 10
    for i in range(1, n+1):
        print(check_odd_even(i))