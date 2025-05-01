# Find the sum of elements in an list

def find_sum_one(arr):
    return sum(arr)

def find_sum_two(arr):
    total = 0
    for i in arr:
        total += i
    return total

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(find_sum_one(arr))
    print(find_sum_two(arr))