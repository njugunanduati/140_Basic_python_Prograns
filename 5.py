# Write a program to print the Fibonacci sequence
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence[:n]


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    while not isinstance(n, int) or n <= 0:
        print("Please enter a positive integer.")
        n = int(input("Enter a number: "))
    print(generate_fibonacci(n))